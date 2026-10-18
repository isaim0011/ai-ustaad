use std::sync::Arc;
use axum::{
    body::Body,
    http::{Request, StatusCode},
};
use tower::util::ServiceExt;

use crate::{
    config::Config,
    db::AppState,
    models::{DiagramRenderRequest, ProgressCompleteRequest, QuizSubmission},
    routes::create_router,
    services::{mentor_service::MentorChatRequest, DiagramService, MentorService, SyllabusStore},
};

#[test]
fn test_syllabus_completeness() {
    let store = SyllabusStore::new();

    // 1. Verify 5 Phases
    assert_eq!(store.phases.len(), 5, "Must have exactly 5 phases");

    // 2. Verify 14 Modules
    let all_modules = store.get_all_modules();
    assert_eq!(all_modules.len(), 14, "Must have exactly 14 modules");
    assert_eq!(store.course.total_modules, 14);

    // 3. Verify 84 Lessons (6 per module)
    let total_lessons: usize = all_modules.iter().map(|m| m.lessons.len()).sum();
    assert_eq!(total_lessons, 84, "Must have exactly 84 lessons (6 per module)");
    assert_eq!(store.course.total_lessons, 84);

    // 4. Verify 3 Specialization Tracks
    assert_eq!(store.course.tracks.len(), 3, "Must have 3 specialization tracks");

    // 5. Verify 10 Badges
    assert_eq!(store.course.badges.len(), 10, "Must have 10 badges");

    // 6. Verify Weekly Challenges
    assert!(!store.challenges.is_empty(), "Must have weekly challenges");

    // 7. Verify Module lookup by slug
    let nlp_mod = store.get_module("nlp-transformers");
    assert!(nlp_mod.is_some(), "Module 'nlp-transformers' must exist");
    let nlp = nlp_mod.unwrap();
    assert_eq!(nlp.lessons.len(), 6);
    assert!(!nlp.urdu_title.is_empty());

    // 8. Verify Lesson lookup by slug
    let lesson_pair = store.get_lesson("self-attention-math");
    assert!(lesson_pair.is_some(), "Lesson 'self-attention-math' must exist");
    let (m, l) = lesson_pair.unwrap();
    assert_eq!(m.slug, "nlp-transformers");
    assert!(l.code_snippet.is_some());
    assert!(!l.explanation_urdu.is_empty());
}

#[test]
fn test_native_diagramkit_compilation_and_rendering() {
    // 1. Test basic Flowchart rendering
    let script = r#"@preset midnight
@animate flow
flow LR: Test Flow
a[Start] -> b[Process]* -> c((End))"#;

    let req = DiagramRenderRequest {
        script: script.to_string(),
        preset: Some("midnight".to_string()),
        mode: Some("dark".to_string()),
        animate: Some("flow".to_string()),
        speed: Some(1.0),
    };

    let res = DiagramService::render(&req);
    assert!(res.is_ok(), "DiagramKit rendering must succeed: {:?}", res.err());
    let output = res.unwrap();
    assert!(output.svg.contains("<svg"), "Output must contain <svg tag");
    assert!(output.svg.contains("</svg>"), "Output must close SVG");
    assert!(output.valid, "Report must be valid geometric check");
    assert_eq!(output.kind, "flowchart");

    // 2. Test Animated Architecture Diagram
    let arch_script = r#"@preset midnight
@animate wave
arch LR: Test Neural Architecture
in[Input] ~purple -> hidden[Hidden Layer]* ~teal -> out[Output] ~ok"#;

    let res_arch = DiagramService::render(&DiagramRenderRequest {
        script: arch_script.to_string(),
        preset: Some("midnight".to_string()),
        mode: Some("dark".to_string()),
        animate: Some("wave".to_string()),
        speed: Some(1.0),
    });
    assert!(res_arch.is_ok());
    let arch_out = res_arch.unwrap();
    assert!(arch_out.svg.contains("animation"));

    // 3. Test All 8 Gallery Diagrams Render Cleanly
    let gallery = DiagramService::get_gallery();
    assert_eq!(gallery.len(), 8, "Gallery must contain 8 curated diagrams");
    for d in gallery {
        assert!(!d.svg.is_empty(), "Diagram {} must have rendered SVG", d.id);
        assert!(d.svg.contains("<svg"), "Diagram {} SVG must be valid", d.id);
    }

    // 4. Test All 14 Module Diagrams Compile & Render Cleanly
    let store = SyllabusStore::new();
    for m in store.get_all_modules() {
        let render_res = DiagramService::render(&DiagramRenderRequest {
            script: m.diagram_script.clone(),
            preset: Some("midnight".to_string()),
            mode: Some("dark".to_string()),
            animate: Some("flow".to_string()),
            speed: Some(1.0),
        });
        assert!(
            render_res.is_ok(),
            "Module {} diagram must compile & render: {:?}",
            m.slug,
            render_res.err()
        );
        let out = render_res.unwrap();
        assert!(out.svg.contains("<svg"), "Module {} must output valid SVG", m.slug);
    }
}

#[tokio::test]
async fn test_gamification_engine_and_quiz_grading() {
    let config = Arc::new(Config::from_env());
    let state = AppState::new(config).await;

    let user_id = "test-student-42";

    // 1. Initial profile check
    let profile = state.get_user_profile(user_id).await;
    assert_eq!(profile.total_xp, 0);
    assert_eq!(profile.current_level, 1);
    assert!(profile.completed_lessons.is_empty());

    // 2. Complete a lesson
    let res = state.complete_lesson(user_id, "python-deep-dive").await;
    assert!(res.is_ok());
    let r = res.unwrap();
    assert!(r.success);
    assert_eq!(r.xp_awarded, 100);
    assert_eq!(r.total_xp, 100);

    // 3. Complete same lesson again (idempotent, no extra XP)
    let res_repeat = state.complete_lesson(user_id, "python-deep-dive").await;
    assert!(res_repeat.is_ok());
    let r_repeat = res_repeat.unwrap();
    assert_eq!(r_repeat.xp_awarded, 0);
    assert_eq!(r_repeat.total_xp, 100);

    // 4. Submit Quiz with failing answers
    let fail_res = state.submit_quiz(user_id, "python-mastery", &[0, 0, 0]).await;
    assert!(fail_res.is_ok());
    let f = fail_res.unwrap();
    assert!(!f.passed);
    assert_eq!(f.xp_awarded, 0);

    // 5. Submit Quiz with 100% correct answers
    // Module 1 quiz has 3 questions, correct answers are [1, 1, 1]
    let pass_res = state.submit_quiz(user_id, "python-mastery", &[1, 1, 1]).await;
    assert!(pass_res.is_ok());
    let p = pass_res.unwrap();
    assert!(p.passed, "Quiz with correct answers must pass");
    assert_eq!(p.score_percent, 100);
    assert_eq!(p.xp_awarded, 150);

    // Profile XP should now be 100 + 150 = 250
    let updated = state.get_user_profile(user_id).await;
    assert_eq!(updated.total_xp, 250);
}

#[tokio::test]
async fn test_mentor_service() {
    // 1. Test Attention query
    let req = MentorChatRequest {
        message: "Can you explain the Transformer attention mechanism?".to_string(),
        module_slug: Some("nlp-transformers".to_string()),
        lesson_slug: Some("self-attention-math".to_string()),
        history: None,
    };
    let res = MentorService::answer(&req);
    assert!(res.is_ok());
    let ans = res.unwrap();
    assert!(ans.reply_urdu.contains("Self-Attention"));
    assert!(ans.code_snippet.is_some());
    assert!(ans.diagram_script.is_some());
    assert!(ans.diagram_svg.is_some());
    assert!(!ans.suggested_followups.is_empty());

    // 2. Test RAG query
    let rag_req = MentorChatRequest {
        message: "How does RAG hybrid search work?".to_string(),
        module_slug: Some("production-rag".to_string()),
        lesson_slug: None,
        history: None,
    };
    let rag_ans = MentorService::answer(&rag_req).unwrap();
    assert!(rag_ans.reply_urdu.contains("RAG"));
    assert!(rag_ans.code_snippet.is_some());
}

#[tokio::test]
async fn test_axum_http_routes() {
    let config = Arc::new(Config::from_env());
    let state = AppState::new(config).await;
    let app = create_router(state);

    // 1. GET /api/health
    let req = Request::builder()
        .uri("/api/health")
        .method("GET")
        .body(Body::empty())
        .unwrap();
    let resp = app.clone().oneshot(req).await.unwrap();
    assert_eq!(resp.status(), StatusCode::OK);

    // 2. GET /api/course
    let req = Request::builder()
        .uri("/api/course")
        .method("GET")
        .body(Body::empty())
        .unwrap();
    let resp = app.clone().oneshot(req).await.unwrap();
    assert_eq!(resp.status(), StatusCode::OK);

    // 3. GET /api/modules
    let req = Request::builder()
        .uri("/api/modules")
        .method("GET")
        .body(Body::empty())
        .unwrap();
    let resp = app.clone().oneshot(req).await.unwrap();
    assert_eq!(resp.status(), StatusCode::OK);

    // 4. GET /api/modules/nlp-transformers
    let req = Request::builder()
        .uri("/api/modules/nlp-transformers")
        .method("GET")
        .body(Body::empty())
        .unwrap();
    let resp = app.clone().oneshot(req).await.unwrap();
    assert_eq!(resp.status(), StatusCode::OK);

    // 5. GET /api/lessons/tokenization-bpe
    let req = Request::builder()
        .uri("/api/lessons/tokenization-bpe")
        .method("GET")
        .body(Body::empty())
        .unwrap();
    let resp = app.clone().oneshot(req).await.unwrap();
    assert_eq!(resp.status(), StatusCode::OK);

    // 6. POST /api/diagrams/render
    let render_body = serde_json::to_string(&DiagramRenderRequest {
        script: "flow LR: Test\na -> b".to_string(),
        preset: Some("midnight".to_string()),
        mode: Some("dark".to_string()),
        animate: Some("flow".to_string()),
        speed: Some(1.0),
    })
    .unwrap();
    let req = Request::builder()
        .uri("/api/diagrams/render")
        .method("POST")
        .header("Content-Type", "application/json")
        .body(Body::from(render_body))
        .unwrap();
    let resp = app.clone().oneshot(req).await.unwrap();
    assert_eq!(resp.status(), StatusCode::OK);

    // 7. GET /api/diagrams/gallery
    let req = Request::builder()
        .uri("/api/diagrams/gallery")
        .method("GET")
        .body(Body::empty())
        .unwrap();
    let resp = app.clone().oneshot(req).await.unwrap();
    assert_eq!(resp.status(), StatusCode::OK);

    // 8. POST /api/progress/complete
    let prog_body = serde_json::to_string(&ProgressCompleteRequest {
        lesson_slug: "python-deep-dive".to_string(),
    })
    .unwrap();
    let req = Request::builder()
        .uri("/api/progress/complete")
        .method("POST")
        .header("Content-Type", "application/json")
        .header("Authorization", "Bearer guest")
        .body(Body::from(prog_body))
        .unwrap();
    let resp = app.clone().oneshot(req).await.unwrap();
    assert_eq!(resp.status(), StatusCode::OK);

    // 9. POST /api/quizzes/python-mastery/submit
    let quiz_body = serde_json::to_string(&QuizSubmission {
        answers: vec![1, 1, 1],
    })
    .unwrap();
    let req = Request::builder()
        .uri("/api/quizzes/python-mastery/submit")
        .method("POST")
        .header("Content-Type", "application/json")
        .header("Authorization", "Bearer guest")
        .body(Body::from(quiz_body))
        .unwrap();
    let resp = app.clone().oneshot(req).await.unwrap();
    assert_eq!(resp.status(), StatusCode::OK);

    // 10. POST /api/ai/mentor
    let mentor_body = serde_json::to_string(&MentorChatRequest {
        message: "Explain LoRA in Roman Urdu".to_string(),
        module_slug: Some("llm-fine-tuning".to_string()),
        lesson_slug: None,
        history: None,
    })
    .unwrap();
    let req = Request::builder()
        .uri("/api/ai/mentor")
        .method("POST")
        .header("Content-Type", "application/json")
        .body(Body::from(mentor_body))
        .unwrap();
    let resp = app.clone().oneshot(req).await.unwrap();
    assert_eq!(resp.status(), StatusCode::OK);
}

#[tokio::test]
async fn test_engineering_blogs_and_cloud_guide() {
    let store = SyllabusStore::new();

    // 1. Verify 10 Engineering Blogs exist
    let blogs = store.get_blogs();
    assert_eq!(blogs.len(), 10, "Must have exactly 10 engineering blogs");

    // 2. Verify all 10 blogs compile cleanly into valid animated SVGs
    for b in blogs {
        assert!(!b.slug.is_empty(), "Blog slug cannot be empty");
        assert!(!b.title.is_empty(), "Blog title cannot be empty");
        assert!(!b.summary_roman_urdu.is_empty(), "Blog summary cannot be empty");
        assert!(!b.content_roman_urdu.is_empty(), "Blog content cannot be empty");
        assert!(!b.diagram_script.is_empty(), "Diagram script cannot be empty");

        // Verify pre-rendered SVG is present and valid
        assert!(
            b.diagram_svg.is_some(),
            "Blog '{}' must have rendered SVG",
            b.slug
        );
        let svg = b.diagram_svg.as_ref().unwrap();
        assert!(svg.contains("<svg"), "Blog '{}' SVG must contain <svg", b.slug);
        assert!(svg.contains("</svg>"), "Blog '{}' SVG must contain </svg>", b.slug);

        // Verify dynamic re-rendering succeeds
        let render_res = DiagramService::render_script_to_svg(
            &b.diagram_script,
            Some(&b.diagram_preset),
            Some(&b.diagram_animation),
        );
        assert!(
            render_res.is_ok(),
            "Blog '{}' diagram must compile & render: {:?}",
            b.slug,
            render_res.err()
        );
    }

    // 3. Verify single blog lookup
    let blog = store.get_blog("zero-gpu-survival-guide-2026");
    assert!(blog.is_some(), "Must be able to find blog by slug");
    let b = blog.unwrap();
    assert_eq!(b.category, "Cloud & Compute");
    assert_eq!(b.order_index, 1);
    assert!(b.compute_recipe.is_some());

    // 4. Verify Zero-GPU Cloud Guide completeness
    let guide = store.get_cloud_guide();
    assert_eq!(guide.colab_free_t4.cost, "$0.00 (100% Free)");
    assert_eq!(guide.kaggle_dual_t4.vram, "30 GB Combined VRAM (2x T4 GPUs)");
    assert!(guide.google_one_compute_units_saver.saver_script.is_some());
    assert_eq!(guide.free_api_providers.len(), 3);

    // 5. Verify all 14 modules have real-world deliverables & zero-gpu recipes
    let all_modules = store.get_all_modules();
    assert_eq!(all_modules.len(), 14);
    for m in all_modules {
        assert!(
            m.real_world_deliverable.is_some(),
            "Module {} must have real_world_deliverable",
            m.slug
        );
        assert!(
            m.zero_gpu_recipe.is_some(),
            "Module {} must have zero_gpu_recipe",
            m.slug
        );
        let recipe = m.zero_gpu_recipe.as_ref().unwrap();
        assert!(!recipe.platform.is_empty());
        assert!(!recipe.vram_required.is_empty());
        assert!(!recipe.estimated_cost.is_empty());
        assert!(!recipe.one_click_command.is_empty());
    }

    // 6. Verify Axum HTTP Endpoints
    let config = Arc::new(Config::from_env());
    let state = AppState::new(config).await;
    let app = create_router(state);

    // GET /api/blogs (200 OK)
    let req = Request::builder()
        .uri("/api/blogs")
        .method("GET")
        .body(Body::empty())
        .unwrap();
    let resp = app.clone().oneshot(req).await.unwrap();
    assert_eq!(resp.status(), StatusCode::OK);

    // GET /api/blogs/zero-gpu-survival-guide-2026 (200 OK)
    let req = Request::builder()
        .uri("/api/blogs/zero-gpu-survival-guide-2026")
        .method("GET")
        .body(Body::empty())
        .unwrap();
    let resp = app.clone().oneshot(req).await.unwrap();
    assert_eq!(resp.status(), StatusCode::OK);

    // GET /api/blogs/unsloth-4bit-qlora (200 OK)
    let req = Request::builder()
        .uri("/api/blogs/unsloth-4bit-qlora")
        .method("GET")
        .body(Body::empty())
        .unwrap();
    let resp = app.clone().oneshot(req).await.unwrap();
    assert_eq!(resp.status(), StatusCode::OK);

    // GET /api/blogs/non-existent-blog (404 Not Found)
    let req = Request::builder()
        .uri("/api/blogs/non-existent-blog")
        .method("GET")
        .body(Body::empty())
        .unwrap();
    let resp = app.clone().oneshot(req).await.unwrap();
    assert_eq!(resp.status(), StatusCode::NOT_FOUND);

    // GET /api/cloud-guide (200 OK)
    let req = Request::builder()
        .uri("/api/cloud-guide")
        .method("GET")
        .body(Body::empty())
        .unwrap();
    let resp = app.clone().oneshot(req).await.unwrap();
    assert_eq!(resp.status(), StatusCode::OK);
}

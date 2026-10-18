# PLAN.md — AI Mastery: Production-Ready Frontend Rebuild

## 1. Goal
Rebuild the frontend of the AI Mastery platform as a production-grade, dynamic web application in **SvelteKit 2 + Svelte 5 (Runes) + TypeScript + TailwindCSS v4 (@tailwindcss/vite)** connected directly to **Supabase** (PostgreSQL, Auth, RLS, RPCs) and the **Rust DiagramKit/Mentor backend** (`http://127.0.0.1:8080`).

## 2. Architecture & Design Principles
- **Design Aesthetic**: Claude.ai-inspired warm minimalist elegance.
  - Backgrounds: Light `#faf9f5` / Dark `#1f1e1d`
  - Surfaces: Light `#f0eee6` / Dark `#262624`
  - Accent: Terracotta `#c96442` (hover `#d97757`)
  - Typography: Serif headings (`Source Serif 4`, Georgia), UI text (`Inter`), Code (`JetBrains Mono`, monospace)
  - Responsive layout, subtle transitions, prefers-reduced-motion compliance, accessible contrast (WCAG AA).
- **Data Architecture**:
  - 100% dynamic data fetched directly from Supabase via server load functions (`+page.server.ts` / `+layout.server.ts`).
  - Tables: `courses`, `phases`, `modules`, `lessons`, `quizzes`, `quiz_questions`, `badges`, `specialization_tracks`, `engineering_blogs`, `weekly_challenges`, `profiles`, `user_lesson_progress`, `user_quiz_attempts`, `user_badges`, `ai_chat_sessions`, `ai_chat_messages`.
  - RPCs: `complete_lesson(p_lesson_id, p_notes)` and `submit_quiz(p_quiz_id, p_score_pct, p_answers)`.
  - Session Management: `@supabase/ssr` with `hooks.server.ts` cookie bridge (`getAll`/`setAll`) and `safeGetSession`.
  - Backend integration: DiagramKit rendering (`POST /api/diagrams/render`), AI Mentor (`POST /api/ai/mentor`) with Supabase session/message persistence.
  - Setup screen: Clean fallback notice if `PUBLIC_SUPABASE_URL` / `PUBLIC_SUPABASE_ANON_KEY` is not configured or placeholder.

## 3. Route Map
- `/`: Landing page (Hero in Roman Urdu, value props, live course/phases from DB, CTA)
- `/login`: Email + password, Magic Link, GitHub / Google OAuth
- `/signup`: Registration with auto profile trigger
- `/auth/callback`: Server route exchanging auth code for session
- `/logout`: Form action signing out and redirecting to `/`
- `/learn`: Authenticated student dashboard (XP, streak, phase progress, continue-where-left-off, badges, challenges)
- `/learn/[module]`: Module overview (outcomes, real-world deliverable, Zero-GPU recipe with copyable unassign snippet, lessons list, DiagramKit diagram)
- `/learn/[module]/[lesson]`: Claude-like reader (collapsible sidebar, centered markdown prose, syntax highlighted code, DiagramKit diagram panel, optimistic "Mark Complete" RPC, prev/next)
- `/learn/[module]/quiz`: Quiz runner (questions from `quiz_questions`, live grading, RPC submission, Roman Urdu explanations)
- `/blog`: Engineering blogs list
- `/blog/[slug]`: Engineering blog article with DiagramKit visual architecture
- `/mentor`: Claude.ai-style AI Mentor chat (bottom composer, autosizing textarea, streaming/polling backend response, Supabase chat session persistence)
- `/profile`: Profile editor (full_name, selected_track, stats, unlocked badges)

## 4. Components
- `TopNav.svelte`: Logo, navigation links, user XP pill, streak flame, auth state, ThemeToggle, mobile drawer.
- `Footer.svelte`: Global footer on every page with "Built by Bimo" linking to https://github.com/isaim0011.
- `Sidebar.svelte`: Collapsible module & lesson syllabus tree with completion checkmarks.
- `Diagram.svelte`: Fetches rendered SVG from backend (`POST /api/diagrams/render`), skeleton loader, error fallback.
- `CodeBlock.svelte`: Shiki-powered syntax highlighter with copy-to-clipboard button and language badge.
- `Markdown.svelte`: Marked parser with code blocks and clean typography styling.
- `ThemeToggle.svelte`: Dark/light toggle with smooth transition and persistence.
- `SupabaseSetupNotice.svelte`: Friendly setup guide when env is missing/placeholder.

## 5. Verification & Testing
1. `npm run check` reports 0 errors, 0 warnings.
2. `npm run build` completes successfully.
3. Live Supabase connection test: fetches real courses, phases, modules, lessons, blogs from Supabase DB.
4. Dev server launches and responds with HTTP 200.

# generate_full_syllabus.py
import os
import json
import sys

# Ensure current dir is in sys.path
cur_dir = os.path.dirname(os.path.abspath(__file__))
if cur_dir not in sys.path:
    sys.path.insert(0, cur_dir)

from seed_base import get_base_sql, esc
from seed_modules_phase1_2 import get_modules_phase1_2
from seed_modules_phase3_5 import get_modules_phase3_5
from seed_quizzes import get_quizzes
from seed_blogs import get_blogs_sql

def main():
    lines = get_base_sql()
    
    all_modules = get_modules_phase1_2() + get_modules_phase3_5()
    
    # Inject 15 Hugging Face interactive sub-projects into practice_checkpoint
    hf_path = os.path.join(cur_dir, "hf_subprojects.json")
    if os.path.exists(hf_path):
        with open(hf_path, "r", encoding="utf-8") as f:
            hf_map = {item["module_number"]: item for item in json.load(f)}
        for m in all_modules:
            num = m.get("module_number")
            if num in hf_map:
                if "practice_checkpoint" not in m or not isinstance(m["practice_checkpoint"], dict):
                    m["practice_checkpoint"] = {}
                m["practice_checkpoint"]["hf_subproject"] = hf_map[num]
    
    lines.append("\n-- 0. SCHEMA UPGRADES")
    lines.append("alter table public.modules add column if not exists practice_checkpoint jsonb default '{}'::jsonb;\n")

    lines.append("\n-- 6. MODULES (ALL 15 MODULES: MODULE 0 TO 14)")
    for m in all_modules:
        lines.append(f"""insert into public.modules (
  phase_id, module_number, slug, title, weeks_range, estimated_hours,
  learning_outcomes, practical_tasks, resources, diagram_script,
  diagram_preset, diagram_animation, badge_slug, real_world_deliverable, zero_gpu_recipe, practice_checkpoint, order_index
)
select
  p.id,
  {m['module_number']},
  {esc(m['slug'])},
  {esc(m['title'])},
  {esc(m['weeks_range'])},
  {m['estimated_hours']},
  {esc(m['learning_outcomes'])},
  {esc(m['practical_tasks'])},
  {esc(m['resources'])},
  {esc(m['diagram_script'])},
  {esc(m['diagram_preset'])},
  {esc(m['diagram_animation'])},
  {esc(m['badge_slug'])},
  {esc(m.get('real_world_deliverable'))},
  {esc(m.get('zero_gpu_recipe', {}))},
  {esc(m.get('practice_checkpoint', {}))},
  {m['order_index']}
from public.phases p
where p.slug = {esc(m['phase_slug'])}
on conflict (slug) do update set
  module_number = excluded.module_number,
  title = excluded.title,
  weeks_range = excluded.weeks_range,
  estimated_hours = excluded.estimated_hours,
  learning_outcomes = excluded.learning_outcomes,
  practical_tasks = excluded.practical_tasks,
  resources = excluded.resources,
  diagram_script = excluded.diagram_script,
  diagram_preset = excluded.diagram_preset,
  diagram_animation = excluded.diagram_animation,
  badge_slug = excluded.badge_slug,
  real_world_deliverable = excluded.real_world_deliverable,
  zero_gpu_recipe = excluded.zero_gpu_recipe,
  practice_checkpoint = excluded.practice_checkpoint,
  order_index = excluded.order_index;\n""")

    lines.append("\n-- 7. LESSONS (DETAILED LESSONS FOR EVERY MODULE)")
    lines.append("delete from public.lessons;\n")
    for m in all_modules:
        for l in m.get('lessons', []):
            lines.append(f"""insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  {esc(l['lesson_code'])},
  {esc(l['slug'])},
  {esc(l['title'])},
  {l['duration_minutes']},
  {esc(l['lesson_type'])},
  {esc(l['roman_urdu_content'])},
  {esc(l['english_summary'])},
  {esc(l['code_example'])},
  {esc(l['diagram_script'])},
  {esc(l['diagram_type'])},
  {esc(l['resources'])},
  {l['xp_reward']},
  {l['order_index']}
from public.modules m
where m.slug = {esc(m['slug'])}
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;\n""")

    # Quizzes
    lines.append("\n-- 8. QUIZZES & QUESTIONS")
    lines.append("delete from public.quiz_questions;\n")
    quizzes = get_quizzes()
    for q in quizzes:
        lines.append(f"""insert into public.quizzes (module_id, title, passing_score_pct, xp_reward)
select m.id, {esc(q['title'])}, {q['passing_score_pct']}, {q['xp_reward']}
from public.modules m
where m.slug = {esc(q['module_slug'])}
on conflict (module_id) do update set
  title = excluded.title,
  passing_score_pct = excluded.passing_score_pct,
  xp_reward = excluded.xp_reward;\n""")

        for quest in q.get('questions', []):
            lines.append(f"""insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  {quest['question_number']},
  {esc(quest['question_roman_urdu'])},
  {esc(quest['options'])},
  {quest['correct_option_index']},
  {esc(quest['explanation_roman_urdu'])}
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = {esc(q['module_slug'])}
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;\n""")

    # 9. Engineering Deep-Dive Blogs
    lines.extend(get_blogs_sql())

    out_file = os.path.join(cur_dir, "migrations", "002_seed_syllabus.sql")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    
    print(f"Successfully generated {out_file} with {len(lines)} lines of SQL!")

if __name__ == "__main__":
    main()

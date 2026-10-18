import sys
sys.path.insert(0, 'supabase')
from seed_modules_phase1_2 import get_modules_phase1_2
from seed_modules_phase3_5 import get_modules_phase3_5
from seed_quizzes import get_quizzes

m1 = get_modules_phase1_2()
m2 = get_modules_phase3_5()
all_m = m1 + m2
print('Total modules:', len(all_m))
for m in all_m:
    print(f"Mod {m['module_number']}: {m['slug']} | {len(m['lessons'])} lessons | Checkpoint: {m.get('practice_checkpoint', {}).get('title')}")

total_lessons = sum(len(m['lessons']) for m in all_m)
print(f"Total lessons: {total_lessons}")

quizzes = get_quizzes()
print('Total quizzes:', len(quizzes))
print('Total quiz questions:', sum(len(q['questions']) for q in quizzes))

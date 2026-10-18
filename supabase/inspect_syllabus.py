import sys
sys.path.insert(0, 'supabase')
from seed_modules_phase1_2 import get_modules_phase1_2

m = get_modules_phase1_2()
print(f"Total Modules in Phase 1-2: {len(m)}")
total = 0
for mod in m:
    lessons = mod.get('lessons', [])
    total += len(lessons)
    print(f"Mod {mod['module_number']}: {mod['slug']} -> {len(lessons)} lessons")
    for l in lessons:
        print(f"    {l['lesson_code']}: {l['slug']} ({l['title']})")

print(f"\nTOTAL PHASE 1-2 LESSONS: {total}")

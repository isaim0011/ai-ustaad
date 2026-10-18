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
    cp = m.get('practice_checkpoint', {})
    hf = cp.get('hf_subproject', {})
    print(f"Mod {m['module_number']:02d}: {m['slug']} | HF Model: {hf.get('hf_model', 'MISSING')} | Dataset: {hf.get('hf_dataset', 'MISSING')}")
    assert 'hf_model' in hf, f"Module {m['module_number']} missing hf_model"
    assert 'hf_dataset' in hf, f"Module {m['module_number']} missing hf_dataset"
    assert 'colab_url' in hf, f"Module {m['module_number']} missing colab_url"
    assert 'kaggle_url' in hf, f"Module {m['module_number']} missing kaggle_url"
    assert 'starter_code' in hf, f"Module {m['module_number']} missing starter_code"
    assert 'gradio_code' in hf, f"Module {m['module_number']} missing gradio_code"

total_lessons = sum(len(m.get('lessons', [])) for m in all_m)
print(f"Total lessons: {total_lessons}")

quizzes = get_quizzes()
print('Total quizzes:', len(quizzes))
print('Total quiz questions:', sum(len(q['questions']) for q in quizzes))

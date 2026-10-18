# seed_modules_phase3_5.py
# Aggregates Phase 3 (Modules 6, 7, 8), Phase 4 (Modules 9, 10, 11), and Phase 5 (Modules 12, 13, 14)

from seed_modules_phase3 import get_modules_phase3
from seed_modules_phase4 import get_modules_phase4
from seed_modules_phase5 import get_modules_phase5

def get_modules_phase3_5():
    return get_modules_phase3() + get_modules_phase4() + get_modules_phase5()

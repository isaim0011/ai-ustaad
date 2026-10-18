import json
import os
from phase1_2 import phase1, phase2
from phase3_4 import phase3, phase4
from phase5_badges import phase5, badges, diagram_gallery, initial_user_profile

all_phases = [phase1, phase2, phase3, phase4, phase5]

output_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../frontend/src/lib/syllabus-data.ts"))

ts_content = f"""import type {{ Phase, Badge, DiagramGalleryItem, UserProfile }} from './types';

export const PHASES_DATA: Phase[] = {json.dumps(all_phases, indent=2)};

export const BADGES_DATA: Badge[] = {json.dumps(badges, indent=2)};

export const DIAGRAM_GALLERY: DiagramGalleryItem[] = {json.dumps(diagram_gallery, indent=2)};

export const INITIAL_USER_PROFILE: UserProfile = {json.dumps(initial_user_profile, indent=2)};
"""

with open(output_path, "w", encoding="utf-8") as f:
    f.write(ts_content)

print(f"SUCCESS: Written complete 14-module syllabus to: {output_path}")
print(f"Total Phases: {len(all_phases)}")
total_mods = sum(len(p['modules']) for p in all_phases)
total_less = sum(len(m['lessons']) for p in all_phases for m in p['modules'])
print(f"Total Modules: {total_mods}")
print(f"Total Lessons: {total_less}")

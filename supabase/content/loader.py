import os
import sys
import importlib

def enrich_with_mastery_content(all_modules):
    """
    Enriches all modules with in-depth, university-grade 4-part Roman Urdu content
    loaded from supabase/content/module_XX.py files.
    """
    content_dir = os.path.dirname(os.path.abspath(__file__))
    if content_dir not in sys.path:
        sys.path.insert(0, content_dir)

    for m in all_modules:
        mod_num = m.get("module_number")
        mod_file_name = f"module_{mod_num:02d}"
        mod_path = os.path.join(content_dir, f"{mod_file_name}.py")
        if not os.path.exists(mod_path):
            continue

        try:
            mod_module = importlib.import_module(mod_file_name)
            # Reload to capture any edits
            importlib.reload(mod_module)
            content_dict = getattr(mod_module, "LESSON_CONTENT", {})
        except Exception as e:
            print(f"[Warning] Failed to import {mod_file_name}: {e}")
            continue

        for lesson in m.get("lessons", []):
            code = lesson.get("lesson_code")
            slug = lesson.get("slug")
            
            # Check by lesson code or slug
            if code in content_dict:
                lesson["roman_urdu_content"] = content_dict[code]
            elif slug in content_dict:
                lesson["roman_urdu_content"] = content_dict[slug]

    return all_modules

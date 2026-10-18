# AI Mastery Platform — Supabase Database Architecture & Syllabus Engine

> **Production-grade PostgreSQL schema, Row Level Security (RLS), Gamification RPCs, and 20-Week Roman Urdu Dynamic Syllabus Engine for the AI Mastery Platform.**

---

## 1. Architecture Overview

The Supabase architecture powers both the dynamic syllabus delivery and user gamification (XP, daily streaks, quiz grading, and badge awards).

```
                      ┌────────────────────────────────────────┐
                      │              auth.users                │
                      └──────────────────┬─────────────────────┘
                                         │ (trigger on insert)
                                         ▼
                      ┌────────────────────────────────────────┐
                      │            public.profiles             │
                      │  (xp_points, streaks, track, role)     │
                      └───────┬──────────────┬───────────┬─────┘
                              │              │           │
           ┌──────────────────┘              │           └──────────────────┐
           ▼                                 ▼                              ▼
┌───────────────────────┐        ┌───────────────────────┐      ┌───────────────────────┐
│ user_lesson_progress  │        │  user_quiz_attempts   │      │      user_badges      │
│  (lesson completion)  │        │ (scores, pass/fail)   │      │  (unlocked trophies)  │
└───────────────────────┘        └───────────────────────┘      └───────────────────────┘

┌────────────────────────────────────────────────────────────────────────────────────────┐
│                                 Course Content Hierarchy                               │
│                                                                                        │
│  courses ──> phases ──> modules ──> lessons                                            │
│                 │          │           ├── roman_urdu_content                          │
│                 │          │           ├── code_example (Python/PyTorch/Rust)          │
│                 │          │           └── diagram_script (DiagramKit @animate flow)   │
│                 │          └── quizzes ──> quiz_questions (MCQs in Roman Urdu)         │
│                 └─────────────> specialization_tracks (Track A, Track B, Track C)      │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Directory Structure

```text
supabase/
├── migrations/
│   ├── 001_initial_schema.sql      # Extensions, tables, indexes, RLS policies, triggers, and RPCs
│   └── 002_seed_syllabus.sql       # Complete 20-week Roman Urdu curriculum, 14 modules, 44 lessons, quizzes
├── generate_full_syllabus.py       # Python generator script (reproducible seed builder)
├── seed_base.py                    # Base SQL definitions (Badges, Course, Phases, Tracks, Challenges)
├── seed_modules_phase1_2.py        # Modules 1-5 definitions with lessons and DiagramKit scripts
├── seed_modules_phase3_5.py        # Modules 6-14 definitions (ColPali, MCP, smolagents, Unsloth, GRPO)
├── seed_quizzes.py                 # Roman Urdu multiple-choice quiz questions and explanations
└── README.md                       # This documentation
```

---

## 3. Database Tables Reference

| Table | Description | RLS Policy |
| :--- | :--- | :--- |
| `public.profiles` | User profile linked to `auth.users`, tracks XP, current/longest streaks, selected track. | Select: Public (leaderboards); Update: `auth.uid() = id` |
| `public.courses` | Top-level course metadata (`ai-mastery-zero-to-production`). | Select: Public |
| `public.phases` | 5 core curriculum phases (Weeks 1 to 20). | Select: Public |
| `public.modules` | 14 in-depth modules with outcomes, practical tasks, DiagramKit scripts, and badge links. | Select: Public |
| `public.lessons` | 44+ granular lessons with Roman Urdu explanations, code, and DiagramKit scripts. | Select: Public |
| `public.specialization_tracks` | Track A (Developers), Track B (Business & Product), Track C (AI Research). | Select: Public |
| `public.badges` | 11 gamification trophies (e.g. `pehla-prompt`, `rag-master`, `agent-architect`). | Select: Public |
| `public.quizzes` | Module-level tests with passing thresholds (`passing_score_pct = 70`). | Select: Public |
| `public.quiz_questions` | MCQs in Roman Urdu with 4 options, correct answer index, and explanations. | Select: Public |
| `public.user_lesson_progress` | User lesson completion state and personal study notes. | Select/Insert/Update: `auth.uid() = user_id` |
| `public.user_quiz_attempts` | Quiz submission history, score percentage, and selected answers. | Select/Insert: `auth.uid() = user_id` |
| `public.user_badges` | Trophy unlocks awarded to students. | Select: Public; Insert: `auth.uid() = user_id` |
| `public.weekly_challenges` | Weekly coding and prompt design challenges with bonus XP. | Select: Public |
| `public.ai_chat_sessions` | AI Mentor chat conversation threads tied to specific lessons. | Select/Insert/Update/Delete: `auth.uid() = user_id` |
| `public.ai_chat_messages` | Individual messages in an AI chat session. | Select/Insert: verified via session ownership |

---

## 4. How to Run Migrations

### Method A: Supabase Local CLI (Recommended)

1. Make sure the Supabase CLI is installed:
   ```bash
   supabase --version
   ```
2. Start the local Supabase container stack:
   ```bash
   supabase start
   ```
3. Run the migrations and seed data:
   ```bash
   supabase db reset
   ```
   *This automatically executes all files in `supabase/migrations/` in numerical order.*

### Method B: Remote Supabase Dashboard (SQL Editor)

1. Open your project on [database.new](https://database.new) or [supabase.com/dashboard](https://supabase.com/dashboard).
2. Go to the **SQL Editor** in the left sidebar.
3. Open `migrations/001_initial_schema.sql`, copy the contents, paste into the editor, and click **Run**.
4. Open `migrations/002_seed_syllabus.sql`, copy the contents, paste into the editor, and click **Run**.

### Method C: Direct PostgreSQL Connection (`psql`)

```bash
# Set your Supabase connection string (Direct or Supavisor Transaction Pooler on port 6543)
export DATABASE_URL="postgresql://postgres.[project-ref]:[password]@aws-0-[region].pooler.supabase.com:6543/postgres"

# Execute schema migration
psql "$DATABASE_URL" -f supabase/migrations/001_initial_schema.sql

# Execute syllabus seed
psql "$DATABASE_URL" -f supabase/migrations/002_seed_syllabus.sql
```

---

## 5. Row Level Security (RLS) & Query Optimization

All tables have RLS enabled. Notice the optimized policy syntax using `(select auth.uid())`:

```sql
-- GOOD: Subquery ensures Postgres executes auth.uid() ONCE per query plan
create policy "Users can read own lesson progress"
  on public.user_lesson_progress for select
  using ((select auth.uid()) = user_id);

-- AVOID: Bare auth.uid() forces row-by-row re-evaluation:
-- using (auth.uid() = user_id);
```

This prevents sequential scans and allows Postgres to utilize index scans (`idx_progress_user` and `idx_quiz_attempts_user`) efficiently under high concurrency.

---

## 6. Stored Procedures & Gamification RPCs

### 1. `complete_lesson(p_lesson_id uuid, p_notes text)`

Marks a lesson as completed for the authenticated user and automatically executes gamification logic:

- **Streak Calculation**:
  - If `last_active_at::date = yesterday`: `current_streak = current_streak + 1`.
  - If `last_active_at::date = today`: streak is maintained.
  - If inactive for $>1$ day: `current_streak = 1`.
  - `longest_streak = max(longest_streak, current_streak)`.
- **First Lesson Badge**: Unlocks the `"pehla-prompt"` badge (`"Safar Ka Aaghaz"`) if this is the student's first completed lesson.
- **Module Completion Badge**: Checks if all lessons in the parent module are now complete. If yes, awards the module's badge (e.g. `"rag-master"`, `"agent-architect"`) and adds the badge's bonus XP to the user's profile.
- **Return Value**:
  ```json
  {
    "success": true,
    "already_completed": false,
    "xp_awarded": 25,
    "current_streak": 3,
    "longest_streak": 5,
    "badge_unlocked": "pehla-prompt",
    "module_completed": false
  }
  ```

### 2. `submit_quiz(p_quiz_id uuid, p_score_pct int, p_answers jsonb)`

Records a quiz attempt and awards XP/badges based on performance:

- Records the attempt in `user_quiz_attempts`.
- If `p_score_pct >= passing_score_pct` (70%) and this quiz was not previously passed, awards `quiz.xp_reward` to the user's profile.
- If `p_score_pct >= 90`, awards the prestigious `"top-performer"` badge (`"90%+ Quiz Score Champion"`, 200 XP bonus).
- **Return Value**:
  ```json
  {
    "success": true,
    "score_pct": 95,
    "passed": true,
    "xp_awarded": 225,
    "badge_unlocked": "top-performer"
  }
  ```

---

## 7. Calling RPCs from Frontend / Backend

### From SvelteKit / Supabase JS Client:

```typescript
import { createClient } from '@supabase/supabase-js';

const supabase = createClient(SUPABASE_URL, SUPABASE_ANON_KEY);

// 1. Mark lesson complete
const { data, error } = await supabase.rpc('complete_lesson', {
  p_lesson_id: 'c8121f64-9428-4ef1-a8bb-e613c0efcfd1',
  p_notes: 'NumPy memory layout aur broadcasting clear ho gaya!'
});

// 2. Submit quiz
const { data: quizResult, error: quizError } = await supabase.rpc('submit_quiz', {
  p_quiz_id: '7b5bcf41-3a05-4c27-9dc2-7c505cb7934c',
  p_score_pct: 92,
  p_answers: { "1": 0, "2": 1, "3": 1 }
});
```

### From Rust Backend (`sqlx`):

```rust
let res: serde_json::Value = sqlx::query_scalar!(
    "select public.complete_lesson($1, $2)",
    lesson_id,
    notes
)
.fetch_one(&pool)
.await?;
```

---

## 8. Modifying or Extending the Syllabus

To regenerate or adjust the syllabus:
1. Update `seed_modules_phase1_2.py`, `seed_modules_phase3_5.py`, or `seed_quizzes.py`.
2. Run the builder script:
   ```bash
   python supabase/generate_full_syllabus.py
   ```
3. Re-run `supabase/migrations/002_seed_syllabus.sql` in your database. All `INSERT` statements use `ON CONFLICT DO UPDATE`, ensuring safe, idempotent updates without dropping existing user data.

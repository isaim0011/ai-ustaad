-- ==============================================================================
-- AI MASTERY PLATFORM: 001_initial_schema.sql
-- Complete Production Database Architecture with RLS, Triggers & Gamification RPCs
-- ==============================================================================

-- 1. Extensions
create extension if not exists "uuid-ossp";
create extension if not exists "pgcrypto";
create extension if not exists "vector";

-- 2. Helper Functions & Triggers
create or replace function public.handle_updated_at()
returns trigger
language plpgsql
as $$
begin
  new.updated_at = now();
  return new;
end;
$$;

-- 3. Profiles (Linked to auth.users)
create table if not exists public.profiles (
  id uuid primary key references auth.users(id) on delete cascade,
  email text not null,
  full_name text,
  avatar_url text,
  role text not null default 'student' check (role in ('student', 'instructor', 'admin')),
  xp_points int not null default 0,
  current_streak int not null default 0,
  longest_streak int not null default 0,
  selected_track text default 'track-a',
  last_active_at timestamptz default now(),
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create trigger tr_profiles_updated_at
  before update on public.profiles
  for each row execute function public.handle_updated_at();

-- Auto-create profile upon auth.users signup
create or replace function public.handle_new_user()
returns trigger
language plpgsql
security definer
set search_path = public
as $$
begin
  insert into public.profiles (id, email, full_name, avatar_url, role)
  values (
    new.id,
    coalesce(new.email, ''),
    coalesce(new.raw_user_meta_data->>'full_name', new.raw_user_meta_data->>'name', split_part(new.email, '@', 1)),
    coalesce(new.raw_user_meta_data->>'avatar_url', new.raw_user_meta_data->>'picture', ''),
    coalesce(new.raw_user_meta_data->>'role', 'student')
  )
  on conflict (id) do nothing;
  return new;
end;
$$;

drop trigger if exists on_auth_user_created on auth.users;
create trigger on_auth_user_created
  after insert on auth.users
  for each row execute function public.handle_new_user();

-- 4. Courses
create table if not exists public.courses (
  id uuid primary key default gen_random_uuid(),
  slug text unique not null,
  title text not null,
  subtitle text,
  description text,
  language text default 'roman-urdu',
  total_weeks int default 20,
  level text default 'Beginner to Advanced',
  design_principles jsonb default '[]'::jsonb,
  zero_gpu_guide jsonb default '{}'::jsonb,
  is_published boolean default true,
  created_at timestamptz not null default now()
);

-- 5. Phases
create table if not exists public.phases (
  id uuid primary key default gen_random_uuid(),
  course_id uuid not null references public.courses(id) on delete cascade,
  phase_number int not null,
  slug text unique not null,
  title text not null,
  weeks_range text not null,
  level text not null,
  description text,
  diagram_script text,
  order_index int not null default 0
);

-- 6. Modules
create table if not exists public.modules (
  id uuid primary key default gen_random_uuid(),
  phase_id uuid not null references public.phases(id) on delete cascade,
  module_number int not null,
  slug text unique not null,
  title text not null,
  weeks_range text not null,
  estimated_hours int default 10,
  learning_outcomes jsonb default '[]'::jsonb,
  practical_tasks jsonb default '[]'::jsonb,
  resources jsonb default '[]'::jsonb,
  diagram_script text,
  diagram_preset text default 'midnight',
  diagram_animation text default 'flow',
  badge_slug text,
  real_world_deliverable text,
  zero_gpu_recipe jsonb default '{}'::jsonb,
  practice_checkpoint jsonb default '{}'::jsonb,
  order_index int not null default 0
);

-- 7. Lessons
create table if not exists public.lessons (
  id uuid primary key default gen_random_uuid(),
  module_id uuid not null references public.modules(id) on delete cascade,
  lesson_code text not null,
  slug text unique not null,
  title text not null,
  duration_minutes int default 25,
  lesson_type text default 'theory_and_code' check (lesson_type in ('theory', 'code', 'theory_and_code', 'project', 'lab')),
  roman_urdu_content text not null,
  english_summary text,
  code_example text,
  diagram_script text,
  diagram_type text default 'flow',
  resources jsonb default '[]'::jsonb,
  xp_reward int not null default 10,
  order_index int not null default 0
);

-- 8. Specialization Tracks
create table if not exists public.specialization_tracks (
  id uuid primary key default gen_random_uuid(),
  course_id uuid not null references public.courses(id) on delete cascade,
  track_code text not null,
  slug text unique not null,
  title text not null,
  description text,
  topics jsonb default '[]'::jsonb,
  diagram_script text
);

-- 9. Badges
create table if not exists public.badges (
  id uuid primary key default gen_random_uuid(),
  slug text unique not null,
  title text not null,
  roman_urdu_subtitle text,
  description text,
  icon text,
  xp_bonus int not null default 50,
  unlock_criteria jsonb default '{}'::jsonb
);

-- 10. Quizzes
create table if not exists public.quizzes (
  id uuid primary key default gen_random_uuid(),
  module_id uuid not null references public.modules(id) on delete cascade,
  title text not null,
  passing_score_pct int not null default 70,
  xp_reward int not null default 20,
  constraint quiz_module_unique unique (module_id)
);

-- 11. Quiz Questions
create table if not exists public.quiz_questions (
  id uuid primary key default gen_random_uuid(),
  quiz_id uuid not null references public.quizzes(id) on delete cascade,
  question_number int not null,
  question_roman_urdu text not null,
  options jsonb not null,
  correct_option_index int not null,
  explanation_roman_urdu text,
  constraint quiz_question_unique unique (quiz_id, question_number)
);

-- 12. User Lesson Progress
create table if not exists public.user_lesson_progress (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references public.profiles(id) on delete cascade,
  lesson_id uuid not null references public.lessons(id) on delete cascade,
  completed boolean not null default true,
  notes text,
  completed_at timestamptz not null default now(),
  constraint user_lesson_unique unique (user_id, lesson_id)
);

-- 13. User Quiz Attempts
create table if not exists public.user_quiz_attempts (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references public.profiles(id) on delete cascade,
  quiz_id uuid not null references public.quizzes(id) on delete cascade,
  score_pct int not null,
  passed boolean not null,
  answers jsonb default '{}'::jsonb,
  created_at timestamptz not null default now()
);

-- 14. User Badges
create table if not exists public.user_badges (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references public.profiles(id) on delete cascade,
  badge_id uuid not null references public.badges(id) on delete cascade,
  awarded_at timestamptz not null default now(),
  constraint user_badge_unique unique (user_id, badge_id)
);

-- 15. Weekly Challenges
create table if not exists public.weekly_challenges (
  id uuid primary key default gen_random_uuid(),
  week_number int not null,
  title text not null,
  description_roman_urdu text not null,
  xp_reward int not null default 50,
  is_active boolean not null default true,
  constraint weekly_challenge_unique unique (week_number)
);

-- 16. AI Chat Sessions & Messages
create table if not exists public.ai_chat_sessions (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references public.profiles(id) on delete cascade,
  title text default 'AI Mentor Conversation',
  context_lesson_id uuid references public.lessons(id) on delete set null,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create trigger tr_ai_chat_sessions_updated_at
  before update on public.ai_chat_sessions
  for each row execute function public.handle_updated_at();

create table if not exists public.ai_chat_messages (
  id uuid primary key default gen_random_uuid(),
  session_id uuid not null references public.ai_chat_sessions(id) on delete cascade,
  sender text not null check (sender in ('user', 'assistant', 'system')),
  content text not null,
  metadata jsonb default '{}'::jsonb,
  created_at timestamptz not null default now()
);

-- 17. Engineering Blogs
create table if not exists public.engineering_blogs (
  id uuid primary key default gen_random_uuid(),
  slug text unique not null,
  title text not null,
  category text not null,
  reading_time_minutes int not null default 10,
  summary_roman_urdu text not null,
  content_roman_urdu text not null,
  code_snippet text,
  compute_recipe text,
  diagram_script text not null,
  diagram_preset text default 'midnight',
  diagram_animation text default 'flow',
  order_index int not null default 0,
  created_at timestamptz not null default now()
);

-- 18. Indexes for Query Optimization
create index if not exists idx_phases_course on public.phases(course_id);
create index if not exists idx_modules_phase on public.modules(phase_id);
create index if not exists idx_lessons_module on public.lessons(module_id);
create index if not exists idx_lessons_order on public.lessons(module_id, order_index);
create index if not exists idx_tracks_course on public.specialization_tracks(course_id);
create index if not exists idx_quizzes_module on public.quizzes(module_id);
create index if not exists idx_quiz_questions_quiz on public.quiz_questions(quiz_id);
create index if not exists idx_progress_user on public.user_lesson_progress(user_id);
create index if not exists idx_progress_lesson on public.user_lesson_progress(lesson_id);
create index if not exists idx_quiz_attempts_user on public.user_quiz_attempts(user_id);
create index if not exists idx_user_badges_user on public.user_badges(user_id);
create index if not exists idx_chat_sessions_user on public.ai_chat_sessions(user_id);
create index if not exists idx_chat_messages_session on public.ai_chat_messages(session_id);
create index if not exists idx_engineering_blogs_order on public.engineering_blogs(order_index);
create index if not exists idx_engineering_blogs_slug on public.engineering_blogs(slug);

-- ==============================================================================
-- 19. Row Level Security (RLS)
-- Optimized using `(select auth.uid())` for statement-level caching
-- ==============================================================================

alter table public.profiles enable row level security;
alter table public.courses enable row level security;
alter table public.phases enable row level security;
alter table public.modules enable row level security;
alter table public.lessons enable row level security;
alter table public.specialization_tracks enable row level security;
alter table public.badges enable row level security;
alter table public.quizzes enable row level security;
alter table public.quiz_questions enable row level security;
alter table public.user_lesson_progress enable row level security;
alter table public.user_quiz_attempts enable row level security;
alter table public.user_badges enable row level security;
alter table public.weekly_challenges enable row level security;
alter table public.ai_chat_sessions enable row level security;
alter table public.ai_chat_messages enable row level security;
alter table public.engineering_blogs enable row level security;

-- Public Read Catalog Policies
create policy "Anyone can read courses"
  on public.courses for select
  using (true);

create policy "Anyone can read phases"
  on public.phases for select
  using (true);

create policy "Anyone can read modules"
  on public.modules for select
  using (true);

create policy "Anyone can read lessons"
  on public.lessons for select
  using (true);

create policy "Anyone can read specialization tracks"
  on public.specialization_tracks for select
  using (true);

create policy "Anyone can read badges"
  on public.badges for select
  using (true);

create policy "Anyone can read quizzes"
  on public.quizzes for select
  using (true);

create policy "Anyone can read quiz questions"
  on public.quiz_questions for select
  using (true);

create policy "Anyone can read weekly challenges"
  on public.weekly_challenges for select
  using (true);

create policy "Anyone can read engineering blogs"
  on public.engineering_blogs for select
  using (true);

-- User Profiles Policies
create policy "Anyone can read profiles for leaderboards"
  on public.profiles for select
  using (true);

create policy "Users can insert own profile"
  on public.profiles for insert
  with check ((select auth.uid()) = id);

create policy "Users can update own profile"
  on public.profiles for update
  using ((select auth.uid()) = id)
  with check ((select auth.uid()) = id);

-- User Lesson Progress Policies
create policy "Users can read own lesson progress"
  on public.user_lesson_progress for select
  using ((select auth.uid()) = user_id);

create policy "Users can insert own lesson progress"
  on public.user_lesson_progress for insert
  with check ((select auth.uid()) = user_id);

create policy "Users can update own lesson progress"
  on public.user_lesson_progress for update
  using ((select auth.uid()) = user_id)
  with check ((select auth.uid()) = user_id);

create policy "Users can delete own lesson progress"
  on public.user_lesson_progress for delete
  using ((select auth.uid()) = user_id);

-- User Quiz Attempts Policies
create policy "Users can read own quiz attempts"
  on public.user_quiz_attempts for select
  using ((select auth.uid()) = user_id);

create policy "Users can insert own quiz attempts"
  on public.user_quiz_attempts for insert
  with check ((select auth.uid()) = user_id);

-- User Badges Policies
create policy "Anyone can view awarded user badges"
  on public.user_badges for select
  using (true);

create policy "Users can insert own badges"
  on public.user_badges for insert
  with check ((select auth.uid()) = user_id);

-- AI Chat Sessions Policies
create policy "Users can read own chat sessions"
  on public.ai_chat_sessions for select
  using ((select auth.uid()) = user_id);

create policy "Users can insert own chat sessions"
  on public.ai_chat_sessions for insert
  with check ((select auth.uid()) = user_id);

create policy "Users can update own chat sessions"
  on public.ai_chat_sessions for update
  using ((select auth.uid()) = user_id)
  with check ((select auth.uid()) = user_id);

create policy "Users can delete own chat sessions"
  on public.ai_chat_sessions for delete
  using ((select auth.uid()) = user_id);

-- AI Chat Messages Policies
create policy "Users can read own chat messages"
  on public.ai_chat_messages for select
  using (
    exists (
      select 1 from public.ai_chat_sessions s
      where s.id = ai_chat_messages.session_id
      and s.user_id = (select auth.uid())
    )
  );

create policy "Users can insert own chat messages"
  on public.ai_chat_messages for insert
  with check (
    exists (
      select 1 from public.ai_chat_sessions s
      where s.id = ai_chat_messages.session_id
      and s.user_id = (select auth.uid())
    )
  );

-- ==============================================================================
-- 19. Gamification RPC Functions
-- ==============================================================================

-- Function 1: Complete Lesson, award XP, compute daily streak, unlock badges
create or replace function public.complete_lesson(
  p_lesson_id uuid,
  p_notes text default null
)
returns jsonb
language plpgsql
security definer
set search_path = public
as $$
declare
  v_user_id uuid;
  v_lesson record;
  v_module_id uuid;
  v_already_completed boolean := false;
  v_user record;
  v_new_streak int := 1;
  v_longest_streak int := 1;
  v_xp_awarded int := 0;
  v_badge_unlocked text := null;
  v_completed_count int;
  v_total_lessons int;
  v_module_completed_count int;
  v_module_completed boolean := false;
  v_module_badge_slug text;
  v_module_badge record;
begin
  v_user_id := auth.uid();
  if v_user_id is null then
    raise exception 'Unauthorized: Please log in to record progress.';
  end if;

  select id, module_id, xp_reward, title into v_lesson
  from public.lessons
  where id = p_lesson_id;

  if not found then
    raise exception 'Lesson with id % not found.', p_lesson_id;
  end if;

  v_module_id := v_lesson.module_id;

  -- Check if already completed
  select exists (
    select 1 from public.user_lesson_progress
    where user_id = v_user_id and lesson_id = p_lesson_id and completed = true
  ) into v_already_completed;

  if not v_already_completed then
    v_xp_awarded := v_lesson.xp_reward;

    -- Upsert lesson progress
    insert into public.user_lesson_progress (user_id, lesson_id, completed, notes, completed_at)
    values (v_user_id, p_lesson_id, true, p_notes, now())
    on conflict (user_id, lesson_id)
    do update set completed = true, notes = coalesce(excluded.notes, user_lesson_progress.notes), completed_at = now();

    -- Calculate streak & update user profile
    select xp_points, current_streak, longest_streak, last_active_at into v_user
    from public.profiles
    where id = v_user_id;

    if v_user.last_active_at is null then
      v_new_streak := 1;
    elsif v_user.last_active_at::date = (now() - interval '1 day')::date then
      v_new_streak := coalesce(v_user.current_streak, 0) + 1;
    elsif v_user.last_active_at::date = now()::date then
      v_new_streak := greatest(coalesce(v_user.current_streak, 1), 1);
    else
      v_new_streak := 1;
    end if;

    v_longest_streak := greatest(coalesce(v_user.longest_streak, 0), v_new_streak);

    update public.profiles
    set xp_points = xp_points + v_xp_awarded,
        current_streak = v_new_streak,
        longest_streak = v_longest_streak,
        last_active_at = now(),
        updated_at = now()
    where id = v_user_id;

    -- Check if first lesson ever completed across platform -> Award "Pehla Prompt" badge
    select count(*) into v_completed_count
    from public.user_lesson_progress
    where user_id = v_user_id and completed = true;

    if v_completed_count = 1 then
      insert into public.user_badges (user_id, badge_id, awarded_at)
      select v_user_id, b.id, now()
      from public.badges b
      where b.slug = 'pehla-prompt'
      on conflict (user_id, badge_id) do nothing;

      v_badge_unlocked := 'pehla-prompt';
    end if;

    -- Check if all lessons in this module are completed
    select count(*) into v_total_lessons
    from public.lessons
    where module_id = v_module_id;

    select count(*) into v_module_completed_count
    from public.user_lesson_progress ulp
    join public.lessons l on l.id = ulp.lesson_id
    where ulp.user_id = v_user_id and ulp.completed = true and l.module_id = v_module_id;

    if v_module_completed_count >= v_total_lessons and v_total_lessons > 0 then
      v_module_completed := true;

      select badge_slug into v_module_badge_slug
      from public.modules
      where id = v_module_id;

      if v_module_badge_slug is not null then
        select id, xp_bonus, slug into v_module_badge
        from public.badges
        where slug = v_module_badge_slug;

        if found then
          insert into public.user_badges (user_id, badge_id, awarded_at)
          values (v_user_id, v_module_badge.id, now())
          on conflict (user_id, badge_id) do nothing;

          update public.profiles
          set xp_points = xp_points + v_module_badge.xp_bonus
          where id = v_user_id;

          v_badge_unlocked := case 
            when v_badge_unlocked is not null then v_badge_unlocked || ', ' || v_module_badge.slug
            else v_module_badge.slug
          end;
          v_xp_awarded := v_xp_awarded + v_module_badge.xp_bonus;
        end if;
      end if;
    end if;

  else
    -- Already completed previously, optionally update notes
    if p_notes is not null then
      update public.user_lesson_progress
      set notes = p_notes
      where user_id = v_user_id and lesson_id = p_lesson_id;
    end if;
  end if;

  return jsonb_build_object(
    'success', true,
    'already_completed', v_already_completed,
    'xp_awarded', v_xp_awarded,
    'current_streak', v_new_streak,
    'longest_streak', v_longest_streak,
    'badge_unlocked', v_badge_unlocked,
    'module_completed', v_module_completed
  );
end;
$$;

-- Function 2: Submit Quiz, record attempt, calculate XP & Top Performer badge
create or replace function public.submit_quiz(
  p_quiz_id uuid,
  p_score_pct int,
  p_answers jsonb default '{}'::jsonb
)
returns jsonb
language plpgsql
security definer
set search_path = public
as $$
declare
  v_user_id uuid;
  v_quiz record;
  v_passed boolean;
  v_already_passed boolean := false;
  v_xp_awarded int := 0;
  v_badge_unlocked text := null;
  v_top_badge record;
begin
  v_user_id := auth.uid();
  if v_user_id is null then
    raise exception 'Unauthorized: Please log in to submit quiz.';
  end if;

  select id, module_id, passing_score_pct, xp_reward into v_quiz
  from public.quizzes
  where id = p_quiz_id;

  if not found then
    raise exception 'Quiz with id % not found.', p_quiz_id;
  end if;

  v_passed := p_score_pct >= v_quiz.passing_score_pct;

  -- Record attempt
  insert into public.user_quiz_attempts (user_id, quiz_id, score_pct, passed, answers, created_at)
  values (v_user_id, p_quiz_id, p_score_pct, v_passed, p_answers, now());

  -- Check if already passed in previous attempts
  select exists (
    select 1 from public.user_quiz_attempts
    where user_id = v_user_id and quiz_id = p_quiz_id and passed = true
    and created_at < now() - interval '1 second'
  ) into v_already_passed;

  -- Award XP only if newly passed
  if v_passed and not v_already_passed then
    v_xp_awarded := v_quiz.xp_reward;
    update public.profiles
    set xp_points = xp_points + v_xp_awarded,
        last_active_at = now()
    where id = v_user_id;
  end if;

  -- If scored 90% or above, award "Top Performer" badge
  if p_score_pct >= 90 then
    select id, xp_bonus, slug into v_top_badge
    from public.badges
    where slug = 'top-performer';

    if found then
      if not exists (select 1 from public.user_badges where user_id = v_user_id and badge_id = v_top_badge.id) then
        insert into public.user_badges (user_id, badge_id, awarded_at)
        values (v_user_id, v_top_badge.id, now());

        update public.profiles
        set xp_points = xp_points + v_top_badge.xp_bonus
        where id = v_user_id;

        v_badge_unlocked := 'top-performer';
        v_xp_awarded := v_xp_awarded + v_top_badge.xp_bonus;
      end if;
    end if;
  end if;

  return jsonb_build_object(
    'success', true,
    'score_pct', p_score_pct,
    'passed', v_passed,
    'xp_awarded', v_xp_awarded,
    'badge_unlocked', v_badge_unlocked
  );
end;
$$;

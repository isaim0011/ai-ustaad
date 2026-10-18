# Stack Digest: Supabase (PostgreSQL + RLS + Auth) & Svelte 5 + Tailwind v4

## Versions & Sources
- **Supabase JS**: `@supabase/supabase-js` `^2.49.0`, `@supabase/ssr` `^0.6.0` — https://supabase.com/docs
- **Svelte**: `^5.25.0` (Runes mode: `$state`, `$derived`, `$effect`, `$props`) — https://svelte.dev/docs/svelte/overview
- **SvelteKit**: `@sveltejs/kit` `^2.20.0` + `@sveltejs/adapter-auto`
- **TailwindCSS**: `^4.0.0` + `@tailwindcss/vite`
- **DiagramKit Web Component / NPM**: `@dkit/diagram` `v0.2.0` (`C:\Users\Bimo\Desktop\diagramkit\integrations\npm` & `studio/dkit-diagram.js`)

## Exact Signatures & Idiomatic Patterns
1. **Supabase Auth & RLS**:
   - Tables: `profiles`, `courses`, `phases`, `modules`, `lessons`, `quizzes`, `quiz_questions`, `badges`, `user_progress`, `user_badges`, `user_xp_ledger`, `ai_chat_sessions`, `ai_chat_messages`.
   - JWT Verification in Rust: Supports both asymmetric JWKS (`{SUPABASE_URL}/auth/v1/.well-known/jwks.json`) and symmetric HS256 (`SUPABASE_JWT_SECRET`).
   - RLS uses `(select auth.uid()) = user_id` for optimal PostgreSQL query plan caching.
2. **Svelte 5 Runes**:
   - Component props: `let { lesson, onComplete } = $props();`
   - Reactive state: `let activeTab = $state<'lesson' | 'diagram' | 'quiz' | 'playground' | 'chat'>('lesson');`
   - Derived state: `let progressPct = $derived(Math.round((completedCount / totalCount) * 100));`
3. **DiagramKit in Svelte 5**:
   - Can render via backend `/api/diagram/render` (native Rust `dkit-diagram` zero-latency SVG with `@animate flow|pulse|wave|ripple|glow|draw`) OR client-side via `<dkit-diagram>` custom element / `dkit.wasm`.

## Gotchas
- In Svelte 5, use `onclick={...}` instead of `on:click={...}`.
- Wrap `(select auth.uid())` in RLS policies so Postgres caches the `auth.uid()` evaluation per statement rather than per row.

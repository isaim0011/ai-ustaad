# Stack Digest: Rust Axum 0.8 + SQLx 0.8 + DiagramKit (`dkit-api` / `dkit-diagram`)

## Versions & Sources
- **Rustc / Cargo**: `1.98.1` (edition `2021`, `rust-version = "1.80"`)
- **Axum**: `0.8.x` — https://docs.rs/axum/latest/axum/
- **SQLx**: `0.8.x` — https://docs.rs/sqlx/latest/sqlx/
- **jsonwebtoken**: `9.3` — https://docs.rs/jsonwebtoken/latest/jsonwebtoken/
- **DiagramKit Local Crates**: `v0.1.0` (`C:\Users\Bimo\Desktop\diagramkit\crates\dkit-core`, `dkit-diagram`, `dkit-api`)

## Exact Signatures & Idiomatic Patterns
1. **Axum 0.8 Path Syntax**:
   - Route parameters use `{param}` instead of `:param`, e.g., `.route("/api/modules/{slug}", get(handler))`
2. **SQLx with Supabase Supavisor Transaction Pooler**:
   - `PgConnectOptions::from_str(database_url)?.statement_cache_capacity(0)` MUST be set when using port `6543` transaction pooler.
3. **DiagramKit Rust Native Rendering**:
   - `dkit_api::script::compile(src: &str) -> Result<Diagram, String>`
   - `dkit_diagram::render(d: &Diagram, opts: &RenderOptions) -> Result<Output, Error>`
   - `dkit_api::route(req: &Req) -> Resp`
   - Built-in presets: `paper`, `mono`, `blueprint`, `midnight`, `sunset`, `forest`, `ocean`, `grape`, `contrast`, `print`
   - Built-in animations: `flow`, `pulse`, `draw`, `glow`, `wave`, `ripple`, `all`, `none`
   - 17 Diagram types: `flow`, `arch`, `state`, `tree`, `deps`, `seq`, `time`, `quad`, `bar`, `pyramid`, `funnel`, `layers`, `er`, `class`, `mind`, `gantt`, `pie`.

## Gotchas
- Axum 0.8 panics at startup if old `:param` syntax is used. Always use `{param}`.
- DiagramKit's `verify::check` and `lint_svg` run automatically and return deterministic WCAG AA compliant SVGs with CSS keyframe animations.

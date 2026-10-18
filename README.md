# AI Ustaad (AI Mastery Platform) 

> **Production-grade AI Engineering Learning Platform** taught in Roman Urdu & English, built with **SvelteKit 2 (Svelte 5 Runes) + TailwindCSS v4**, backed by **Supabase PostgreSQL & Auth**, and powered by a high-performance **Rust Axum DiagramKit backend**.

[![GitHub Repository](https://img.shields.io/badge/GitHub-isaim0011%2Fai--ustaad-blue?logo=github)](https://github.com/isaim0011/ai-ustaad)
[![Cloudflare Pages](https://img.shields.io/badge/Cloudflare_Pages-ai--ustaad.pages.dev-orange?logo=cloudflare)](https://ai-ustaad.pages.dev)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

##  Overview

**AI Ustaad** is designed to take engineers from zero to deploying production-grade AI systems, LLM architectures, RAG pipelines, fine-tuning, and multi-agent swarms. Every concept is explained with deep conceptual clarity, architectural diagrams, and interactive quizzes.

### Key Features
- **Claude.ai Warm Minimalist UI**: Warm terracotta aesthetic (`#c96442`), serif headings, and dark/light mode toggles.
- **SvelteKit 2 + Svelte 5 (Runes)**: Ultra-fast, reactive client interface using modern Svelte runes (`$state`, `$derived`, `$props`).
- **Supabase Cloud Infrastructure**: PostgreSQL database with Row-Level Security (RLS), custom RPCs (`complete_lesson`, `submit_quiz`), and user session cookies via `@supabase/ssr`.
- **Rust Axum DiagramKit Backend**: High-throughput SVG diagram rendering and AI mentor endpoint in native Rust.
- **Interactive Quizzes & Badges**: Real-time evaluation, XP tracking, streaks, and gamified achievement unlocks.
- **Edge Deployment on Cloudflare Pages**: Fully serverless SvelteKit deployment via `@sveltejs/adapter-cloudflare`.

---

## ️ Project Architecture

```
ai-mastery-platform/
├── frontend/                # SvelteKit 2 + Svelte 5 + TailwindCSS v4 application
│   ├── src/
│   │   ├── lib/             # Reusable components (TopNav, Footer, Markdown, Diagram)
│   │   └── routes/          # App routes (/, /learn, /blog, /mentor, /profile, /auth)
│   ├── svelte.config.js     # Configured with @sveltejs/adapter-cloudflare
│   └── package.json
├── backend/                 # Rust Axum backend
│   ├── src/                 # REST endpoints (/api/diagrams/render, /api/ai/mentor)
│   └── Cargo.toml
├── supabase/                # PostgreSQL migrations, schema, and seed scripts
│   └── migrations/          # 001_initial_schema.sql, RLS policies, RPC functions
└── PLAN.md                  # Comprehensive platform architecture specification
```

---

##  Getting Started

### Prerequisites
- Node.js 18+ & npm
- Rust & Cargo (optional, for local diagram rendering backend)
- Supabase project credentials

### 1. Frontend Setup
```bash
cd frontend
cp .env.example .env
npm install
npm run dev
```

### 2. Backend Setup (Optional)
```bash
cd backend
cp .env.example .env
cargo run
```

---

##  Deployment

- **Frontend**: Deployed to [Cloudflare Pages](https://ai-ustaad.pages.dev) via `@sveltejs/adapter-cloudflare`.
- **Database & Auth**: Hosted on [Supabase](https://supabase.com).

---

## ‍ Author

Built with ❤️ by **[Bimo (@isaim0011)](https://github.com/isaim0011)**.

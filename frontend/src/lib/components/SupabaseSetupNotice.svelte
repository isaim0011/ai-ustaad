<script lang="ts">
	import { AlertCircle, Key, Database, ArrowRight, CheckCircle2 } from 'lucide-svelte';
</script>

<div class="mx-auto my-12 max-w-2xl px-4">
	<div class="overflow-hidden rounded-2xl border border-amber-500/30 bg-[#faf9f5] shadow-sm dark:border-amber-500/20 dark:bg-[#232321]">
		<div class="border-b border-amber-500/20 bg-amber-500/10 px-6 py-4">
			<div class="flex items-center gap-3">
				<div class="flex h-9 w-9 items-center justify-center rounded-xl bg-amber-500/20 text-amber-700 dark:text-amber-400">
					<Database class="h-5 w-5" />
				</div>
				<div>
					<h2 class="font-serif text-lg font-semibold text-[#141413] dark:text-[#f5f4ed]">
						Supabase Configuration (Optional for Cloudflare Preview)
					</h2>
					<p class="text-xs text-[#6f6e69] dark:text-[#a19f97]">
						AI Ustaad (ai-ustaad.pages.dev) uses Supabase PostgreSQL for persistent user progress & gamification
					</p>
				</div>
			</div>
		</div>

		<div class="p-6 space-y-5 text-sm text-[#2c2b28] dark:text-[#dcd9ce]">
			<p class="leading-relaxed">
				App is currently running with placeholder environment variables. To connect to your Supabase instance, follow these 3 quick steps:
			</p>

			<ol class="space-y-4">
				<li class="flex items-start gap-3">
					<span class="flex h-6 w-6 shrink-0 items-center justify-center rounded-full bg-[#c96442] text-xs font-bold text-white">1</span>
					<div>
						<div class="font-medium text-[#141413] dark:text-[#f5f4ed]">Apply Database Migrations</div>
						<p class="mt-0.5 text-xs text-[#6f6e69] dark:text-[#a19f97]">
							In your Supabase SQL Editor, run <code class="rounded bg-[#f0eee6] px-1 py-0.5 font-mono text-[11px] text-[#c96442] dark:bg-[#2e2d2a]">001_initial_schema.sql</code> and <code class="rounded bg-[#f0eee6] px-1 py-0.5 font-mono text-[11px] text-[#c96442] dark:bg-[#2e2d2a]">002_seed_syllabus.sql</code> from <code class="rounded bg-[#f0eee6] px-1 py-0.5 font-mono text-[11px] dark:bg-[#2e2d2a]">supabase/migrations/</code>.
						</p>
					</div>
				</li>

				<li class="flex items-start gap-3">
					<span class="flex h-6 w-6 shrink-0 items-center justify-center rounded-full bg-[#c96442] text-xs font-bold text-white">2</span>
					<div>
						<div class="font-medium text-[#141413] dark:text-[#f5f4ed]">Configure Environment Variables</div>
						<p class="mt-0.5 text-xs text-[#6f6e69] dark:text-[#a19f97]">
							Copy <code class="rounded bg-[#f0eee6] px-1 py-0.5 font-mono text-[11px] dark:bg-[#2e2d2a]">.env.example</code> to <code class="rounded bg-[#f0eee6] px-1 py-0.5 font-mono text-[11px] dark:bg-[#2e2d2a]">.env</code> inside <code class="rounded bg-[#f0eee6] px-1 py-0.5 font-mono text-[11px] dark:bg-[#2e2d2a]">frontend/</code> and add your Project URL and Anon/Publishable Key:
						</p>
						<pre class="mt-2 overflow-x-auto rounded-lg border border-[#e5e2d9] bg-[#f0eee6] p-3 text-xs font-mono text-[#141413] dark:border-[#343330] dark:bg-[#181817] dark:text-[#f5f4ed]">PUBLIC_SUPABASE_URL=https://your-project.supabase.co
PUBLIC_SUPABASE_ANON_KEY=your-publishable-or-anon-key
PUBLIC_API_URL=http://127.0.0.1:8080</pre>
					</div>
				</li>

				<li class="flex items-start gap-3">
					<span class="flex h-6 w-6 shrink-0 items-center justify-center rounded-full bg-[#c96442] text-xs font-bold text-white">3</span>
					<div>
						<div class="font-medium text-[#141413] dark:text-[#f5f4ed]">Enable Auth Providers & Redirect URLs</div>
						<p class="mt-0.5 text-xs text-[#6f6e69] dark:text-[#a19f97]">
							In Supabase Dashboard &gt; Authentication &gt; URL Configuration, add <code class="rounded bg-[#f0eee6] px-1 py-0.5 font-mono text-[11px] text-[#c96442] dark:bg-[#2e2d2a]">http://localhost:5173/auth/callback</code> and <code class="rounded bg-[#f0eee6] px-1 py-0.5 font-mono text-[11px] text-[#c96442] dark:bg-[#2e2d2a]">https://ai-ustaad.pages.dev/auth/callback</code> to Redirect URLs.
						</p>
					</div>
				</li>
			</ol>
		</div>
	</div>
</div>

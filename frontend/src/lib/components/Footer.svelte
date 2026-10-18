<script lang="ts">
	import { Sparkles, Terminal, BookOpen, Compass, ExternalLink } from 'lucide-svelte';
</script>

<footer class="mt-auto border-t border-[#e5e2d9] bg-[#f0eee6]/60 dark:border-[#343330] dark:bg-[#181817]">
	<div class="mx-auto max-w-7xl px-4 py-12 sm:px-6 lg:px-8">
		<div class="grid grid-cols-1 gap-8 md:grid-cols-4">
			<!-- Col 1: Brand & Roman Urdu Mission -->
			<div class="md:col-span-2">
				<div class="flex items-center gap-2">
					<div class="flex h-7 w-7 items-center justify-center rounded-lg bg-[#c96442] text-white font-serif font-bold text-sm">
						AU
					</div>
					<span class="font-serif text-lg font-semibold tracking-tight text-[#141413] dark:text-[#f5f4ed]">
						AI Ustaad
					</span>
					<span class="rounded bg-[#c96442]/10 px-2 py-0.5 text-xs font-mono font-medium text-[#c96442] dark:bg-[#c96442]/20">
						ai-ustaad.pages.dev
					</span>
				</div>
				<p class="mt-3 max-w-md text-sm leading-relaxed text-[#6f6e69] dark:text-[#a19f97]">
					Zero se Hero tak: South Asia ka pehla complete, production-grade Roman Urdu AI Engineering curriculum. Zero-GPU cloud recipes, first-principles tensor math, aur 2026 SOTA tools.
				</p>
				<div class="mt-4 flex items-center gap-4 text-xs font-mono text-[#6f6e69] dark:text-[#a19f97]">
					<span>5 Phases</span>
					<span>•</span>
					<span>14 Modules</span>
					<span>•</span>
					<span>Zero-GPU Guaranteed</span>
				</div>
			</div>

			<!-- Col 2: Learning Pathways -->
			<div>
				<h3 class="text-xs font-mono uppercase tracking-wider text-[#141413] dark:text-[#f5f4ed]">
					Pathways
				</h3>
				<ul class="mt-3 space-y-2 text-sm text-[#6f6e69] dark:text-[#a19f97]">
					<li>
						<a href="/learn" class="transition-colors hover:text-[#c96442]">Curriculum Overview</a>
					</li>
					<li>
						<a href="/blog" class="transition-colors hover:text-[#c96442]">Engineering Blogs</a>
					</li>
					<li>
						<a href="/mentor" class="transition-colors hover:text-[#c96442]">AI Mentor (Urdu)</a>
					</li>
					<li>
						<a href="/learn/zero-gpu-cloud-compute-guide" class="transition-colors hover:text-[#c96442]">Zero-GPU Survival Guide</a>
					</li>
				</ul>
			</div>

			<!-- Col 3: Community & Open Source -->
			<div>
				<h3 class="text-xs font-mono uppercase tracking-wider text-[#141413] dark:text-[#f5f4ed]">
					System & Stack
				</h3>
				<ul class="mt-3 space-y-2 text-sm text-[#6f6e69] dark:text-[#a19f97]">
					<li>
						<span class="inline-flex items-center gap-1.5 text-xs font-mono">
							<span class="h-1.5 w-1.5 rounded-full bg-emerald-500"></span>
							SvelteKit 2 + Svelte 5
						</span>
					</li>
					<li>
						<span class="inline-flex items-center gap-1.5 text-xs font-mono">
							<span class="h-1.5 w-1.5 rounded-full bg-emerald-500"></span>
							Supabase PostgreSQL + RLS
						</span>
					</li>
					<li>
						<span class="inline-flex items-center gap-1.5 text-xs font-mono">
							<span class="h-1.5 w-1.5 rounded-full bg-emerald-500"></span>
							DiagramKit Core Engine
						</span>
					</li>
					<li>
						<span class="inline-flex items-center gap-1.5 text-xs font-mono">
							<span class="h-1.5 w-1.5 rounded-full bg-emerald-500"></span>
							Rust Axum 0.8 Backend
						</span>
					</li>
				</ul>
			</div>
		</div>

		<!-- Bottom Line: Built by Bimo -->
		<div class="mt-10 flex flex-col items-center justify-between border-t border-[#e5e2d9] pt-6 text-xs text-[#6f6e69] sm:flex-row dark:border-[#343330] dark:text-[#a19f97]">
			<p>© 2026 AI Ustaad (ai-ustaad.pages.dev). All rights reserved.</p>
			<p class="mt-3 sm:mt-0 font-medium">
				Built by <a
					href="https://github.com/isaim0011"
					target="_blank"
					rel="noopener noreferrer"
					class="font-semibold text-[#c96442] underline underline-offset-4 transition-colors hover:text-[#d97757]"
				>
					Bimo
				</a>
			</p>
		</div>
	</div>
</footer>

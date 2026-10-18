<script lang="ts">
	import { Sparkles, Terminal, BookOpen, Compass, ExternalLink } from 'lucide-svelte';
	import Logo from '$lib/components/Logo.svelte';
</script>

<footer class="mt-auto border-t border-[#e5e2d9] bg-[#f0eee6]/60 dark:border-[#2c2b28] dark:bg-[#191918]">
	<div class="mx-auto max-w-7xl px-4 py-12 sm:px-6 lg:px-8">
		<div class="grid grid-cols-1 gap-8 md:grid-cols-4">
			<!-- Col 1: Brand & Roman Urdu Mission -->
			<div class="md:col-span-2">
				<div class="flex items-center gap-2.5">
					<Logo size={32} />
					<span class="font-serif text-lg font-bold tracking-tight text-[#141413] dark:text-[#f5f4ed]">
						AI Ustaad
					</span>
					<span class="rounded-full bg-[#c96442]/10 px-2.5 py-0.5 text-xs font-mono font-medium text-[#c96442] dark:bg-[#c96442]/20">
						ai-ustaad.pages.dev
					</span>
				</div>
				<p class="mt-3 max-w-md text-sm leading-relaxed text-[#6f6e69] dark:text-[#a19f97]">
					Zero se Hero tak: South Asia ka pehla complete, production-grade Roman Urdu AI Engineering curriculum. Zero-GPU cloud recipes, first-principles tensor math, aur 2026 SOTA tools.
				</p>
				<div class="mt-4 flex items-center gap-4 text-xs font-mono text-[#6f6e69] dark:text-[#a19f97]">
					<span>Prerequisite Track: Python Zero Se Hero</span>
					<span>•</span>
					<span>5 AI Phases</span>
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

			<!-- Col 3: Community & Practice Notebooks -->
			<div>
				<h3 class="text-xs font-mono uppercase tracking-wider text-[#141413] dark:text-[#f5f4ed]">
					Free Practice & Tools
				</h3>
				<ul class="mt-3 space-y-2 text-sm text-[#6f6e69] dark:text-[#a19f97]">
					<li>
						<a href="https://colab.research.google.com" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-1.5 transition-colors hover:text-[#c96442]">
							<span>Google Colab Free T4</span>
							<ExternalLink class="h-3 w-3 text-[#6f6e69]" />
						</a>
					</li>
					<li>
						<a href="https://www.kaggle.com" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-1.5 transition-colors hover:text-[#c96442]">
							<span>Kaggle Dual-T4 (30h/wk)</span>
							<ExternalLink class="h-3 w-3 text-[#6f6e69]" />
						</a>
					</li>
					<li>
						<a href="https://github.com/isaim0011" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-1.5 transition-colors hover:text-[#c96442]">
							<span>Open Source GitHub</span>
							<ExternalLink class="h-3 w-3 text-[#6f6e69]" />
						</a>
					</li>
				</ul>
			</div>
		</div>

		<!-- Bottom Line: Built by Bimo -->
		<div class="mt-10 flex flex-col items-center justify-between border-t border-[#e5e2d9] pt-6 text-xs text-[#6f6e69] sm:flex-row dark:border-[#2c2b28] dark:text-[#a19f97]">
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

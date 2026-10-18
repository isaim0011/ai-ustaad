<script lang="ts">
	import { ArrowRight, Sparkles, Cpu, Terminal, Shield, Zap, BookOpen, Layers, CheckCircle2, ExternalLink } from 'lucide-svelte';
	import Diagram from '$lib/components/Diagram.svelte';
	import type { PageData } from './$types';

	let { data }: { data: PageData } = $props();

	const course = $derived(data.course);
	const phases = $derived(data.phases ?? []);
	const tracks = $derived(data.tracks ?? []);
	const blogs = $derived(data.featuredBlogs ?? []);
</script>

<div class="relative overflow-hidden">
	<!-- Hero Section -->
	<section class="relative mx-auto max-w-7xl px-4 pt-16 pb-20 sm:px-6 sm:pt-24 sm:pb-28 lg:px-8">
		<div class="mx-auto max-w-3xl text-center">
			<!-- Tagline Pill -->
			<div class="inline-flex items-center gap-2 rounded-full border border-[#c96442]/30 bg-[#c96442]/10 px-3 py-1 text-xs font-mono font-medium text-[#c96442] shadow-xs">
				<Sparkles class="h-3.5 w-3.5" />
				<span>AI Ustaad (ai-ustaad.pages.dev) — Zero Se Hero Tak</span>
			</div>

			<!-- Main Hero Headline (Serif) -->
			<h1 class="mt-6 font-serif text-4xl font-bold tracking-tight text-[#141413] sm:text-6xl sm:leading-[1.15] dark:text-[#f5f4ed]">
				AI seekho — Zero se Production tak, <span class="text-[#c96442] italic">Roman Urdu</span> mein.
			</h1>

			<!-- Subtitle -->
			<p class="mt-6 text-lg leading-relaxed text-[#6f6e69] sm:text-xl dark:text-[#a19f97]">
				{course?.subtitle ||
					'Pakistan aur South Asia ka pehla complete, production-grade Roman Urdu AI Engineering curriculum.'}
				Python aur tensors se le kar Deep Learning, Transformers, Modern RAG, Autonomous Multi-Agent Systems, DeepSeek-R1 GRPO, aur Production MLOps tak.
			</p>

			<!-- Action Buttons -->
			<div class="mt-8 flex flex-col items-center justify-center gap-4 sm:flex-row">
				<a
					href="/signup"
					class="inline-flex h-12 w-full items-center justify-center gap-2 rounded-xl bg-[#c96442] px-6 text-sm font-semibold text-white shadow-sm transition-all hover:bg-[#d97757] focus:outline-none focus:ring-2 focus:ring-[#c96442]/50 sm:w-auto"
				>
					<span>Start Learning Free</span>
					<ArrowRight class="h-4 w-4" />
				</a>
				<a
					href="/learn"
					class="inline-flex h-12 w-full items-center justify-center gap-2 rounded-xl border border-[#e5e2d9] bg-[#f0eee6] px-6 text-sm font-semibold text-[#141413] transition-all hover:border-[#c96442]/40 hover:bg-[#e8e5db] sm:w-auto dark:border-[#343330] dark:bg-[#262624] dark:text-[#f5f4ed] dark:hover:bg-[#2e2d2a]"
				>
					<BookOpen class="h-4 w-4 text-[#6f6e69] dark:text-[#a19f97]" />
					<span>Explore Curriculum</span>
				</a>
			</div>

			<!-- Live Key Metrics Banner -->
			<div class="mt-12 grid grid-cols-2 gap-4 border-t border-[#e5e2d9] pt-8 sm:grid-cols-4 dark:border-[#343330]">
				<div>
					<div class="font-serif text-2xl font-bold text-[#141413] dark:text-[#f5f4ed]">20 Weeks</div>
					<div class="text-xs font-mono text-[#6f6e69] dark:text-[#a19f97]">Complete Roadmap</div>
				</div>
				<div>
					<div class="font-serif text-2xl font-bold text-[#141413] dark:text-[#f5f4ed]">5 Phases</div>
					<div class="text-xs font-mono text-[#6f6e69] dark:text-[#a19f97]">Zero to Hero</div>
				</div>
				<div>
					<div class="font-serif text-2xl font-bold text-[#141413] dark:text-[#f5f4ed]">Zero-GPU</div>
					<div class="text-xs font-mono text-[#6f6e69] dark:text-[#a19f97]">100% Free Cloud Compute</div>
				</div>
				<div>
					<div class="font-serif text-2xl font-bold text-[#141413] dark:text-[#f5f4ed]">100% SOTA</div>
					<div class="text-xs font-mono text-[#6f6e69] dark:text-[#a19f97]">DeepSeek-R1 • MCP</div>
				</div>
			</div>
		</div>

		<!-- Interactive Diagram Preview -->
		<div class="mt-14 mx-auto max-w-4xl">
			<Diagram
				script={`@preset midnight
@animate flow
flow LR: AI Ustaad Learning Trajectory
  p1[Phase 1: Python & Math Foundations] $terminal -> p2[Phase 2: Core ML & Transformers] $brain
  p2 -> p3[Phase 3: Modern RAG & Agents] $database
  p3 -> p4[Phase 4: LoRA & DeepSeek GRPO] $cpu
  p4 -> p5[Phase 5: Enterprise Capstone] $server *`}
				title="Complete 20-Week Master Curriculum Architecture"
			/>
		</div>
	</section>

	<!-- Value Props Section -->
	<section class="border-t border-[#e5e2d9] bg-[#f0eee6]/40 py-20 dark:border-[#343330] dark:bg-[#181817]">
		<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
			<div class="mx-auto max-w-2xl text-center">
				<h2 class="font-serif text-3xl font-bold tracking-tight text-[#141413] sm:text-4xl dark:text-[#f5f4ed]">
					Kyun AI Ustaad? Teen Bunyadi Assool.
				</h2>
				<p class="mt-4 text-base text-[#6f6e69] dark:text-[#a19f97]">
					Hum surface-level prompt wrappers nahi sikhate — hum real production AI engineering build karte hain.
				</p>
			</div>

			<div class="mt-12 grid grid-cols-1 gap-8 md:grid-cols-3">
				<!-- Prop 1 -->
				<div class="rounded-2xl border border-[#e5e2d9] bg-[#faf9f5] p-6 shadow-xs transition-shadow hover:shadow-md dark:border-[#343330] dark:bg-[#232321]">
					<div class="flex h-10 w-10 items-center justify-center rounded-xl bg-[#c96442]/10 text-[#c96442]">
						<Cpu class="h-5 w-5" />
					</div>
					<h3 class="mt-4 font-serif text-lg font-semibold text-[#141413] dark:text-[#f5f4ed]">
						Zero-GPU Cloud Recipes
					</h3>
					<p class="mt-2 text-sm leading-relaxed text-[#6f6e69] dark:text-[#a19f97]">
						Local expensive RTX GPU ki bilkul zaroorat nahi! Google Colab Free T4, Kaggle 30h/week Dual-T4 (30GB VRAM), aur Google One Pro compute units ko optimize karke 100% free model training aur fine-tuning karein.
					</p>
				</div>

				<!-- Prop 2 -->
				<div class="rounded-2xl border border-[#e5e2d9] bg-[#faf9f5] p-6 shadow-xs transition-shadow hover:shadow-md dark:border-[#343330] dark:bg-[#232321]">
					<div class="flex h-10 w-10 items-center justify-center rounded-xl bg-amber-500/10 text-amber-600 dark:text-amber-400">
						<Terminal class="h-5 w-5" />
					</div>
					<h3 class="mt-4 font-serif text-lg font-semibold text-[#141413] dark:text-[#f5f4ed]">
						Roman Urdu Intuition + Real Math
					</h3>
					<p class="mt-2 text-sm leading-relaxed text-[#6f6e69] dark:text-[#a19f97]">
						Math aur tensor operations first-principles se samjhein. Scaled Dot-Product Attention, Backpropagation, Gradient Descent, aur Causal Masking ko raw PyTorch tensors mein khud likhein.
					</p>
				</div>

				<!-- Prop 3 -->
				<div class="rounded-2xl border border-[#e5e2d9] bg-[#faf9f5] p-6 shadow-xs transition-shadow hover:shadow-md dark:border-[#343330] dark:bg-[#232321]">
					<div class="flex h-10 w-10 items-center justify-center rounded-xl bg-emerald-500/10 text-emerald-600 dark:text-emerald-400">
						<Zap class="h-5 w-5" />
					</div>
					<h3 class="mt-4 font-serif text-lg font-semibold text-[#141413] dark:text-[#f5f4ed]">
						2026 SOTA Production Stack
					</h3>
					<p class="mt-2 text-sm leading-relaxed text-[#6f6e69] dark:text-[#a19f97]">
						Purani 2023 tutorials ko alvida bolein. DeepSeek-R1 GRPO reinforcement learning, Anthropic Model Context Protocol (MCP), ColPali multi-vector PDF search, Unsloth QLoRA, aur Rust vLLM gateways.
					</p>
				</div>
			</div>
		</div>
	</section>

	<!-- 5-Phase Roadmap Section (Pulled Live from Supabase DB) -->
	<section class="mx-auto max-w-7xl px-4 py-20 sm:px-6 lg:px-8">
		<div class="mx-auto max-w-2xl text-center">
			<div class="text-xs font-mono uppercase tracking-wider text-[#c96442]">Curriculum Roadmap</div>
			<h2 class="mt-2 font-serif text-3xl font-bold tracking-tight text-[#141413] sm:text-4xl dark:text-[#f5f4ed]">
				5 Phases: Step-by-Step AI Engineering
			</h2>
			<p class="mt-3 text-base text-[#6f6e69] dark:text-[#a19f97]">
				Syllabus direct database se live load ho raha hai — har phase ke andar structured modules aur real-world deliverables shamil hain.
			</p>
		</div>

		<div class="mt-12 space-y-6">
			{#each phases as phase (phase.id)}
				<div class="overflow-hidden rounded-2xl border border-[#e5e2d9] bg-[#faf9f5] p-6 shadow-xs transition-all hover:border-[#c96442]/30 dark:border-[#343330] dark:bg-[#232321]">
					<div class="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
						<div>
							<div class="flex items-center gap-2">
								<span class="rounded bg-[#c96442]/10 px-2 py-0.5 text-xs font-mono font-medium text-[#c96442]">
									Phase {phase.phase_number}
								</span>
								<span class="rounded bg-[#f0eee6] px-2 py-0.5 text-xs font-mono text-[#6f6e69] dark:bg-[#262624] dark:text-[#a19f97]">
									{phase.weeks_range}
								</span>
								<span class="rounded bg-emerald-500/10 px-2 py-0.5 text-xs font-mono text-emerald-700 dark:text-emerald-400">
									{phase.level}
								</span>
							</div>
							<h3 class="mt-2 font-serif text-xl font-bold text-[#141413] dark:text-[#f5f4ed]">
								{phase.title}
							</h3>
							<p class="mt-1 max-w-2xl text-sm leading-relaxed text-[#6f6e69] dark:text-[#a19f97]">
								{phase.description}
							</p>
						</div>

						<a
							href="/learn"
							class="inline-flex items-center gap-1.5 text-xs font-mono font-medium text-[#c96442] hover:text-[#d97757]"
						>
							<span>Explore Phase</span>
							<ArrowRight class="h-3.5 w-3.5" />
						</a>
					</div>

					<!-- Modules in Phase -->
					{#if phase.modules && phase.modules.length > 0}
						<div class="mt-5 grid grid-cols-1 gap-3 sm:grid-cols-2 lg:grid-cols-3">
							{#each phase.modules as mod (mod.id)}
								<a
									href="/learn/{mod.slug}"
									class="group block rounded-xl border border-[#e5e2d9] bg-[#f0eee6]/50 p-3.5 transition-colors hover:border-[#c96442]/40 hover:bg-[#e8e5db]/60 dark:border-[#343330] dark:bg-[#1a1a19] dark:hover:bg-[#262624]"
								>
									<div class="flex items-center justify-between text-[11px] font-mono text-[#6f6e69] dark:text-[#a19f97]">
										<span>Module {mod.module_number}</span>
										<span>{mod.weeks_range}</span>
									</div>
									<div class="mt-1 font-serif text-sm font-semibold text-[#141413] group-hover:text-[#c96442] dark:text-[#f5f4ed]">
										{mod.title}
									</div>
									{#if mod.real_world_deliverable}
										<div class="mt-1.5 line-clamp-1 text-xs text-[#6f6e69] dark:text-[#a19f97]">
											📦 {mod.real_world_deliverable}
										</div>
									{/if}
								</a>
							{/each}
						</div>
					{/if}
				</div>
			{/each}
		</div>
	</section>

	<!-- Specialization Tracks Section -->
	{#if tracks.length > 0}
		<section class="border-t border-[#e5e2d9] bg-[#f0eee6]/40 py-20 dark:border-[#343330] dark:bg-[#181817]">
			<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
				<div class="mx-auto max-w-2xl text-center">
					<div class="text-xs font-mono uppercase tracking-wider text-[#c96442]">Phase 5 Specialization</div>
					<h2 class="mt-2 font-serif text-3xl font-bold tracking-tight text-[#141413] sm:text-4xl dark:text-[#f5f4ed]">
						Choose Your Specialization Track
					</h2>
					<p class="mt-3 text-base text-[#6f6e69] dark:text-[#a19f97]">
						Foundations ke baad apne career goal ke mutabiq specialized track select karein.
					</p>
				</div>

				<div class="mt-12 grid grid-cols-1 gap-8 md:grid-cols-3">
					{#each tracks as track (track.id)}
						<div class="flex flex-col justify-between rounded-2xl border border-[#e5e2d9] bg-[#faf9f5] p-6 shadow-xs dark:border-[#343330] dark:bg-[#232321]">
							<div>
								<span class="rounded bg-[#c96442]/10 px-2.5 py-1 text-xs font-mono font-medium text-[#c96442]">
									{track.track_code}
								</span>
								<h3 class="mt-4 font-serif text-lg font-semibold text-[#141413] dark:text-[#f5f4ed]">
									{track.title}
								</h3>
								<p class="mt-2 text-sm leading-relaxed text-[#6f6e69] dark:text-[#a19f97]">
									{track.description}
								</p>

								{#if track.topics && Array.isArray(track.topics)}
									<ul class="mt-4 space-y-1.5 text-xs text-[#2c2b28] dark:text-[#dcd9ce]">
										{#each track.topics as topic}
											<li class="flex items-center gap-2">
												<CheckCircle2 class="h-3.5 w-3.5 text-emerald-600 dark:text-emerald-400" />
												<span>{topic}</span>
											</li>
										{/each}
									</ul>
								{/if}
							</div>

							<div class="mt-6 pt-4 border-t border-[#e5e2d9] dark:border-[#343330]">
								<a
									href="/signup"
									class="inline-flex w-full items-center justify-center gap-1.5 rounded-lg border border-[#e5e2d9] bg-[#f0eee6] py-2 text-xs font-medium text-[#141413] hover:border-[#c96442]/40 hover:bg-[#e8e5db] dark:border-[#343330] dark:bg-[#262624] dark:text-[#f5f4ed]"
								>
									<span>Enroll in {track.track_code}</span>
									<ArrowRight class="h-3 w-3" />
								</a>
							</div>
						</div>
					{/each}
				</div>
			</div>
		</section>
	{/if}

	<!-- Featured Engineering Blogs Section -->
	{#if blogs.length > 0}
		<section class="mx-auto max-w-7xl px-4 py-20 sm:px-6 lg:px-8">
			<div class="flex flex-col items-start justify-between gap-4 sm:flex-row sm:items-end">
				<div>
					<div class="text-xs font-mono uppercase tracking-wider text-[#c96442]">Deep-Dive Articles</div>
					<h2 class="mt-1 font-serif text-3xl font-bold tracking-tight text-[#141413] dark:text-[#f5f4ed]">
						Engineering Blogs (Roman Urdu)
					</h2>
				</div>
				<a
					href="/blog"
					class="inline-flex items-center gap-1.5 text-sm font-medium text-[#c96442] hover:text-[#d97757]"
				>
					<span>View all blogs</span>
					<ArrowRight class="h-4 w-4" />
				</a>
			</div>

			<div class="mt-8 grid grid-cols-1 gap-6 md:grid-cols-3">
				{#each blogs as blog (blog.id)}
					<a
						href="/blog/{blog.slug}"
						class="group flex flex-col justify-between rounded-2xl border border-[#e5e2d9] bg-[#faf9f5] p-5 shadow-xs transition-all hover:border-[#c96442]/40 hover:shadow-md dark:border-[#343330] dark:bg-[#232321]"
					>
						<div>
							<div class="flex items-center justify-between text-xs font-mono text-[#6f6e69] dark:text-[#a19f97]">
								<span class="rounded bg-[#f0eee6] px-2 py-0.5 text-[10px] uppercase dark:bg-[#262624]">
									{blog.category}
								</span>
								<span>{blog.reading_time_minutes} min read</span>
							</div>
							<h3 class="mt-3 font-serif text-base font-semibold text-[#141413] group-hover:text-[#c96442] dark:text-[#f5f4ed]">
								{blog.title}
							</h3>
							<p class="mt-2 line-clamp-3 text-xs leading-relaxed text-[#6f6e69] dark:text-[#a19f97]">
								{blog.summary_roman_urdu}
							</p>
						</div>

						<div class="mt-4 flex items-center gap-1 text-xs font-mono text-[#c96442]">
							<span>Read technical deep-dive</span>
							<ArrowRight class="h-3 w-3 transition-transform group-hover:translate-x-0.5" />
						</div>
					</a>
				{/each}
			</div>
		</section>
	{/if}

	<!-- Final CTA Banner -->
	<section class="border-t border-[#e5e2d9] bg-[#f0eee6]/60 py-16 dark:border-[#343330] dark:bg-[#181817]">
		<div class="mx-auto max-w-4xl px-4 text-center sm:px-6 lg:px-8">
			<h2 class="font-serif text-3xl font-bold tracking-tight text-[#141413] sm:text-4xl dark:text-[#f5f4ed]">
				AI Engineer Banne Ka Safar Aaj Hi Shuru Karein.
			</h2>
			<p class="mx-auto mt-4 max-w-2xl text-base text-[#6f6e69] dark:text-[#a19f97]">
				100% free account banayein, interactive quizzes solve karke XP earn karein, aur local GPU ke baghair Google Colab par models train karein.
			</p>
			<div class="mt-8 flex justify-center">
				<a
					href="/signup"
					class="inline-flex h-12 items-center justify-center gap-2 rounded-xl bg-[#c96442] px-8 text-sm font-semibold text-white shadow-sm transition-all hover:bg-[#d97757] focus:outline-none focus:ring-2 focus:ring-[#c96442]/40"
				>
					<span>Sign Up Free with Email or Google</span>
					<ArrowRight class="h-4 w-4" />
				</a>
			</div>
		</div>
	</section>
</div>

<script lang="ts">
	import { ArrowRight, CheckCircle2, Circle, Clock, Sparkles, Cpu, Layers, HelpCircle, ExternalLink, Award, Play } from 'lucide-svelte';
	import Diagram from '$lib/components/Diagram.svelte';
	import CodeBlock from '$lib/components/CodeBlock.svelte';
	import { getPracticeProject } from '$lib/data/fallback';
	import type { PageData } from './$types';

	let { data }: { data: PageData } = $props();

	const mod = $derived(data.module);
	const lessons = $derived(data.lessons ?? []);
	const quiz = $derived(data.quiz);
	const badge = $derived(data.badge);
	const completedSet = $derived(new Set(data.completedLessonIds));

	const completedCount = $derived(lessons.filter((l: any) => completedSet.has(l.id)).length);
	const totalLessons = $derived(lessons.length);
	const pct = $derived(totalLessons > 0 ? Math.round((completedCount / totalLessons) * 100) : 0);

	const zeroGpu = $derived(mod.zero_gpu_recipe || {});
	const unassignSnippet = $derived(
		zeroGpu.unassign_code ||
		`# Auto unassign to prevent burning Colab GPU credits:\nfrom google.colab import runtime\nruntime.unassign()`
	);

	const practiceProject = $derived(
		mod.practice_project || getPracticeProject(mod.slug || mod.module_number)
	);
</script>

<div class="mx-auto max-w-5xl px-4 py-10 sm:px-6 lg:px-8 space-y-10">
	<!-- Breadcrumbs -->
	<nav class="flex items-center gap-2 text-xs font-mono text-[#6f6e69] dark:text-[#a19f97]">
		<a href="/learn" class="hover:text-[#c96442]">Curriculum</a>
		<span>/</span>
		<span>Phase {mod.phase?.phase_number || 1}</span>
		<span>/</span>
		<span class="text-[#141413] dark:text-[#f5f4ed]">Module {mod.module_number}</span>
	</nav>

	<!-- Header Banner -->
	<div class="border-b border-[#e5e2d9] pb-8 dark:border-[#343330]">
		<div class="flex flex-wrap items-center gap-2">
			<span class="rounded bg-[#c96442]/10 px-2.5 py-0.5 text-xs font-mono font-medium text-[#c96442]">
				Module {mod.module_number}
			</span>
			<span class="rounded bg-[#f0eee6] px-2 py-0.5 text-xs font-mono text-[#6f6e69] dark:bg-[#262624] dark:text-[#a19f97]">
				{mod.weeks_range}
			</span>
			<span class="rounded bg-[#f0eee6] px-2 py-0.5 text-xs font-mono text-[#6f6e69] dark:bg-[#262624] dark:text-[#a19f97]">
				~{mod.estimated_hours || 10} Hours
			</span>
			{#if badge}
				<span class="inline-flex items-center gap-1 rounded bg-amber-500/10 px-2 py-0.5 text-xs font-mono font-medium text-amber-700 dark:text-amber-400">
					<Award class="h-3 w-3" />
					Badge: {badge.title} (+{badge.xp_bonus} XP)
				</span>
			{/if}
		</div>

		<h1 class="mt-4 font-serif text-3xl font-bold tracking-tight text-[#141413] sm:text-4xl dark:text-[#f5f4ed]">
			{mod.title}
		</h1>

		<!-- Progress Bar -->
		<div class="mt-4 flex items-center gap-4">
			<div class="h-2 w-48 rounded-full bg-[#e5e2d9] overflow-hidden dark:bg-[#343330]">
				<div class="h-full bg-[#c96442] transition-all" style="width: {pct}%"></div>
			</div>
			<span class="text-xs font-mono text-[#6f6e69] dark:text-[#a19f97]">
				{completedCount} of {totalLessons} completed ({pct}%)
			</span>
		</div>
	</div>

	<!-- Deliverable Callout -->
	{#if mod.real_world_deliverable}
		<div class="rounded-2xl border border-emerald-500/30 bg-emerald-500/5 p-5 dark:border-emerald-500/20">
			<div class="flex items-center gap-2 text-xs font-mono uppercase tracking-wider text-emerald-800 dark:text-emerald-400">
				<Sparkles class="h-4 w-4" />
				<span>Real-World Deliverable (Production Project)</span>
			</div>
			<p class="mt-2 font-serif text-base font-semibold text-[#141413] dark:text-[#f5f4ed]">
				{mod.real_world_deliverable}
			</p>
		</div>
	{/if}

	<!-- Gamified Real-Time Practice: Culturally Relatable & Funny Sub-Project -->
	{#if practiceProject}
		<div class="rounded-2xl border-2 border-dashed border-[#c96442]/40 bg-[#c96442]/5 p-6 shadow-sm dark:border-[#c96442]/30 dark:bg-[#c96442]/10">
			<div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
				<div class="flex items-center gap-3.5">
					<div class="flex h-12 w-12 shrink-0 items-center justify-center rounded-2xl bg-[#c96442] text-white shadow-sm">
						<Sparkles class="h-6 w-6" />
					</div>
					<div>
						<div class="flex flex-wrap items-center gap-2">
							<span class="rounded-full bg-[#c96442] px-2.5 py-0.5 text-[10px] font-mono font-bold uppercase text-white tracking-wider">
								Real-Time Practice Checkpoint
							</span>
							<span class="rounded-full border border-amber-500/30 bg-amber-500/10 px-2.5 py-0.5 text-xs font-mono font-semibold text-amber-700 dark:text-amber-400">
								{practiceProject.humorous_badge}
							</span>
							<span class="rounded-full bg-emerald-500/10 px-2.5 py-0.5 text-xs font-mono font-bold text-emerald-700 dark:text-emerald-400">
								+{practiceProject.xp_reward} XP
							</span>
						</div>
						<h3 class="mt-1 font-serif text-xl font-bold tracking-tight text-[#141413] dark:text-[#f5f4ed]">
							{practiceProject.title}
						</h3>
					</div>
				</div>

				<a
					href={practiceProject.colab_url}
					target="_blank"
					rel="noopener noreferrer"
					class="inline-flex h-11 items-center justify-center gap-2 rounded-xl bg-[#c96442] px-5 text-xs font-semibold text-white shadow-sm transition-all hover:bg-[#d97757] hover:scale-[1.02] focus:outline-none focus:ring-2 focus:ring-[#c96442]/40 shrink-0"
				>
					<span>Open Google Colab Practice Notebook</span>
					<ExternalLink class="h-3.5 w-3.5" />
				</a>
			</div>

			<p class="mt-4 text-sm leading-relaxed text-[#2c2b28] dark:text-[#dcd9ce]">
				{practiceProject.description_roman_urdu}
			</p>

			<!-- Interactive Checklist & Test Criteria -->
			{#if practiceProject.checklist && practiceProject.checklist.length > 0}
				<div class="mt-5 rounded-xl border border-[#e5e2d9] bg-[#faf9f5]/80 p-4 dark:border-[#343330] dark:bg-[#1f1e1d]/80">
					<div class="flex items-center justify-between text-xs font-mono uppercase tracking-wider text-[#6f6e69] dark:text-[#a19f97] mb-3">
						<span>Sub-Project Checklist & Test Criteria</span>
						<span class="text-emerald-600 dark:text-emerald-400">100% Free Colab Practice</span>
					</div>
					<div class="grid grid-cols-1 gap-2 sm:grid-cols-2">
						{#each practiceProject.checklist as item}
							<div class="flex items-start gap-2.5 text-xs text-[#141413] dark:text-[#f5f4ed]">
								<CheckCircle2 class="h-4 w-4 shrink-0 text-emerald-600 dark:text-emerald-400 mt-0.5" />
								<span class="leading-relaxed">{item}</span>
							</div>
						{/each}
					</div>
				</div>
			{/if}
		</div>
	{/if}

	<!-- Zero-GPU Recipe -->
	<div class="rounded-2xl border border-[#e5e2d9] bg-[#faf9f5] p-6 shadow-xs dark:border-[#343330] dark:bg-[#232321]">
		<div class="flex items-center justify-between">
			<div class="flex items-center gap-2">
				<div class="flex h-8 w-8 items-center justify-center rounded-lg bg-[#c96442]/10 text-[#c96442]">
					<Cpu class="h-4 w-4" />
				</div>
				<div>
					<h2 class="font-serif text-base font-semibold text-[#141413] dark:text-[#f5f4ed]">
						Zero-GPU Cloud Compute Recipe
					</h2>
					<p class="text-xs text-[#6f6e69] dark:text-[#a19f97]">
						Local GPU ki zaroorat nahi — Colab Free T4 ya Kaggle Dual-T4 par run karein
					</p>
				</div>
			</div>

			<div class="flex items-center gap-2">
				<a
					href="https://colab.research.google.com"
					target="_blank"
					rel="noopener noreferrer"
					class="inline-flex items-center gap-1 rounded-lg border border-[#e5e2d9] bg-[#f0eee6] px-2.5 py-1 text-xs font-mono text-[#141413] hover:border-[#c96442]/40 dark:border-[#343330] dark:bg-[#262624] dark:text-[#f5f4ed]"
				>
					<span>Open Colab</span>
					<ExternalLink class="h-3 w-3" />
				</a>
				<a
					href="https://www.kaggle.com"
					target="_blank"
					rel="noopener noreferrer"
					class="inline-flex items-center gap-1 rounded-lg border border-[#e5e2d9] bg-[#f0eee6] px-2.5 py-1 text-xs font-mono text-[#141413] hover:border-[#c96442]/40 dark:border-[#343330] dark:bg-[#262624] dark:text-[#f5f4ed]"
				>
					<span>Kaggle Dual-T4</span>
					<ExternalLink class="h-3 w-3" />
				</a>
			</div>
		</div>

		<div class="mt-4">
			<p class="text-xs leading-relaxed text-[#2c2b28] dark:text-[#dcd9ce]">
				Training session khatam hone ke baad runtime unassign zaroor karein taake background idle hours na count hon:
			</p>
			<CodeBlock code={unassignSnippet} language="python" title="Credit Saver Snippet" />
		</div>
	</div>

	<!-- Architecture Diagram -->
	{#if mod.diagram_script}
		<div>
			<h2 class="font-serif text-xl font-bold text-[#141413] dark:text-[#f5f4ed]">
				Module Architecture Blueprint
			</h2>
			<Diagram
				script={mod.diagram_script}
				preset={mod.diagram_preset || 'midnight'}
				animate={mod.diagram_animation || 'flow'}
				title="Module Concept Diagram"
			/>
		</div>
	{/if}

	<!-- Learning Outcomes & Tasks (2-Col) -->
	<div class="grid grid-cols-1 gap-6 md:grid-cols-2">
		<!-- Outcomes -->
		{#if mod.learning_outcomes && Array.isArray(mod.learning_outcomes)}
			<div class="rounded-2xl border border-[#e5e2d9] bg-[#faf9f5] p-5 shadow-xs dark:border-[#343330] dark:bg-[#232321]">
				<h3 class="font-serif text-base font-semibold text-[#141413] dark:text-[#f5f4ed]">
					Learning Outcomes
				</h3>
				<ul class="mt-3 space-y-2 text-xs text-[#2c2b28] dark:text-[#dcd9ce]">
					{#each mod.learning_outcomes as outcome}
						<li class="flex items-start gap-2">
							<CheckCircle2 class="h-4 w-4 shrink-0 text-emerald-600 dark:text-emerald-400 mt-0.5" />
							<span class="leading-relaxed">{outcome}</span>
						</li>
					{/each}
				</ul>
			</div>
		{/if}

		<!-- Practical Tasks -->
		{#if mod.practical_tasks && Array.isArray(mod.practical_tasks)}
			<div class="rounded-2xl border border-[#e5e2d9] bg-[#faf9f5] p-5 shadow-xs dark:border-[#343330] dark:bg-[#232321]">
				<h3 class="font-serif text-base font-semibold text-[#141413] dark:text-[#f5f4ed]">
					Practical Lab Tasks
				</h3>
				<ul class="mt-3 space-y-2 text-xs text-[#2c2b28] dark:text-[#dcd9ce]">
					{#each mod.practical_tasks as task}
						<li class="flex items-start gap-2">
							<CheckCircle2 class="h-4 w-4 shrink-0 text-[#c96442] mt-0.5" />
							<span class="leading-relaxed">{task}</span>
						</li>
					{/each}
				</ul>
			</div>
		{/if}
	</div>

	<!-- Lessons List -->
	<div>
		<div class="flex items-center justify-between">
			<h2 class="font-serif text-2xl font-bold text-[#141413] dark:text-[#f5f4ed]">
				Module Lessons ({lessons.length})
			</h2>
			<span class="text-xs font-mono text-[#6f6e69] dark:text-[#a19f97]">
				Click any lesson to start reading
			</span>
		</div>

		<div class="mt-4 divide-y divide-[#e5e2d9] rounded-2xl border border-[#e5e2d9] bg-[#faf9f5] shadow-xs overflow-hidden dark:divide-[#343330] dark:border-[#343330] dark:bg-[#232321]">
			{#each lessons as lesson (lesson.id)}
				{@const completed = completedSet.has(lesson.id)}
				<a
					href="/learn/{mod.slug}/{lesson.slug}"
					class="group flex items-center justify-between p-4 transition-colors hover:bg-[#f0eee6]/60 dark:hover:bg-[#2e2d2a]"
				>
					<div class="flex items-center gap-3">
						{#if completed}
							<CheckCircle2 class="h-5 w-5 text-emerald-600 dark:text-emerald-400" />
						{:else}
							<Circle class="h-5 w-5 text-[#a19f97] dark:text-[#6f6e69]" />
						{/if}
						<div>
							<div class="flex items-center gap-2">
								<span class="font-mono text-xs text-[#c96442]">{lesson.lesson_code}</span>
								<span class="font-serif text-sm font-semibold text-[#141413] group-hover:text-[#c96442] dark:text-[#f5f4ed]">
									{lesson.title}
								</span>
							</div>
							<div class="mt-0.5 text-xs text-[#6f6e69] dark:text-[#a19f97]">
								{lesson.english_summary || 'Roman Urdu explanation with code & diagrams'}
							</div>
						</div>
					</div>

					<div class="flex items-center gap-4 text-xs font-mono text-[#6f6e69] dark:text-[#a19f97]">
						<span class="flex items-center gap-1">
							<Clock class="h-3.5 w-3.5" />
							{lesson.duration_minutes}m
						</span>
						<span class="rounded bg-[#c96442]/10 px-2 py-0.5 text-[#c96442]">
							+{lesson.xp_reward} XP
						</span>
						<ArrowRight class="h-4 w-4 text-[#6f6e69] transition-transform group-hover:translate-x-1 group-hover:text-[#c96442]" />
					</div>
				</a>
			{/each}
		</div>
	</div>

	<!-- Module Quiz Card -->
	{#if quiz}
		<div class="rounded-2xl border border-amber-500/30 bg-amber-500/5 p-6 shadow-xs dark:border-amber-500/20">
			<div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
				<div>
					<div class="flex items-center gap-2 text-xs font-mono uppercase tracking-wider text-amber-800 dark:text-amber-400">
						<HelpCircle class="h-4 w-4" />
						<span>Module Assessment</span>
					</div>
					<h3 class="mt-1 font-serif text-xl font-bold text-[#141413] dark:text-[#f5f4ed]">
						{quiz.title}
					</h3>
					<p class="mt-1 text-xs text-[#6f6e69] dark:text-[#a19f97]">
						Passing criteria: {quiz.passing_score_pct}%. Earn +{quiz.xp_reward} XP. Score 90%+ for the "Top Performer" badge!
					</p>
				</div>

				<a
					href="/learn/{mod.slug}/quiz"
					class="inline-flex h-11 items-center justify-center gap-2 rounded-xl bg-[#c96442] px-6 text-xs font-semibold text-white shadow-sm transition-all hover:bg-[#d97757]"
				>
					<span>Take Quiz</span>
					<ArrowRight class="h-4 w-4" />
				</a>
			</div>
		</div>
	{/if}
</div>

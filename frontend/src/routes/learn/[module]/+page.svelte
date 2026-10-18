<script lang="ts">
	import { ArrowRight, CheckCircle2, Circle, Clock, Sparkles, Cpu, Layers, HelpCircle, ExternalLink, Award, Play } from 'lucide-svelte';
	import Diagram from '$lib/components/Diagram.svelte';
	import CodeBlock from '$lib/components/CodeBlock.svelte';
	import HfSubprojectCard from '$lib/components/HfSubprojectCard.svelte';
	import { getPracticeProject, getHfSubproject } from '$lib/data/fallback';
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

	const hfSubproject = $derived(
		mod.practice_checkpoint?.hf_subproject ||
		practiceProject?.hf_subproject ||
		getHfSubproject(mod.slug || mod.module_number)
	);
</script>

<div class="mx-auto flex max-w-5xl flex-col gap-10 px-4 py-10 sm:px-6 lg:px-8">
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

	<!-- Consolidated Hands-on Project Lab -->
	{#if mod.real_world_deliverable || practiceProject || hfSubproject}
		<section class="order-4 space-y-5 rounded-2xl border border-[#d8d5cb] bg-white p-6 shadow-xs dark:border-[#343330] dark:bg-[#232321]">
			<div class="flex flex-col gap-4 sm:flex-row sm:items-start sm:justify-between">
				<div>
					<div class="flex flex-wrap items-center gap-2 text-[11px] font-mono font-semibold">
						<span class="rounded-md bg-[#c96442]/10 px-2 py-0.5 text-[#c96442]">Hands-on Project Lab</span>
						{#if practiceProject}
							<span class="rounded-md bg-stone-200/70 px-2 py-0.5 text-stone-700 dark:bg-stone-800 dark:text-stone-300">{practiceProject.humorous_badge}</span>
							<span class="rounded-md bg-emerald-500/10 px-2 py-0.5 text-emerald-700 dark:text-emerald-400">+{practiceProject.xp_reward} XP</span>
						{/if}
					</div>
					<h2 class="mt-2 font-serif text-xl font-bold text-[#141413] dark:text-[#f5f4ed]">
						{practiceProject?.title || mod.real_world_deliverable}
					</h2>
					{#if mod.real_world_deliverable && practiceProject}
						<p class="mt-1 text-sm text-[#52514c] dark:text-[#a19f97]">Deliverable: {mod.real_world_deliverable}</p>
					{/if}
				</div>
				<div class="flex shrink-0 flex-wrap gap-2">
					<a href={practiceProject?.colab_url || 'https://colab.research.google.com'} target="_blank" rel="noopener noreferrer" class="inline-flex h-10 items-center gap-2 rounded-xl bg-[#c96442] px-4 text-xs font-semibold text-white hover:bg-[#d97757]">
						<span>Open in Colab</span><ExternalLink class="h-3.5 w-3.5" />
					</a>
					<a href="https://www.kaggle.com/code" target="_blank" rel="noopener noreferrer" class="inline-flex h-10 items-center gap-2 rounded-xl border border-[#d8d5cb] px-4 text-xs font-semibold text-[#141413] hover:border-[#c96442]/50 dark:border-[#343330] dark:text-[#f5f4ed]">
						<span>Kaggle Dual-T4</span><ExternalLink class="h-3.5 w-3.5" />
					</a>
				</div>
			</div>

			{#if practiceProject?.description_roman_urdu}
				<p class="text-sm leading-relaxed text-[#2c2b28] dark:text-[#dcd9ce]">{practiceProject.description_roman_urdu}</p>
			{/if}

			{#if practiceProject?.checklist?.length}
				<ul class="grid grid-cols-1 gap-2 sm:grid-cols-2">
					{#each practiceProject.checklist as item}
						<li class="flex items-start gap-2 text-xs text-[#141413] dark:text-[#f5f4ed]">
							<CheckCircle2 class="mt-0.5 h-4 w-4 shrink-0 text-emerald-600 dark:text-emerald-400" />
							<span>{item}</span>
						</li>
					{/each}
				</ul>
			{/if}

			{#if hfSubproject}
				<HfSubprojectCard subproject={hfSubproject} moduleNumber={mod.module_number} />
			{/if}

			<details class="rounded-xl border border-[#d8d5cb] p-4 dark:border-[#343330]">
				<summary class="cursor-pointer text-xs font-mono font-semibold uppercase tracking-wider text-[#52514c] dark:text-[#a19f97]">
					Zero-GPU tip: protect your Colab compute units
				</summary>
				<div class="mt-3">
					<CodeBlock code={unassignSnippet} language="python" title="Credit Saver Snippet" />
				</div>
			</details>
		</section>
	{/if}


	<!-- Architecture Diagram -->
	{#if mod.diagram_script}
		<div class="order-3">
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
	<div class="order-5 grid grid-cols-1 gap-6 md:grid-cols-2">
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
	<div class="order-2">
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
		<div class="order-6 rounded-2xl border border-amber-500/30 bg-amber-500/5 p-6 shadow-xs dark:border-amber-500/20">
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

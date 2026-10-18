<script lang="ts">
	import { Flame, Sparkles, BookOpen, ArrowRight, Award, Trophy, Play, CheckCircle2, Circle, Clock, Terminal, Shield } from 'lucide-svelte';
	import Seo from '$lib/components/Seo.svelte';
	import type { PageData } from './$types';

	let { data }: { data: PageData } = $props();

	const profile = $derived(data.profile);
	const user = $derived(data.user);
	const phaseStats = $derived(data.phaseStats ?? []);
	const continueLesson = $derived(data.continueLesson);
	const userBadges = $derived(data.userBadges ?? []);
	const allBadges = $derived(data.allBadges ?? []);
	const activeChallenge = $derived(data.activeChallenge);

	const unlockedSlugSet = $derived(
		new Set(userBadges.map((ub: any) => (Array.isArray(ub.badge) ? ub.badge[0] : ub.badge)?.slug))
	);
	const totalCompleted = $derived(data.completedLessonIds?.length ?? 0);
	const totalLessons = $derived(phaseStats.reduce((acc: number, p: any) => acc + p.totalLessons, 0));
	const overallPct = $derived(totalLessons > 0 ? Math.round((totalCompleted / totalLessons) * 100) : 0);
</script>

<Seo
	title="Curriculum & Roadmap | AI Ustaad"
	description="Explore the complete 20-week production AI engineering curriculum in Roman Urdu: Python prerequisites, Tensors, PyTorch, Transformers, Modern RAG, Agents, and MLOps."
	canonical="https://ai-ustaad.pages.dev/learn"
	ogType="website"
	ogImage="/og-image.png"
	jsonLd={[
		{
			"@context": "https://schema.org",
			"@type": "BreadcrumbList",
			"itemListElement": [
				{
					"@type": "ListItem",
					"position": 1,
					"name": "Home",
					"item": "https://ai-ustaad.pages.dev"
				},
				{
					"@type": "ListItem",
					"position": 2,
					"name": "Curriculum",
					"item": "https://ai-ustaad.pages.dev/learn"
				}
			]
		},
		{
			"@context": "https://schema.org",
			"@type": "ItemList",
			"name": "AI Ustaad Curriculum Phases",
			"description": "20-week production AI engineering roadmap from prerequisites to advanced LLM post-training and distributed MLOps.",
			"itemListElement": (phaseStats ?? []).map((p: any, idx: number) => ({
				"@type": "ListItem",
				"position": idx + 1,
				"name": p.title,
				"description": p.description || `Phase ${p.phase_number}`
			}))
		}
	]}
/>

<div class="mx-auto max-w-7xl px-4 py-10 sm:px-6 lg:px-8 space-y-10">
	<!-- Welcome Header -->
	<div class="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between border-b border-[#e5e2d9] pb-8 dark:border-[#343330]">
		<div>
			<div class="flex items-center gap-2">
				<span class="rounded bg-[#c96442]/10 px-2.5 py-0.5 text-xs font-mono font-medium text-[#c96442]">
					Student Dashboard
				</span>
				<span class="rounded bg-[#f0eee6] px-2 py-0.5 text-xs font-mono text-[#6f6e69] dark:bg-[#262624] dark:text-[#a19f97]">
					Track: {profile?.selected_track || 'Track A (Developers)'}
				</span>
			</div>
			<h1 class="mt-2 font-serif text-3xl font-bold tracking-tight text-[#141413] sm:text-4xl dark:text-[#f5f4ed]">
				Khushamdeed, {profile?.full_name || user?.email?.split('@')[0] || 'Engineer'}!
			</h1>
			<p class="mt-1 text-sm text-[#6f6e69] dark:text-[#a19f97]">
				Apne 20-week AI engineering roadmap par regular consistency banaye rakhein.
			</p>
		</div>

		{#if continueLesson}
			<a
				href="/learn/{continueLesson.moduleSlug}/{continueLesson.lessonSlug}"
				class="inline-flex h-11 items-center gap-2 rounded-xl bg-[#c96442] px-5 text-xs font-semibold text-white shadow-sm transition-all hover:bg-[#d97757] focus:outline-none focus:ring-2 focus:ring-[#c96442]/40"
			>
				<Play class="h-3.5 w-3.5 fill-current" />
				<span>Continue Learning</span>
			</a>
		{/if}
	</div>

	<!-- Prerequisite Track Alert Banner -->
	<div class="rounded-2xl border border-amber-500/30 bg-amber-500/10 p-5 shadow-xs backdrop-blur-sm sm:flex sm:items-center sm:justify-between dark:border-amber-500/20 dark:bg-amber-500/5">
		<div class="flex items-center gap-3.5">
			<div class="flex h-11 w-11 shrink-0 items-center justify-center rounded-xl bg-amber-500/20 text-amber-700 dark:text-amber-400">
				<Terminal class="h-5 w-5" />
			</div>
			<div>
				<div class="flex items-center gap-2">
					<span class="rounded bg-amber-500/20 px-2 py-0.5 text-[10px] font-mono font-bold uppercase text-amber-800 dark:text-amber-300">
						Prerequisite Foundation
					</span>
					<span class="font-serif text-sm font-bold text-[#141413] dark:text-[#f5f4ed]">
						Python Zero Se Hero (Beginner to AI Engineer)
					</span>
				</div>
				<p class="mt-1 text-xs text-[#2c2b28] dark:text-[#dcd9ce]">
					<span class="font-semibold text-amber-800 dark:text-amber-300">Naye hain aur Python nahi aati?</span> Pehle Python Zero Se Hero complete karein, phir AI Mastery shuru karein!
				</p>
			</div>
		</div>
		<a
			href="/learn/m00-python-zero-se-hero"
			class="mt-3 inline-flex items-center justify-center gap-1.5 rounded-xl bg-amber-600 px-4 py-2 text-xs font-semibold text-white transition-all hover:bg-amber-700 sm:mt-0 sm:shrink-0"
		>
			<span>Open Python Track</span>
			<ArrowRight class="h-3.5 w-3.5" />
		</a>
	</div>

	<!-- 4 Metric Cards -->
	<div class="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-4">
		<!-- Card 1: Total XP -->
		<div class="rounded-2xl border border-[#e5e2d9] bg-[#faf9f5] p-5 shadow-xs dark:border-[#343330] dark:bg-[#232321]">
			<div class="flex items-center justify-between text-xs text-[#6f6e69] dark:text-[#a19f97]">
				<span class="font-mono uppercase tracking-wider">Experience Points</span>
				<Sparkles class="h-4 w-4 text-[#c96442]" />
			</div>
			<div class="mt-3 font-serif text-3xl font-bold text-[#141413] dark:text-[#f5f4ed]">
				{profile?.xp_points ?? 0} <span class="text-sm font-sans font-normal text-[#6f6e69] dark:text-[#a19f97]">XP</span>
			</div>
			<div class="mt-3 text-xs text-[#6f6e69] dark:text-[#a19f97]">
				Earn XP by completing lessons & quizzes
			</div>
		</div>

		<!-- Card 2: Streak -->
		<div class="rounded-2xl border border-[#e5e2d9] bg-[#faf9f5] p-5 shadow-xs dark:border-[#343330] dark:bg-[#232321]">
			<div class="flex items-center justify-between text-xs text-[#6f6e69] dark:text-[#a19f97]">
				<span class="font-mono uppercase tracking-wider">Daily Streak</span>
				<Flame class="h-4 w-4 fill-amber-500 text-amber-500" />
			</div>
			<div class="mt-3 font-serif text-3xl font-bold text-amber-600 dark:text-amber-400">
				{profile?.current_streak ?? 0} <span class="text-sm font-sans font-normal text-[#6f6e69] dark:text-[#a19f97]">Days</span>
			</div>
			<div class="mt-3 text-xs text-[#6f6e69] dark:text-[#a19f97]">
				Longest streak: {profile?.longest_streak ?? 0} days
			</div>
		</div>

		<!-- Card 3: Lessons Completed -->
		<div class="rounded-2xl border border-[#e5e2d9] bg-[#faf9f5] p-5 shadow-xs dark:border-[#343330] dark:bg-[#232321]">
			<div class="flex items-center justify-between text-xs text-[#6f6e69] dark:text-[#a19f97]">
				<span class="font-mono uppercase tracking-wider">Curriculum Progress</span>
				<BookOpen class="h-4 w-4 text-emerald-600 dark:text-emerald-400" />
			</div>
			<div class="mt-3 font-serif text-3xl font-bold text-[#141413] dark:text-[#f5f4ed]">
				{overallPct}%
			</div>
			<div class="mt-3 text-xs text-[#6f6e69] dark:text-[#a19f97]">
				{totalCompleted} of {totalLessons} lessons completed
			</div>
		</div>

		<!-- Card 4: Badges -->
		<div class="rounded-2xl border border-[#e5e2d9] bg-[#faf9f5] p-5 shadow-xs dark:border-[#343330] dark:bg-[#232321]">
			<div class="flex items-center justify-between text-xs text-[#6f6e69] dark:text-[#a19f97]">
				<span class="font-mono uppercase tracking-wider">Badges Unlocked</span>
				<Trophy class="h-4 w-4 text-amber-500" />
			</div>
			<div class="mt-3 font-serif text-3xl font-bold text-[#141413] dark:text-[#f5f4ed]">
				{userBadges.length} <span class="text-sm font-sans font-normal text-[#6f6e69] dark:text-[#a19f97]">/ {allBadges.length}</span>
			</div>
			<div class="mt-3 text-xs text-[#6f6e69] dark:text-[#a19f97]">
				Syllabus milestones & quiz achievements
			</div>
		</div>
	</div>

	<!-- Continue Where Left Off & Weekly Challenge (2-Col) -->
	<div class="grid grid-cols-1 gap-6 lg:grid-cols-3">
		<!-- Continue Learning Box -->
		{#if continueLesson}
			<div class="lg:col-span-2 rounded-2xl border border-[#c96442]/30 bg-[#faf9f5] p-6 shadow-xs dark:border-[#c96442]/20 dark:bg-[#232321]">
				<div class="flex items-center justify-between text-xs font-mono text-[#c96442]">
					<span class="flex items-center gap-1.5 font-medium">
						<Play class="h-3.5 w-3.5 fill-current" />
						Resume Where You Left Off
					</span>
					<span>Next Lesson</span>
				</div>
				<div class="mt-3">
					<div class="text-xs text-[#6f6e69] dark:text-[#a19f97]">
						{continueLesson.moduleTitle}
					</div>
					<h2 class="mt-1 font-serif text-2xl font-bold text-[#141413] dark:text-[#f5f4ed]">
						{continueLesson.lessonTitle}
					</h2>
				</div>
				<div class="mt-6 flex items-center justify-between pt-4 border-t border-[#e5e2d9] dark:border-[#343330]">
					<div class="flex items-center gap-4 text-xs font-mono text-[#6f6e69] dark:text-[#a19f97]">
						<span>Roman Urdu Content</span>
						<span>•</span>
						<span>Code & Diagrams</span>
					</div>
					<a
						href="/learn/{continueLesson.moduleSlug}/{continueLesson.lessonSlug}"
						class="inline-flex items-center gap-1.5 rounded-lg bg-[#c96442] px-4 py-2 text-xs font-semibold text-white transition-colors hover:bg-[#d97757]"
					>
						<span>Open Lesson</span>
						<ArrowRight class="h-3.5 w-3.5" />
					</a>
				</div>
			</div>
		{/if}

		<!-- Active Weekly Challenge Box -->
		{#if activeChallenge}
			<div class="rounded-2xl border border-amber-500/30 bg-[#faf9f5] p-6 shadow-xs dark:border-amber-500/20 dark:bg-[#232321]">
				<div class="flex items-center justify-between text-xs font-mono text-amber-700 dark:text-amber-400">
					<span>Week {activeChallenge.week_number} Challenge</span>
					<span class="rounded bg-amber-500/10 px-2 py-0.5 font-bold">+{activeChallenge.xp_reward} XP</span>
				</div>
				<h3 class="mt-3 font-serif text-lg font-bold text-[#141413] dark:text-[#f5f4ed]">
					{activeChallenge.title}
				</h3>
				<p class="mt-2 text-xs leading-relaxed text-[#6f6e69] dark:text-[#a19f97]">
					{activeChallenge.description_roman_urdu}
				</p>
				<div class="mt-6 pt-3 border-t border-[#e5e2d9] dark:border-[#343330]">
					<span class="inline-flex items-center gap-1.5 text-xs font-mono text-[#6f6e69] dark:text-[#a19f97]">
						<CheckCircle2 class="h-3.5 w-3.5 text-emerald-600 dark:text-emerald-400" />
						Auto-evaluates with tests
					</span>
				</div>
			</div>
		{/if}
	</div>

	<!-- 5 Phases Detailed Progress Breakdown -->
	<div>
		<div class="flex items-center justify-between">
			<div>
				<h2 class="font-serif text-2xl font-bold text-[#141413] dark:text-[#f5f4ed]">
					Phase-wise Mastery Progress
				</h2>
				<p class="text-xs text-[#6f6e69] dark:text-[#a19f97]">
					Har phase ke modules aur lessons complete karke badge unlock karein
				</p>
			</div>
		</div>

		<div class="mt-6 space-y-4">
			{#each phaseStats as phase (phase.id)}
				<div class="rounded-2xl border border-[#e5e2d9] bg-[#faf9f5] p-5 shadow-xs dark:border-[#343330] dark:bg-[#232321]">
					<div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-2">
						<div>
							<div class="flex items-center gap-2">
								<span class="rounded bg-[#c96442]/10 px-2 py-0.5 text-xs font-mono font-medium text-[#c96442]">
									Phase {phase.phase_number}
								</span>
								<span class="text-xs font-mono text-[#6f6e69] dark:text-[#a19f97]">
									{phase.weeks_range} • {phase.level}
								</span>
							</div>
							<h3 class="mt-1 font-serif text-lg font-semibold text-[#141413] dark:text-[#f5f4ed]">
								{phase.title}
							</h3>
						</div>

						<div class="flex items-center gap-3">
							<span class="text-xs font-mono font-semibold text-[#141413] dark:text-[#f5f4ed]">
								{phase.completedCount} / {phase.totalLessons} ({phase.pct}%)
							</span>
							<div class="h-2 w-28 rounded-full bg-[#e5e2d9] overflow-hidden dark:bg-[#343330]">
								<div class="h-full bg-[#c96442] transition-all duration-500" style="width: {phase.pct}%"></div>
							</div>
						</div>
					</div>
				</div>
			{/each}
		</div>
	</div>

	<!-- Badges Showcase -->
	<div>
		<div class="flex items-center justify-between">
			<div>
				<h2 class="font-serif text-2xl font-bold text-[#141413] dark:text-[#f5f4ed]">
					Badges & Achievements ({userBadges.length}/{allBadges.length})
				</h2>
				<p class="text-xs text-[#6f6e69] dark:text-[#a19f97]">
					Badges earn karne par direct user profile par extra bonus XP add hoti hai
				</p>
			</div>
		</div>

		<div class="mt-6 grid grid-cols-2 gap-4 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6">
			{#each allBadges as b (b.id)}
				{@const unlocked = unlockedSlugSet.has(b.slug)}
				<div
					class="flex flex-col items-center rounded-2xl border p-4 text-center transition-all {unlocked
						? 'border-amber-500/40 bg-amber-500/5 shadow-xs dark:border-amber-500/30'
						: 'border-[#e5e2d9] bg-[#faf9f5] opacity-50 grayscale dark:border-[#343330] dark:bg-[#232321]'}"
				>
					<div class="flex h-12 w-12 items-center justify-center rounded-xl {unlocked ? 'bg-amber-500/20 text-amber-600 dark:text-amber-400' : 'bg-[#f0eee6] text-[#6f6e69] dark:bg-[#262624] dark:text-[#a19f97]'}">
						<Award class="h-6 w-6" />
					</div>
					<div class="mt-2 font-serif text-xs font-semibold text-[#141413] dark:text-[#f5f4ed]">
						{b.title}
					</div>
					<div class="mt-0.5 text-[10px] text-[#6f6e69] dark:text-[#a19f97]">
						{b.roman_urdu_subtitle}
					</div>
					<div class="mt-2 rounded bg-[#f0eee6] px-1.5 py-0.5 text-[10px] font-mono text-[#c96442] dark:bg-[#262624]">
						+{b.xp_bonus} XP
					</div>
				</div>
			{/each}
		</div>
	</div>
</div>

<script lang="ts">
	import { enhance } from '$app/forms';
	import { CheckCircle2, Clock, Sparkles, ArrowLeft, ArrowRight, BookOpen, Layers, Menu, X, Award, ExternalLink } from 'lucide-svelte';
	import Sidebar from '$lib/components/Sidebar.svelte';
	import Markdown from '$lib/components/Markdown.svelte';
	import Diagram from '$lib/components/Diagram.svelte';
	import CodeBlock from '$lib/components/CodeBlock.svelte';
	import HfSubprojectCard from '$lib/components/HfSubprojectCard.svelte';
	import { getPracticeProject, getHfSubproject } from '$lib/data/fallback';
	import type { ActionData, PageData } from './$types';

	let { data, form }: { data: PageData; form: ActionData } = $props();

	const lesson = $derived(data.lesson);
	const mod = $derived(data.module);
	const prevLesson = $derived(data.prevLesson);
	const nextLesson = $derived(data.nextLesson);

	let sidebarOpen = $state(false);
	let isOptimisticCompleted = $state(false);

	const isCompleted = $derived(isOptimisticCompleted || data.isCompleted || form?.success);
	const practiceProject = $derived(getPracticeProject(mod.slug || mod.module_number));
	const hfSubproject = $derived(
		(mod as any).practice_checkpoint?.hf_subproject ||
		practiceProject?.hf_subproject ||
		getHfSubproject(mod.slug || mod.module_number)
	);
</script>

<div class="flex min-h-[calc(100vh-4rem)]">
	<!-- Collapsible Syllabus Sidebar -->
	<Sidebar
		modules={data.allModules}
		currentLessonSlug={lesson.slug}
		currentModuleSlug={mod.slug}
		completedLessonIds={data.completedLessonIds}
		isOpen={sidebarOpen}
		onClose={() => (sidebarOpen = false)}
	/>

	<!-- Main Reading Area (Centered Prose max-w-720px) -->
	<div class="flex-1 overflow-y-auto">
		<!-- Reading Top Bar -->
		<div class="sticky top-16 z-20 flex items-center justify-between border-b border-[#e5e2d9] bg-[#faf9f5]/90 px-4 py-2.5 backdrop-blur-md sm:px-8 dark:border-[#343330] dark:bg-[#1f1e1d]/90">
			<div class="flex items-center gap-3">
				<button
					type="button"
					onclick={() => (sidebarOpen = !sidebarOpen)}
					class="inline-flex h-8 w-8 items-center justify-center rounded-lg border border-[#e5e2d9] text-[#6f6e69] hover:text-[#141413] md:hidden dark:border-[#343330] dark:text-[#a19f97]"
					aria-label="Toggle syllabus sidebar"
				>
					<Menu class="h-4 w-4" />
				</button>

				<nav class="flex items-center gap-2 text-xs font-mono text-[#6f6e69] dark:text-[#a19f97]">
					<a href="/learn/{mod.slug}" class="hover:text-[#c96442] line-clamp-1">
						{mod.title}
					</a>
					<span>/</span>
					<span class="text-[#c96442]">{lesson.lesson_code}</span>
				</nav>
			</div>

			<div class="flex items-center gap-2">
				{#if isCompleted}
					<span class="inline-flex items-center gap-1.5 rounded-full border border-emerald-500/20 bg-emerald-500/10 px-3 py-1 text-xs font-mono font-medium text-emerald-700 dark:text-emerald-400">
						<CheckCircle2 class="h-3.5 w-3.5" />
						<span>Completed</span>
					</span>
				{:else}
					<span class="inline-flex items-center gap-1 rounded-full border border-[#c96442]/20 bg-[#c96442]/10 px-2.5 py-0.5 text-xs font-mono font-medium text-[#c96442]">
						+{lesson.xp_reward} XP
					</span>
				{/if}
			</div>
		</div>

		<!-- Centered Prose Document (max-w-[720px]) -->
		<article class="mx-auto max-w-[720px] px-4 py-12 sm:px-6">
			<!-- Lesson Header -->
			<header class="border-b border-[#e5e2d9] pb-8 dark:border-[#343330]">
				<div class="flex items-center gap-2 text-xs font-mono text-[#6f6e69] dark:text-[#a19f97]">
					<span class="rounded bg-[#c96442]/10 px-2 py-0.5 text-[#c96442]">{lesson.lesson_code}</span>
					<span>•</span>
					<span class="flex items-center gap-1">
						<Clock class="h-3 w-3" />
						{lesson.duration_minutes} mins
					</span>
					<span>•</span>
					<span class="capitalize">{lesson.lesson_type?.replace('_', ' ') || 'Theory & Code'}</span>
				</div>

				<h1 class="mt-4 font-serif text-3xl font-bold tracking-tight text-[#141413] sm:text-4xl sm:leading-tight dark:text-[#f5f4ed]">
					{lesson.title}
				</h1>

				{#if lesson.english_summary}
					<div class="mt-4 rounded-xl border border-[#e5e2d9] bg-[#f0eee6]/60 p-4 text-xs leading-relaxed text-[#6f6e69] dark:border-[#343330] dark:bg-[#232321] dark:text-[#a19f97]">
						<span class="font-mono uppercase tracking-wider text-[10px] text-[#141413] dark:text-[#f5f4ed]">English Summary: </span>
						{lesson.english_summary}
					</div>
				{/if}
			</header>

			<!-- Badge Unlocked Toast Notification -->
			{#if form?.badge_unlocked}
				<div class="my-6 flex items-center gap-3 rounded-2xl border border-amber-500/40 bg-amber-500/10 p-4 text-sm text-amber-800 dark:text-amber-300 shadow-sm animate-pulse">
					<Award class="h-6 w-6 shrink-0 text-amber-600 dark:text-amber-400" />
					<div>
						<div class="font-semibold">Mubarak Ho! Badge Unlocked!</div>
						<div class="text-xs opacity-90">Aap ne "{form.badge_unlocked}" badge earn kar liya hai aur extra XP profile mein add ho chuki hai!</div>
					</div>
				</div>
			{/if}

			<!-- Concept Diagram (DiagramKit) -->
			{#if lesson.diagram_script}
				<div class="my-8">
					<Diagram
						script={lesson.diagram_script}
						preset="midnight"
						animate={lesson.diagram_type || 'flow'}
						title="{lesson.lesson_code} Conceptual Architecture"
					/>
				</div>
			{/if}

			<!-- Main Roman Urdu Content (Markdown) -->
			<div class="py-6">
				<Markdown content={lesson.roman_urdu_content} />
			</div>

			<!-- Code Example (if separated in DB) -->
			{#if lesson.code_example}
				<div class="my-8">
					<div class="text-xs font-mono uppercase tracking-wider text-[#6f6e69] dark:text-[#a19f97] mb-1">
						Production Implementation
					</div>
					<CodeBlock code={lesson.code_example} language="python" title="PyTorch / Python Code" />
				</div>
			{/if}

			<!-- Quick Practice Checkpoint -->
			{#if practiceProject}
				<div class="my-8 rounded-2xl border border-amber-500/30 bg-amber-500/5 p-5 dark:border-amber-500/20">
					<div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-3">
						<div class="flex items-center gap-3">
							<div class="flex h-9 w-9 shrink-0 items-center justify-center rounded-xl bg-amber-500/20 text-amber-600 dark:text-amber-400">
								<Sparkles class="h-4 w-4" />
							</div>
							<div>
								<div class="flex items-center gap-2">
									<span class="rounded bg-amber-500/20 px-2 py-0.5 text-[10px] font-mono font-bold uppercase text-amber-800 dark:text-amber-300">
										Module Practice Checkpoint
									</span>
									<span class="rounded bg-emerald-500/10 px-2 py-0.5 text-[10px] font-mono font-bold text-emerald-700 dark:text-emerald-400">
										+{practiceProject.xp_reward} XP
									</span>
								</div>
								<h4 class="mt-1 font-serif text-sm font-bold text-[#141413] dark:text-[#f5f4ed]">
									{practiceProject.title} ({practiceProject.humorous_badge})
								</h4>
							</div>
						</div>
						<a
							href={practiceProject.colab_url}
							target="_blank"
							rel="noopener noreferrer"
							class="inline-flex items-center justify-center gap-1.5 rounded-xl bg-[#c96442] px-4 py-2 text-xs font-semibold text-white transition-all hover:bg-[#d97757] shrink-0"
						>
							<span>Open Colab Practice</span>
							<ExternalLink class="h-3.5 w-3.5" />
						</a>
					</div>
					<p class="mt-2 text-xs leading-relaxed text-[#6f6e69] dark:text-[#a19f97]">
						{practiceProject.description_roman_urdu}
					</p>
				</div>
			{/if}

			<!-- Hugging Face Interactive Sub-Project & Real-Time Lab -->
			{#if hfSubproject}
				<div class="my-8">
					<HfSubprojectCard subproject={hfSubproject} moduleNumber={mod.module_number} />
				</div>
			{/if}

			<!-- Mark Complete CTA Section -->
			<div class="my-12 rounded-2xl border border-[#e5e2d9] bg-[#f0eee6]/50 p-6 text-center dark:border-[#343330] dark:bg-[#232321]">
				{#if isCompleted}
					<div class="flex flex-col items-center gap-2">
						<div class="flex h-12 w-12 items-center justify-center rounded-full bg-emerald-500/20 text-emerald-600 dark:text-emerald-400">
							<CheckCircle2 class="h-6 w-6" />
						</div>
						<h3 class="font-serif text-lg font-semibold text-[#141413] dark:text-[#f5f4ed]">
							Lesson Mukammal Ho Chuka Hai!
						</h3>
						<p class="text-xs text-[#6f6e69] dark:text-[#a19f97]">
							Aap ke account mein +{lesson.xp_reward} XP add ho chuki hai aur streak record update ho chuka hai.
						</p>
					</div>
				{:else}
					<form
						method="POST"
						action="?/completeLesson"
						use:enhance={() => {
							isOptimisticCompleted = true;
						}}
					>
						<input type="hidden" name="lessonId" value={lesson.id} />
						<div class="flex flex-col items-center gap-3">
							<div class="flex h-10 w-10 items-center justify-center rounded-full bg-[#c96442]/10 text-[#c96442]">
								<Sparkles class="h-5 w-5" />
							</div>
							<div>
								<h3 class="font-serif text-lg font-semibold text-[#141413] dark:text-[#f5f4ed]">
									Lesson Samajh Aa Gaya?
								</h3>
								<p class="mt-0.5 text-xs text-[#6f6e69] dark:text-[#a19f97]">
									Complete mark karein aur +{lesson.xp_reward} XP earn karein
								</p>
							</div>
							<button
								type="submit"
								class="inline-flex h-11 items-center gap-2 rounded-xl bg-[#c96442] px-6 text-xs font-semibold text-white shadow-sm transition-all hover:bg-[#d97757] focus:outline-none focus:ring-2 focus:ring-[#c96442]/40"
							>
								<CheckCircle2 class="h-4 w-4" />
								<span>Mark as Complete (+{lesson.xp_reward} XP)</span>
							</button>
						</div>
					</form>
				{/if}
			</div>

			<!-- Prev / Next Navigation -->
			<div class="mt-12 flex flex-col items-stretch justify-between gap-4 border-t border-[#e5e2d9] pt-8 sm:flex-row sm:items-center dark:border-[#343330]">
				{#if prevLesson}
					<a
						href="/learn/{mod.slug}/{prevLesson.slug}"
						class="group flex flex-col rounded-xl border border-[#e5e2d9] bg-[#faf9f5] p-4 text-left transition-colors hover:border-[#c96442]/40 hover:bg-[#f0eee6] sm:max-w-xs dark:border-[#343330] dark:bg-[#232321] dark:hover:bg-[#262624]"
					>
						<span class="inline-flex items-center gap-1 text-[11px] font-mono text-[#6f6e69] dark:text-[#a19f97]">
							<ArrowLeft class="h-3 w-3" />
							Previous Lesson
						</span>
						<span class="mt-1 font-serif text-xs font-semibold text-[#141413] group-hover:text-[#c96442] dark:text-[#f5f4ed] truncate">
							{prevLesson.lesson_code}: {prevLesson.title}
						</span>
					</a>
				{:else}
					<div></div>
				{/if}

				{#if nextLesson}
					<a
						href="/learn/{mod.slug}/{nextLesson.slug}"
						class="group flex flex-col rounded-xl border border-[#e5e2d9] bg-[#faf9f5] p-4 text-right transition-colors hover:border-[#c96442]/40 hover:bg-[#f0eee6] sm:max-w-xs dark:border-[#343330] dark:bg-[#232321] dark:hover:bg-[#262624]"
					>
						<span class="inline-flex items-center justify-end gap-1 text-[11px] font-mono text-[#6f6e69] dark:text-[#a19f97]">
							Next Lesson
							<ArrowRight class="h-3 w-3" />
						</span>
						<span class="mt-1 font-serif text-xs font-semibold text-[#141413] group-hover:text-[#c96442] dark:text-[#f5f4ed] truncate">
							{nextLesson.lesson_code}: {nextLesson.title}
						</span>
					</a>
				{:else}
					<a
						href="/learn/{mod.slug}/quiz"
						class="group flex flex-col rounded-xl border border-amber-500/30 bg-amber-500/10 p-4 text-right transition-colors hover:bg-amber-500/20 sm:max-w-xs"
					>
						<span class="inline-flex items-center justify-end gap-1 text-[11px] font-mono text-amber-700 dark:text-amber-400">
							Module Quiz
							<ArrowRight class="h-3 w-3" />
						</span>
						<span class="mt-1 font-serif text-xs font-semibold text-amber-900 dark:text-amber-200 truncate">
							Take Module Quiz & Earn Badge
						</span>
					</a>
				{/if}
			</div>
		</article>
	</div>
</div>

<script lang="ts">
	import { CheckCircle2, Circle, ChevronDown, ChevronRight, HelpCircle, BookOpen, Layers } from 'lucide-svelte';

	interface LessonItem {
		id: string;
		module_id: string;
		lesson_code: string;
		slug: string;
		title: string;
		duration_minutes: number;
		xp_reward: number;
		order_index: number;
	}

	interface ModuleItem {
		id: string;
		module_number: number;
		slug: string;
		title: string;
		weeks_range: string;
		lessons?: LessonItem[];
	}

	interface Props {
		modules: ModuleItem[];
		currentLessonSlug?: string;
		currentModuleSlug?: string;
		completedLessonIds?: string[];
		isOpen?: boolean;
		onClose?: () => void;
	}

	let {
		modules = [],
		currentLessonSlug = '',
		currentModuleSlug = '',
		completedLessonIds = [],
		isOpen = false,
		onClose = () => {}
	}: Props = $props();

	// Set of expanded module IDs
	let expandedModules = $state<Record<string, boolean>>({});

	$effect(() => {
		// Auto-expand current module
		if (currentModuleSlug && modules.length > 0) {
			const mod = modules.find((m) => m.slug === currentModuleSlug);
			if (mod) {
				expandedModules[mod.id] = true;
			}
		}
	});

	function toggleModule(moduleId: string) {
		expandedModules[moduleId] = !expandedModules[moduleId];
	}

	function isCompleted(lessonId: string): boolean {
		return completedLessonIds.includes(lessonId);
	}
</script>

<!-- Desktop Sidebar & Mobile Drawer -->
<aside
	class="fixed inset-y-0 left-0 z-30 w-72 transform border-r border-[#e5e2d9] bg-[#faf9f5] pt-16 transition-transform duration-200 ease-in-out md:static md:translate-x-0 dark:border-[#343330] dark:bg-[#1f1e1d] {isOpen
		? 'translate-x-0'
		: '-translate-x-full'}"
>
	<div class="flex h-full flex-col">
		<!-- Header -->
		<div class="flex items-center justify-between border-b border-[#e5e2d9] px-4 py-3 dark:border-[#343330]">
			<div class="flex items-center gap-2">
				<BookOpen class="h-4 w-4 text-[#c96442]" />
				<span class="font-serif text-sm font-semibold tracking-tight text-[#141413] dark:text-[#f5f4ed]">
					Syllabus Explorer
				</span>
			</div>
			<span class="rounded bg-[#f0eee6] px-1.5 py-0.5 text-[10px] font-mono text-[#6f6e69] dark:bg-[#262624] dark:text-[#a19f97]">
				{modules.length} Modules
			</span>
		</div>

		<!-- Module & Lesson List -->
		<div class="flex-1 overflow-y-auto px-2 py-3 space-y-1">
			{#each modules as mod (mod.id)}
				{@const isCurrentModule = mod.slug === currentModuleSlug}
				{@const isExpanded = expandedModules[mod.id] ?? isCurrentModule}

				<div class="rounded-lg border border-transparent {isCurrentModule ? 'bg-[#f0eee6]/50 dark:bg-[#262624]/50' : ''}">
					<!-- Module Header Button -->
					<div class="flex items-center justify-between px-2.5 py-2 text-xs font-medium text-[#141413] dark:text-[#f5f4ed]">
						<button
							type="button"
							onclick={() => toggleModule(mod.id)}
							class="flex flex-1 items-center gap-2 text-left hover:text-[#c96442]"
						>
							{#if isExpanded}
								<ChevronDown class="h-3.5 w-3.5 text-[#6f6e69] dark:text-[#a19f97]" />
							{:else}
								<ChevronRight class="h-3.5 w-3.5 text-[#6f6e69] dark:text-[#a19f97]" />
							{/if}
							<span class="font-mono text-[11px] text-[#c96442]">M{mod.module_number}</span>
							<span class="line-clamp-1 flex-1">{mod.title}</span>
						</button>
						<a
							href="/learn/{mod.slug}"
							class="ml-1 rounded p-1 text-[#6f6e69] hover:bg-[#e4e1d8] hover:text-[#141413] dark:text-[#a19f97] dark:hover:bg-[#2e2d2a]"
							title="View Module Overview"
						>
							<Layers class="h-3 w-3" />
						</a>
					</div>

					<!-- Lessons List -->
					{#if isExpanded && mod.lessons && mod.lessons.length > 0}
						<div class="ml-4 space-y-0.5 border-l border-[#e5e2d9] pl-2 pb-1.5 dark:border-[#343330]">
							{#each mod.lessons as lesson (lesson.id)}
								{@const isActive = lesson.slug === currentLessonSlug}
								{@const completed = isCompleted(lesson.id)}

								<a
									href="/learn/{mod.slug}/{lesson.slug}"
									onclick={onClose}
									class="group flex items-center justify-between rounded-md px-2 py-1.5 text-xs transition-colors {isActive
										? 'bg-[#c96442]/10 font-medium text-[#c96442]'
										: 'text-[#6f6e69] hover:bg-[#f0eee6] hover:text-[#141413] dark:text-[#a19f97] dark:hover:bg-[#262624] dark:hover:text-[#f5f4ed]'}"
								>
									<div class="flex items-center gap-2 min-w-0">
										{#if completed}
											<CheckCircle2 class="h-3.5 w-3.5 shrink-0 text-emerald-600 dark:text-emerald-400" />
										{:else}
											<Circle class="h-3.5 w-3.5 shrink-0 text-[#a19f97] dark:text-[#6f6e69]" />
										{/if}
										<span class="truncate">{lesson.title}</span>
									</div>
									<span class="text-[10px] font-mono text-[#a19f97] dark:text-[#6f6e69]">
										{lesson.duration_minutes}m
									</span>
								</a>
							{/each}

							<!-- Quiz Link -->
							<a
								href="/learn/{mod.slug}/quiz"
								onclick={onClose}
								class="flex items-center gap-2 rounded-md px-2 py-1.5 text-xs font-mono text-amber-700 hover:bg-amber-50 dark:text-amber-400 dark:hover:bg-amber-950/20"
							>
								<HelpCircle class="h-3.5 w-3.5" />
								<span>Module Quiz & XP</span>
							</a>
						</div>
					{/if}
				</div>
			{/each}
		</div>
	</div>
</aside>

{#if isOpen}
	<button
		type="button"
		onclick={onClose}
		class="fixed inset-0 z-20 bg-black/40 backdrop-blur-xs md:hidden"
		aria-label="Close syllabus navigation"
	></button>
{/if}

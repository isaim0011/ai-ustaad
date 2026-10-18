<script lang="ts">
	import { enhance } from '$app/forms';
	import { CheckCircle2, XCircle, AlertCircle, Sparkles, Award, ArrowLeft, ArrowRight, RotateCcw, HelpCircle } from 'lucide-svelte';
	import type { ActionData, PageData } from './$types';

	let { data, form }: { data: PageData; form: ActionData } = $props();

	const mod = $derived(data.module);
	const quiz = $derived(data.quiz);
	const questions = $derived(data.questions ?? []);

	let selectedAnswers = $state<Record<string, number>>({});
	let isSubmitted = $derived(Boolean(form?.success));

	function selectOption(questionId: string, optionIndex: number) {
		if (isSubmitted) return;
		selectedAnswers = { ...selectedAnswers, [questionId]: optionIndex };
	}

	const answeredCount = $derived(Object.keys(selectedAnswers).length);
	const allAnswered = $derived(answeredCount === questions.length && questions.length > 0);
</script>

<div class="mx-auto max-w-3xl px-4 py-10 sm:px-6 lg:px-8 space-y-8">
	<!-- Breadcrumbs -->
	<nav class="flex items-center gap-2 text-xs font-mono text-[#6f6e69] dark:text-[#a19f97]">
		<a href="/learn" class="hover:text-[#c96442]">Curriculum</a>
		<span>/</span>
		<a href="/learn/{mod.slug}" class="hover:text-[#c96442]">{mod.title}</a>
		<span>/</span>
		<span class="text-[#141413] dark:text-[#f5f4ed]">Module Quiz</span>
	</nav>

	<!-- Quiz Header Banner -->
	<div class="border-b border-[#e5e2d9] pb-6 dark:border-[#343330]">
		<div class="flex items-center gap-2 text-xs font-mono text-[#c96442]">
			<HelpCircle class="h-4 w-4" />
			<span>Module {mod.module_number} Knowledge Check</span>
		</div>
		<h1 class="mt-2 font-serif text-3xl font-bold tracking-tight text-[#141413] dark:text-[#f5f4ed]">
			{quiz.title}
		</h1>
		<div class="mt-3 flex flex-wrap items-center gap-4 text-xs font-mono text-[#6f6e69] dark:text-[#a19f97]">
			<span>{questions.length} Questions</span>
			<span>•</span>
			<span>Passing Score: {quiz.passing_score_pct}%</span>
			<span>•</span>
			<span class="text-[#c96442]">Reward: +{quiz.xp_reward} XP</span>
		</div>
	</div>

	<!-- Results Card (if submitted) -->
	{#if form?.success}
		{@const passed = form.score_pct >= quiz.passing_score_pct}
		<div
			class="rounded-2xl border p-6 text-center shadow-xs {passed
				? 'border-emerald-500/30 bg-emerald-500/10 dark:border-emerald-500/20'
				: 'border-amber-500/30 bg-amber-500/10 dark:border-amber-500/20'}"
		>
			<div class="mx-auto flex h-14 w-14 items-center justify-center rounded-full {passed ? 'bg-emerald-500/20 text-emerald-600 dark:text-emerald-400' : 'bg-amber-500/20 text-amber-600 dark:text-amber-400'}">
				{#if passed}
					<CheckCircle2 class="h-8 w-8" />
				{:else}
					<RotateCcw class="h-8 w-8" />
				{/if}
			</div>

			<h2 class="mt-4 font-serif text-2xl font-bold text-[#141413] dark:text-[#f5f4ed]">
				{passed ? 'Zabardast! Aap Pass Ho Gaye!' : 'Thori Si Mazeed Practice Darkar Hai'}
			</h2>

			<div class="mt-2 text-sm text-[#6f6e69] dark:text-[#a19f97]">
				Aap ka score: <span class="font-bold font-mono text-base text-[#141413] dark:text-[#f5f4ed]">{form.score_pct}%</span>
				({form.correctCount} / {form.totalQuestions} right)
			</div>

			{#if form.xp_awarded > 0}
				<div class="mt-3 inline-flex items-center gap-1.5 rounded-full border border-[#c96442]/30 bg-[#c96442]/10 px-3 py-1 text-xs font-mono font-medium text-[#c96442]">
					<Sparkles class="h-3.5 w-3.5" />
					<span>+{form.xp_awarded} XP Earned!</span>
				</div>
			{/if}

			{#if form.badge_unlocked}
				<div class="mt-4 mx-auto max-w-md rounded-xl border border-amber-500/40 bg-amber-500/20 p-3 text-xs font-medium text-amber-900 dark:text-amber-200">
					👑 Badge Unlocked: <strong>{form.badge_unlocked}</strong>! (Bonus XP added to profile)
				</div>
			{/if}

			<div class="mt-6 flex justify-center gap-4">
				<a
					href="/learn/{mod.slug}"
					class="inline-flex items-center gap-1.5 rounded-xl border border-[#e5e2d9] bg-[#faf9f5] px-4 py-2 text-xs font-semibold text-[#141413] hover:border-[#c96442]/40 dark:border-[#343330] dark:bg-[#232321] dark:text-[#f5f4ed]"
				>
					<ArrowLeft class="h-3.5 w-3.5" />
					<span>Back to Module</span>
				</a>
			</div>
		</div>
	{/if}

	<!-- Questions List -->
	<div class="space-y-6">
		{#each questions as q, idx (q.id)}
			{@const userChoice = selectedAnswers[q.id]}
			{@const isCorrect = userChoice === q.correct_option_index}

			<div class="rounded-2xl border border-[#e5e2d9] bg-[#faf9f5] p-6 shadow-xs dark:border-[#343330] dark:bg-[#232321]">
				<!-- Question Header -->
				<div class="flex items-center justify-between text-xs font-mono text-[#6f6e69] dark:text-[#a19f97]">
					<span>Sawal {q.question_number} of {questions.length}</span>
					{#if isSubmitted}
						{#if isCorrect}
							<span class="inline-flex items-center gap-1 text-emerald-600 dark:text-emerald-400 font-medium">
								<CheckCircle2 class="h-3.5 w-3.5" /> Correct
							</span>
						{:else}
							<span class="inline-flex items-center gap-1 text-rose-600 dark:text-rose-400 font-medium">
								<XCircle class="h-3.5 w-3.5" /> Incorrect
							</span>
						{/if}
					{/if}
				</div>

				<!-- Question Text in Roman Urdu -->
				<h3 class="mt-3 font-serif text-base font-semibold leading-relaxed text-[#141413] dark:text-[#f5f4ed]">
					{q.question_roman_urdu}
				</h3>

				<!-- Options List -->
				<div class="mt-4 space-y-2.5">
					{#if Array.isArray(q.options)}
						{#each q.options as opt, optIdx}
							{@const isSelected = userChoice === optIdx}
							{@const isThisCorrect = optIdx === q.correct_option_index}

							<button
								type="button"
								disabled={isSubmitted}
								onclick={() => selectOption(q.id, optIdx)}
								class="flex w-full items-start gap-3 rounded-xl border p-3 text-left text-xs transition-colors {isSubmitted
									? isThisCorrect
										? 'border-emerald-500 bg-emerald-500/10 text-[#141413] dark:text-[#f5f4ed]'
										: isSelected
											? 'border-rose-500 bg-rose-500/10 text-[#141413] dark:text-[#f5f4ed]'
											: 'border-[#e5e2d9] opacity-60 dark:border-[#343330]'
									: isSelected
										? 'border-[#c96442] bg-[#c96442]/10 font-medium text-[#c96442]'
										: 'border-[#e5e2d9] bg-[#f0eee6]/40 text-[#2c2b28] hover:border-[#c96442]/40 hover:bg-[#e8e5db]/60 dark:border-[#343330] dark:bg-[#1a1a19] dark:text-[#dcd9ce]'}"
							>
								<span
									class="flex h-5 w-5 shrink-0 items-center justify-center rounded-full font-mono text-[11px] {isSelected
										? 'bg-[#c96442] text-white'
										: 'bg-[#e5e2d9] text-[#6f6e69] dark:bg-[#343330] dark:text-[#a19f97]'}"
								>
									{String.fromCharCode(65 + optIdx)}
								</span>
								<span class="leading-relaxed pt-0.5">{opt}</span>
							</button>
						{/each}
					{/if}
				</div>

				<!-- Explanation in Roman Urdu (Shown after submission) -->
				{#if isSubmitted && q.explanation_roman_urdu}
					<div class="mt-4 rounded-xl border border-[#e5e2d9] bg-[#f0eee6]/60 p-3.5 text-xs text-[#2c2b28] dark:border-[#343330] dark:bg-[#191918] dark:text-[#dcd9ce]">
						<div class="font-mono text-[10px] uppercase tracking-wider text-[#c96442] mb-1">
							Roman Urdu Tashreeh (Explanation):
						</div>
						<p class="leading-relaxed">{q.explanation_roman_urdu}</p>
					</div>
				{/if}
			</div>
		{/each}
	</div>

	<!-- Submit Button Form -->
	{#if !isSubmitted}
		<div class="sticky bottom-6 rounded-2xl border border-[#e5e2d9] bg-[#faf9f5]/95 p-4 backdrop-blur-md shadow-lg dark:border-[#343330] dark:bg-[#232321]/95">
			<form method="POST" action="?/submitQuiz" use:enhance class="flex items-center justify-between">
				<input type="hidden" name="quizId" value={quiz.id} />
				<input type="hidden" name="answers" value={JSON.stringify(selectedAnswers)} />

				<div class="text-xs font-mono text-[#6f6e69] dark:text-[#a19f97]">
					{answeredCount} of {questions.length} answered
				</div>

				<button
					type="submit"
					disabled={!allAnswered}
					class="inline-flex h-11 items-center gap-2 rounded-xl bg-[#c96442] px-6 text-xs font-semibold text-white shadow-sm transition-all hover:bg-[#d97757] disabled:cursor-not-allowed disabled:opacity-40"
				>
					<span>Submit Quiz & Claim XP</span>
					<ArrowRight class="h-4 w-4" />
				</button>
			</form>
		</div>
	{/if}
</div>

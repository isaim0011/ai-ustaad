<script lang="ts">
	import {
		Sparkles,
		Cpu,
		Database,
		ExternalLink,
		Layers,
		Terminal,
		Play,
		Check,
		Copy,
		Code2,
		Share2,
		Flame
	} from 'lucide-svelte';
	import CodeBlock from '$lib/components/CodeBlock.svelte';
	import type { HfSubproject } from '$lib/types';

	interface Props {
		subproject: HfSubproject;
		moduleNumber?: number;
		className?: string;
	}

	let { subproject, moduleNumber, className = '' }: Props = $props();

	let activeTab = $state<'starter' | 'gradio'>('starter');
	let copiedLink = $state(false);

	const starterCode = $derived(
		subproject.starter_code || subproject.runnable_starter_code || ''
	);
	const gradioCode = $derived(
		subproject.gradio_code || subproject.gradio_demo_code || ''
	);

	const currentCode = $derived(activeTab === 'starter' ? starterCode : gradioCode);
	const currentTitle = $derived(
		activeTab === 'starter'
			? `Python Starter Pipeline (${subproject.hf_model})`
			: `Gradio 5 Interactive Web App (${subproject.project_slug})`
	);

	function copyShareUrl() {
		if (typeof window !== 'undefined') {
			navigator.clipboard.writeText(window.location.href).catch(() => {});
			copiedLink = true;
			setTimeout(() => {
				copiedLink = false;
			}, 2000);
		}
	}
</script>

<div
	class="relative overflow-hidden rounded-2xl border-2 border-[#c96442]/30 bg-gradient-to-b from-[#c96442]/5 via-white to-white p-6 shadow-sm transition-all dark:border-[#c96442]/40 dark:from-[#c96442]/10 dark:via-[#1c1b18] dark:to-[#181715] {className}"
>
	<!-- Top Label & Tags -->
	<div class="flex flex-wrap items-center justify-between gap-3 border-b border-[#e5e2d9] pb-5 dark:border-[#343330]">
		<div class="flex items-center gap-2.5">
			<div class="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl bg-[#c96442] text-white shadow-sm">
				<Sparkles class="h-5 w-5" />
			</div>
			<div>
				<div class="flex flex-wrap items-center gap-2">
					<span class="rounded bg-[#c96442] px-2 py-0.5 text-[10px] font-mono font-bold uppercase tracking-wider text-white">
						Hugging Face Lab
					</span>
					{#if moduleNumber !== undefined}
						<span class="rounded bg-[#f0eee6] px-2 py-0.5 text-[11px] font-mono text-[#6f6e69] dark:bg-[#262624] dark:text-[#a19f97]">
							Module {moduleNumber} Interactive Project
						</span>
					{/if}
					<span class="rounded bg-emerald-500/10 px-2 py-0.5 text-[11px] font-mono font-semibold text-emerald-700 dark:text-emerald-400">
						100% Free Open-Source
					</span>
				</div>
				<h3 class="mt-1 font-serif text-xl font-bold tracking-tight text-[#141413] sm:text-2xl dark:text-[#f5f4ed]">
					{subproject.project_title}
				</h3>
			</div>
		</div>

		<!-- Quick Specs -->
		<div class="flex flex-wrap items-center gap-2 text-xs font-mono text-[#6f6e69] dark:text-[#a19f97]">
			<span class="inline-flex items-center gap-1 rounded-lg bg-[#f0eee6] px-2.5 py-1 dark:bg-[#262624]">
				<Cpu class="h-3.5 w-3.5 text-[#c96442]" />
				{subproject.hardware_requirement}
			</span>
			<span class="inline-flex items-center gap-1 rounded-lg bg-[#f0eee6] px-2.5 py-1 dark:bg-[#262624]">
				<Terminal class="h-3.5 w-3.5 text-emerald-600 dark:text-emerald-400" />
				Runtime: {subproject.estimated_runtime_seconds}
			</span>
		</div>
	</div>

	<!-- Badges Row: Model & Dataset -->
	<div class="mt-5 grid grid-cols-1 gap-3 sm:grid-cols-2">
		<!-- HF Model Badge -->
		<a
			href={subproject.hf_model_url}
			target="_blank"
			rel="noopener noreferrer"
			class="group flex items-center justify-between rounded-xl border border-amber-500/30 bg-amber-500/5 p-3.5 transition-all hover:border-amber-500/60 hover:bg-amber-500/10 dark:border-amber-500/20 dark:bg-amber-500/5"
			title="View model weights, model card & metrics on Hugging Face Hub"
		>
			<div class="flex items-center gap-3 min-w-0">
				<div class="flex h-9 w-9 shrink-0 items-center justify-center rounded-lg bg-amber-500/20 text-amber-700 dark:text-amber-400">
					<Layers class="h-4 w-4" />
				</div>
				<div class="min-w-0">
					<div class="text-[10px] font-mono uppercase tracking-wider text-amber-700 dark:text-amber-400">
						Hugging Face Model
					</div>
					<div class="truncate font-mono text-xs font-bold text-[#141413] group-hover:text-[#c96442] dark:text-[#f5f4ed]">
						{subproject.hf_model}
					</div>
				</div>
			</div>
			<ExternalLink class="h-4 w-4 shrink-0 text-amber-700 opacity-60 transition-opacity group-hover:opacity-100 dark:text-amber-400" />
		</a>

		<!-- HF Dataset Badge -->
		<a
			href={subproject.hf_dataset_url}
			target="_blank"
			rel="noopener noreferrer"
			class="group flex items-center justify-between rounded-xl border border-blue-500/30 bg-blue-500/5 p-3.5 transition-all hover:border-blue-500/60 hover:bg-blue-500/10 dark:border-blue-500/20 dark:bg-blue-500/5"
			title="View dataset card, splits & viewer on Hugging Face Hub"
		>
			<div class="flex items-center gap-3 min-w-0">
				<div class="flex h-9 w-9 shrink-0 items-center justify-center rounded-lg bg-blue-500/20 text-blue-700 dark:text-blue-400">
					<Database class="h-4 w-4" />
				</div>
				<div class="min-w-0">
					<div class="text-[10px] font-mono uppercase tracking-wider text-blue-700 dark:text-blue-400">
						Hugging Face Dataset
					</div>
					<div class="truncate font-mono text-xs font-bold text-[#141413] group-hover:text-blue-600 dark:text-[#f5f4ed]">
						{subproject.hf_dataset}
					</div>
				</div>
			</div>
			<ExternalLink class="h-4 w-4 shrink-0 text-blue-700 opacity-60 transition-opacity group-hover:opacity-100 dark:text-blue-400" />
		</a>
	</div>

	<!-- Learning Takeaway Summary -->
	{#if subproject.key_learning_takeaway}
		<div class="mt-4 rounded-xl border border-[#e5e2d9] bg-[#f9f8f5] p-3.5 text-xs text-[#6f6e69] dark:border-[#343330] dark:bg-[#201f1c] dark:text-[#a19f97]">
			<span class="font-bold text-[#141413] dark:text-[#f5f4ed]">Architecture & Learning Goals:</span>
			{subproject.key_learning_takeaway}
		</div>
	{/if}

	<!-- 1-Click Action Buttons -->
	<div class="mt-5 flex flex-wrap items-center gap-3">
		<!-- Open in Google Colab (Free T4) -->
		<a
			href={subproject.colab_url}
			target="_blank"
			rel="noopener noreferrer"
			class="inline-flex h-10 items-center gap-2 rounded-xl bg-[#c96442] px-4 text-xs font-semibold text-white shadow-sm transition-all hover:bg-[#d97757] hover:scale-[1.02] focus:outline-none focus:ring-2 focus:ring-[#c96442]/40"
		>
			<Play class="h-3.5 w-3.5 fill-current" />
			<span>Open in Google Colab (Free T4)</span>
		</a>

		<!-- Run in Kaggle (30h/wk) -->
		<a
			href={subproject.kaggle_url}
			target="_blank"
			rel="noopener noreferrer"
			class="inline-flex h-10 items-center gap-2 rounded-xl border border-sky-500/40 bg-sky-500/10 px-4 text-xs font-semibold text-sky-800 transition-all hover:bg-sky-500/20 hover:scale-[1.02] dark:border-sky-500/30 dark:bg-sky-500/10 dark:text-sky-300"
		>
			<Cpu class="h-3.5 w-3.5 text-sky-600 dark:text-sky-400" />
			<span>Run in Kaggle (Dual-T4 Free)</span>
		</a>

		<!-- View on Hugging Face Hub -->
		<a
			href={subproject.hf_model_url}
			target="_blank"
			rel="noopener noreferrer"
			class="inline-flex h-10 items-center gap-2 rounded-xl border border-[#e5e2d9] bg-[#f0eee6] px-4 text-xs font-semibold text-[#141413] transition-all hover:border-[#c96442] hover:bg-white dark:border-[#343330] dark:bg-[#262624] dark:text-[#f5f4ed] dark:hover:bg-[#1f1e1b]"
		>
			<Layers class="h-3.5 w-3.5 text-amber-600 dark:text-amber-400" />
			<span>View on Hugging Face Hub</span>
			<ExternalLink class="h-3 w-3 opacity-60" />
		</a>
	</div>

	<!-- In-Browser Starter Code & Gradio Live UI Tabs -->
	<div class="mt-6">
		<div class="flex items-center justify-between border-b border-[#e5e2d9] pb-2 dark:border-[#343330]">
			<div class="flex items-center gap-2">
				<button
					type="button"
					onclick={() => (activeTab = 'starter')}
					class="inline-flex items-center gap-1.5 rounded-lg px-3 py-1.5 text-xs font-mono font-medium transition-all {activeTab === 'starter'
						? 'bg-[#c96442] text-white shadow-sm'
						: 'text-[#6f6e69] hover:bg-[#f0eee6] dark:text-[#a19f97] dark:hover:bg-[#262624]'}"
				>
					<Terminal class="h-3.5 w-3.5" />
					<span>Runnable Starter Script</span>
				</button>
				<button
					type="button"
					onclick={() => (activeTab = 'gradio')}
					class="inline-flex items-center gap-1.5 rounded-lg px-3 py-1.5 text-xs font-mono font-medium transition-all {activeTab === 'gradio'
						? 'bg-[#c96442] text-white shadow-sm'
						: 'text-[#6f6e69] hover:bg-[#f0eee6] dark:text-[#a19f97] dark:hover:bg-[#262624]'}"
				>
					<Code2 class="h-3.5 w-3.5" />
					<span>Gradio 5 Live UI App</span>
				</button>
			</div>

			<span class="text-[11px] font-mono text-[#6f6e69] dark:text-[#a19f97] hidden sm:inline">
				{activeTab === 'starter' ? 'transformers / datasets pipeline' : 'gradio.Interface web server'}
			</span>
		</div>

		<!-- Code Display -->
		<div class="mt-3">
			<CodeBlock
				code={currentCode}
				language="python"
				title={currentTitle}
				showColab={true}
			/>
		</div>
	</div>
</div>

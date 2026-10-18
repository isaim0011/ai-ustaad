<script lang="ts">
	import { ArrowRight, BookOpen, Clock, Sparkles } from 'lucide-svelte';
	import type { PageData } from './$types';

	let { data }: { data: PageData } = $props();

	const blogs = $derived(data.blogs ?? []);
	let selectedCategory = $state<string>('All');

	const categories = $derived(['All', ...new Set(blogs.map((b: any) => b.category))]);

	const filteredBlogs = $derived(
		selectedCategory === 'All'
			? blogs
			: blogs.filter((b: any) => b.category === selectedCategory)
	);
</script>

<div class="mx-auto max-w-7xl px-4 py-12 sm:px-6 lg:px-8 space-y-10">
	<!-- Header -->
	<div class="mx-auto max-w-3xl text-center">
		<div class="inline-flex items-center gap-2 rounded-full border border-[#c96442]/30 bg-[#c96442]/10 px-3 py-1 text-xs font-mono font-medium text-[#c96442]">
			<Sparkles class="h-3.5 w-3.5" />
			<span>System Architecture & Production Engineering</span>
		</div>
		<h1 class="mt-4 font-serif text-3xl font-bold tracking-tight text-[#141413] sm:text-5xl dark:text-[#f5f4ed]">
			Engineering Blogs in Roman Urdu
		</h1>
		<p class="mt-4 text-base text-[#6f6e69] dark:text-[#a19f97]">
			Deep-dive technical articles: FlashAttention, ColPali Multi-Vector RAG, Anthropic MCP Swarms, DeepSeek GRPO, aur Rust Axum microservices.
		</p>
	</div>

	<!-- Category Filter Pills -->
	<div class="flex flex-wrap items-center justify-center gap-2">
		{#each categories as cat}
			<button
				type="button"
				onclick={() => (selectedCategory = cat)}
				class="rounded-full px-3.5 py-1.5 text-xs font-mono transition-colors {selectedCategory === cat
					? 'bg-[#c96442] text-white shadow-xs'
					: 'border border-[#e5e2d9] bg-[#f0eee6] text-[#6f6e69] hover:border-[#c96442]/40 hover:text-[#141413] dark:border-[#343330] dark:bg-[#262624] dark:text-[#a19f97] dark:hover:text-[#f5f4ed]'}"
			>
				{cat}
			</button>
		{/each}
	</div>

	<!-- Blog Grid -->
	<div class="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3">
		{#each filteredBlogs as blog (blog.id)}
			<a
				href="/blog/{blog.slug}"
				class="group flex flex-col justify-between rounded-2xl border border-[#e5e2d9] bg-[#faf9f5] p-6 shadow-xs transition-all hover:border-[#c96442]/40 hover:shadow-md dark:border-[#343330] dark:bg-[#232321]"
			>
				<div>
					<div class="flex items-center justify-between text-xs font-mono text-[#6f6e69] dark:text-[#a19f97]">
						<span class="rounded bg-[#f0eee6] px-2 py-0.5 text-[10px] uppercase font-medium dark:bg-[#262624]">
							{blog.category}
						</span>
						<span class="flex items-center gap-1">
							<Clock class="h-3 w-3" />
							{blog.reading_time_minutes} min read
						</span>
					</div>

					<h2 class="mt-4 font-serif text-lg font-bold text-[#141413] group-hover:text-[#c96442] dark:text-[#f5f4ed]">
						{blog.title}
					</h2>

					<p class="mt-2 line-clamp-3 text-xs leading-relaxed text-[#6f6e69] dark:text-[#a19f97]">
						{blog.summary_roman_urdu}
					</p>
				</div>

				<div class="mt-6 flex items-center gap-1.5 pt-4 border-t border-[#e5e2d9] text-xs font-mono text-[#c96442] dark:border-[#343330]">
					<span>Read technical article</span>
					<ArrowRight class="h-3.5 w-3.5 transition-transform group-hover:translate-x-1" />
				</div>
			</a>
		{/each}
	</div>
</div>

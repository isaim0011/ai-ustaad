<script lang="ts">
	import { ArrowLeft, ArrowRight, Clock, Sparkles, Cpu, BookOpen, Share2 } from 'lucide-svelte';
	import Diagram from '$lib/components/Diagram.svelte';
	import Markdown from '$lib/components/Markdown.svelte';
	import CodeBlock from '$lib/components/CodeBlock.svelte';
	import Seo from '$lib/components/Seo.svelte';
	import type { PageData } from './$types';

	let { data }: { data: PageData } = $props();

	const blog = $derived(data.blog);
	const adjacent = $derived(data.adjacent ?? []);
</script>

<Seo
	title={blog.title}
	description={blog.summary_roman_urdu}
	canonical={`https://ai-ustaad.pages.dev/blog/${blog.slug}`}
	ogType="article"
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
					"name": "Engineering Blog",
					"item": "https://ai-ustaad.pages.dev/blog"
				},
				{
					"@type": "ListItem",
					"position": 3,
					"name": blog.title,
					"item": `https://ai-ustaad.pages.dev/blog/${blog.slug}`
				}
			]
		},
		{
			"@context": "https://schema.org",
			"@type": "TechArticle",
			"headline": blog.title,
			"description": blog.summary_roman_urdu,
			"image": "https://ai-ustaad.pages.dev/og-image.png",
			"author": {
				"@type": "Person",
				"name": "Bimo",
				"url": "https://github.com/isaim0011"
			},
			"publisher": {
				"@type": "EducationalOrganization",
				"name": "AI Ustaad",
				"url": "https://ai-ustaad.pages.dev",
				"logo": "https://ai-ustaad.pages.dev/favicon.svg"
			},
			"mainEntityOfPage": {
				"@type": "WebPage",
				"@id": `https://ai-ustaad.pages.dev/blog/${blog.slug}`
			},
			"inLanguage": ["ur-Latn", "en"],
			"articleSection": blog.category
		}
	]}
/>

<div class="mx-auto max-w-4xl px-4 py-12 sm:px-6 lg:px-8 space-y-10">
	<!-- Breadcrumbs -->
	<nav class="flex items-center gap-2 text-xs font-mono text-[#6f6e69] dark:text-[#a19f97]">
		<a href="/blog" class="hover:text-[#c96442]">Engineering Blog</a>
		<span>/</span>
		<span class="rounded bg-[#f0eee6] px-1.5 py-0.5 text-[10px] uppercase font-medium dark:bg-[#262624]">
			{blog.category}
		</span>
	</nav>

	<!-- Article Header -->
	<header class="border-b border-[#e5e2d9] pb-8 dark:border-[#343330]">
		<div class="flex items-center gap-2 text-xs font-mono text-[#6f6e69] dark:text-[#a19f97]">
			<span class="flex items-center gap-1">
				<Clock class="h-3.5 w-3.5" />
				{blog.reading_time_minutes} min read
			</span>
			<span>•</span>
			<span>Roman Urdu Technical Deep-Dive</span>
		</div>

		<h1 class="mt-4 font-serif text-3xl font-bold tracking-tight text-[#141413] sm:text-5xl sm:leading-tight dark:text-[#f5f4ed]">
			{blog.title}
		</h1>

		<p class="mt-4 text-base leading-relaxed text-[#6f6e69] sm:text-lg dark:text-[#a19f97]">
			{blog.summary_roman_urdu}
		</p>
	</header>

	<!-- Architecture Diagram (DiagramKit) -->
	{#if blog.diagram_script}
		<div class="my-8">
			<Diagram
				script={blog.diagram_script}
				preset={blog.diagram_preset || 'midnight'}
				animate={blog.diagram_animation || 'flow'}
				title="System Architecture Diagram"
			/>
		</div>
	{/if}

	<!-- Main Prose (Markdown) -->
	<div class="py-4">
		<Markdown content={blog.content_roman_urdu} />
	</div>

	<!-- Production Code Snippet -->
	{#if blog.code_snippet}
		<div class="my-8">
			<div class="text-xs font-mono uppercase tracking-wider text-[#6f6e69] dark:text-[#a19f97] mb-1">
				Production Implementation Snippet
			</div>
			<CodeBlock code={blog.code_snippet} language="python" title="Code Walkthrough" />
		</div>
	{/if}

	<!-- Compute Recipe -->
	{#if blog.compute_recipe}
		<div class="my-8 rounded-2xl border border-amber-500/30 bg-amber-500/5 p-6 shadow-xs dark:border-amber-500/20">
			<div class="flex items-center gap-2 text-xs font-mono uppercase tracking-wider text-amber-800 dark:text-amber-400">
				<Cpu class="h-4 w-4" />
				<span>Zero-GPU Cloud Compute Recipe</span>
			</div>
			<div class="mt-2 text-xs leading-relaxed text-[#2c2b28] dark:text-[#dcd9ce]">
				<CodeBlock code={blog.compute_recipe} language="bash" title="Compute Setup Recipe" />
			</div>
		</div>
	{/if}

	<!-- Adjacent Recommended Articles -->
	{#if adjacent.length > 0}
		<div class="border-t border-[#e5e2d9] pt-10 dark:border-[#343330]">
			<h3 class="font-serif text-xl font-bold text-[#141413] dark:text-[#f5f4ed]">
				Next Technical Deep-Dives
			</h3>
			<div class="mt-4 grid grid-cols-1 gap-4 sm:grid-cols-2">
				{#each adjacent as item}
					<a
						href="/blog/{item.slug}"
						class="group rounded-xl border border-[#e5e2d9] bg-[#faf9f5] p-4 transition-colors hover:border-[#c96442]/40 hover:bg-[#f0eee6] dark:border-[#343330] dark:bg-[#232321] dark:hover:bg-[#262624]"
					>
						<span class="text-[10px] font-mono uppercase text-[#c96442]">{item.category}</span>
						<h4 class="mt-1 font-serif text-sm font-semibold text-[#141413] group-hover:text-[#c96442] dark:text-[#f5f4ed]">
							{item.title}
						</h4>
						<div class="mt-2 flex items-center gap-1 text-xs font-mono text-[#6f6e69] dark:text-[#a19f97]">
							<span>{item.reading_time_minutes} min read</span>
							<ArrowRight class="h-3 w-3 transition-transform group-hover:translate-x-1" />
						</div>
					</a>
				{/each}
			</div>
		</div>
	{/if}
</div>

<script lang="ts">
	import './layout.css';
	import { ModeWatcher } from 'mode-watcher';
	import TopNav from '$lib/components/TopNav.svelte';
	import Footer from '$lib/components/Footer.svelte';
	import SupabaseSetupNotice from '$lib/components/SupabaseSetupNotice.svelte';
	import type { LayoutData } from './$types';

	let { data, children }: { data: LayoutData; children: any } = $props();
</script>

<svelte:head>
	<title>AI Ustaad — Zero se Production tak (ai-ustaad.pages.dev)</title>
	<meta name="description" content="AI Ustaad by Bimo (ai-ustaad.pages.dev) — South Asia ka pehla complete, production-grade Roman Urdu AI Engineering curriculum." />
	<link rel="canonical" href="https://ai-ustaad.pages.dev" />
	
	<!-- OpenGraph -->
	<meta property="og:type" content="website" />
	<meta property="og:site_name" content="AI Ustaad" />
	<meta property="og:title" content="AI Ustaad — Zero se Production tak | by Bimo" />
	<meta property="og:description" content="Zero-GPU cloud recipes, first-principles tensor math, Transformers, Modern RAG, Anthropic MCP, DeepSeek-R1 GRPO aur Rust Axum." />
	<meta property="og:url" content="https://ai-ustaad.pages.dev" />
	<meta property="og:image" content="https://ai-ustaad.pages.dev/favicon.svg" />
	
	<!-- Twitter -->
	<meta name="twitter:card" content="summary_large_image" />
	<meta name="twitter:title" content="AI Ustaad — Zero se Production tak | by Bimo" />
	<meta name="twitter:description" content="Zero-GPU cloud recipes, first-principles tensor math, Transformers, Modern RAG, Anthropic MCP, DeepSeek-R1 GRPO aur Rust Axum." />
	<meta name="twitter:image" content="https://ai-ustaad.pages.dev/favicon.svg" />
</svelte:head>

<ModeWatcher defaultMode="system" />

<div class="flex min-h-screen flex-col bg-[#faf9f5] text-[#141413] transition-colors dark:bg-[#141413] dark:text-[#f5f4ed]">
	<TopNav user={data.user} profile={data.profile} supabaseConfigured={data.supabaseConfigured} />

	{#if !data.supabaseConfigured}
		<SupabaseSetupNotice />
	{/if}

	<main class="flex-1">
		{@render children()}
	</main>

	<Footer />
</div>

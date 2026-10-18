<script lang="ts">
	import './layout.css';
	import { ModeWatcher } from 'mode-watcher';
	import TopNav from '$lib/components/TopNav.svelte';
	import Footer from '$lib/components/Footer.svelte';
	import SupabaseSetupNotice from '$lib/components/SupabaseSetupNotice.svelte';
	import type { LayoutData } from './$types';

	let { data, children }: { data: LayoutData; children: any } = $props();
</script>


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

<script lang="ts">
	import { toggleMode, mode } from 'mode-watcher';
	import { Sun, Moon } from 'lucide-svelte';
</script>

<button
	onclick={toggleMode}
	type="button"
	class="inline-flex h-9 w-9 items-center justify-center rounded-lg border border-[#e5e2d9] bg-[#f0eee6] text-[#6f6e69] transition-colors hover:border-[#c96442]/40 hover:bg-[#e8e5db] hover:text-[#141413] dark:border-[#343330] dark:bg-[#262624] dark:text-[#a19f97] dark:hover:border-[#c96442]/40 dark:hover:bg-[#2e2d2a] dark:hover:text-[#f5f4ed] focus:outline-none focus:ring-2 focus:ring-[#c96442]/30"
	aria-label="Toggle color theme"
	title="Toggle theme"
>
	{#if $mode === 'dark'}
		<Sun class="h-4 w-4 text-[#d97757]" />
	{:else}
		<Moon class="h-4 w-4 text-[#6f6e69]" />
	{/if}
</button>

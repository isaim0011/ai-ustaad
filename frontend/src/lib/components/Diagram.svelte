<script lang="ts">
	import { PUBLIC_API_URL } from '$env/static/public';
	import { Maximize2, Minimize2, RefreshCw, Sparkles } from 'lucide-svelte';
	import { b64url, renderDiagramKitSvg } from '$lib/utils/diagramkit';

	interface Props {
		script: string;
		preset?: string;
		animate?: string;
		title?: string;
		class?: string;
	}

	let {
		script = '',
		preset = 'midnight',
		animate = 'flow',
		title = 'Architecture Diagram',
		class: className = ''
	}: Props = $props();

	let svg = $state<string>('');
	let loading = $state<boolean>(true);
	let isExpanded = $state<boolean>(false);
	let renderSource = $state<string>('DiagramKit Engine');

	const localApiUrl = PUBLIC_API_URL || 'http://127.0.0.1:8080';

	async function fetchWithTimeout(url: string, options: RequestInit, timeoutMs = 2000): Promise<Response> {
		const controller = new AbortController();
		const timeoutId = setTimeout(() => controller.abort(), timeoutMs);
		try {
			const res = await fetch(url, { ...options, signal: controller.signal });
			clearTimeout(timeoutId);
			return res;
		} catch (e) {
			clearTimeout(timeoutId);
			throw e;
		}
	}

	async function renderDiagram() {
		if (!script || script.trim() === '') {
			loading = false;
			return;
		}

		loading = true;

		// Tier 1: Try local backend if configured / reachable
		try {
			if (typeof window !== 'undefined' && (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1' || PUBLIC_API_URL)) {
				const res = await fetchWithTimeout(
					`${localApiUrl}/api/diagrams/render`,
					{
						method: 'POST',
						headers: { 'Content-Type': 'application/json' },
						body: JSON.stringify({ script, preset, animate })
					},
					1500
				);

				if (res.ok) {
					const data = await res.json();
					if (data.svg) {
						svg = data.svg;
						renderSource = 'DiagramKit Core (Rust Axum)';
						loading = false;
						return;
					}
				}
			}
		} catch {
			// Tier 1 skipped or timed out, move to Tier 2
		}

		// Tier 2: Try DiagramKit Cloudflare Pages Edge Service
		try {
			const encoded = b64url(script);
			const edgeUrl = `https://diagramkit.pages.dev/d/${encoded}.svg?preset=${encodeURIComponent(preset)}&animate=${encodeURIComponent(animate)}`;
			const edgeRes = await fetchWithTimeout(edgeUrl, { method: 'GET' }, 2000);

			if (edgeRes.ok) {
				const edgeSvg = await edgeRes.text();
				if (edgeSvg && edgeSvg.includes('<svg')) {
					svg = edgeSvg;
					renderSource = 'DiagramKit Edge Service';
					loading = false;
					return;
				}
			}
		} catch {
			// Tier 2 skipped or offline, proceed to Tier 3
		}

		// Tier 3: Client-side Deterministic SVG Compiler (100% resilient, zero standby error card!)
		try {
			svg = renderDiagramKitSvg(script, preset, animate);
			renderSource = 'DiagramKit Universal Engine';
		} catch (err) {
			console.error('Local DiagramKit render error:', err);
		} finally {
			loading = false;
		}
	}

	$effect(() => {
		if (script) {
			renderDiagram();
		}
	});

	function toggleExpand() {
		isExpanded = !isExpanded;
	}
</script>

<div
	class="relative my-6 overflow-hidden rounded-xl border border-[#e5e2d9] bg-[#f0eee6]/40 dark:border-[#343330] dark:bg-[#181817] {isExpanded
		? 'fixed inset-4 z-50 flex flex-col bg-[#faf9f5] dark:bg-[#181817] shadow-2xl overflow-y-auto'
		: ''} {className}"
>
	<!-- Diagram Header -->
	<div
		class="flex items-center justify-between border-b border-[#e5e2d9] bg-[#f0eee6] px-4 py-2.5 text-xs font-mono text-[#6f6e69] dark:border-[#343330] dark:bg-[#232321] dark:text-[#a19f97]"
	>
		<div class="flex items-center gap-2">
			<Sparkles class="h-3.5 w-3.5 text-[#c96442]" />
			<span class="font-medium text-[#141413] dark:text-[#f5f4ed]">{title}</span>
			<span class="rounded bg-[#c96442]/10 px-1.5 py-0.5 text-[10px] text-[#c96442] dark:bg-[#c96442]/20">
				{renderSource}
			</span>
		</div>

		<div class="flex items-center gap-1.5">
			<button
				type="button"
				onclick={renderDiagram}
				class="rounded p-1 text-[#6f6e69] transition-colors hover:bg-[#e4e1d8] hover:text-[#141413] dark:text-[#a19f97] dark:hover:bg-[#2e2d2a] dark:hover:text-[#f5f4ed]"
				title="Re-render diagram"
				aria-label="Re-render diagram"
			>
				<RefreshCw class="h-3.5 w-3.5 {loading ? 'animate-spin text-[#c96442]' : ''}" />
			</button>
			<button
				type="button"
				onclick={toggleExpand}
				class="rounded p-1 text-[#6f6e69] transition-colors hover:bg-[#e4e1d8] hover:text-[#141413] dark:text-[#a19f97] dark:hover:bg-[#2e2d2a] dark:hover:text-[#f5f4ed]"
				title={isExpanded ? 'Exit full view' : 'Expand full view'}
				aria-label={isExpanded ? 'Exit full view' : 'Expand full view'}
			>
				{#if isExpanded}
					<Minimize2 class="h-3.5 w-3.5" />
				{:else}
					<Maximize2 class="h-3.5 w-3.5" />
				{/if}
			</button>
		</div>
	</div>

	<!-- Diagram Body -->
	<div class="relative flex min-h-[220px] items-center justify-center p-4">
		{#if loading && !svg}
			<div class="flex flex-col items-center gap-3 py-10 text-[#6f6e69] dark:text-[#a19f97]">
				<div class="h-6 w-6 animate-spin rounded-full border-2 border-[#c96442] border-t-transparent"></div>
				<span class="text-xs font-mono">Generating DiagramKit reactive SVG...</span>
			</div>
		{:else if svg}
			<div class="w-full overflow-x-auto flex justify-center [&>svg]:max-w-full [&>svg]:h-auto transition-opacity duration-300">
				{@html svg}
			</div>
		{/if}
	</div>
</div>

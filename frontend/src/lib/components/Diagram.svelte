<script lang="ts">
	import { PUBLIC_API_URL } from '$env/static/public';
	import {
		Maximize2,
		Minimize2,
		RefreshCw,
		Sparkles,
		ZoomIn,
		ZoomOut,
		RotateCcw,
		Move,
		Copy,
		Check,
		X
	} from 'lucide-svelte';
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
	let isModalOpen = $state<boolean>(false);
	let renderSource = $state<string>('DiagramKit Engine');
	let copied = $state<boolean>(false);

	// Interactive Modal State (Pan & Zoom)
	let activePreset = $state<string>('midnight');
	let activeAnimate = $state<string>('flow');

	$effect(() => {
		activePreset = preset;
	});
	$effect(() => {
		activeAnimate = animate;
	});

	let zoom = $state<number>(1.0);
	let panX = $state<number>(0);
	let panY = $state<number>(0);
	let isDragging = $state<boolean>(false);
	let dragStartX = $state<number>(0);
	let dragStartY = $state<number>(0);

	const localApiUrl = PUBLIC_API_URL || 'http://127.0.0.1:8080';

	async function fetchWithTimeout(url: string, options: RequestInit, timeoutMs = 1500): Promise<Response> {
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

		// Tier 1: Try local backend if configured
		try {
			if (
				typeof window !== 'undefined' &&
				(window.location.hostname === 'localhost' ||
					window.location.hostname === '127.0.0.1' ||
					PUBLIC_API_URL)
			) {
				const res = await fetchWithTimeout(
					`${localApiUrl}/api/diagrams/render`,
					{
						method: 'POST',
						headers: { 'Content-Type': 'application/json' },
						body: JSON.stringify({ script, preset: activePreset, animate: activeAnimate })
					},
					1200
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
			// Backend offline, fallback to edge/local
		}

		// Tier 2: Try DiagramKit Edge Service
		try {
			const encoded = b64url(script);
			const edgeUrl = `https://diagramkit.pages.dev/d/${encoded}.svg?preset=${encodeURIComponent(activePreset)}&animate=${encodeURIComponent(activeAnimate)}`;
			const edgeRes = await fetchWithTimeout(edgeUrl, { method: 'GET' }, 1500);

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
			// Edge offline, fallback to universal engine
		}

		// Tier 3: Client-side Deterministic SVG Compiler (100% resilient, 0 latency)
		try {
			svg = renderDiagramKitSvg(script, activePreset, activeAnimate);
			renderSource = 'DiagramKit Universal Engine';
		} catch (err) {
			console.error('DiagramKit render error:', err);
		} finally {
			loading = false;
		}
	}

	$effect(() => {
		if (script || activePreset || activeAnimate) {
			renderDiagram();
		}
	});

	function openModal() {
		isModalOpen = true;
		resetView();
		if (typeof document !== 'undefined') {
			document.body.style.overflow = 'hidden';
		}
	}

	function closeModal() {
		isModalOpen = false;
		if (typeof document !== 'undefined') {
			document.body.style.overflow = '';
		}
	}

	function zoomIn() {
		zoom = Math.min(3.5, +(zoom + 0.2).toFixed(2));
	}

	function zoomOut() {
		zoom = Math.max(0.3, +(zoom - 0.2).toFixed(2));
	}

	function resetView() {
		zoom = 1.0;
		panX = 0;
		panY = 0;
	}

	function handleWheel(e: WheelEvent) {
		if (!isModalOpen) return;
		e.preventDefault();
		const delta = e.deltaY < 0 ? 0.12 : -0.12;
		zoom = Math.min(3.5, Math.max(0.3, +(zoom + delta).toFixed(2)));
	}

	function handlePointerDown(e: PointerEvent) {
		isDragging = true;
		dragStartX = e.clientX - panX;
		dragStartY = e.clientY - panY;
		(e.target as HTMLElement)?.setPointerCapture?.(e.pointerId);
	}

	function handlePointerMove(e: PointerEvent) {
		if (!isDragging) return;
		panX = e.clientX - dragStartX;
		panY = e.clientY - dragStartY;
	}

	function handlePointerUp(e: PointerEvent) {
		isDragging = false;
		try {
			(e.target as HTMLElement)?.releasePointerCapture?.(e.pointerId);
		} catch {
			// ignore
		}
	}

	function handleKeydown(e: KeyboardEvent) {
		if (!isModalOpen) return;
		if (e.key === 'Escape') {
			closeModal();
		} else if (e.key === '+' || e.key === '=') {
			zoomIn();
		} else if (e.key === '-' || e.key === '_') {
			zoomOut();
		} else if (e.key === '0') {
			resetView();
		}
	}

	async function copyScript() {
		if (typeof navigator !== 'undefined' && navigator.clipboard) {
			await navigator.clipboard.writeText(script);
			copied = true;
			setTimeout(() => {
				copied = false;
			}, 2000);
		}
	}
</script>

<svelte:window onkeydown={handleKeydown} />

<!-- In-line Diagram Card -->
<div
	class="relative my-6 overflow-hidden rounded-xl border border-[#e5e2d9] bg-[#f0eee6]/40 dark:border-[#343330] dark:bg-[#181817] {className}"
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
				onclick={copyScript}
				class="rounded p-1 text-[#6f6e69] transition-colors hover:bg-[#e4e1d8] hover:text-[#141413] dark:text-[#a19f97] dark:hover:bg-[#2e2d2a] dark:hover:text-[#f5f4ed]"
				title="Copy DiagramKit Script"
				aria-label="Copy DiagramKit Script"
			>
				{#if copied}
					<Check class="h-3.5 w-3.5 text-emerald-500" />
				{:else}
					<Copy class="h-3.5 w-3.5" />
				{/if}
			</button>
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
				onclick={openModal}
				class="inline-flex items-center gap-1 rounded bg-[#e4e1d8] px-2 py-1 text-[11px] font-sans font-medium text-[#141413] transition-colors hover:bg-[#c96442] hover:text-white dark:bg-[#2e2d2a] dark:text-[#f5f4ed] dark:hover:bg-[#c96442]"
				title="Open Fullscreen Lightbox & Pan Tool"
				aria-label="Open Fullscreen Lightbox & Pan Tool"
			>
				<Maximize2 class="h-3 w-3" />
				<span>Expand</span>
			</button>
		</div>
	</div>

	<!-- Diagram Body Preview -->
	<div class="relative flex min-h-[220px] items-center justify-center p-4">
		{#if loading && !svg}
			<div class="flex flex-col items-center gap-3 py-10 text-[#6f6e69] dark:text-[#a19f97]">
				<div class="h-6 w-6 animate-spin rounded-full border-2 border-[#c96442] border-t-transparent"></div>
				<span class="text-xs font-mono">Generating DiagramKit reactive SVG...</span>
			</div>
		{:else if svg}
			<div
				class="w-full overflow-x-auto flex justify-center [&>svg]:max-w-full [&>svg]:h-auto transition-opacity duration-300"
			>
				{@html svg}
			</div>
		{/if}
	</div>
</div>

<!-- Gorgeous Full-Viewport Lightbox Modal with Pan, Zoom & Hand Grab Tool -->
{#if isModalOpen}
	<div
		class="fixed inset-0 z-50 flex flex-col bg-black/85 backdrop-blur-md select-none animate-in fade-in duration-200"
		role="dialog"
		aria-modal="true"
		aria-label="{title} Fullscreen Viewer"
	>
		<!-- Lightbox Header Bar -->
		<div
			class="flex flex-wrap items-center justify-between gap-3 border-b border-[#343330] bg-[#18181b]/95 px-5 py-3 text-xs font-mono text-[#a19f97] shadow-lg"
		>
			<!-- Title & Engine -->
			<div class="flex items-center gap-3">
				<div class="flex h-7 w-7 items-center justify-center rounded-lg bg-[#c96442]/20 text-[#c96442]">
					<Sparkles class="h-4 w-4" />
				</div>
				<div>
					<h3 class="font-serif text-sm font-semibold text-[#f5f4ed]">{title}</h3>
					<div class="flex items-center gap-2 text-[11px] text-[#a19f97]">
						<span class="text-emerald-400">● Live Canvas</span>
						<span>•</span>
						<span>{renderSource}</span>
					</div>
				</div>
			</div>

			<!-- Center Controls Toolbar (Zoom, Pan Status, Style) -->
			<div class="flex items-center gap-2 rounded-xl border border-[#343330] bg-[#222226] p-1.5 shadow-inner">
				<!-- Hand Grab indicator -->
				<div
					class="hidden sm:flex items-center gap-1.5 rounded-lg bg-[#18181b] px-2.5 py-1 text-[11px] text-[#f5f4ed]"
					title="Click and drag anywhere to pan diagram"
				>
					<Move class="h-3 w-3 text-[#c96442]" />
					<span>Hand Grab</span>
				</div>

				<div class="hidden sm:block h-4 w-px bg-[#3f3f46]"></div>

				<!-- Zoom Controls -->
				<button
					type="button"
					onclick={zoomOut}
					class="rounded-lg p-1.5 text-[#a19f97] transition-colors hover:bg-[#2e2e33] hover:text-[#f5f4ed]"
					title="Zoom out (-)"
					aria-label="Zoom out"
				>
					<ZoomOut class="h-3.5 w-3.5" />
				</button>
				<span class="min-w-[44px] text-center font-mono text-[11px] font-semibold text-[#f5f4ed]">
					{Math.round(zoom * 100)}%
				</span>
				<button
					type="button"
					onclick={zoomIn}
					class="rounded-lg p-1.5 text-[#a19f97] transition-colors hover:bg-[#2e2e33] hover:text-[#f5f4ed]"
					title="Zoom in (+)"
					aria-label="Zoom in"
				>
					<ZoomIn class="h-3.5 w-3.5" />
				</button>

				<button
					type="button"
					onclick={resetView}
					class="rounded-lg p-1.5 text-[#a19f97] transition-colors hover:bg-[#2e2e33] hover:text-[#f5f4ed]"
					title="Reset view (100% / Key 0)"
					aria-label="Reset view"
				>
					<RotateCcw class="h-3.5 w-3.5" />
				</button>

				<div class="h-4 w-px bg-[#3f3f46]"></div>

				<!-- Animation Selector -->
				<select
					bind:value={activeAnimate}
					class="rounded-lg border border-[#343330] bg-[#18181b] px-2 py-1 text-[11px] text-[#f5f4ed] focus:outline-none focus:ring-1 focus:ring-[#c96442]"
					aria-label="Select diagram animation"
				>
					<option value="flow">Animate: Flow</option>
					<option value="pulse">Animate: Pulse</option>
					<option value="glow">Animate: Glow</option>
					<option value="none">Animate: Static</option>
				</select>
			</div>

			<!-- Right Actions: Copy DSL & Close -->
			<div class="flex items-center gap-2">
				<button
					type="button"
					onclick={copyScript}
					class="inline-flex items-center gap-1.5 rounded-lg border border-[#343330] bg-[#222226] px-3 py-1.5 text-xs text-[#f5f4ed] transition-colors hover:border-[#c96442]/60 hover:text-[#c96442]"
					title="Copy DiagramKit DSL"
				>
					{#if copied}
						<Check class="h-3.5 w-3.5 text-emerald-400" />
						<span>Copied!</span>
					{:else}
						<Copy class="h-3.5 w-3.5" />
						<span class="hidden sm:inline">Copy DSL</span>
					{/if}
				</button>

				<button
					type="button"
					onclick={closeModal}
					class="flex h-8 w-8 items-center justify-center rounded-lg border border-[#343330] bg-[#222226] text-[#a19f97] transition-colors hover:bg-rose-950/40 hover:text-rose-400"
					title="Close Lightbox (Esc)"
					aria-label="Close Lightbox"
				>
					<X class="h-4 w-4" />
				</button>
			</div>
		</div>

		<!-- Interactive Viewport Canvas (Draggable / Hand Grab) -->
		<!-- svelte-ignore a11y_no_noninteractive_element_interactions -->
		<div
			class="relative flex-1 overflow-hidden {isDragging ? 'cursor-grabbing' : 'cursor-grab'}"
			onwheel={handleWheel}
			onpointerdown={handlePointerDown}
			onpointermove={handlePointerMove}
			onpointerup={handlePointerUp}
			onpointercancel={handlePointerUp}
			role="region"
			aria-label="Interactive Diagram Canvas"
		>
			<div
				class="absolute inset-0 flex items-center justify-center pointer-events-none"
				style="transform: translate({panX}px, {panY}px) scale({zoom}); transform-origin: center center; transition: {isDragging
					? 'none'
					: 'transform 0.12s ease-out'};"
			>
				<div class="pointer-events-auto shadow-2xl rounded-2xl [&>svg]:max-w-none">
					{@html svg}
				</div>
			</div>

			<!-- Floating Instructions Pill -->
			<div
				class="absolute bottom-6 left-1/2 -translate-x-1/2 pointer-events-none rounded-full border border-[#343330] bg-[#18181b]/80 px-4 py-1.5 text-[11px] font-mono text-[#a19f97] backdrop-blur-sm shadow-md"
			>
				<span>🖐️ Drag canvas to pan</span>
				<span class="mx-2">•</span>
				<span>🔍 Scroll wheel to zoom</span>
				<span class="mx-2">•</span>
				<span>⌨️ Esc to close</span>
			</div>
		</div>
	</div>
{/if}

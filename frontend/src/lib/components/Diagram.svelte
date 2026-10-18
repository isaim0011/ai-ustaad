<script lang="ts">
	import { PUBLIC_API_URL } from '$env/static/public';
	import { mode } from 'mode-watcher';
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
		X,
		Download,
		FileCode,
		Image as ImageIcon,
		Scan,
		Palette,
		Play
	} from 'lucide-svelte';
	import {
		b64url,
		renderDiagramKitSvg,
		resolvePresetName,
		PRESET_OPTIONS
	} from '$lib/utils/diagramkit';

	interface Props {
		script: string;
		preset?: string;
		animate?: string;
		title?: string;
		class?: string;
	}

	let {
		script = '',
		preset = undefined,
		animate = 'flow',
		title = 'Architecture Diagram',
		class: className = ''
	}: Props = $props();

	let svg = $state<string>('');
	let loading = $state<boolean>(true);
	let isModalOpen = $state<boolean>(false);
	let renderSource = $state<string>('DiagramKit Engine');
	let copied = $state<boolean>(false);
	let isExportingPng = $state<boolean>(false);

	// Theme tracking for auto preset
	let isDarkTheme = $derived(
		$mode === 'dark' ||
			(typeof document !== 'undefined' && document.documentElement.classList.contains('dark'))
	);

	// Controls state (preset & animation)
	let activePreset = $state<string>('auto');
	let activeAnimate = $state<string>('flow');

	// Synchronize when parent updates props
	$effect(() => {
		if (preset !== undefined) {
			activePreset = preset;
		}
	});
	$effect(() => {
		if (animate !== undefined) {
			activeAnimate = animate;
		}
	});

	// Inline Zoom & Pan state
	let inlineContainerRef: HTMLElement | null = $state(null);
	let inlineZoom = $state<number>(1.0);
	let inlinePanX = $state<number>(0);
	let inlinePanY = $state<number>(0);
	let isInlineDragging = $state<boolean>(false);
	let inlineDragStartX = $state<number>(0);
	let inlineDragStartY = $state<number>(0);

	// Fullscreen Modal Zoom & Pan state
	let modalRef: HTMLElement | null = $state(null);
	let modalZoom = $state<number>(1.0);
	let modalPanX = $state<number>(0);
	let modalPanY = $state<number>(0);
	let isModalDragging = $state<boolean>(false);
	let modalDragStartX = $state<number>(0);
	let modalDragStartY = $state<number>(0);

	// Touch pinch state
	let initialTouchDistance = 0;
	let initialTouchZoom = 1.0;
	let isTouchPinching = false;

	// Focus trap tracker
	let lastFocusedElement: HTMLElement | null = null;

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

		// Resolve effective preset for network requests
		const effectivePreset = resolvePresetName(activePreset, isDarkTheme);

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
						body: JSON.stringify({ script, preset: effectivePreset, animate: activeAnimate })
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
			const edgeUrl = `https://diagramkit.pages.dev/d/${encoded}.svg?preset=${encodeURIComponent(effectivePreset)}&animate=${encodeURIComponent(activeAnimate)}`;
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

		// Tier 3: Client-side Deterministic SVG Compiler (100% resilient, 0 latency, theme-aware)
		try {
			svg = renderDiagramKitSvg(script, activePreset, activeAnimate, isDarkTheme);
			renderSource = 'DiagramKit Universal Engine';
		} catch (err) {
			console.error('DiagramKit render error:', err);
		} finally {
			loading = false;
		}
	}

	// Re-render when script, active preset, animation, or theme changes
	$effect(() => {
		const _s = script;
		const _p = activePreset;
		const _a = activeAnimate;
		const _dark = isDarkTheme;
		if (_s) {
			renderDiagram();
		}
	});

	// Inline zoom & pan handlers
	function inlineZoomIn() {
		inlineZoom = Math.min(3.0, +(inlineZoom + 0.15).toFixed(2));
	}

	function inlineZoomOut() {
		inlineZoom = Math.max(0.4, +(inlineZoom - 0.15).toFixed(2));
	}

	function inlineResetView() {
		inlineZoom = 1.0;
		inlinePanX = 0;
		inlinePanY = 0;
	}

	function inlineFitToScreen() {
		if (!svg || !inlineContainerRef) {
			inlineResetView();
			return;
		}
		const match = svg.match(/viewBox=["']0\s+0\s+(\d+(?:\.\d+)?)\s+(\d+(?:\.\d+)?)["']/);
		const svgW = match ? parseFloat(match[1]) : 740;
		const svgH = match ? parseFloat(match[2]) : 300;
		const availableW = Math.max(inlineContainerRef.clientWidth - 40, 280);
		const availableH = Math.max(inlineContainerRef.clientHeight - 40, 200);
		const scaleW = availableW / svgW;
		const scaleH = availableH / svgH;
		const fitScale = Math.min(scaleW, scaleH, 1.0);
		inlineZoom = Math.max(0.4, +fitScale.toFixed(2));
		inlinePanX = 0;
		inlinePanY = 0;
	}

	function handleInlineWheel(e: WheelEvent) {
		if (inlineZoom === 1.0 && inlinePanX === 0 && inlinePanY === 0 && Math.abs(e.deltaY) < 5) {
			return;
		}
		// Allow wheel zoom if user holds Ctrl/Cmd or if already zoomed
		if (e.ctrlKey || e.metaKey || inlineZoom !== 1.0) {
			e.preventDefault();
			const delta = e.deltaY < 0 ? 0.12 : -0.12;
			inlineZoom = Math.min(3.0, Math.max(0.4, +(inlineZoom + delta).toFixed(2)));
		}
	}

	function handleInlinePointerDown(e: PointerEvent) {
		if (inlineZoom <= 1.0 && inlinePanX === 0 && inlinePanY === 0) return;
		isInlineDragging = true;
		inlineDragStartX = e.clientX - inlinePanX;
		inlineDragStartY = e.clientY - inlinePanY;
		(e.target as HTMLElement)?.setPointerCapture?.(e.pointerId);
	}

	function handleInlinePointerMove(e: PointerEvent) {
		if (!isInlineDragging) return;
		inlinePanX = e.clientX - inlineDragStartX;
		inlinePanY = e.clientY - inlineDragStartY;
	}

	function handleInlinePointerUp(e: PointerEvent) {
		isInlineDragging = false;
		try {
			(e.target as HTMLElement)?.releasePointerCapture?.(e.pointerId);
		} catch {
			// ignore
		}
	}

	// Modal handlers (Pan, Zoom, Lightbox)
	function openModal() {
		lastFocusedElement = (typeof document !== 'undefined' ? document.activeElement : null) as HTMLElement | null;
		isModalOpen = true;
		modalResetView();
		if (typeof document !== 'undefined') {
			document.body.style.overflow = 'hidden';
		}
		setTimeout(() => {
			if (modalRef) {
				const focusable = modalRef.querySelector<HTMLElement>(
					'button:not([disabled]), select:not([disabled])'
				);
				focusable?.focus();
			}
		}, 50);
	}

	function closeModal() {
		isModalOpen = false;
		if (typeof document !== 'undefined') {
			document.body.style.overflow = '';
		}
		lastFocusedElement?.focus?.();
	}

	function modalZoomIn() {
		modalZoom = Math.min(4.0, +(modalZoom + 0.2).toFixed(2));
	}

	function modalZoomOut() {
		modalZoom = Math.max(0.2, +(modalZoom - 0.2).toFixed(2));
	}

	function modalResetView() {
		modalZoom = 1.0;
		modalPanX = 0;
		modalPanY = 0;
	}

	function modalFitToScreen() {
		if (!svg) {
			modalResetView();
			return;
		}
		const match = svg.match(/viewBox=["']0\s+0\s+(\d+(?:\.\d+)?)\s+(\d+(?:\.\d+)?)["']/);
		const svgW = match ? parseFloat(match[1]) : 740;
		const svgH = match ? parseFloat(match[2]) : 300;

		if (typeof window !== 'undefined') {
			const availableW = window.innerWidth - 80;
			const availableH = window.innerHeight - 170;
			const scaleW = availableW / svgW;
			const scaleH = availableH / svgH;
			const fitScale = Math.min(scaleW, scaleH, 1.8);
			modalZoom = Math.max(0.2, +fitScale.toFixed(2));
			modalPanX = 0;
			modalPanY = 0;
		}
	}

	function handleModalWheel(e: WheelEvent) {
		if (!isModalOpen) return;
		e.preventDefault();
		const delta = e.deltaY < 0 ? 0.15 : -0.15;
		modalZoom = Math.min(4.0, Math.max(0.2, +(modalZoom + delta).toFixed(2)));
	}

	function handleModalPointerDown(e: PointerEvent) {
		isModalDragging = true;
		modalDragStartX = e.clientX - modalPanX;
		modalDragStartY = e.clientY - modalPanY;
		(e.target as HTMLElement)?.setPointerCapture?.(e.pointerId);
	}

	function handleModalPointerMove(e: PointerEvent) {
		if (!isModalDragging) return;
		modalPanX = e.clientX - modalDragStartX;
		modalPanY = e.clientY - modalDragStartY;
	}

	function handleModalPointerUp(e: PointerEvent) {
		isModalDragging = false;
		try {
			(e.target as HTMLElement)?.releasePointerCapture?.(e.pointerId);
		} catch {
			// ignore
		}
	}

	// Touch pinch-to-zoom handlers
	function handleTouchStart(e: TouchEvent) {
		if (e.touches.length === 2) {
			isTouchPinching = true;
			const t1 = e.touches[0];
			const t2 = e.touches[1];
			initialTouchDistance = Math.hypot(t1.clientX - t2.clientX, t1.clientY - t2.clientY);
			initialTouchZoom = isModalOpen ? modalZoom : inlineZoom;
		} else if (e.touches.length === 1 && isModalOpen) {
			isTouchPinching = false;
			const t = e.touches[0];
			isModalDragging = true;
			modalDragStartX = t.clientX - modalPanX;
			modalDragStartY = t.clientY - modalPanY;
		}
	}

	function handleTouchMove(e: TouchEvent) {
		if (isTouchPinching && e.touches.length === 2) {
			e.preventDefault();
			const t1 = e.touches[0];
			const t2 = e.touches[1];
			const dist = Math.hypot(t1.clientX - t2.clientX, t1.clientY - t2.clientY);
			if (initialTouchDistance > 0) {
				const factor = dist / initialTouchDistance;
				const newZoom = Math.min(4.0, Math.max(0.2, +(initialTouchZoom * factor).toFixed(2)));
				if (isModalOpen) {
					modalZoom = newZoom;
				} else {
					inlineZoom = newZoom;
				}
			}
		} else if (!isTouchPinching && e.touches.length === 1 && isModalDragging && isModalOpen) {
			const t = e.touches[0];
			modalPanX = t.clientX - modalDragStartX;
			modalPanY = t.clientY - modalDragStartY;
		}
	}

	function handleTouchEnd(e: TouchEvent) {
		if (e.touches.length < 2) {
			isTouchPinching = false;
		}
		if (e.touches.length === 0) {
			isModalDragging = false;
			isInlineDragging = false;
		}
	}

	// Keyboard controls with focus trap
	function handleKeydown(e: KeyboardEvent) {
		if (!isModalOpen) return;
		if (e.key === 'Escape') {
			e.preventDefault();
			closeModal();
		} else if (e.key === '+' || e.key === '=') {
			e.preventDefault();
			modalZoomIn();
		} else if (e.key === '-' || e.key === '_') {
			e.preventDefault();
			modalZoomOut();
		} else if (e.key === '0') {
			e.preventDefault();
			modalResetView();
		} else if (e.key === 'Tab') {
			trapFocus(e);
		}
	}

	function trapFocus(e: KeyboardEvent) {
		if (!modalRef) return;
		const focusables = Array.from(
			modalRef.querySelectorAll<HTMLElement>(
				'button:not([disabled]), [href], input:not([disabled]), select:not([disabled]), textarea:not([disabled]), [tabindex]:not([tabindex="-1"])'
			)
		);
		if (focusables.length === 0) return;
		const first = focusables[0];
		const last = focusables[focusables.length - 1];

		if (e.shiftKey) {
			if (document.activeElement === first) {
				e.preventDefault();
				last.focus();
			}
		} else {
			if (document.activeElement === last) {
				e.preventDefault();
				first.focus();
			}
		}
	}

	// Copy DSL script
	async function copyScript() {
		if (typeof navigator !== 'undefined' && navigator.clipboard) {
			try {
				await navigator.clipboard.writeText(script);
				copied = true;
				setTimeout(() => {
					copied = false;
				}, 2000);
			} catch (err) {
				console.error('Failed to copy script:', err);
			}
		}
	}

	// Export SVG (serialize, Blob download)
	function exportSvg() {
		if (!svg || typeof document === 'undefined') return;
		const blob = new Blob([svg], { type: 'image/svg+xml;charset=utf-8' });
		const url = URL.createObjectURL(blob);
		const a = document.createElement('a');
		const safeName = (title || 'diagram')
			.toLowerCase()
			.replace(/[^a-z0-9_-]/g, '-')
			.replace(/-+/g, '-');
		a.href = url;
		a.download = `${safeName}.svg`;
		document.body.appendChild(a);
		a.click();
		document.body.removeChild(a);
		URL.revokeObjectURL(url);
	}

	// Export PNG (draw to HTML5 Canvas at high DPI 2x/3x)
	async function exportPng(scale = 2) {
		if (!svg || typeof document === 'undefined' || isExportingPng) return;
		isExportingPng = true;
		try {
			const match = svg.match(/viewBox=["']0\s+0\s+(\d+(?:\.\d+)?)\s+(\d+(?:\.\d+)?)["']/);
			const width = match ? parseFloat(match[1]) : 740;
			const height = match ? parseFloat(match[2]) : 300;

			const canvas = document.createElement('canvas');
			canvas.width = Math.round(width * scale);
			canvas.height = Math.round(height * scale);
			const ctx = canvas.getContext('2d');
			if (!ctx) return;

			ctx.imageSmoothingEnabled = true;
			ctx.imageSmoothingQuality = 'high';

			const svgBlob = new Blob([svg], { type: 'image/svg+xml;charset=utf-8' });
			const url = URL.createObjectURL(svgBlob);
			const img = new Image();

			await new Promise<void>((resolve, reject) => {
				img.onload = () => {
					ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
					URL.revokeObjectURL(url);
					resolve();
				};
				img.onerror = (err) => {
					URL.revokeObjectURL(url);
					reject(err);
				};
				img.src = url;
			});

			canvas.toBlob((blob) => {
				if (!blob) return;
				const pngUrl = URL.createObjectURL(blob);
				const a = document.createElement('a');
				const safeName = (title || 'diagram')
					.toLowerCase()
					.replace(/[^a-z0-9_-]/g, '-')
					.replace(/-+/g, '-');
				a.href = pngUrl;
				a.download = `${safeName}@${scale}x.png`;
				document.body.appendChild(a);
				a.click();
				document.body.removeChild(a);
				URL.revokeObjectURL(pngUrl);
			}, 'image/png');
		} catch (err) {
			console.error('Failed to export PNG:', err);
		} finally {
			isExportingPng = false;
		}
	}
</script>

<svelte:window onkeydown={handleKeydown} />

<!-- In-line Diagram Card with Toolbar -->
<div
	class="relative my-6 overflow-hidden rounded-xl border border-[#e5e2d9] bg-[#faf9f5] dark:border-[#343330] dark:bg-[#141413] shadow-xs {className}"
>
	<!-- Diagram Header & Responsive Toolbar -->
	<div
		class="flex flex-wrap items-center justify-between gap-2.5 border-b border-[#e5e2d9] bg-[#f0eee6] px-3.5 py-2 text-xs font-mono text-[#6f6e69] dark:border-[#343330] dark:bg-[#1c1c1b] dark:text-[#a19f97]"
	>
		<!-- Left: Title & Engine Source Pill -->
		<div class="flex items-center gap-2 min-w-0">
			<Sparkles class="h-3.5 w-3.5 shrink-0 text-[#c96442]" />
			<span class="truncate font-sans font-semibold text-[#141413] dark:text-[#f5f4ed]">{title}</span>
			<span
				class="hidden sm:inline-block rounded bg-[#c96442]/10 px-1.5 py-0.5 text-[10px] font-mono text-[#c96442] dark:bg-[#c96442]/20"
			>
				{renderSource}
			</span>
		</div>

		<!-- Right: Controls & Actions (Presets, Animations, Zoom, Export, Copy, Lightbox) -->
		<div class="flex flex-wrap items-center gap-1.5">
			<!-- Preset Dropdown -->
			<div class="flex items-center gap-1 rounded-md border border-[#d8d5cb] bg-[#faf9f5] px-1.5 py-0.5 dark:border-[#343330] dark:bg-[#262624]">
				<Palette class="h-3 w-3 text-[#c96442]" />
				<select
					bind:value={activePreset}
					class="bg-transparent text-[11px] font-sans font-medium text-[#141413] dark:text-[#f5f4ed] focus:outline-none"
					aria-label="Preset theme selector"
				>
					{#each PRESET_OPTIONS as opt}
						<option value={opt.id} class="bg-[#faf9f5] text-[#141413] dark:bg-[#262624] dark:text-[#f5f4ed]">
							{opt.label}
						</option>
					{/each}
				</select>
			</div>

			<!-- Animation Selector -->
			<div class="hidden md:flex items-center gap-1 rounded-md border border-[#d8d5cb] bg-[#faf9f5] px-1.5 py-0.5 dark:border-[#343330] dark:bg-[#262624]">
				<Play class="h-3 w-3 text-[#c96442]" />
				<select
					bind:value={activeAnimate}
					class="bg-transparent text-[11px] font-sans font-medium text-[#141413] dark:text-[#f5f4ed] focus:outline-none"
					aria-label="Animation style selector"
				>
					<option value="flow" class="bg-[#faf9f5] text-[#141413] dark:bg-[#262624] dark:text-[#f5f4ed]">Animate: Flow</option>
					<option value="pulse" class="bg-[#faf9f5] text-[#141413] dark:bg-[#262624] dark:text-[#f5f4ed]">Animate: Pulse</option>
					<option value="glow" class="bg-[#faf9f5] text-[#141413] dark:bg-[#262624] dark:text-[#f5f4ed]">Animate: Glow</option>
					<option value="none" class="bg-[#faf9f5] text-[#141413] dark:bg-[#262624] dark:text-[#f5f4ed]">Animate: Static</option>
				</select>
			</div>

			<!-- Inline Zoom Controls -->
			<div class="flex items-center rounded-md border border-[#d8d5cb] bg-[#faf9f5] p-0.5 dark:border-[#343330] dark:bg-[#262624]">
				<button
					type="button"
					onclick={inlineZoomOut}
					class="rounded p-1 text-[#6f6e69] transition-colors hover:bg-[#e4e1d8] hover:text-[#141413] dark:text-[#a19f97] dark:hover:bg-[#343330] dark:hover:text-[#f5f4ed]"
					title="Zoom out"
					aria-label="Zoom out"
				>
					<ZoomOut class="h-3 w-3" />
				</button>
				<span class="min-w-[36px] text-center font-mono text-[10px] font-semibold text-[#141413] dark:text-[#f5f4ed]">
					{Math.round(inlineZoom * 100)}%
				</span>
				<button
					type="button"
					onclick={inlineZoomIn}
					class="rounded p-1 text-[#6f6e69] transition-colors hover:bg-[#e4e1d8] hover:text-[#141413] dark:text-[#a19f97] dark:hover:bg-[#343330] dark:hover:text-[#f5f4ed]"
					title="Zoom in"
					aria-label="Zoom in"
				>
					<ZoomIn class="h-3 w-3" />
				</button>
				<button
					type="button"
					onclick={inlineResetView}
					class="rounded p-1 text-[#6f6e69] transition-colors hover:bg-[#e4e1d8] hover:text-[#141413] dark:text-[#a19f97] dark:hover:bg-[#343330] dark:hover:text-[#f5f4ed]"
					title="Reset zoom (100%)"
					aria-label="Reset zoom"
				>
					<RotateCcw class="h-3 w-3" />
				</button>
				<button
					type="button"
					onclick={inlineFitToScreen}
					class="rounded p-1 text-[#6f6e69] transition-colors hover:bg-[#e4e1d8] hover:text-[#141413] dark:text-[#a19f97] dark:hover:bg-[#343330] dark:hover:text-[#f5f4ed]"
					title="Fit to card"
					aria-label="Fit to card"
				>
					<Scan class="h-3 w-3" />
				</button>
			</div>

			<!-- Export SVG -->
			<button
				type="button"
				onclick={exportSvg}
				class="inline-flex items-center gap-1 rounded-md border border-[#d8d5cb] bg-[#faf9f5] px-2 py-1 text-[11px] font-sans font-medium text-[#141413] transition-colors hover:border-[#c96442]/60 hover:text-[#c96442] dark:border-[#343330] dark:bg-[#262624] dark:text-[#f5f4ed] dark:hover:border-[#c96442]/60 dark:hover:text-[#c96442]"
				title="Export SVG"
				aria-label="Export SVG"
			>
				<FileCode class="h-3 w-3" />
				<span class="hidden sm:inline">SVG</span>
			</button>

			<!-- Export PNG (2x) -->
			<button
				type="button"
				onclick={() => exportPng(2)}
				disabled={isExportingPng}
				class="inline-flex items-center gap-1 rounded-md border border-[#d8d5cb] bg-[#faf9f5] px-2 py-1 text-[11px] font-sans font-medium text-[#141413] transition-colors hover:border-[#c96442]/60 hover:text-[#c96442] dark:border-[#343330] dark:bg-[#262624] dark:text-[#f5f4ed] dark:hover:border-[#c96442]/60 dark:hover:text-[#c96442] disabled:opacity-50"
				title="Export PNG (2x Retina)"
				aria-label="Export PNG (2x Retina)"
			>
				<ImageIcon class="h-3 w-3 {isExportingPng ? 'animate-spin' : ''}" />
				<span class="hidden sm:inline">PNG</span>
			</button>

			<!-- Copy DSL -->
			<button
				type="button"
				onclick={copyScript}
				class="rounded-md border border-[#d8d5cb] bg-[#faf9f5] p-1 text-[#6f6e69] transition-colors hover:bg-[#e4e1d8] hover:text-[#141413] dark:border-[#343330] dark:bg-[#262624] dark:text-[#a19f97] dark:hover:bg-[#343330] dark:hover:text-[#f5f4ed]"
				title="Copy DiagramKit Script"
				aria-label="Copy DiagramKit Script"
			>
				{#if copied}
					<Check class="h-3.5 w-3.5 text-emerald-500" />
				{:else}
					<Copy class="h-3.5 w-3.5" />
				{/if}
			</button>

			<!-- Refresh / Re-render -->
			<button
				type="button"
				onclick={renderDiagram}
				class="rounded-md border border-[#d8d5cb] bg-[#faf9f5] p-1 text-[#6f6e69] transition-colors hover:bg-[#e4e1d8] hover:text-[#141413] dark:border-[#343330] dark:bg-[#262624] dark:text-[#a19f97] dark:hover:bg-[#343330] dark:hover:text-[#f5f4ed]"
				title="Re-render diagram"
				aria-label="Re-render diagram"
			>
				<RefreshCw class="h-3.5 w-3.5 {loading ? 'animate-spin text-[#c96442]' : ''}" />
			</button>

			<!-- Fullscreen Lightbox Button -->
			<button
				type="button"
				onclick={openModal}
				class="inline-flex items-center gap-1 rounded-md bg-[#e4e1d8] px-2 py-1 text-[11px] font-sans font-medium text-[#141413] transition-colors hover:bg-[#c96442] hover:text-white dark:bg-[#2e2d2a] dark:text-[#f5f4ed] dark:hover:bg-[#c96442]"
				title="Open Fullscreen Lightbox"
				aria-label="Open Fullscreen Lightbox"
			>
				<Maximize2 class="h-3 w-3" />
				<span>Expand</span>
			</button>
		</div>
	</div>

	<!-- Diagram Body Preview (Interactive Inline Zoom & Pan Canvas) -->
	<!-- svelte-ignore a11y_no_noninteractive_element_interactions -->
	<div
		bind:this={inlineContainerRef}
		class="relative flex min-h-[220px] items-center justify-center p-3 sm:p-5 overflow-hidden {inlineZoom !== 1.0 || inlinePanX !== 0 || inlinePanY !== 0 ? (isInlineDragging ? 'cursor-grabbing' : 'cursor-grab') : ''}"
		onwheel={handleInlineWheel}
		onpointerdown={handleInlinePointerDown}
		onpointermove={handleInlinePointerMove}
		onpointerup={handleInlinePointerUp}
		onpointercancel={handleInlinePointerUp}
		ontouchstart={handleTouchStart}
		ontouchmove={handleTouchMove}
		ontouchend={handleTouchEnd}
		ontouchcancel={handleTouchEnd}
		role="region"
		aria-label="Diagram Preview"
	>
		{#if loading && !svg}
			<div class="flex flex-col items-center gap-3 py-10 text-[#6f6e69] dark:text-[#a19f97]">
				<div class="h-6 w-6 animate-spin rounded-full border-2 border-[#c96442] border-t-transparent"></div>
				<span class="text-xs font-mono">Generating DiagramKit reactive SVG...</span>
			</div>
		{:else if svg}
			<div
				class="w-full flex justify-center [&>svg]:max-w-full [&>svg]:h-auto transition-transform duration-100 ease-out"
				style="transform: translate({inlinePanX}px, {inlinePanY}px) scale({inlineZoom}); transform-origin: center center;"
			>
				{@html svg}
			</div>
		{/if}
	</div>
</div>

<!-- Full-Viewport Lightbox Modal with Pan, Zoom & Hand Grab Tool -->
{#if isModalOpen}
	<div
		bind:this={modalRef}
		class="fixed inset-0 z-50 flex flex-col bg-black/85 backdrop-blur-md select-none animate-in fade-in duration-200"
		role="dialog"
		aria-modal="true"
		aria-label="{title} Fullscreen Viewer"
	>
		<!-- Lightbox Header Bar -->
		<div
			class="flex flex-wrap items-center justify-between gap-3 border-b border-[#343330] bg-[#18181b]/95 px-5 py-3 text-xs font-mono text-[#a19f97] shadow-lg"
		>
			<!-- Title & Engine Source -->
			<div class="flex items-center gap-3">
				<div class="flex h-7 w-7 items-center justify-center rounded-lg bg-[#c96442]/20 text-[#c96442]">
					<Sparkles class="h-4 w-4" />
				</div>
				<div>
					<h3 class="font-serif text-sm font-semibold text-[#f5f4ed]">{title}</h3>
					<div class="flex items-center gap-2 text-[11px] text-[#a19f97]">
						<span class="inline-flex items-center gap-1.5 text-emerald-400">
							<span class="h-1.5 w-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
							<span>Live Canvas</span>
						</span>
						<span>•</span>
						<span>{renderSource}</span>
					</div>
				</div>
			</div>

			<!-- Center Controls Toolbar (Preset, Animation, Hand Grab, Zoom, Fit) -->
			<div class="flex flex-wrap items-center gap-2 rounded-xl border border-[#343330] bg-[#222226] p-1.5 shadow-inner">
				<!-- Preset Selector in Lightbox -->
				<div class="flex items-center gap-1 rounded-lg bg-[#18181b] px-2 py-1">
					<Palette class="h-3 w-3 text-[#c96442]" />
					<select
						bind:value={activePreset}
						class="bg-transparent text-[11px] font-sans font-medium text-[#f5f4ed] focus:outline-none"
						aria-label="Select diagram preset in lightbox"
					>
						{#each PRESET_OPTIONS as opt}
							<option value={opt.id} class="bg-[#18181b] text-[#f5f4ed]">
								{opt.label}
							</option>
						{/each}
					</select>
				</div>

				<!-- Animation Selector in Lightbox -->
				<div class="flex items-center gap-1 rounded-lg bg-[#18181b] px-2 py-1">
					<Play class="h-3 w-3 text-[#c96442]" />
					<select
						bind:value={activeAnimate}
						class="bg-transparent text-[11px] font-sans font-medium text-[#f5f4ed] focus:outline-none"
						aria-label="Select animation style in lightbox"
					>
						<option value="flow" class="bg-[#18181b] text-[#f5f4ed]">Animate: Flow</option>
						<option value="pulse" class="bg-[#18181b] text-[#f5f4ed]">Animate: Pulse</option>
						<option value="glow" class="bg-[#18181b] text-[#f5f4ed]">Animate: Glow</option>
						<option value="none" class="bg-[#18181b] text-[#f5f4ed]">Animate: Static</option>
					</select>
				</div>

				<div class="hidden sm:block h-4 w-px bg-[#3f3f46]"></div>

				<!-- Hand Grab indicator -->
				<div
					class="hidden md:flex items-center gap-1.5 rounded-lg bg-[#18181b] px-2 py-1 text-[11px] text-[#f5f4ed]"
					title="Click and drag anywhere to pan diagram"
				>
					<Move class="h-3 w-3 text-[#c96442]" />
					<span>Hand Grab</span>
				</div>

				<div class="hidden md:block h-4 w-px bg-[#3f3f46]"></div>

				<!-- Zoom Out Button -->
				<button
					type="button"
					onclick={modalZoomOut}
					class="rounded-lg p-1.5 text-[#a19f97] transition-colors hover:bg-[#2e2e33] hover:text-[#f5f4ed]"
					title="Zoom out (-)"
					aria-label="Zoom out"
				>
					<ZoomOut class="h-3.5 w-3.5" />
				</button>

				<!-- Zoom Percentage Display -->
				<span class="min-w-[44px] text-center font-mono text-[11px] font-semibold text-[#f5f4ed]">
					{Math.round(modalZoom * 100)}%
				</span>

				<!-- Zoom In Button -->
				<button
					type="button"
					onclick={modalZoomIn}
					class="rounded-lg p-1.5 text-[#a19f97] transition-colors hover:bg-[#2e2e33] hover:text-[#f5f4ed]"
					title="Zoom in (+)"
					aria-label="Zoom in"
				>
					<ZoomIn class="h-3.5 w-3.5" />
				</button>

				<!-- Reset Zoom Button -->
				<button
					type="button"
					onclick={modalResetView}
					class="rounded-lg p-1.5 text-[#a19f97] transition-colors hover:bg-[#2e2e33] hover:text-[#f5f4ed]"
					title="Reset view (100% / Key 0)"
					aria-label="Reset view"
				>
					<RotateCcw class="h-3.5 w-3.5" />
				</button>

				<!-- Fit to Screen Button -->
				<button
					type="button"
					onclick={modalFitToScreen}
					class="rounded-lg p-1.5 text-[#a19f97] transition-colors hover:bg-[#2e2e33] hover:text-[#f5f4ed]"
					title="Fit diagram to viewport"
					aria-label="Fit diagram to viewport"
				>
					<Scan class="h-3.5 w-3.5" />
				</button>
			</div>

			<!-- Right Actions: Export SVG, Export PNG, Copy DSL & Close -->
			<div class="flex items-center gap-2">
				<button
					type="button"
					onclick={exportSvg}
					class="inline-flex items-center gap-1.5 rounded-lg border border-[#343330] bg-[#222226] px-2.5 py-1.5 text-xs text-[#f5f4ed] transition-colors hover:border-[#c96442]/60 hover:text-[#c96442]"
					title="Export SVG file"
					aria-label="Export SVG"
				>
					<FileCode class="h-3.5 w-3.5" />
					<span class="hidden sm:inline">SVG</span>
				</button>

				<button
					type="button"
					onclick={() => exportPng(2)}
					disabled={isExportingPng}
					class="inline-flex items-center gap-1.5 rounded-lg border border-[#343330] bg-[#222226] px-2.5 py-1.5 text-xs text-[#f5f4ed] transition-colors hover:border-[#c96442]/60 hover:text-[#c96442] disabled:opacity-50"
					title="Export PNG 2x Retina"
					aria-label="Export PNG 2x Retina"
				>
					<ImageIcon class="h-3.5 w-3.5 {isExportingPng ? 'animate-spin' : ''}" />
					<span class="hidden sm:inline">PNG</span>
				</button>

				<button
					type="button"
					onclick={copyScript}
					class="inline-flex items-center gap-1.5 rounded-lg border border-[#343330] bg-[#222226] px-3 py-1.5 text-xs text-[#f5f4ed] transition-colors hover:border-[#c96442]/60 hover:text-[#c96442]"
					title="Copy DiagramKit DSL"
					aria-label="Copy DiagramKit DSL"
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

		<!-- Interactive Viewport Canvas (Draggable / Hand Grab & Touch Pinch) -->
		<!-- svelte-ignore a11y_no_noninteractive_element_interactions -->
		<div
			class="relative flex-1 overflow-hidden {isModalDragging ? 'cursor-grabbing' : 'cursor-grab'}"
			onwheel={handleModalWheel}
			onpointerdown={handleModalPointerDown}
			onpointermove={handleModalPointerMove}
			onpointerup={handleModalPointerUp}
			onpointercancel={handleModalPointerUp}
			ontouchstart={handleTouchStart}
			ontouchmove={handleTouchMove}
			ontouchend={handleTouchEnd}
			ontouchcancel={handleTouchEnd}
			role="region"
			aria-label="Interactive Diagram Canvas"
		>
			<div
				class="absolute inset-0 flex items-center justify-center pointer-events-none"
				style="transform: translate({modalPanX}px, {modalPanY}px) scale({modalZoom}); transform-origin: center center; transition: {isModalDragging
					? 'none'
					: 'transform 0.12s ease-out'};"
			>
				<div class="pointer-events-auto shadow-2xl rounded-2xl [&>svg]:max-w-none">
					{@html svg}
				</div>
			</div>

			<!-- Floating Instructions Pill -->
			<div
				class="absolute bottom-6 left-1/2 -translate-x-1/2 pointer-events-none flex flex-wrap items-center justify-center gap-3 rounded-full border border-[#343330] bg-[#18181b]/90 px-4 py-1.5 text-[11px] font-mono text-[#a19f97] backdrop-blur-sm shadow-md"
			>
				<span class="inline-flex items-center gap-1.5">
					<Move class="h-3 w-3 text-[#c96442]" />
					<span>Drag to pan</span>
				</span>
				<span class="text-[#454440]">•</span>
				<span class="inline-flex items-center gap-1.5">
					<ZoomIn class="h-3 w-3 text-[#c96442]" />
					<span>Scroll / Pinch to zoom</span>
				</span>
				<span class="text-[#454440]">•</span>
				<span class="inline-flex items-center gap-1.5">
					<kbd class="rounded bg-[#2a2927] px-1 py-0.5 text-[9px] text-[#f5f4ed]">0</kbd>
					<span>reset</span>
				</span>
				<span class="text-[#454440]">•</span>
				<span class="inline-flex items-center gap-1.5">
					<kbd class="rounded bg-[#2a2927] px-1 py-0.5 text-[9px] text-[#f5f4ed]">Esc</kbd>
					<span>close</span>
				</span>
			</div>
		</div>
	</div>
{/if}

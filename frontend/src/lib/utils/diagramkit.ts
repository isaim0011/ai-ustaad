// Self-contained DiagramKit SVG compiler and edge renderer
// Generates fully animated, responsive SVG diagrams with zero backend dependency.

export function b64url(str: string): string {
	const bytes = new TextEncoder().encode(str);
	let binary = '';
	for (let i = 0; i < bytes.byteLength; i++) {
		binary += String.fromCharCode(bytes[i]);
	}
	return btoa(binary)
		.replace(/\+/g, '-')
		.replace(/\//g, '_')
		.replace(/=+$/, '');
}

interface ParsedNode {
	id: string;
	label: string;
	subLabel?: string;
	shape: 'rect' | 'circle' | 'diamond' | 'cylinder';
	color: string;
	icon?: string;
	isFinal: boolean;
	layer: number;
	x: number;
	y: number;
	width: number;
	height: number;
}

interface ParsedEdge {
	from: string;
	to: string;
	label?: string;
}

const COLOR_MAP: Record<string, { bg: string; border: string; glow: string; text: string }> = {
	primary: { bg: '#2b1c18', border: '#c96442', glow: 'rgba(201, 100, 66, 0.4)', text: '#fca082' },
	purple: { bg: '#231834', border: '#8b5cf6', glow: 'rgba(139, 92, 246, 0.4)', text: '#c4b5fd' },
	teal: { bg: '#13282b', border: '#14b8a6', glow: 'rgba(20, 184, 166, 0.4)', text: '#5eead4' },
	info: { bg: '#132438', border: '#3b82f6', glow: 'rgba(59, 130, 246, 0.4)', text: '#93c5fd' },
	ok: { bg: '#14291e', border: '#10b981', glow: 'rgba(16, 185, 129, 0.4)', text: '#6ee7b7' },
	warn: { bg: '#302414', border: '#f59e0b', glow: 'rgba(245, 158, 11, 0.4)', text: '#fde68a' },
	danger: { bg: '#33161a', border: '#ef4444', glow: 'rgba(239, 68, 68, 0.4)', text: '#fca5a5' },
	default: { bg: '#1d1d20', border: '#3f3f46', glow: 'rgba(113, 113, 122, 0.25)', text: '#e4e4e7' }
};

const ICONS: Record<string, string> = {
	terminal: `<polyline points="4 17 10 11 4 5"></polyline><line x1="12" y1="19" x2="20" y2="19"></line>`,
	brain: `<path d="M12 4.5a2.5 2.5 0 0 0-4.96-.46 2.5 2.5 0 0 0-1.98 3 2.5 2.5 0 0 0-1.32 4.24 3 3 0 0 0 .34 4.18 2.5 2.5 0 0 0 3.92 2.54M12 4.5a2.5 2.5 0 0 1 4.96-.46 2.5 2.5 0 0 1 1.98 3 2.5 2.5 0 0 1 1.32 4.24 3 3 0 0 1-.34 4.18 2.5 2.5 0 0 1-3.92 2.54"></path>`,
	database: `<ellipse cx="12" cy="5" rx="9" ry="3"></ellipse><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"></path><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"></path>`,
	cpu: `<rect x="4" y="4" width="16" height="16" rx="2"></rect><rect x="9" y="9" width="6" height="6"></rect><line x1="9" y1="1" x2="9" y2="4"></line><line x1="15" y1="1" x2="15" y2="4"></line><line x1="9" y1="20" x2="9" y2="23"></line><line x1="15" y1="20" x2="15" y2="23"></line><line x1="20" y1="9" x2="23" y2="9"></line><line x1="20" y1="14" x2="23" y2="14"></line><line x1="1" y1="9" x2="4" y2="9"></line><line x1="1" y1="14" x2="4" y2="14"></line>`,
	server: `<rect x="2" y="2" width="20" height="8" rx="2" ry="2"></rect><rect x="2" y="14" width="20" height="8" rx="2" ry="2"></rect><line x1="6" y1="6" x2="6.01" y2="6"></line><line x1="6" y1="18" x2="6.01" y2="18"></line>`,
	filter: `<polygon points="22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3"></polygon>`,
	layers: `<polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline>`
};

export function renderDiagramKitSvg(
	script: string,
	userPreset: string = 'midnight',
	userAnimate: string = 'flow'
): string {
	const lines = script
		.split('\n')
		.map((l) => l.trim())
		.filter((l) => l && !l.startsWith('//'));

	let preset = userPreset || 'midnight';
	let animate = userAnimate || 'flow';
	let title = 'Architecture Workflow';
	let subtitle = 'DiagramKit Reactive Topology';
	let direction: 'LR' | 'TD' = 'LR';

	const nodesMap = new Map<string, ParsedNode>();
	const edges: ParsedEdge[] = [];

	// Parse header directives & title
	for (const line of lines) {
		if (line.startsWith('@preset')) {
			const p = line.replace('@preset', '').trim();
			if (p) preset = p;
		} else if (line.startsWith('@animate')) {
			const a = line.replace('@animate', '').trim();
			if (a) animate = a;
		} else if (line.match(/^(arch|flow|graph|sequence)\b/i)) {
			const match = line.match(/^(?:arch|flow|graph|sequence)\s+(LR|TD)?(?::\s*([^|\n]+))?(?:\|\s*(.*))?/i);
			if (match) {
				if (match[1]) direction = match[1].toUpperCase() as 'LR' | 'TD';
				if (match[2]) title = match[2].trim();
				if (match[3]) subtitle = match[3].trim();
			}
		}
	}

	function parseNodeToken(token: string): string {
		let clean = token.trim();
		let isFinal = false;
		if (clean.endsWith('*')) {
			isFinal = true;
			clean = clean.slice(0, -1).trim();
		}

		let color = 'default';
		const colorMatch = clean.match(/~(\w+)/);
		if (colorMatch) {
			color = colorMatch[1];
			clean = clean.replace(/~(\w+)/, '').trim();
		}

		let icon: string | undefined = undefined;
		const iconMatch = clean.match(/\$(\w+)/);
		if (iconMatch) {
			icon = iconMatch[1];
			clean = clean.replace(/\$(\w+)/, '').trim();
		}

		let id = '';
		let label = '';
		let subLabel: string | undefined = undefined;
		let shape: 'rect' | 'circle' | 'diamond' | 'cylinder' = 'rect';

		const circleMatch = clean.match(/^([a-zA-Z0-9_\-]+)\(\((.+?)\)\)$/);
		const rectMatch = clean.match(/^([a-zA-Z0-9_\-]+)\[(.+?)\]$/);
		const dbMatch = clean.match(/^([a-zA-Z0-9_\-]+)\[\((.+?)\)\]$/);
		const plainMatch = clean.match(/^([a-zA-Z0-9_\-]+)$/);

		if (dbMatch) {
			id = dbMatch[1];
			label = dbMatch[2];
			shape = 'cylinder';
		} else if (circleMatch) {
			id = circleMatch[1];
			label = circleMatch[2];
			shape = 'circle';
		} else if (rectMatch) {
			id = rectMatch[1];
			label = rectMatch[2];
			shape = 'rect';
		} else if (plainMatch) {
			id = plainMatch[1];
			label = id;
		} else {
			id = clean.replace(/[^a-zA-Z0-9_\-]/g, '_');
			label = clean;
		}

		if (label.includes('//')) {
			const parts = label.split('//');
			label = parts[0].trim();
			subLabel = parts[1].trim();
		}

		if (!nodesMap.has(id)) {
			nodesMap.set(id, {
				id,
				label,
				subLabel,
				shape,
				color: COLOR_MAP[color] ? color : 'default',
				icon,
				isFinal,
				layer: 0,
				x: 0,
				y: 0,
				width: Math.max(160, Math.min(220, label.length * 8 + (icon ? 30 : 0) + 24)),
				height: subLabel ? 64 : 50
			});
		} else {
			const existing = nodesMap.get(id)!;
			if (label !== id && (!existing.label || existing.label === id)) {
				existing.label = label;
			}
			if (subLabel) existing.subLabel = subLabel;
			if (color !== 'default') existing.color = color;
			if (icon) existing.icon = icon;
			if (isFinal) existing.isFinal = true;
		}

		return id;
	}

	// Parse edges and inline nodes
	for (const line of lines) {
		if (line.startsWith('@') || line.match(/^(arch|flow|graph|sequence)\b/i)) {
			continue;
		}

		if (line.includes('->')) {
			const parts = line.split('->').map((p) => p.trim());
			for (let i = 0; i < parts.length - 1; i++) {
				const fromId = parseNodeToken(parts[i]);
				const toId = parseNodeToken(parts[i + 1]);
				if (fromId && toId) {
					edges.push({ from: fromId, to: toId });
				}
			}
		} else if (line.match(/[\[\(]/)) {
			parseNodeToken(line);
		}
	}

	// Layer computation using topological hierarchy
	const inDegree = new Map<string, number>();
	for (const [id] of nodesMap) {
		inDegree.set(id, 0);
	}
	for (const edge of edges) {
		inDegree.set(edge.to, (inDegree.get(edge.to) || 0) + 1);
	}

	// Assign layers
	const queue: string[] = [];
	for (const [id, deg] of inDegree) {
		if (deg === 0) {
			queue.push(id);
			nodesMap.get(id)!.layer = 0;
		}
	}

	while (queue.length > 0) {
		const curr = queue.shift()!;
		const currLayer = nodesMap.get(curr)!.layer;
		const nextEdges = edges.filter((e) => e.from === curr);

		for (const edge of nextEdges) {
			const target = nodesMap.get(edge.to);
			if (target) {
				target.layer = Math.max(target.layer, currLayer + 1);
				queue.push(edge.to);
			}
		}
	}

	// Group nodes by layer
	const layerGroups = new Map<number, ParsedNode[]>();
	for (const [, node] of nodesMap) {
		const l = node.layer;
		if (!layerGroups.has(l)) layerGroups.set(l, []);
		layerGroups.get(l)!.push(node);
	}

	const sortedLayers = Array.from(layerGroups.keys()).sort((a, b) => a - b);
	const maxNodesInLayer = Math.max(...Array.from(layerGroups.values()).map((g) => g.length), 1);

	// Coordinate calculations
	const paddingX = 40;
	const paddingY = 80; // space for header
	const colGap = 90;
	const rowGap = 35;
	const defaultNodeHeight = 54;
	const defaultNodeWidth = 180;

	let totalWidth = paddingX * 2;
	let totalHeight = paddingY + 50;

	if (direction === 'LR') {
		totalWidth = paddingX * 2 + sortedLayers.length * (defaultNodeWidth + colGap) - colGap;
		totalHeight = paddingY + maxNodesInLayer * (defaultNodeHeight + rowGap) + 40;

		sortedLayers.forEach((lIndex, col) => {
			const group = layerGroups.get(lIndex)!;
			const totalGroupHeight = group.length * defaultNodeHeight + (group.length - 1) * rowGap;
			const startY = paddingY + (totalHeight - paddingY - totalGroupHeight) / 2;

			group.forEach((node, row) => {
				node.x = paddingX + col * (defaultNodeWidth + colGap);
				node.y = startY + row * (defaultNodeHeight + rowGap);
				node.width = defaultNodeWidth;
				node.height = node.subLabel ? 64 : defaultNodeHeight;
			});
		});
	} else {
		// TD
		totalWidth = paddingX * 2 + maxNodesInLayer * (defaultNodeWidth + colGap);
		totalHeight = paddingY + sortedLayers.length * (defaultNodeHeight + rowGap) + 40;

		sortedLayers.forEach((lIndex, row) => {
			const group = layerGroups.get(lIndex)!;
			const totalGroupWidth = group.length * defaultNodeWidth + (group.length - 1) * colGap;
			const startX = paddingX + (totalWidth - paddingX - totalGroupWidth) / 2;

			group.forEach((node, col) => {
				node.x = startX + col * (defaultNodeWidth + colGap);
				node.y = paddingY + row * (defaultNodeHeight + rowGap);
				node.width = defaultNodeWidth;
				node.height = node.subLabel ? 64 : defaultNodeHeight;
			});
		});
	}

	totalWidth = Math.max(totalWidth, 680);
	totalHeight = Math.max(totalHeight, 260);

	// Animation CSS
	const animKeyframes = `
		@keyframes dkit-flow {
			0% { stroke-dashoffset: 48; }
			100% { stroke-dashoffset: 0; }
		}
		@keyframes dkit-pulse {
			0%, 100% { transform: scale(1); opacity: 1; }
			50% { transform: scale(1.02); opacity: 0.95; }
		}
		@keyframes dkit-wave {
			0% { filter: drop-shadow(0 0 2px rgba(201,100,66,0.3)); }
			50% { filter: drop-shadow(0 0 10px rgba(201,100,66,0.8)); }
			100% { filter: drop-shadow(0 0 2px rgba(201,100,66,0.3)); }
		}
		@keyframes dkit-glow {
			0%, 100% { stroke-opacity: 0.4; }
			50% { stroke-opacity: 1; }
		}
		.dkit-anim-flow {
			stroke-dasharray: 6 6;
			animation: dkit-flow 1.5s linear infinite;
		}
		.dkit-anim-pulse {
			animation: dkit-pulse 2.8s ease-in-out infinite;
			transform-origin: center;
		}
		.dkit-anim-wave {
			animation: dkit-wave 2.2s ease-in-out infinite;
		}
		.dkit-anim-glow {
			animation: dkit-glow 2s ease-in-out infinite;
		}
	`;

	// SVG generation
	let svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${totalWidth} ${totalHeight}" width="100%" height="100%" class="diagramkit-svg" style="background:#131315; border-radius:12px; font-family:'JetBrains Mono', monospace, sans-serif;">
		<defs>
			<style>${animKeyframes}</style>
			<marker id="dkit-arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
				<path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#c96442" />
			</marker>
			<marker id="dkit-arrow-muted" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
				<path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#71717a" />
			</marker>
			<filter id="dkit-blur" x="-20%" y="-20%" width="140%" height="140%">
				<feGaussianBlur stdDeviation="3" result="blur" />
				<feComposite in="SourceGraphic" in2="blur" operator="over" />
			</filter>
		</defs>

		<!-- Subtle Grid Background -->
		<pattern id="dkit-grid" width="24" height="24" patternUnits="userSpaceOnUse">
			<path d="M 24 0 L 0 0 0 24" fill="none" stroke="#1f1f23" stroke-width="0.8" />
		</pattern>
		<rect width="100%" height="100%" fill="url(#dkit-grid)" rx="12" />

		<!-- Header Banner -->
		<g transform="translate(24, 28)">
			<rect x="0" y="0" width="8" height="8" rx="2" fill="#c96442" />
			<text x="16" y="8" fill="#f5f4ed" font-size="13" font-weight="600" letter-spacing="-0.01em">${title}</text>
			<text x="16" y="24" fill="#a19f97" font-size="10">${subtitle}</text>
			<rect x="${totalWidth - 140}" y="-6" width="90" height="20" rx="10" fill="#221b18" stroke="#c96442" stroke-width="0.8" />
			<text x="${totalWidth - 95}" y="8" fill="#c96442" font-size="9" text-anchor="middle" font-weight="500">DiagramKit Edge</text>
		</g>

		<!-- Connection Edges -->
		<g class="dkit-edges">
	`;

	for (const edge of edges) {
		const fromNode = nodesMap.get(edge.from);
		const toNode = nodesMap.get(edge.to);
		if (!fromNode || !toNode) continue;

		let startX = fromNode.x + fromNode.width;
		let startY = fromNode.y + fromNode.height / 2;
		let endX = toNode.x;
		let endY = toNode.y + toNode.height / 2;

		if (direction === 'TD') {
			startX = fromNode.x + fromNode.width / 2;
			startY = fromNode.y + fromNode.height;
			endX = toNode.x + toNode.width / 2;
			endY = toNode.y;
		}

		const midX = (startX + endX) / 2;
		const midY = (startY + endY) / 2;

		const pathD =
			direction === 'LR'
				? `M ${startX} ${startY} C ${midX} ${startY}, ${midX} ${endY}, ${endX - 6} ${endY}`
				: `M ${startX} ${startY} C ${startX} ${midY}, ${endX} ${midY}, ${endX} ${endY - 6}`;

		svg += `
			<!-- Edge ${edge.from} -> ${edge.to} -->
			<path d="${pathD}" fill="none" stroke="#27272a" stroke-width="2.5" />
			<path d="${pathD}" fill="none" stroke="#c96442" stroke-width="1.8" class="${animate === 'flow' ? 'dkit-anim-flow' : animate === 'glow' ? 'dkit-anim-glow' : ''}" marker-end="url(#dkit-arrow)" />
		`;
	}

	svg += `</g>\n<!-- Nodes -->\n<g class="dkit-nodes">`;

	for (const [, node] of nodesMap) {
		const colors = COLOR_MAP[node.color] || COLOR_MAP.default;
		const iconSvg = node.icon && ICONS[node.icon] ? ICONS[node.icon] : '';

		svg += `
			<!-- Node: ${node.id} -->
			<g transform="translate(${node.x}, ${node.y})" class="${node.isFinal ? 'dkit-anim-wave' : animate === 'pulse' ? 'dkit-anim-pulse' : ''}">
				<!-- Card Body -->
				<rect
					x="0"
					y="0"
					width="${node.width}"
					height="${node.height}"
					rx="10"
					fill="${colors.bg}"
					stroke="${colors.border}"
					stroke-width="${node.isFinal ? '2' : '1.2'}"
					style="filter: drop-shadow(0 4px 12px ${colors.glow});"
				/>

				${
					iconSvg
						? `
					<!-- Icon Badge -->
					<g transform="translate(10, ${(node.height - 18) / 2})">
						<rect x="0" y="0" width="22" height="22" rx="5" fill="#18181b" stroke="${colors.border}" stroke-width="0.8" />
						<g transform="translate(3, 3) scale(0.65)" stroke="${colors.text}" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
							${iconSvg}
						</g>
					</g>
					<text x="40" y="${node.subLabel ? 24 : node.height / 2 + 4}" fill="${colors.text}" font-size="11" font-weight="600" letter-spacing="-0.01em">${node.label}</text>
				`
						: `
					<text x="14" y="${node.subLabel ? 24 : node.height / 2 + 4}" fill="${colors.text}" font-size="11" font-weight="600" letter-spacing="-0.01em">${node.label}</text>
				`
				}

				${
					node.subLabel
						? `
					<text x="${iconSvg ? 40 : 14}" y="44" fill="#a19f97" font-size="9" font-family="'JetBrains Mono', monospace">${node.subLabel}</text>
				`
						: ''
				}

				${
					node.isFinal
						? `
					<!-- Final Target Star Badge -->
					<circle cx="${node.width - 10}" cy="10" r="4" fill="#10b981" />
				`
						: ''
				}
			</g>
		`;
	}

	svg += `</g>\n</svg>`;
	return svg;
}

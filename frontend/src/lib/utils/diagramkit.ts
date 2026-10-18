// Self-contained DiagramKit SVG compiler and edge renderer
// Generates fully animated, responsive SVG diagrams with zero backend dependency.
// Supports modern DiagramKit DSL: directives, shapes, edge labels, icons, presets, animations, and clean DAG topology.

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

export interface ParsedNode {
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

export interface ParsedEdge {
	from: string;
	to: string;
	label?: string;
}

export const COLOR_MAP: Record<string, { bg: string; border: string; glow: string; text: string }> = {
	primary: { bg: '#2b1c18', border: '#c96442', glow: 'rgba(201, 100, 66, 0.4)', text: '#fca082' },
	purple: { bg: '#231834', border: '#8b5cf6', glow: 'rgba(139, 92, 246, 0.4)', text: '#c4b5fd' },
	teal: { bg: '#13282b', border: '#14b8a6', glow: 'rgba(20, 184, 166, 0.4)', text: '#5eead4' },
	info: { bg: '#132438', border: '#3b82f6', glow: 'rgba(59, 130, 246, 0.4)', text: '#93c5fd' },
	ok: { bg: '#14291e', border: '#10b981', glow: 'rgba(16, 185, 129, 0.4)', text: '#6ee7b7' },
	emerald: { bg: '#14291e', border: '#10b981', glow: 'rgba(16, 185, 129, 0.4)', text: '#6ee7b7' },
	warn: { bg: '#302414', border: '#f59e0b', glow: 'rgba(245, 158, 11, 0.4)', text: '#fde68a' },
	amber: { bg: '#302414', border: '#f59e0b', glow: 'rgba(245, 158, 11, 0.4)', text: '#fde68a' },
	danger: { bg: '#33161a', border: '#ef4444', glow: 'rgba(239, 68, 68, 0.4)', text: '#fca5a5' },
	default: { bg: '#1d1d20', border: '#3f3f46', glow: 'rgba(113, 113, 122, 0.25)', text: '#e4e4e7' }
};

export const ICONS: Record<string, string> = {
	code: `<polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline>`,
	terminal: `<polyline points="4 17 10 11 4 5"></polyline><line x1="12" y1="19" x2="20" y2="19"></line>`,
	brain: `<path d="M12 4.5a2.5 2.5 0 0 0-4.96-.46 2.5 2.5 0 0 0-1.98 3 2.5 2.5 0 0 0-1.32 4.24 3 3 0 0 0 .34 4.18 2.5 2.5 0 0 0 3.92 2.54M12 4.5a2.5 2.5 0 0 1 4.96-.46 2.5 2.5 0 0 1 1.98 3 2.5 2.5 0 0 1 1.32 4.24 3 3 0 0 1-.34 4.18 2.5 2.5 0 0 1-3.92 2.54"></path>`,
	database: `<ellipse cx="12" cy="5" rx="9" ry="3"></ellipse><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"></path><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"></path>`,
	cpu: `<rect x="4" y="4" width="16" height="16" rx="2"></rect><rect x="9" y="9" width="6" height="6"></rect><line x1="9" y1="1" x2="9" y2="4"></line><line x1="15" y1="1" x2="15" y2="4"></line><line x1="9" y1="20" x2="9" y2="23"></line><line x1="15" y1="20" x2="15" y2="23"></line><line x1="20" y1="9" x2="23" y2="9"></line><line x1="20" y1="14" x2="23" y2="14"></line><line x1="1" y1="9" x2="4" y2="9"></line><line x1="1" y1="14" x2="4" y2="14"></line>`,
	server: `<rect x="2" y="2" width="20" height="8" rx="2" ry="2"></rect><rect x="2" y="14" width="20" height="8" rx="2" ry="2"></rect><line x1="6" y1="6" x2="6.01" y2="6"></line><line x1="6" y1="18" x2="6.01" y2="18"></line>`,
	filter: `<polygon points="22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3"></polygon>`,
	layers: `<polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline>`,
	bolt: `<polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon>`,
	sparkles: `<path d="m12 3-1.9 5.8a2 2 0 0 1-1.3 1.3L3 12l5.8 1.9a2 2 0 0 1 1.3 1.3L12 21l1.9-5.8a2 2 0 0 1 1.3-1.3L21 12l-5.8-1.9a2 2 0 0 1-1.3-1.3L12 3z"></path>`,
	lock: `<rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path>`,
	rocket: `<path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z"></path><path d="m12 15-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z"></path><path d="M9 12H4s.55-3.03 2-4c1.62-1.08 5 0 5 0"></path><path d="M12 15v5s3.03-.55 4-2c1.08-1.62 0-5 0-5"></path>`,
	globe: `<circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>`,
	zap: `<polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon>`
};

export function renderDiagramKitSvg(
	script: string,
	userPreset: string = 'midnight',
	userAnimate: string = 'flow'
): string {
	const rawLines = script
		.split('\n')
		.map((l) => l.trim())
		.filter((l) => l && !l.startsWith('//') && !l.startsWith('#'));

	let preset = userPreset || 'midnight';
	let animate = userAnimate || 'flow';
	let title = 'Architecture Workflow';
	let subtitle = 'DiagramKit Reactive Topology';
	let direction: 'LR' | 'TD' = 'LR';

	const nodesMap = new Map<string, ParsedNode>();
	const edges: ParsedEdge[] = [];

	// Parse directives & header title
	for (const line of rawLines) {
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

	// Helper to parse individual node token safely without duplicate phantom nodes
	function parseNodeToken(token: string): string {
		let clean = token.trim();
		if (!clean) return '';

		let isFinal = false;
		if (clean.endsWith('*')) {
			isFinal = true;
			clean = clean.slice(0, -1).trim();
		}

		let color = 'default';
		const colorMatch = clean.match(/~(\w+)/);
		if (colorMatch) {
			color = colorMatch[1].toLowerCase();
			clean = clean.replace(/~(\w+)/, '').trim();
		}

		let icon: string | undefined = undefined;
		const iconMatch = clean.match(/\$(\w+)/);
		if (iconMatch) {
			icon = iconMatch[1].toLowerCase();
			clean = clean.replace(/\$(\w+)/, '').trim();
		}

		let id = '';
		let label = '';
		let subLabel: string | undefined = undefined;
		let shape: 'rect' | 'circle' | 'diamond' | 'cylinder' = 'rect';

		// Shape matchers
		const dbMatch = clean.match(/^([a-zA-Z0-9_\-]+)\s*\[\(\s*(.+?)\s*\)\]$/);
		const circleMatch = clean.match(/^([a-zA-Z0-9_\-]+)\s*\(\(\s*(.+?)\s*\)\)$/);
		const diamondMatch = clean.match(/^([a-zA-Z0-9_\-]+)\s*\{\s*(.+?)\s*\}$/);
		const rectMatch = clean.match(/^([a-zA-Z0-9_\-]+)\s*\[\s*(.+?)\s*\]$/);
		const plainMatch = clean.match(/^([a-zA-Z0-9_\-]+)$/);

		if (dbMatch) {
			id = dbMatch[1].trim();
			label = dbMatch[2].trim();
			shape = 'cylinder';
		} else if (circleMatch) {
			id = circleMatch[1].trim();
			label = circleMatch[2].trim();
			shape = 'circle';
		} else if (diamondMatch) {
			id = diamondMatch[1].trim();
			label = diamondMatch[2].trim();
			shape = 'diamond';
		} else if (rectMatch) {
			id = rectMatch[1].trim();
			label = rectMatch[2].trim();
			shape = 'rect';
		} else if (plainMatch) {
			id = plainMatch[1].trim();
			label = id;
		} else {
			// Fallback: extract identifier before any punctuation
			const idMatch = clean.match(/^([a-zA-Z0-9_\-]+)/);
			id = idMatch ? idMatch[1] : clean.replace(/[^a-zA-Z0-9_\-]/g, '_');
			label = clean;
		}

		// Handle sublabel: "Main Label // Sub Label"
		if (label.includes('//')) {
			const parts = label.split('//');
			label = parts[0].trim();
			subLabel = parts[1].trim();
		}

		// Calculate appropriate width and height based on text & shape
		const calculatedWidth = Math.max(
			shape === 'diamond' ? 190 : 170,
			Math.min(260, Math.max(label.length, (subLabel || '').length) * 8.2 + (icon ? 36 : 0) + 32)
		);
		const calculatedHeight = subLabel ? 62 : shape === 'diamond' ? 56 : 50;

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
				width: calculatedWidth,
				height: calculatedHeight
			});
		} else {
			// Update existing node properties if richer information is provided
			const existing = nodesMap.get(id)!;
			if (label !== id && (!existing.label || existing.label === id)) {
				existing.label = label;
				existing.width = Math.max(existing.width, calculatedWidth);
			}
			if (subLabel && !existing.subLabel) {
				existing.subLabel = subLabel;
				existing.height = calculatedHeight;
			}
			if (shape !== 'rect' && existing.shape === 'rect') {
				existing.shape = shape;
			}
			if (color !== 'default') {
				existing.color = color;
			}
			if (icon && !existing.icon) {
				existing.icon = icon;
			}
			if (isFinal) {
				existing.isFinal = true;
			}
		}

		return id;
	}

	// Edge line parser with edge label support:
	// Supports: A -> B, A --> B, A ->|Label| B, A -->|Label| B, A -> B: Label
	for (const line of rawLines) {
		if (line.startsWith('@') || line.match(/^(arch|flow|graph|sequence)\b/i)) {
			continue;
		}

		// Check for arrow edges
		if (line.includes('->')) {
			// Normalize multi-dash arrows "-->" to "->"
			const normalizedLine = line.replace(/-->/g, '->');
			const rawParts = normalizedLine.split('->').map((p) => p.trim());

			for (let i = 0; i < rawParts.length - 1; i++) {
				const fromSegment = rawParts[i];
				let toSegment = rawParts[i + 1];
				let edgeLabel: string | undefined = undefined;

				// Check for edge label in format: |Label| Target
				const labelMatch = toSegment.match(/^\|\s*([^|]+)\s*\|\s*(.*)$/);
				if (labelMatch) {
					edgeLabel = labelMatch[1].trim();
					toSegment = labelMatch[2].trim();
				}

				const fromId = parseNodeToken(fromSegment);
				const toId = parseNodeToken(toSegment);

				if (fromId && toId) {
					edges.push({ from: fromId, to: toId, label: edgeLabel });
				}
			}
		} else if (line.match(/[\[\(\{]/)) {
			// Standalone node declaration
			parseNodeToken(line);
		}
	}

	// Topological ranking (Longest path to preserve DAG structure and eliminate backward crossings)
	const inDegree = new Map<string, number>();
	for (const [id] of nodesMap) {
		inDegree.set(id, 0);
	}
	for (const edge of edges) {
		inDegree.set(edge.to, (inDegree.get(edge.to) || 0) + 1);
	}

	const queue: string[] = [];
	for (const [id, deg] of inDegree) {
		if (deg === 0) {
			queue.push(id);
			nodesMap.get(id)!.layer = 0;
		}
	}

	// Safe traversal with cycle breaker limit
	let steps = 0;
	const maxSteps = nodesMap.size * 5;
	while (queue.length > 0 && steps < maxSteps) {
		steps++;
		const curr = queue.shift()!;
		const currLayer = nodesMap.get(curr)!.layer;
		const outEdges = edges.filter((e) => e.from === curr);

		for (const edge of outEdges) {
			const target = nodesMap.get(edge.to);
			if (target) {
				const nextLayer = currLayer + 1;
				if (nextLayer > target.layer) {
					target.layer = nextLayer;
					queue.push(edge.to);
				}
			}
		}
	}

	// Group nodes by assigned layer
	const layerGroups = new Map<number, ParsedNode[]>();
	for (const [, node] of nodesMap) {
		const l = node.layer;
		if (!layerGroups.has(l)) layerGroups.set(l, []);
		layerGroups.get(l)!.push(node);
	}

	const sortedLayers = Array.from(layerGroups.keys()).sort((a, b) => a - b);
	const maxNodesInLayer = Math.max(...Array.from(layerGroups.values()).map((g) => g.length), 1);

	// Coordinate calculations & Spacing
	const paddingX = 48;
	const paddingY = 84;
	const colGap = 100;
	const rowGap = 36;
	const defaultNodeHeight = 52;

	let totalWidth = paddingX * 2;
	let totalHeight = paddingY + 60;

	if (direction === 'LR') {
		// Calculate dynamic column widths based on maximum node width in each layer
		const layerWidths = sortedLayers.map((lIndex) => {
			const group = layerGroups.get(lIndex)!;
			return Math.max(...group.map((n) => n.width), 170);
		});

		let currentX = paddingX;
		const layerXCoords: number[] = [];
		layerWidths.forEach((w) => {
			layerXCoords.push(currentX);
			currentX += w + colGap;
		});

		totalWidth = currentX - colGap + paddingX;
		totalHeight = paddingY + maxNodesInLayer * (defaultNodeHeight + rowGap) + 40;

		sortedLayers.forEach((lIndex, colIdx) => {
			const group = layerGroups.get(lIndex)!;
			const colX = layerXCoords[colIdx];
			const totalGroupHeight = group.reduce((acc, n) => acc + n.height, 0) + (group.length - 1) * rowGap;
			const startY = paddingY + Math.max(0, (totalHeight - paddingY - totalGroupHeight) / 2);

			let curY = startY;
			group.forEach((node) => {
				node.x = colX;
				node.y = curY;
				curY += node.height + rowGap;
			});
		});
	} else {
		// Top to Bottom (TD)
		const layerHeights = sortedLayers.map((lIndex) => {
			const group = layerGroups.get(lIndex)!;
			return Math.max(...group.map((n) => n.height), defaultNodeHeight);
		});

		let currentY = paddingY;
		const layerYCoords: number[] = [];
		layerHeights.forEach((h) => {
			layerYCoords.push(currentY);
			currentY += h + colGap;
		});

		totalHeight = currentY - colGap + 60;
		totalWidth = paddingX * 2 + maxNodesInLayer * (210 + colGap);

		sortedLayers.forEach((lIndex, rowIdx) => {
			const group = layerGroups.get(lIndex)!;
			const rowY = layerYCoords[rowIdx];
			const totalGroupWidth = group.reduce((acc, n) => acc + n.width, 0) + (group.length - 1) * rowGap;
			const startX = paddingX + Math.max(0, (totalWidth - paddingX - totalGroupWidth) / 2);

			let curX = startX;
			group.forEach((node) => {
				node.x = curX;
				node.y = rowY;
				curX += node.width + rowGap;
			});
		});
	}

	totalWidth = Math.max(totalWidth, 720);
	totalHeight = Math.max(totalHeight, 280);

	// CSS Animation styles
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
			0%, 100% { stroke-opacity: 0.45; }
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
	let svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${totalWidth} ${totalHeight}" width="100%" height="100%" class="diagramkit-svg" style="background:#131315; border-radius:12px; font-family:'JetBrains Mono', monospace, -apple-system, BlinkMacSystemFont, sans-serif;">
		<defs>
			<style>${animKeyframes}</style>
			<marker id="dkit-arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
				<path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#c96442" />
			</marker>
			<marker id="dkit-arrow-muted" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
				<path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#71717a" />
			</marker>
		</defs>

		<!-- Subtle Blueprint Grid -->
		<pattern id="dkit-grid-${totalWidth}" width="24" height="24" patternUnits="userSpaceOnUse">
			<path d="M 24 0 L 0 0 0 24" fill="none" stroke="#222226" stroke-width="0.8" />
		</pattern>
		<rect width="100%" height="100%" fill="url(#dkit-grid-${totalWidth})" rx="12" />

		<!-- Header Banner -->
		<g transform="translate(24, 28)">
			<rect x="0" y="0" width="8" height="8" rx="2" fill="#c96442" />
			<text x="16" y="8" fill="#f5f4ed" font-size="13" font-weight="600" letter-spacing="-0.01em">${title}</text>
			<text x="16" y="24" fill="#a19f97" font-size="10">${subtitle}</text>
			<g transform="translate(${totalWidth - 146}, -6)">
				<rect width="98" height="22" rx="11" fill="#201a18" stroke="#c96442" stroke-opacity="0.6" stroke-width="0.8" />
				<text x="49" y="14" fill="#c96442" font-size="9" text-anchor="middle" font-weight="600">DiagramKit Core</text>
			</g>
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
			<path d="${pathD}" fill="none" stroke="#2a2a2e" stroke-width="2.6" />
			<path d="${pathD}" fill="none" stroke="#c96442" stroke-width="1.8" class="${animate === 'flow' ? 'dkit-anim-flow' : animate === 'glow' ? 'dkit-anim-glow' : ''}" marker-end="url(#dkit-arrow)" />
		`;

		// Render edge label if present
		if (edge.label) {
			const labelWidth = Math.max(50, edge.label.length * 6.5 + 16);
			svg += `
				<g transform="translate(${midX}, ${midY})">
					<rect x="${-labelWidth / 2}" y="-10" width="${labelWidth}" height="20" rx="5" fill="#18181b" stroke="#3f3f46" stroke-width="0.9" />
					<text x="0" y="3.5" fill="#e4e4e7" font-size="9.5" text-anchor="middle" font-weight="500">${edge.label}</text>
				</g>
			`;
		}
	}

	svg += `</g>\n<!-- Nodes -->\n<g class="dkit-nodes">`;

	for (const [, node] of nodesMap) {
		const colors = COLOR_MAP[node.color] || COLOR_MAP.default;
		const iconSvg = node.icon && ICONS[node.icon] ? ICONS[node.icon] : '';

		svg += `
			<!-- Node: ${node.id} (${node.shape}) -->
			<g transform="translate(${node.x}, ${node.y})" class="${node.isFinal ? 'dkit-anim-wave' : animate === 'pulse' ? 'dkit-anim-pulse' : ''}">
		`;

		if (node.shape === 'diamond') {
			// Diamond / Decision shape
			svg += `
				<rect
					x="0"
					y="0"
					width="${node.width}"
					height="${node.height}"
					rx="${node.height / 2}"
					fill="${colors.bg}"
					stroke="${colors.border}"
					stroke-width="${node.isFinal ? '2' : '1.4'}"
					stroke-dasharray="4 2"
					style="filter: drop-shadow(0 4px 12px ${colors.glow});"
				/>
				<text x="${node.width / 2}" y="${node.subLabel ? 24 : node.height / 2 + 4}" fill="${colors.text}" font-size="11" font-weight="600" text-anchor="middle">${node.label}</text>
			`;
		} else if (node.shape === 'cylinder') {
			// Cylinder shape
			svg += `
				<rect
					x="0"
					y="0"
					width="${node.width}"
					height="${node.height}"
					rx="12"
					fill="${colors.bg}"
					stroke="${colors.border}"
					stroke-width="${node.isFinal ? '2' : '1.4'}"
					style="filter: drop-shadow(0 4px 12px ${colors.glow});"
				/>
				<ellipse cx="${node.width / 2}" cy="8" rx="${node.width / 2 - 8}" ry="4" fill="none" stroke="${colors.border}" stroke-width="1" opacity="0.6" />
			`;
		} else {
			// Standard card shape or circle pill
			svg += `
				<rect
					x="0"
					y="0"
					width="${node.width}"
					height="${node.height}"
					rx="${node.shape === 'circle' ? node.height / 2 : 10}"
					fill="${colors.bg}"
					stroke="${colors.border}"
					stroke-width="${node.isFinal ? '2' : '1.4'}"
					style="filter: drop-shadow(0 4px 12px ${colors.glow});"
				/>
			`;
		}

		if (node.shape !== 'diamond') {
			if (iconSvg) {
				svg += `
					<!-- Icon Badge -->
					<g transform="translate(10, ${(node.height - 22) / 2})">
						<rect x="0" y="0" width="22" height="22" rx="5" fill="#18181b" stroke="${colors.border}" stroke-width="0.8" />
						<g transform="translate(3, 3) scale(0.68)" stroke="${colors.text}" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
							${iconSvg}
						</g>
					</g>
					<text x="40" y="${node.subLabel ? 23 : node.height / 2 + 4}" fill="${colors.text}" font-size="11" font-weight="600" letter-spacing="-0.01em">${node.label}</text>
				`;
			} else {
				svg += `
					<text x="14" y="${node.subLabel ? 23 : node.height / 2 + 4}" fill="${colors.text}" font-size="11" font-weight="600" letter-spacing="-0.01em">${node.label}</text>
				`;
			}
		}

		if (node.subLabel) {
			const subX = node.shape === 'diamond' ? node.width / 2 : iconSvg ? 40 : 14;
			const subAnchor = node.shape === 'diamond' ? 'text-anchor="middle"' : '';
			svg += `
				<text x="${subX}" y="43" fill="#a19f97" font-size="9" font-family="'JetBrains Mono', monospace" ${subAnchor}>${node.subLabel}</text>
			`;
		}

		if (node.isFinal) {
			svg += `
				<!-- Final Target Star Badge -->
				<circle cx="${node.width - 10}" cy="10" r="4" fill="#10b981" />
			`;
		}

		svg += `</g>`;
	}

	svg += `</g>\n</svg>`;
	return svg;
}

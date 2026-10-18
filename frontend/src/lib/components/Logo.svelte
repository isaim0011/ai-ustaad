<script lang="ts">
	interface Props {
		size?: number;
		class?: string;
	}

	let { size = 32, class: className = '' }: Props = $props();
</script>

<div
	class="relative flex items-center justify-center shrink-0 overflow-hidden rounded-xl shadow-xs transition-transform duration-200 group-hover:scale-105 {className}"
	style="width: {size}px; height: {size}px;"
>
	<svg
		xmlns="http://www.w3.org/2000/svg"
		viewBox="0 0 64 64"
		class="w-full h-full"
		aria-hidden="true"
	>
		<defs>
			<linearGradient id="auBgComp" x1="0%" y1="0%" x2="100%" y2="100%">
				<stop offset="0%" stop-color="#242220" />
				<stop offset="100%" stop-color="#141413" />
			</linearGradient>
			<linearGradient id="auAccentComp" x1="0%" y1="0%" x2="100%" y2="100%">
				<stop offset="0%" stop-color="#e07a5f" />
				<stop offset="50%" stop-color="#c96442" />
				<stop offset="100%" stop-color="#10b981" />
			</linearGradient>
			<filter id="glowComp" x="-20%" y="-20%" width="140%" height="140%">
				<feGaussianBlur stdDeviation="1.5" result="blur" />
				<feComposite in="SourceGraphic" in2="blur" operator="over" />
			</filter>
		</defs>

		<!-- Container background -->
		<rect x="2" y="2" width="60" height="60" rx="14" fill="url(#auBgComp)" stroke="#c96442" stroke-opacity="0.4" stroke-width="1.8" />
		
		<!-- Neural Grid ring -->
		<circle cx="32" cy="32" r="23" fill="none" stroke="#c96442" stroke-opacity="0.15" stroke-dasharray="3 3" />

		<!-- Monogram AU -->
		<g filter="url(#glowComp)">
			<!-- Letter A -->
			<path d="M 18 45 L 26 19 L 34 45" fill="none" stroke="url(#auAccentComp)" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" />
			<path d="M 21.5 35 L 30.5 35" fill="none" stroke="#10b981" stroke-width="2.5" stroke-linecap="round" />
			
			<!-- Letter U -->
			<path d="M 35 27 L 35 38 C 35 43, 44 43, 44 38 L 44 24" fill="none" stroke="#f5f4ed" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" />
		</g>

		<!-- Synapse Dots -->
		<circle cx="26" cy="19" r="2.5" fill="#e07a5f" />
		<circle cx="21.5" cy="35" r="1.8" fill="#10b981" />
		<circle cx="30.5" cy="35" r="1.8" fill="#10b981" />
		<circle cx="44" cy="24" r="2.2" fill="#10b981" />
	</svg>
</div>

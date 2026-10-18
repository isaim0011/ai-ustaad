<script lang="ts">
	interface Props {
		size?: number;
		class?: string;
		interactive?: boolean;
	}

	let { size = 34, class: className = '', interactive = true }: Props = $props();
</script>

<div
	class="relative flex items-center justify-center shrink-0 overflow-hidden rounded-xl shadow-xs transition-all duration-300 group-hover:scale-105 group-hover:shadow-md {className}"
	style="width: {size}px; height: {size}px;"
>
	<svg
		xmlns="http://www.w3.org/2000/svg"
		viewBox="0 0 64 64"
		class="w-full h-full {interactive ? 'logo-interactive' : ''}"
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
			<linearGradient id="auCircuitComp" x1="0%" y1="0%" x2="100%" y2="100%">
				<stop offset="0%" stop-color="#c96442" stop-opacity="0.8" />
				<stop offset="100%" stop-color="#10b981" stop-opacity="0.8" />
			</linearGradient>
			<filter id="glowComp" x="-20%" y="-20%" width="140%" height="140%">
				<feGaussianBlur stdDeviation="1.5" result="blur" />
				<feComposite in="SourceGraphic" in2="blur" operator="over" />
			</filter>
		</defs>

		<style>
			.logo-ring {
				stroke-dasharray: 6 9;
				animation: logoRotate 12s linear infinite;
				transform-origin: 32px 32px;
			}
			.logo-interactive:hover .logo-ring {
				animation-duration: 4s;
			}
			.logo-pulse-1 {
				animation: logoPulse 2.8s ease-in-out infinite alternate;
			}
			.logo-pulse-2 {
				animation: logoPulse 2.8s ease-in-out 1.4s infinite alternate;
			}
			.logo-trace {
				stroke-dasharray: 40;
				stroke-dashoffset: 80;
				animation: logoTrace 3.5s ease-in-out infinite;
			}

			@keyframes logoRotate {
				from { transform: rotate(0deg); }
				to { transform: rotate(360deg); }
			}
			@keyframes logoPulse {
				0% { r: 1.8; opacity: 0.7; }
				50% { r: 2.8; opacity: 1; filter: drop-shadow(0 0 2px #10b981); }
				100% { r: 1.8; opacity: 0.7; }
			}
			@keyframes logoTrace {
				0% { stroke-dashoffset: 80; opacity: 0.5; }
				50% { opacity: 1; }
				100% { stroke-dashoffset: 0; opacity: 0.5; }
			}
		</style>

		<!-- Container background -->
		<rect x="2" y="2" width="60" height="60" rx="14" fill="url(#auBgComp)" stroke="#c96442" stroke-opacity="0.45" stroke-width="1.8" />
		
		<!-- Rotating Neural Grid ring -->
		<circle cx="32" cy="32" r="23" fill="none" stroke="url(#auCircuitComp)" stroke-width="1.2" stroke-opacity="0.35" class="logo-ring" />

		<!-- Monogram AU -->
		<g filter="url(#glowComp)">
			<!-- Letter A -->
			<path d="M 17 46 L 26 18 L 35 46" fill="none" stroke="url(#auAccentComp)" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" />
			<path d="M 20.5 36 L 31.5 36" fill="none" stroke="#10b981" stroke-width="2.5" stroke-linecap="round" class="logo-trace" />
			
			<!-- Letter U -->
			<path d="M 35 27 L 35 38 C 35 44, 45 44, 45 38 L 45 22" fill="none" stroke="#f5f4ed" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" />
		</g>

		<!-- Synapse Dots -->
		<circle cx="26" cy="18" r="2.5" fill="#e07a5f" class="logo-pulse-1" />
		<circle cx="20.5" cy="36" r="2" fill="#10b981" class="logo-pulse-2" />
		<circle cx="31.5" cy="36" r="2" fill="#10b981" class="logo-pulse-1" />
		<circle cx="45" cy="22" r="2.3" fill="#10b981" class="logo-pulse-2" />
		<circle cx="35" cy="27" r="1.8" fill="#c96442" class="logo-pulse-1" />
	</svg>
</div>

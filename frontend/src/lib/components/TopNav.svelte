<script lang="ts">
	import { Flame, Sparkles, User, Menu, X, LogOut, ChevronDown } from 'lucide-svelte';
	import ThemeToggle from '$lib/components/ThemeToggle.svelte';
	import Logo from '$lib/components/Logo.svelte';
	interface SupabaseUser {
		id: string;
		email?: string;
		user_metadata?: Record<string, any>;
	}

	interface Profile {
		id: string;
		email: string;
		full_name: string | null;
		avatar_url: string | null;
		xp_points: number;
		current_streak: number;
		selected_track: string | null;
	}

	interface Props {
		user: SupabaseUser | null;
		profile: Profile | null;
		supabaseConfigured?: boolean;
	}

	let { user = null, profile = null, supabaseConfigured = true }: Props = $props();

	let mobileMenuOpen = $state(false);
	let profileDropdownOpen = $state(false);

	const xp = $derived(profile?.xp_points ?? 0);
	const streak = $derived(profile?.current_streak ?? 0);
	const displayName = $derived(
		profile?.full_name || user?.user_metadata?.full_name || user?.email?.split('@')[0] || 'Student'
	);
</script>

<header class="sticky top-0 z-40 border-b border-[#e5e2d9] bg-[#faf9f5]/90 backdrop-blur-md dark:border-[#2c2b28] dark:bg-[#141413]/90">
	<div class="mx-auto flex h-16 max-w-7xl items-center justify-between px-4 sm:px-6 lg:px-8">
		<!-- Brand Logo -->
		<div class="flex items-center gap-2.5 sm:gap-3">
			<a href="/" class="group flex items-center gap-2.5 transition-opacity hover:opacity-95">
				<Logo size={34} />
				<span class="text-lg font-serif font-bold tracking-tight text-[#141413] dark:text-[#f5f4ed]">
					AI Ustaad
				</span>
			</a>
			<span class="text-xs px-2 py-0.5 rounded-full bg-amber-500/10 text-amber-600 dark:text-amber-400 font-mono border border-amber-500/20">
				AI Mastery
			</span>
			<a
				href="https://github.com/isaim0011"
				target="_blank"
				rel="noopener noreferrer"
				class="rounded-full border border-[#e5e2d9] bg-[#f0eee6]/80 px-2.5 py-0.5 text-xs font-mono font-medium text-[#6f6e69] transition-all hover:border-[#c96442]/50 hover:bg-[#c96442]/10 hover:text-[#c96442] dark:border-[#343330] dark:bg-[#262624] dark:text-[#a19f97] dark:hover:text-[#f5f4ed]"
			>
				by Bimo
			</a>
		</div>

		<!-- Desktop Navigation Links -->
		<nav class="hidden items-center gap-6 md:flex">
			<a
				href="/learn"
				class="text-sm font-medium text-[#6f6e69] transition-colors hover:text-[#141413] dark:text-[#a19f97] dark:hover:text-[#f5f4ed]"
			>
				Curriculum
			</a>
			<a
				href="/blog"
				class="text-sm font-medium text-[#6f6e69] transition-colors hover:text-[#141413] dark:text-[#a19f97] dark:hover:text-[#f5f4ed]"
			>
				Engineering Blog
			</a>
			<a
				href="/mentor"
				class="inline-flex items-center gap-1.5 text-sm font-medium text-[#6f6e69] transition-colors hover:text-[#c96442] dark:text-[#a19f97] dark:hover:text-[#c96442]"
			>
				<Sparkles class="h-3.5 w-3.5 text-[#c96442]" />
				<span>AI Mentor</span>
			</a>
		</nav>

		<!-- Right Side Controls: XP, Streak, Auth, Theme -->
		<div class="flex items-center gap-2.5 sm:gap-3">
			{#if user}
				<!-- Streak Counter -->
				<div
					class="hidden items-center gap-1 rounded-full border border-amber-500/20 bg-amber-500/10 px-2.5 py-1 text-xs font-mono font-medium text-amber-700 sm:flex dark:text-amber-400"
					title="Daily Learning Streak"
				>
					<Flame class="h-3.5 w-3.5 fill-amber-500 text-amber-500" />
					<span>{streak} {streak === 1 ? 'day' : 'days'}</span>
				</div>

				<!-- XP Points -->
				<div
					class="flex items-center gap-1 rounded-full border border-[#c96442]/20 bg-[#c96442]/10 px-2.5 py-1 text-xs font-mono font-medium text-[#c96442]"
					title="Total Earned XP"
				>
					<Sparkles class="h-3.5 w-3.5" />
					<span>{xp} XP</span>
				</div>

				<!-- User Profile / Dropdown -->
				<div class="relative">
					<button
						type="button"
						onclick={() => (profileDropdownOpen = !profileDropdownOpen)}
						class="flex items-center gap-2 rounded-full border border-[#e5e2d9] bg-[#f0eee6] p-1.5 text-xs text-[#141413] transition-colors hover:border-[#c96442]/40 dark:border-[#343330] dark:bg-[#262624] dark:text-[#f5f4ed]"
						aria-label="User profile options"
					>
						{#if profile?.avatar_url}
							<img src={profile.avatar_url} alt={displayName} class="h-6 w-6 rounded-full object-cover" />
						{:else}
							<div class="flex h-6 w-6 items-center justify-center rounded-full bg-[#c96442] text-white text-[11px] font-bold">
								{displayName.charAt(0).toUpperCase()}
							</div>
						{/if}
						<ChevronDown class="h-3 w-3 text-[#6f6e69] dark:text-[#a19f97]" />
					</button>

					{#if profileDropdownOpen}
						<div
							class="absolute right-0 mt-2 w-48 rounded-xl border border-[#e5e2d9] bg-[#faf9f5] p-1.5 shadow-lg dark:border-[#343330] dark:bg-[#232321]"
						>
							<div class="border-b border-[#e5e2d9] px-3 py-2 text-xs text-[#6f6e69] dark:border-[#343330] dark:text-[#a19f97]">
								<div class="font-medium text-[#141413] dark:text-[#f5f4ed] truncate">{displayName}</div>
								<div class="truncate text-[11px]">{user.email}</div>
							</div>
							<a
								href="/profile"
								onclick={() => (profileDropdownOpen = false)}
								class="flex items-center gap-2 rounded-lg px-3 py-2 text-xs text-[#2c2b28] hover:bg-[#f0eee6] dark:text-[#dcd9ce] dark:hover:bg-[#2e2d2a]"
							>
								<User class="h-3.5 w-3.5" />
								Profile Settings
							</a>
							<a
								href="/learn"
								onclick={() => (profileDropdownOpen = false)}
								class="flex items-center gap-2 rounded-lg px-3 py-2 text-xs text-[#2c2b28] hover:bg-[#f0eee6] dark:text-[#dcd9ce] dark:hover:bg-[#2e2d2a]"
							>
								Dashboard
							</a>
							<form action="/logout" method="POST" class="pt-1">
								<button
									type="submit"
									class="flex w-full items-center gap-2 rounded-lg px-3 py-2 text-left text-xs text-rose-600 hover:bg-rose-50 dark:text-rose-400 dark:hover:bg-rose-950/20"
								>
									<LogOut class="h-3.5 w-3.5" />
									Sign Out
								</button>
							</form>
						</div>
					{/if}
				</div>
			{:else}
				<a
					href="/login"
					class="text-xs sm:text-sm font-medium text-[#6f6e69] transition-colors hover:text-[#141413] dark:text-[#a19f97] dark:hover:text-[#f5f4ed]"
				>
					Sign In
				</a>
				<a
					href="/signup"
					class="rounded-lg bg-[#c96442] px-3.5 py-1.5 text-xs sm:text-sm font-medium text-white shadow-sm transition-all hover:bg-[#d97757] focus:outline-none focus:ring-2 focus:ring-[#c96442]/40"
				>
					Start Free
				</a>
			{/if}

			<!-- Theme Toggle -->
			<ThemeToggle />

			<!-- Mobile Menu Toggle -->
			<button
				type="button"
				onclick={() => (mobileMenuOpen = !mobileMenuOpen)}
				class="inline-flex h-9 w-9 items-center justify-center rounded-lg border border-[#e5e2d9] text-[#6f6e69] md:hidden dark:border-[#343330] dark:text-[#a19f97]"
				aria-label="Toggle navigation menu"
			>
				{#if mobileMenuOpen}
					<X class="h-4 w-4" />
				{:else}
					<Menu class="h-4 w-4" />
				{/if}
			</button>
		</div>
	</div>

	<!-- Mobile Drawer -->
	{#if mobileMenuOpen}
		<div class="border-b border-[#e5e2d9] bg-[#faf9f5] px-4 py-4 md:hidden dark:border-[#2c2b28] dark:bg-[#141413]">
			<nav class="flex flex-col gap-3">
				<a
					href="/learn"
					onclick={() => (mobileMenuOpen = false)}
					class="rounded-lg px-3 py-2 text-sm font-medium text-[#2c2b28] hover:bg-[#f0eee6] dark:text-[#dcd9ce] dark:hover:bg-[#262624]"
				>
					Curriculum
				</a>
				<a
					href="/blog"
					onclick={() => (mobileMenuOpen = false)}
					class="rounded-lg px-3 py-2 text-sm font-medium text-[#2c2b28] hover:bg-[#f0eee6] dark:text-[#dcd9ce] dark:hover:bg-[#262624]"
				>
					Engineering Blog
				</a>
				<a
					href="/mentor"
					onclick={() => (mobileMenuOpen = false)}
					class="flex items-center gap-2 rounded-lg px-3 py-2 text-sm font-medium text-[#c96442] hover:bg-[#f0eee6] dark:hover:bg-[#262624]"
				>
					<Sparkles class="h-4 w-4" />
					AI Mentor (Roman Urdu)
				</a>
				{#if user}
					<a
						href="/profile"
						onclick={() => (mobileMenuOpen = false)}
						class="rounded-lg px-3 py-2 text-sm font-medium text-[#2c2b28] hover:bg-[#f0eee6] dark:text-[#dcd9ce] dark:hover:bg-[#262624]"
					>
						Profile ({displayName})
					</a>
					<form action="/logout" method="POST" class="pt-2">
						<button
							type="submit"
							class="flex w-full items-center gap-2 rounded-lg px-3 py-2 text-sm font-medium text-rose-600 hover:bg-rose-50 dark:text-rose-400 dark:hover:bg-rose-950/20"
						>
							<LogOut class="h-4 w-4" />
							Sign Out
						</button>
					</form>
				{/if}
			</nav>
		</div>
	{/if}
</header>

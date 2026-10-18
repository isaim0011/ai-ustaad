<script lang="ts">
	import { enhance } from '$app/forms';
	import { User, Sparkles, Flame, Trophy, Award, CheckCircle2, AlertCircle, Save } from 'lucide-svelte';
	import type { ActionData, PageData } from './$types';

	let { data, form }: { data: PageData; form: ActionData } = $props();

	const profile = $derived(data.profile);
	const user = $derived(data.user);
	const tracks = $derived(data.tracks ?? []);
	const userBadges = $derived(data.userBadges ?? []);

	let isSubmitting = $state(false);
</script>

<div class="mx-auto max-w-4xl px-4 py-12 sm:px-6 lg:px-8 space-y-10">
	<!-- Profile Header -->
	<div class="border-b border-[#e5e2d9] pb-8 dark:border-[#343330]">
		<div class="flex flex-col sm:flex-row sm:items-center gap-4">
			<div class="flex h-16 w-16 items-center justify-center rounded-2xl bg-[#c96442] text-white font-serif font-bold text-2xl shadow-sm">
				{profile?.full_name?.charAt(0).toUpperCase() || user?.email?.charAt(0).toUpperCase() || 'S'}
			</div>
			<div>
				<div class="flex items-center gap-2">
					<h1 class="font-serif text-3xl font-bold tracking-tight text-[#141413] dark:text-[#f5f4ed]">
						{profile?.full_name || 'Student Profile'}
					</h1>
					<span class="rounded bg-[#c96442]/10 px-2.5 py-0.5 text-xs font-mono font-medium text-[#c96442]">
						{profile?.role || 'student'}
					</span>
				</div>
				<p class="mt-1 text-xs text-[#6f6e69] dark:text-[#a19f97]">
					{user?.email} • Member since {new Date(profile?.created_at || Date.now()).toLocaleDateString()}
				</p>
			</div>
		</div>
	</div>

	<!-- Stats Overview -->
	<div class="grid grid-cols-1 gap-4 sm:grid-cols-3">
		<div class="rounded-2xl border border-[#e5e2d9] bg-[#faf9f5] p-5 shadow-xs dark:border-[#343330] dark:bg-[#232321]">
			<div class="flex items-center justify-between text-xs font-mono text-[#6f6e69] dark:text-[#a19f97]">
				<span>Total Earned XP</span>
				<Sparkles class="h-4 w-4 text-[#c96442]" />
			</div>
			<div class="mt-3 font-serif text-3xl font-bold text-[#141413] dark:text-[#f5f4ed]">
				{profile?.xp_points ?? 0}
			</div>
		</div>

		<div class="rounded-2xl border border-[#e5e2d9] bg-[#faf9f5] p-5 shadow-xs dark:border-[#343330] dark:bg-[#232321]">
			<div class="flex items-center justify-between text-xs font-mono text-[#6f6e69] dark:text-[#a19f97]">
				<span>Current Daily Streak</span>
				<Flame class="h-4 w-4 fill-amber-500 text-amber-500" />
			</div>
			<div class="mt-3 font-serif text-3xl font-bold text-amber-600 dark:text-amber-400">
				{profile?.current_streak ?? 0} days
			</div>
		</div>

		<div class="rounded-2xl border border-[#e5e2d9] bg-[#faf9f5] p-5 shadow-xs dark:border-[#343330] dark:bg-[#232321]">
			<div class="flex items-center justify-between text-xs font-mono text-[#6f6e69] dark:text-[#a19f97]">
				<span>Longest Streak</span>
				<Trophy class="h-4 w-4 text-emerald-600 dark:text-emerald-400" />
			</div>
			<div class="mt-3 font-serif text-3xl font-bold text-emerald-600 dark:text-emerald-400">
				{profile?.longest_streak ?? 0} days
			</div>
		</div>
	</div>

	<!-- Form Success / Error -->
	{#if form?.message}
		<div
			class="flex items-center gap-2 rounded-xl p-4 text-xs font-medium {form.success
				? 'border border-emerald-500/30 bg-emerald-500/10 text-emerald-700 dark:text-emerald-400'
				: 'border border-rose-500/30 bg-rose-500/10 text-rose-700 dark:text-rose-400'}"
		>
			{#if form.success}
				<CheckCircle2 class="h-4 w-4 shrink-0" />
			{:else}
				<AlertCircle class="h-4 w-4 shrink-0" />
			{/if}
			<span>{form.message}</span>
		</div>
	{/if}

	<!-- Edit Profile Form -->
	<div class="rounded-2xl border border-[#e5e2d9] bg-[#faf9f5] p-6 shadow-xs sm:p-8 dark:border-[#343330] dark:bg-[#232321]">
		<h2 class="font-serif text-xl font-bold text-[#141413] dark:text-[#f5f4ed]">
			Edit Profile Settings
		</h2>

		<form
			method="POST"
			action="?/updateProfile"
			use:enhance={() => {
				isSubmitting = true;
				return async ({ update }) => {
					isSubmitting = false;
					await update();
				};
			}}
			class="mt-6 space-y-6"
		>
			<!-- Full Name -->
			<div>
				<label for="fullName" class="block text-xs font-medium text-[#141413] dark:text-[#f5f4ed]">
					Full Name
				</label>
				<input
					type="text"
					id="fullName"
					name="fullName"
					value={profile?.full_name || ''}
					placeholder="Ali Khan"
					class="mt-1 w-full rounded-xl border border-[#e5e2d9] bg-[#f0eee6]/50 px-3.5 py-2.5 text-xs text-[#141413] focus:border-[#c96442] focus:bg-[#faf9f5] focus:outline-none focus:ring-1 focus:ring-[#c96442] dark:border-[#343330] dark:bg-[#1f1e1d] dark:text-[#f5f4ed]"
				/>
			</div>

			<!-- Selected Specialization Track -->
			<div>
				<label for="selectedTrack" class="block text-xs font-medium text-[#141413] dark:text-[#f5f4ed]">
					Selected Specialization Track (Phase 5)
				</label>
				<p class="mt-0.5 text-xs text-[#6f6e69] dark:text-[#a19f97]">
					Apne career focus ke mutabiq track select karein:
				</p>

				<div class="mt-3 space-y-3">
					{#each tracks as track}
						{@const isSelected = (profile?.selected_track || 'track-a') === track.slug || (profile?.selected_track || 'track-a') === track.track_code.toLowerCase()}
						<label
							class="flex cursor-pointer items-start gap-3 rounded-xl border p-4 transition-colors {isSelected
								? 'border-[#c96442] bg-[#c96442]/5'
								: 'border-[#e5e2d9] bg-[#f0eee6]/40 hover:bg-[#e8e5db]/60 dark:border-[#343330] dark:bg-[#1a1a19] dark:hover:bg-[#262624]'}"
						>
							<input
								type="radio"
								name="selectedTrack"
								value={track.slug}
								checked={isSelected}
								class="mt-1 text-[#c96442] focus:ring-[#c96442]"
							/>
							<div>
								<div class="flex items-center gap-2">
									<span class="font-mono text-xs font-medium text-[#c96442]">{track.track_code}</span>
									<span class="font-serif text-sm font-semibold text-[#141413] dark:text-[#f5f4ed]">{track.title}</span>
								</div>
								<p class="mt-1 text-xs text-[#6f6e69] dark:text-[#a19f97]">
									{track.description}
								</p>
							</div>
						</label>
					{/each}
				</div>
			</div>

			<!-- Save Button -->
			<div class="pt-4 border-t border-[#e5e2d9] dark:border-[#343330]">
				<button
					type="submit"
					disabled={isSubmitting}
					class="inline-flex h-11 items-center gap-2 rounded-xl bg-[#c96442] px-6 text-xs font-semibold text-white shadow-sm transition-all hover:bg-[#d97757] focus:outline-none focus:ring-2 focus:ring-[#c96442]/40 disabled:opacity-50"
				>
					<Save class="h-4 w-4" />
					<span>{isSubmitting ? 'Saving...' : 'Save Profile Changes'}</span>
				</button>
			</div>
		</form>
	</div>

	<!-- Unlocked Badges Collection -->
	{#if userBadges.length > 0}
		<div class="rounded-2xl border border-[#e5e2d9] bg-[#faf9f5] p-6 shadow-xs sm:p-8 dark:border-[#343330] dark:bg-[#232321]">
			<h2 class="font-serif text-xl font-bold text-[#141413] dark:text-[#f5f4ed]">
				Unlocked Badges ({userBadges.length})
			</h2>

			<div class="mt-4 grid grid-cols-1 gap-4 sm:grid-cols-2 md:grid-cols-3">
				{#each userBadges as ub}
					{@const b = Array.isArray(ub.badge) ? ub.badge[0] : ub.badge}
					<div class="flex items-center gap-3 rounded-xl border border-amber-500/30 bg-amber-500/10 p-3.5">
						<div class="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl bg-amber-500/20 text-amber-600 dark:text-amber-400">
							<Award class="h-5 w-5" />
						</div>
						<div>
							<div class="font-serif text-xs font-semibold text-[#141413] dark:text-[#f5f4ed]">
								{b?.title}
							</div>
							<div class="text-[10px] text-[#6f6e69] dark:text-[#a19f97]">
								{b?.roman_urdu_subtitle}
							</div>
							<div class="mt-1 font-mono text-[10px] text-[#c96442]">
								+{b?.xp_bonus} XP Awarded
							</div>
						</div>
					</div>
				{/each}
			</div>
		</div>
	{/if}
</div>

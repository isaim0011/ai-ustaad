<script lang="ts">
	import { enhance } from '$app/forms';
	import { getBrowserSupabase } from '$lib/supabase';
	import { ArrowRight, AlertCircle, CheckCircle2 } from 'lucide-svelte';
	import type { ActionData } from './$types';

	let { form }: { form: ActionData } = $props();

	let oauthError = $state<string | null>(null);

	async function handleOAuth(provider: 'google' | 'github') {
		const supabase = getBrowserSupabase();
		if (!supabase) {
			oauthError = 'Supabase client is not configured.';
			return;
		}

		oauthError = null;
		try {
			const { error } = await supabase.auth.signInWithOAuth({
				provider,
				options: {
					redirectTo: `${window.location.origin}/auth/callback`
				}
			});
			if (error) oauthError = error.message;
		} catch (err: unknown) {
			oauthError = err instanceof Error ? err.message : 'OAuth sign in failed';
		}
	}
</script>

<div class="mx-auto flex min-h-[calc(100vh-16rem)] max-w-md items-center justify-center px-4 py-12">
	<div class="w-full rounded-2xl border border-[#e5e2d9] bg-[#faf9f5] p-6 shadow-sm sm:p-8 dark:border-[#343330] dark:bg-[#232321]">
		<!-- Heading -->
		<div class="text-center">
			<div class="mx-auto flex h-10 w-10 items-center justify-center rounded-xl bg-[#c96442] text-white font-serif font-bold text-base shadow-xs">
				AI
			</div>
			<h1 class="mt-4 font-serif text-2xl font-bold tracking-tight text-[#141413] dark:text-[#f5f4ed]">
				Start Your AI Journey
			</h1>
			<p class="mt-1 text-xs text-[#6f6e69] dark:text-[#a19f97]">
				100% Free Account • Zero-GPU Needed • Roman Urdu Curriculum
			</p>
		</div>

		<!-- Feedback Messages -->
		{#if form?.message && !form?.success}
			<div class="mt-4 flex items-center gap-2 rounded-lg border border-rose-500/20 bg-rose-500/10 p-3 text-xs text-rose-700 dark:text-rose-400">
				<AlertCircle class="h-4 w-4 shrink-0" />
				<span>{form.message}</span>
			</div>
		{/if}

		{#if form?.success}
			<div class="mt-4 flex items-center gap-2 rounded-lg border border-emerald-500/20 bg-emerald-500/10 p-3 text-xs text-emerald-700 dark:text-emerald-400">
				<CheckCircle2 class="h-4 w-4 shrink-0" />
				<span>{form.message}</span>
			</div>
		{/if}

		{#if oauthError}
			<div class="mt-4 flex items-center gap-2 rounded-lg border border-rose-500/20 bg-rose-500/10 p-3 text-xs text-rose-700 dark:text-rose-400">
				<AlertCircle class="h-4 w-4 shrink-0" />
				<span>{oauthError}</span>
			</div>
		{/if}

		<!-- OAuth Buttons -->
		<div class="mt-6 space-y-2.5">
			<button
				type="button"
				onclick={() => handleOAuth('google')}
				class="flex h-10 w-full items-center justify-center gap-2 rounded-xl border border-[#e5e2d9] bg-[#f0eee6] text-xs font-medium text-[#141413] transition-colors hover:border-[#c96442]/40 hover:bg-[#e8e5db] dark:border-[#343330] dark:bg-[#262624] dark:text-[#f5f4ed] dark:hover:bg-[#2e2d2a]"
			>
				<svg class="h-4 w-4" viewBox="0 0 24 24">
					<path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/>
					<path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/>
					<path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.06H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.94l2.85-2.22.81-.63z"/>
					<path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.06l3.66 2.84c.87-2.6 3.3-4.52 6.16-4.52z"/>
				</svg>
				<span>Sign Up with Google</span>
			</button>

			<button
				type="button"
				onclick={() => handleOAuth('github')}
				class="flex h-10 w-full items-center justify-center gap-2 rounded-xl border border-[#e5e2d9] bg-[#f0eee6] text-xs font-medium text-[#141413] transition-colors hover:border-[#c96442]/40 hover:bg-[#e8e5db] dark:border-[#343330] dark:bg-[#262624] dark:text-[#f5f4ed] dark:hover:bg-[#2e2d2a]"
			>
				<svg class="h-4 w-4 fill-current" viewBox="0 0 24 24">
					<path fill-rule="evenodd" clip-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.53 1.032 1.53 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z"/>
				</svg>
				<span>Sign Up with GitHub</span>
			</button>
		</div>

		<!-- Divider -->
		<div class="relative my-6 text-center">
			<div class="absolute inset-0 flex items-center">
				<div class="w-full border-t border-[#e5e2d9] dark:border-[#343330]"></div>
			</div>
			<span class="relative bg-[#faf9f5] px-2 text-[11px] font-mono uppercase tracking-wider text-[#6f6e69] dark:bg-[#232321] dark:text-[#a19f97]">
				or with email
			</span>
		</div>

		<!-- Sign Up Form -->
		<form method="POST" action="?/signup" use:enhance class="space-y-4">
			<div>
				<label for="fullName" class="block text-xs font-medium text-[#141413] dark:text-[#f5f4ed]">Full Name</label>
				<div class="relative mt-1">
					<input
						type="text"
						id="fullName"
						name="fullName"
						placeholder="Ali Khan"
						class="w-full rounded-xl border border-[#e5e2d9] bg-[#f0eee6]/50 px-3.5 py-2.5 text-xs text-[#141413] placeholder-[#6f6e69] focus:border-[#c96442] focus:bg-[#faf9f5] focus:outline-none focus:ring-1 focus:ring-[#c96442] dark:border-[#343330] dark:bg-[#1f1e1d] dark:text-[#f5f4ed]"
					/>
				</div>
			</div>

			<div>
				<label for="email" class="block text-xs font-medium text-[#141413] dark:text-[#f5f4ed]">Email address</label>
				<div class="relative mt-1">
					<input
						type="email"
						id="email"
						name="email"
						required
						placeholder="student@example.com"
						class="w-full rounded-xl border border-[#e5e2d9] bg-[#f0eee6]/50 px-3.5 py-2.5 text-xs text-[#141413] placeholder-[#6f6e69] focus:border-[#c96442] focus:bg-[#faf9f5] focus:outline-none focus:ring-1 focus:ring-[#c96442] dark:border-[#343330] dark:bg-[#1f1e1d] dark:text-[#f5f4ed]"
					/>
				</div>
			</div>

			<div>
				<label for="password" class="block text-xs font-medium text-[#141413] dark:text-[#f5f4ed]">Password (min 6 characters)</label>
				<div class="relative mt-1">
					<input
						type="password"
						id="password"
						name="password"
						required
						minlength="6"
						placeholder="••••••••"
						class="w-full rounded-xl border border-[#e5e2d9] bg-[#f0eee6]/50 px-3.5 py-2.5 text-xs text-[#141413] placeholder-[#6f6e69] focus:border-[#c96442] focus:bg-[#faf9f5] focus:outline-none focus:ring-1 focus:ring-[#c96442] dark:border-[#343330] dark:bg-[#1f1e1d] dark:text-[#f5f4ed]"
					/>
				</div>
			</div>

			<button
				type="submit"
				class="flex h-11 w-full items-center justify-center gap-2 rounded-xl bg-[#c96442] text-xs font-semibold text-white shadow-sm transition-all hover:bg-[#d97757] focus:outline-none focus:ring-2 focus:ring-[#c96442]/40"
			>
				<span>Create Free Account</span>
				<ArrowRight class="h-4 w-4" />
			</button>
		</form>

		<!-- Switch to Sign In -->
		<div class="mt-6 text-center text-xs text-[#6f6e69] dark:text-[#a19f97]">
			Pehle se account hai?{' '}
			<a href="/login" class="font-semibold text-[#c96442] hover:underline">
				Sign In
			</a>
		</div>
	</div>
</div>

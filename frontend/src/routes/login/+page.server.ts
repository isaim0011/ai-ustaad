import { fail, redirect } from '@sveltejs/kit';
import type { Actions, PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ locals }) => {
	const { session } = await locals.safeGetSession();
	if (session) {
		throw redirect(303, '/learn');
	}
	return {};
};

export const actions: Actions = {
	login: async ({ request, locals }) => {
		if (!locals.supabase) {
			return fail(500, { message: 'Database configuration missing.' });
		}

		const formData = await request.formData();
		const email = formData.get('email') as string;
		const password = formData.get('password') as string;

		if (!email || !password) {
			return fail(400, { message: 'Email and password are required.' });
		}

		const { error } = await locals.supabase.auth.signInWithPassword({
			email,
			password
		});

		if (error) {
			return fail(400, { message: error.message });
		}

		throw redirect(303, '/learn');
	},

	magicLink: async ({ request, locals, url }) => {
		if (!locals.supabase) {
			return fail(500, { message: 'Database configuration missing.' });
		}

		const formData = await request.formData();
		const email = formData.get('email') as string;

		if (!email) {
			return fail(400, { message: 'Email is required for magic link.' });
		}

		const { error } = await locals.supabase.auth.signInWithOtp({
			email,
			options: {
				emailRedirectTo: `${url.origin}/auth/callback`
			}
		});

		if (error) {
			return fail(400, { message: error.message });
		}

		return { success: true, message: 'Check your email for the magic login link!' };
	}
};

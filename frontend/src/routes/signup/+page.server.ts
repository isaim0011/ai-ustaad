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
	signup: async ({ request, locals, url }) => {
		if (!locals.supabase) {
			return fail(500, { message: 'Database configuration missing.' });
		}

		const formData = await request.formData();
		const fullName = formData.get('fullName') as string;
		const email = formData.get('email') as string;
		const password = formData.get('password') as string;

		if (!email || !password) {
			return fail(400, { message: 'Email and password are required.' });
		}

		if (password.length < 6) {
			return fail(400, { message: 'Password must be at least 6 characters.' });
		}

		const { data, error } = await locals.supabase.auth.signUp({
			email,
			password,
			options: {
				data: {
					full_name: fullName || email.split('@')[0]
				},
				emailRedirectTo: `${url.origin}/auth/callback`
			}
		});

		if (error) {
			return fail(400, { message: error.message });
		}

		// If user session is returned immediately (e.g. auto-confirm enabled)
		if (data.session) {
			throw redirect(303, '/learn');
		}

		return {
			success: true,
			message: 'Account created! Please check your email to confirm your account, then log in.'
		};
	}
};

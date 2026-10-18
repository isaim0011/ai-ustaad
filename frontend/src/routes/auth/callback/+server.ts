import { redirect } from '@sveltejs/kit';
import type { RequestHandler } from './$types';

export const GET: RequestHandler = async ({ url, locals }) => {
	const code = url.searchParams.get('code');
	const next = url.searchParams.get('next') ?? '/learn';

	if (code && locals.supabase) {
		const { error } = await locals.supabase.auth.exchangeCodeForSession(code);
		if (!error) {
			const target = next.startsWith('/') ? next : `/${next}`;
			redirect(303, target);
		}
	}

	// Return user to login with error
	redirect(303, '/login?error=auth_callback_failed');
};

import type { LayoutServerLoad } from './$types';
import { isSupabaseConfigured } from '$lib/supabase';

export const load: LayoutServerLoad = async ({ locals, cookies }) => {
	const configured = isSupabaseConfigured();
	const { session, user } = await locals.safeGetSession();

	let profile = null;
	if (configured && user && locals.supabase) {
		try {
			const { data, error } = await locals.supabase
				.from('profiles')
				.select('*')
				.eq('id', user.id)
				.single();
			if (!error) {
				profile = data;
			}
		} catch (err) {
			console.error('Error fetching profile in layout:', err);
		}
	}

	return {
		session,
		user,
		profile,
		supabaseConfigured: configured,
		cookies: cookies.getAll()
	};
};

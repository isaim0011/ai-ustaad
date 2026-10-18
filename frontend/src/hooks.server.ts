import { createServerClient } from '@supabase/ssr';
import { type Handle } from '@sveltejs/kit';
import { PUBLIC_SUPABASE_URL, PUBLIC_SUPABASE_ANON_KEY } from '$env/static/public';
import { isSupabaseConfigured } from '$lib/supabase';

export const handle: Handle = async ({ event, resolve }) => {
	const configured = isSupabaseConfigured();

	if (configured) {
		event.locals.supabase = createServerClient(PUBLIC_SUPABASE_URL, PUBLIC_SUPABASE_ANON_KEY, {
			cookies: {
				getAll: () => event.cookies.getAll(),
				setAll: (cookiesToSet) => {
					cookiesToSet.forEach((cookie: { name: string; value: string; options: any }) => {
						event.cookies.set(cookie.name, cookie.value, { ...cookie.options, path: '/' });
					});
				}
			}
		});

		event.locals.safeGetSession = async () => {
			try {
				const {
					data: { session }
				} = await event.locals.supabase.auth.getSession();
				if (!session) {
					return { session: null, user: null };
				}

				const {
					data: { user },
					error
				} = await event.locals.supabase.auth.getUser();
				if (error) {
					return { session: null, user: null };
				}

				return { session, user };
			} catch (err) {
				console.error('Error fetching Supabase session:', err);
				return { session: null, user: null };
			}
		};
	} else {
		event.locals.supabase = null as unknown as typeof event.locals.supabase;
		event.locals.safeGetSession = async () => ({ session: null, user: null });
	}

	return resolve(event, {
		filterSerializedResponseHeaders(name) {
			return name === 'content-range' || name === 'x-supabase-api-version';
		}
	});
};

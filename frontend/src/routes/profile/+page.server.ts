import { fail, redirect } from '@sveltejs/kit';
import type { Actions, PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ locals }) => {
	const { session, user } = await locals.safeGetSession();
	if (!session || !user) {
		throw redirect(303, '/login');
	}

	const supabase = locals.supabase;
	if (!supabase) {
		throw redirect(303, '/login');
	}

	try {
		// 1. Fetch profile
		const { data: profile } = await supabase
			.from('profiles')
			.select('*')
			.eq('id', user.id)
			.single();

		// 2. Fetch tracks
		const { data: tracks } = await supabase
			.from('specialization_tracks')
			.select('*')
			.order('track_code', { ascending: true });

		// 3. Fetch user badges
		const { data: userBadges } = await supabase
			.from('user_badges')
			.select(`
				id,
				awarded_at,
				badge:badges (
					id,
					slug,
					title,
					roman_urdu_subtitle,
					icon,
					xp_bonus
				)
			`)
			.eq('user_id', user.id);

		return {
			profile: profile ?? null,
			tracks: tracks ?? [],
			userBadges: userBadges ?? [],
			user
		};
	} catch (err) {
		console.error('Error in profile load:', err);
		return {
			profile: null,
			tracks: [],
			userBadges: [],
			user
		};
	}
};

export const actions: Actions = {
	updateProfile: async ({ request, locals }) => {
		const { user } = await locals.safeGetSession();
		if (!user || !locals.supabase) {
			return fail(401, { message: 'Unauthorized' });
		}

		const formData = await request.formData();
		const fullName = formData.get('fullName') as string;
		const selectedTrack = formData.get('selectedTrack') as string;

		try {
			const { error } = await locals.supabase
				.from('profiles')
				.update({
					full_name: fullName || null,
					selected_track: selectedTrack || 'track-a'
				})
				.eq('id', user.id);

			if (error) {
				return fail(400, { message: error.message });
			}

			return { success: true, message: 'Profile updated successfully!' };
		} catch (err: unknown) {
			const msg = err instanceof Error ? err.message : 'Failed to update profile';
			return fail(500, { message: msg });
		}
	}
};

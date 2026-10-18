import type { PageServerLoad } from './$types';
import {
	FALLBACK_COURSE,
	FALLBACK_PHASES,
	FALLBACK_TRACKS,
	FALLBACK_BLOGS
} from '$lib/data/fallback';

export const load: PageServerLoad = async ({ locals }) => {
	const supabase = locals.supabase;
	if (!supabase) {
		return {
			course: FALLBACK_COURSE,
			phases: FALLBACK_PHASES,
			tracks: FALLBACK_TRACKS,
			featuredBlogs: FALLBACK_BLOGS
		};
	}

	try {
		// 1. Fetch main course
		const { data: course } = await supabase
			.from('courses')
			.select('*')
			.eq('slug', 'ai-mastery-zero-to-production')
			.maybeSingle();

		// 2. Fetch all 5 phases with their modules
		const { data: phases } = await supabase
			.from('phases')
			.select(`
				id,
				phase_number,
				slug,
				title,
				weeks_range,
				level,
				description,
				diagram_script,
				order_index,
				modules (
					id,
					module_number,
					slug,
					title,
					weeks_range,
					estimated_hours,
					real_world_deliverable
				)
			`)
			.order('order_index', { ascending: true });

		// 3. Fetch specialization tracks
		const { data: tracks } = await supabase
			.from('specialization_tracks')
			.select('*')
			.order('track_code', { ascending: true });

		// 4. Fetch featured engineering blogs
		const { data: featuredBlogs } = await supabase
			.from('engineering_blogs')
			.select('id, slug, title, category, reading_time_minutes, summary_roman_urdu, diagram_script')
			.order('order_index', { ascending: true })
			.limit(3);

		return {
			course: course || FALLBACK_COURSE,
			phases: phases && phases.length > 0 ? phases : FALLBACK_PHASES,
			tracks: tracks && tracks.length > 0 ? tracks : FALLBACK_TRACKS,
			featuredBlogs: featuredBlogs && featuredBlogs.length > 0 ? featuredBlogs : FALLBACK_BLOGS
		};
	} catch (err) {
		console.error('Error fetching landing page data from Supabase, using fallback data:', err);
		return {
			course: FALLBACK_COURSE,
			phases: FALLBACK_PHASES,
			tracks: FALLBACK_TRACKS,
			featuredBlogs: FALLBACK_BLOGS
		};
	}
};

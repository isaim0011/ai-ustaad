import { error } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ params, locals, parent }) => {
	const parentData = await parent();
	const supabase = locals.supabase;
	if (!supabase) {
		throw error(500, 'Database is not configured.');
	}

	const moduleSlug = params.module;

	// 1. Fetch Module with Phase
	const { data: moduleData, error: modErr } = await supabase
		.from('modules')
		.select(`
			*,
			phase:phases (
				id,
				phase_number,
				title,
				slug,
				weeks_range
			)
		`)
		.eq('slug', moduleSlug)
		.maybeSingle();

	if (modErr || !moduleData) {
		throw error(404, `Module "${moduleSlug}" not found.`);
	}

	// 2. Fetch Lessons for this module
	const { data: lessons } = await supabase
		.from('lessons')
		.select('*')
		.eq('module_id', moduleData.id)
		.order('order_index', { ascending: true });

	// 3. Fetch Quiz for this module
	const { data: quiz } = await supabase
		.from('quizzes')
		.select('*')
		.eq('module_id', moduleData.id)
		.maybeSingle();

	// 4. Fetch Badge for this module if badge_slug is set
	let badge = null;
	if (moduleData.badge_slug) {
		const { data: badgeData } = await supabase
			.from('badges')
			.select('*')
			.eq('slug', moduleData.badge_slug)
			.maybeSingle();
		badge = badgeData;
	}

	return {
		module: moduleData,
		lessons: lessons ?? [],
		quiz: quiz ?? null,
		badge,
		completedLessonIds: parentData.completedLessonIds
	};
};

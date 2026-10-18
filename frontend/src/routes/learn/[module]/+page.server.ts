import { error } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';
import { FALLBACK_PHASES } from '$lib/data/fallback';

export const load: PageServerLoad = async ({ params, locals, parent }) => {
	const parentData = await parent();
	const supabase = locals.supabase;
	const moduleSlug = params.module;

	if (!supabase) {
		// Fallback lookup
		for (const p of FALLBACK_PHASES) {
			const foundMod = p.modules?.find((m) => m.slug === moduleSlug);
			if (foundMod) {
				return {
					module: {
						...foundMod,
						phase: {
							id: p.id,
							phase_number: p.phase_number,
							title: p.title,
							slug: p.slug,
							weeks_range: p.weeks_range
						}
					},
					lessons: foundMod.lessons ?? [],
					quiz: null,
					badge: {
						id: 'badge-python',
						slug: 'python-ustad',
						title: 'Dhabay Ka Pythoneer',
						roman_urdu_subtitle: 'Python 3.12 Core Syntax Master',
						xp_bonus: 150
					},
					completedLessonIds: parentData.completedLessonIds
				};
			}
		}
		throw error(500, 'Database is not configured.');
	}

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
		// Fallback lookup for Module 0 (or new modules)
		for (const p of FALLBACK_PHASES) {
			const foundMod = p.modules?.find((m) => m.slug === moduleSlug);
			if (foundMod) {
				return {
					module: {
						...foundMod,
						phase: {
							id: p.id,
							phase_number: p.phase_number,
							title: p.title,
							slug: p.slug,
							weeks_range: p.weeks_range
						}
					},
					lessons: foundMod.lessons ?? [],
					quiz: null,
					badge: {
						id: 'badge-python',
						slug: 'python-ustad',
						title: 'Dhabay Ka Pythoneer',
						roman_urdu_subtitle: 'Python 3.12 Core Syntax Master',
						xp_bonus: 150
					},
					completedLessonIds: parentData.completedLessonIds
				};
			}
		}
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

import { redirect } from '@sveltejs/kit';
import type { LayoutServerLoad } from './$types';
import { FALLBACK_PHASES } from '$lib/data/fallback';

export const load: LayoutServerLoad = async ({ locals }) => {
	const { session, user } = await locals.safeGetSession();
	if (!session || !user) {
		throw redirect(303, '/login');
	}

	const supabase = locals.supabase;
	if (!supabase) {
		const allModules: any[] = [];
		FALLBACK_PHASES.forEach((p) => {
			if (p.modules) {
				p.modules.forEach((m) => allModules.push(m));
			}
		});
		return {
			phases: FALLBACK_PHASES,
			modules: allModules,
			completedLessonIds: [] as string[]
		};
	}

	try {
		// Fetch phases and modules with lessons
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
				order_index,
				modules (
					id,
					phase_id,
					module_number,
					slug,
					title,
					weeks_range,
					estimated_hours,
					real_world_deliverable,
					order_index,
					lessons (
						id,
						module_id,
						lesson_code,
						slug,
						title,
						duration_minutes,
						xp_reward,
						order_index
					)
				)
			`)
			.order('order_index', { ascending: true });

		// Fetch user completed lessons
		const { data: userProgress } = await supabase
			.from('user_lesson_progress')
			.select('lesson_id')
			.eq('user_id', user.id)
			.eq('completed', true);

		const completedLessonIds = (userProgress ?? []).map((p) => p.lesson_id);

		// Flatten and sort modules
		const allModules: any[] = [];
		(phases ?? []).forEach((p) => {
			if (p.modules) {
				const sortedMods = [...p.modules].sort((a, b) => a.order_index - b.order_index);
				sortedMods.forEach((m) => {
					if (m.lessons) {
						m.lessons.sort((a: any, b: any) => a.order_index - b.order_index);
					}
					allModules.push(m);
				});
			}
		});

		return {
			phases: phases ?? [],
			modules: allModules,
			completedLessonIds
		};
	} catch (err) {
		console.error('Error fetching learn layout data:', err);
		return {
			phases: [],
			modules: [],
			completedLessonIds: [] as string[]
		};
	}
};

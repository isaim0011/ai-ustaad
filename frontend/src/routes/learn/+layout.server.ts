import { redirect } from '@sveltejs/kit';
import type { LayoutServerLoad } from './$types';
import { FALLBACK_PHASES } from '$lib/data/fallback';

export const load: LayoutServerLoad = async ({ locals }) => {
	const { session, user } = await locals.safeGetSession();
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

		// Fetch user completed lessons if authenticated
		let completedLessonIds: string[] = [];
		if (user) {
			const { data: userProgress } = await supabase
				.from('user_lesson_progress')
				.select('lesson_id')
				.eq('user_id', user.id)
				.eq('completed', true);
			completedLessonIds = (userProgress ?? []).map((p) => p.lesson_id);
		}

		// Ensure Phase 0 (Python Zero Se Hero) is present
		const effectivePhases: any[] = [...(phases ?? [])];
		if (!effectivePhases.some((p) => p.slug === 'phase-0-python-prerequisite' || p.phase_number === 0)) {
			const p0 = FALLBACK_PHASES.find((p) => p.phase_number === 0);
			if (p0) {
				effectivePhases.unshift(p0);
			}
		}

		// Flatten and sort modules
		const allModules: any[] = [];
		effectivePhases.forEach((p) => {
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
			user: user ?? null,
			phases: effectivePhases,
			modules: allModules,
			completedLessonIds
		};
	} catch (err) {
		console.error('Error fetching learn layout data:', err);
		return {
			user: user ?? null,
			phases: [],
			modules: [],
			completedLessonIds: [] as string[]
		};
	}
};

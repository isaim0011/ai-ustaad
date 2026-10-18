import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ locals, parent }) => {
	const parentData = await parent();
	const supabase = locals.supabase;
	const user = parentData.user;

	if (!supabase || !user) {
		return {
			allBadges: [],
			userBadges: [],
			activeChallenge: null,
			continueLesson: null,
			phaseStats: []
		};
	}

	try {
		// 1. Fetch all badges
		const { data: allBadges } = await supabase
			.from('badges')
			.select('*')
			.order('xp_bonus', { ascending: true });

		// 2. Fetch user unlocked badges
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
					description,
					icon,
					xp_bonus
				)
			`)
			.eq('user_id', user.id);

		// 3. Fetch active weekly challenge
		const { data: activeChallenge } = await supabase
			.from('weekly_challenges')
			.select('*')
			.eq('is_active', true)
			.order('week_number', { ascending: true })
			.limit(1)
			.maybeSingle();

		// 4. Calculate progress per phase & find "continue where left off"
		const completedSet = new Set(parentData.completedLessonIds);
		let continueLesson: { moduleSlug: string; lessonSlug: string; lessonTitle: string; moduleTitle: string } | null = null;

		const phaseStats = (parentData.phases ?? []).map((phase: any) => {
			let totalLessons = 0;
			let completedCount = 0;

			if (phase.modules) {
				phase.modules.forEach((mod: any) => {
					if (mod.lessons) {
						totalLessons += mod.lessons.length;
						mod.lessons.forEach((l: any) => {
							if (completedSet.has(l.id)) {
								completedCount++;
							} else if (!continueLesson) {
								continueLesson = {
									moduleSlug: mod.slug,
									lessonSlug: l.slug,
									lessonTitle: l.title,
									moduleTitle: mod.title
								};
							}
						});
					}
				});
			}

			const pct = totalLessons > 0 ? Math.round((completedCount / totalLessons) * 100) : 0;
			return {
				id: phase.id,
				phase_number: phase.phase_number,
				title: phase.title,
				weeks_range: phase.weeks_range,
				level: phase.level,
				totalLessons,
				completedCount,
				pct
			};
		});

		// If all completed or none found, fallback to first lesson
		if (!continueLesson && parentData.modules.length > 0 && parentData.modules[0].lessons?.length > 0) {
			const m = parentData.modules[0];
			const l = m.lessons[0];
			continueLesson = {
				moduleSlug: m.slug,
				lessonSlug: l.slug,
				lessonTitle: l.title,
				moduleTitle: m.title
			};
		}

		return {
			allBadges: allBadges ?? [],
			userBadges: userBadges ?? [],
			activeChallenge: activeChallenge ?? null,
			continueLesson,
			phaseStats
		};
	} catch (err) {
		console.error('Error fetching dashboard data:', err);
		return {
			allBadges: [],
			userBadges: [],
			activeChallenge: null,
			continueLesson: null,
			phaseStats: []
		};
	}
};

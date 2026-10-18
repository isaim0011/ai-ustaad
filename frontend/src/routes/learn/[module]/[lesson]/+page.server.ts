import { error, fail, redirect } from '@sveltejs/kit';
import type { Actions, PageServerLoad } from './$types';
import { FALLBACK_PHASES } from '$lib/data/fallback';

export const load: PageServerLoad = async ({ params, locals, parent }) => {
	const parentData = await parent();
	const supabase = locals.supabase;
	const { module: moduleSlug, lesson: lessonSlug } = params;

	function getFallbackData() {
		for (const p of FALLBACK_PHASES) {
			const m = p.modules?.find((mod) => mod.slug === moduleSlug);
			if (m && m.lessons) {
				const lesIndex = m.lessons.findIndex((l) => l.slug === lessonSlug);
				if (lesIndex !== -1) {
					const lesson = m.lessons[lesIndex];
					const prevLesson = lesIndex > 0 ? m.lessons[lesIndex - 1] : null;
					const nextLesson = lesIndex < m.lessons.length - 1 ? m.lessons[lesIndex + 1] : null;
					const completedList = (parentData.completedLessonIds || []) as string[];
					return {
						lesson,
						module: {
							id: m.id,
							slug: m.slug,
							title: m.title,
							module_number: m.module_number,
							practice_checkpoint: m.practice_checkpoint || m.practice_project
						},
						prevLesson,
						nextLesson,
						isCompleted: completedList.includes(String(lesson.id)),
						completedLessonIds: parentData.completedLessonIds,
						allModules: parentData.modules
					};
				}
			}
		}
		return null;
	}

	if (!supabase) {
		const fallback = getFallbackData();
		if (fallback) return fallback;
		throw error(500, 'Database connection is not configured.');
	}

	// 1. Fetch current module
	const { data: moduleData, error: modErr } = await supabase
		.from('modules')
		.select('id, slug, title, module_number, practice_checkpoint')
		.eq('slug', moduleSlug)
		.maybeSingle();

	if (modErr || !moduleData) {
		const fallback = getFallbackData();
		if (fallback) return fallback;
		throw error(404, `Module "${moduleSlug}" not found.`);
	}

	// 2. Fetch current lesson
	const { data: lesson, error: lesErr } = await supabase
		.from('lessons')
		.select('*')
		.eq('module_id', moduleData.id)
		.eq('slug', lessonSlug)
		.maybeSingle();

	if (lesErr || !lesson) {
		const fallback = getFallbackData();
		if (fallback) return fallback;
		throw error(404, `Lesson "${lessonSlug}" not found.`);
	}

	// 3. Fetch siblings in this module to find prev and next
	const { data: siblingLessons } = await supabase
		.from('lessons')
		.select('id, slug, title, lesson_code, order_index')
		.eq('module_id', moduleData.id)
		.order('order_index', { ascending: true });

	const siblings = siblingLessons ?? [];
	const currentIndex = siblings.findIndex((s) => s.id === lesson.id);
	const prevLesson = currentIndex > 0 ? siblings[currentIndex - 1] : null;
	const nextLesson = currentIndex < siblings.length - 1 ? siblings[currentIndex + 1] : null;

	// 4. Check if current lesson is completed
	const completedList = (parentData.completedLessonIds || []) as string[];
	const isCompleted = completedList.includes(String(lesson.id));

	return {
		lesson,
		module: moduleData,
		prevLesson,
		nextLesson,
		isCompleted,
		completedLessonIds: parentData.completedLessonIds,
		allModules: parentData.modules
	};
};

export const actions: Actions = {
	completeLesson: async ({ request, locals }) => {
		const { session, user } = await locals.safeGetSession();
		if (!session || !user) {
			throw redirect(303, '/login');
		}

		if (!locals.supabase) {
			return fail(500, { message: 'Database client missing.' });
		}

		const formData = await request.formData();
		const lessonId = formData.get('lessonId') as string;
		const notes = formData.get('notes') as string | null;

		if (!lessonId) {
			return fail(400, { message: 'Lesson ID required.' });
		}

		try {
			// Call the RPC complete_lesson
			const { data, error } = await locals.supabase.rpc('complete_lesson', {
				p_lesson_id: lessonId,
				p_notes: notes || null
			});

			if (error) {
				return fail(400, { message: error.message });
			}

			return {
				success: true,
				...data
			};
		} catch (err: unknown) {
			const msg = err instanceof Error ? err.message : 'Failed to mark lesson complete';
			return fail(500, { message: msg });
		}
	}
};

import { error, fail } from '@sveltejs/kit';
import type { Actions, PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ params, locals, parent }) => {
	const parentData = await parent();
	const supabase = locals.supabase;
	if (!supabase) {
		throw error(500, 'Database connection is not configured.');
	}

	const { module: moduleSlug, lesson: lessonSlug } = params;

	// 1. Fetch current module
	const { data: moduleData, error: modErr } = await supabase
		.from('modules')
		.select('id, slug, title, module_number')
		.eq('slug', moduleSlug)
		.maybeSingle();

	if (modErr || !moduleData) {
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

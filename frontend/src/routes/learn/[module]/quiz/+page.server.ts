import { error, fail } from '@sveltejs/kit';
import type { Actions, PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ params, locals, parent }) => {
	const parentData = await parent();
	const supabase = locals.supabase;
	if (!supabase) {
		throw error(500, 'Database is not configured.');
	}

	const moduleSlug = params.module;

	// 1. Fetch module
	const { data: moduleData, error: modErr } = await supabase
		.from('modules')
		.select('id, slug, title, module_number')
		.eq('slug', moduleSlug)
		.maybeSingle();

	if (modErr || !moduleData) {
		throw error(404, `Module "${moduleSlug}" not found.`);
	}

	// 2. Fetch quiz
	const { data: quiz, error: qErr } = await supabase
		.from('quizzes')
		.select('*')
		.eq('module_id', moduleData.id)
		.maybeSingle();

	if (qErr || !quiz) {
		throw error(404, `Quiz for module "${moduleSlug}" not found.`);
	}

	// 3. Fetch quiz questions
	const { data: questions } = await supabase
		.from('quiz_questions')
		.select('*')
		.eq('quiz_id', quiz.id)
		.order('question_number', { ascending: true });

	// 4. Fetch user previous quiz attempts
	const { data: previousAttempts } = await supabase
		.from('user_quiz_attempts')
		.select('*')
		.eq('quiz_id', quiz.id)
		.order('created_at', { ascending: false })
		.limit(5);

	return {
		module: moduleData,
		quiz,
		questions: questions ?? [],
		previousAttempts: previousAttempts ?? []
	};
};

export const actions: Actions = {
	submitQuiz: async ({ request, locals }) => {
		if (!locals.supabase) {
			return fail(500, { message: 'Database client missing.' });
		}

		const formData = await request.formData();
		const quizId = formData.get('quizId') as string;
		const answersRaw = formData.get('answers') as string;

		if (!quizId || !answersRaw) {
			return fail(400, { message: 'Quiz submission payload missing.' });
		}

		let userAnswers: Record<string, number> = {};
		try {
			userAnswers = JSON.parse(answersRaw);
		} catch {
			return fail(400, { message: 'Invalid answers format.' });
		}

		// Fetch official questions to verify score server-side
		const { data: questions } = await locals.supabase
			.from('quiz_questions')
			.select('id, question_number, correct_option_index')
			.eq('quiz_id', quizId);

		if (!questions || questions.length === 0) {
			return fail(400, { message: 'No questions found for this quiz.' });
		}

		let correctCount = 0;
		questions.forEach((q) => {
			const userAns = userAnswers[q.id];
			if (userAns !== undefined && userAns === q.correct_option_index) {
				correctCount++;
			}
		});

		const scorePct = Math.round((correctCount / questions.length) * 100);

		// Call submit_quiz RPC
		const { data: rpcRes, error: rpcErr } = await locals.supabase.rpc('submit_quiz', {
			p_quiz_id: quizId,
			p_score_pct: scorePct,
			p_answers: userAnswers
		});

		if (rpcErr) {
			return fail(400, { message: rpcErr.message });
		}

		return {
			success: true,
			correctCount,
			totalQuestions: questions.length,
			scorePct,
			...rpcRes
		};
	}
};

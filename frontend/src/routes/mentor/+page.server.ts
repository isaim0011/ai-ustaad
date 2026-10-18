import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ locals }) => {
	const { session, user } = await locals.safeGetSession();
	const supabase = locals.supabase;

	if (!supabase || !user) {
		return {
			sessionId: null,
			messages: [],
			user: null
		};
	}

	try {
		// 1. Fetch user's latest chat session or create one
		let { data: chatSession } = await supabase
			.from('ai_chat_sessions')
			.select('id, title, updated_at')
			.eq('user_id', user.id)
			.order('updated_at', { ascending: false })
			.limit(1)
			.maybeSingle();

		if (!chatSession) {
			const { data: newSession } = await supabase
				.from('ai_chat_sessions')
				.insert({
					user_id: user.id,
					title: 'Roman Urdu AI Mentor'
				})
				.select('id, title, updated_at')
				.single();
			chatSession = newSession;
		}

		// 2. Fetch existing messages for this session
		let messages: any[] = [];
		if (chatSession?.id) {
			const { data: dbMessages } = await supabase
				.from('ai_chat_messages')
				.select('*')
				.eq('session_id', chatSession.id)
				.order('created_at', { ascending: true });
			messages = dbMessages ?? [];
		}

		return {
			sessionId: chatSession?.id ?? null,
			messages,
			user
		};
	} catch (err) {
		console.error('Error in mentor server load:', err);
		return {
			sessionId: null,
			messages: [],
			user
		};
	}
};

import type { PageServerLoad } from './$types';
import { FALLBACK_BLOGS } from '$lib/data/fallback';

export const load: PageServerLoad = async ({ locals }) => {
	const supabase = locals.supabase;
	if (!supabase) {
		return { blogs: FALLBACK_BLOGS };
	}

	try {
		const { data: blogs } = await supabase
			.from('engineering_blogs')
			.select('id, slug, title, category, reading_time_minutes, summary_roman_urdu, diagram_script, order_index, created_at')
			.order('order_index', { ascending: true });

		return {
			blogs: blogs && blogs.length > 0 ? blogs : FALLBACK_BLOGS
		};
	} catch (err) {
		console.error('Error fetching blogs, using fallback data:', err);
		return { blogs: FALLBACK_BLOGS };
	}
};

import { error } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ params, locals }) => {
	const supabase = locals.supabase;
	if (!supabase) {
		throw error(500, 'Database is not configured.');
	}

	const slug = params.slug;

	const { data: blog, error: err } = await supabase
		.from('engineering_blogs')
		.select('*')
		.eq('slug', slug)
		.maybeSingle();

	if (err || !blog) {
		throw error(404, `Article "${slug}" not found.`);
	}

	// Fetch adjacent blogs for recommendations
	const { data: adjacent } = await supabase
		.from('engineering_blogs')
		.select('slug, title, category, reading_time_minutes')
		.neq('id', blog.id)
		.limit(2);

	return {
		blog,
		adjacent: adjacent ?? []
	};
};

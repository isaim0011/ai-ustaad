import { error } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';
import { FALLBACK_BLOGS } from '$lib/data/fallback';

export const load: PageServerLoad = async ({ params, locals }) => {
	const slug = params.slug;
	const supabase = locals.supabase;

	if (!supabase) {
		const blog = FALLBACK_BLOGS.find((b) => b.slug === slug);
		if (!blog) {
			throw error(404, `Article "${slug}" not found.`);
		}
		const adjacent = FALLBACK_BLOGS.filter((b) => b.slug !== slug).slice(0, 2);
		return { blog, adjacent };
	}

	try {
		const { data: blog, error: err } = await supabase
			.from('engineering_blogs')
			.select('*')
			.eq('slug', slug)
			.maybeSingle();

		if (err || !blog) {
			const fallbackBlog = FALLBACK_BLOGS.find((b) => b.slug === slug);
			if (fallbackBlog) {
				const adjacent = FALLBACK_BLOGS.filter((b) => b.slug !== slug).slice(0, 2);
				return { blog: fallbackBlog, adjacent };
			}
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
	} catch (e: any) {
		const fallbackBlog = FALLBACK_BLOGS.find((b) => b.slug === slug);
		if (fallbackBlog) {
			const adjacent = FALLBACK_BLOGS.filter((b) => b.slug !== slug).slice(0, 2);
			return { blog: fallbackBlog, adjacent };
		}
		throw error(404, `Article "${slug}" not found.`);
	}
};

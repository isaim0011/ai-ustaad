import type { RequestHandler } from './$types';
import { FALLBACK_BLOGS, FALLBACK_PHASES } from '$lib/data/fallback';

export const GET: RequestHandler = async ({ locals }) => {
	const siteUrl = 'https://ai-ustaad.pages.dev';
	const now = new Date().toISOString();

	// Core static routes
	const staticRoutes = [
		{ path: '', priority: '1.0', changefreq: 'daily' },
		{ path: '/learn', priority: '0.95', changefreq: 'daily' },
		{ path: '/blog', priority: '0.90', changefreq: 'daily' },
		{ path: '/mentor', priority: '0.85', changefreq: 'weekly' },
		{ path: '/signup', priority: '0.70', changefreq: 'monthly' },
		{ path: '/login', priority: '0.50', changefreq: 'monthly' }
	];

	// Canonical 10 engineering blog slugs
	const defaultBlogSlugs = [
		'zero-gpu-survival-guide-2026',
		'why-85-percent-fail-ai',
		'tensors-memory-strides',
		'the-illustrated-transformer',
		'kv-cache-paged-attention',
		'vector-search-vs-hybrid-rag',
		'mcp-and-smolagents',
		'unsloth-4bit-qlora',
		'deepseek-r1-and-grpo',
		'learner-to-3k-ai-engineer'
	];

	let blogSlugs = defaultBlogSlugs;

	// Attempt to pull latest from Supabase if connected
	if (locals.supabase) {
		try {
			const { data: dbBlogs } = await locals.supabase
				.from('engineering_blogs')
				.select('slug');
			if (dbBlogs && dbBlogs.length > 0) {
				const merged = new Set([...defaultBlogSlugs, ...dbBlogs.map((b: { slug: string }) => b.slug)]);
				blogSlugs = Array.from(merged);
			}
		} catch {
			// Fallback to canonical list
		}
	}

	// Module slugs from fallback phases
	const moduleSlugs: string[] = [];
	for (const phase of FALLBACK_PHASES) {
		for (const mod of phase.modules) {
			if (mod.slug) moduleSlugs.push(mod.slug);
		}
	}

	const xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${staticRoutes
	.map(
		(r) => `  <url>
    <loc>${siteUrl}${r.path}</loc>
    <lastmod>${now}</lastmod>
    <changefreq>${r.changefreq}</changefreq>
    <priority>${r.priority}</priority>
  </url>`
	)
	.join('\n')}
${blogSlugs
	.map(
		(slug) => `  <url>
    <loc>${siteUrl}/blog/${slug}</loc>
    <lastmod>${now}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.80</priority>
  </url>`
	)
	.join('\n')}
${moduleSlugs
	.map(
		(slug) => `  <url>
    <loc>${siteUrl}/learn/${slug}</loc>
    <lastmod>${now}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.85</priority>
  </url>`
	)
	.join('\n')}
</urlset>`.trim();

	return new Response(xml, {
		headers: {
			'Content-Type': 'application/xml; charset=utf-8',
			'Cache-Control': 'public, max-age=3600, s-maxage=86400'
		}
	});
};

import type { RequestHandler } from './$types';
import { FALLBACK_BLOGS, FALLBACK_PHASES } from '$lib/data/fallback';

export const GET: RequestHandler = async ({ locals }) => {
	const siteUrl = 'https://ai-ustaad.pages.dev';
	const now = new Date().toISOString();

	// Core public static indexable routes (disallow auth/login/signup/profile)
	const staticRoutes = [
		{ path: '', priority: '1.0', changefreq: 'daily' },
		{ path: '/learn', priority: '0.95', changefreq: 'daily' },
		{ path: '/blog', priority: '0.90', changefreq: 'daily' },
		{ path: '/mentor', priority: '0.80', changefreq: 'weekly' }
	];

	// Maps for deduplication and lastmod tracking
	const blogsMap = new Map<string, string>();
	const modulesMap = new Map<string, string>();
	const lessonsMap = new Map<string, string>(); // key: `${moduleSlug}/${lessonSlug}`, value: lastmod

	// 1. Populate from fallback data
	for (const b of FALLBACK_BLOGS) {
		if (b.slug) {
			blogsMap.set(b.slug, now);
		}
	}

	for (const phase of FALLBACK_PHASES) {
		const mods = phase.modules ?? [];
		for (const mod of mods) {
			if (mod.slug) {
				if (!modulesMap.has(mod.slug)) {
					modulesMap.set(mod.slug, now);
				}
				const lessons = mod.lessons ?? [];
				for (const les of lessons) {
					if (les.slug) {
						lessonsMap.set(`${mod.slug}/${les.slug}`, now);
					}
				}
			}
		}
	}

	// 2. Merge with Supabase database if available
	if (locals.supabase) {
		try {
			// Query engineering blogs
			const { data: dbBlogs } = await locals.supabase
				.from('engineering_blogs')
				.select('slug, updated_at');
			if (dbBlogs) {
				for (const b of dbBlogs) {
					if (b.slug) {
						blogsMap.set(b.slug, b.updated_at || now);
					}
				}
			}
		} catch {
			// Fallback retained
		}

		try {
			// Query modules
			const { data: dbModules } = await locals.supabase
				.from('modules')
				.select('id, slug, updated_at');
			if (dbModules) {
				const moduleMapById = new Map<string, string>();
				for (const m of dbModules) {
					if (m.slug) {
						modulesMap.set(m.slug, m.updated_at || now);
						moduleMapById.set(m.id, m.slug);
					}
				}

				// Query lessons
				const { data: dbLessons } = await locals.supabase
					.from('lessons')
					.select('module_id, slug, updated_at');
				if (dbLessons) {
					for (const l of dbLessons) {
						const modSlug = moduleMapById.get(l.module_id);
						if (modSlug && l.slug) {
							lessonsMap.set(`${modSlug}/${l.slug}`, l.updated_at || now);
						}
					}
				}
			}
		} catch {
			// Fallback retained
		}
	}

	// Build XML
	const urlEntries: string[] = [];

	for (const route of staticRoutes) {
		urlEntries.push(`  <url>
    <loc>${siteUrl}${route.path}</loc>
    <lastmod>${now}</lastmod>
    <changefreq>${route.changefreq}</changefreq>
    <priority>${route.priority}</priority>
  </url>`);
	}

	for (const [slug, lastmod] of blogsMap.entries()) {
		urlEntries.push(`  <url>
    <loc>${siteUrl}/blog/${slug}</loc>
    <lastmod>${lastmod}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.75</priority>
  </url>`);
	}

	for (const [slug, lastmod] of modulesMap.entries()) {
		urlEntries.push(`  <url>
    <loc>${siteUrl}/learn/${slug}</loc>
    <lastmod>${lastmod}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.85</priority>
  </url>`);
	}

	for (const [path, lastmod] of lessonsMap.entries()) {
		urlEntries.push(`  <url>
    <loc>${siteUrl}/learn/${path}</loc>
    <lastmod>${lastmod}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.80</priority>
  </url>`);
	}

	const xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${urlEntries.join('\n')}
</urlset>`.trim();

	return new Response(xml, {
		headers: {
			'Content-Type': 'application/xml; charset=utf-8',
			'Cache-Control': 'public, max-age=3600, s-maxage=86400'
		}
	});
};

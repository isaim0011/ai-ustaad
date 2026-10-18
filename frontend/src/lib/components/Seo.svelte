<script lang="ts">
	interface HrefLang {
		lang: string;
		href: string;
	}

	interface SeoProps {
		title?: string;
		description?: string;
		canonical?: string;
		ogType?: 'website' | 'article' | 'course';
		ogImage?: string;
		ogImageAlt?: string;
		twitterCard?: 'summary' | 'summary_large_image';
		keywords?: string;
		author?: string;
		noindex?: boolean;
		hreflangs?: HrefLang[];
		jsonLd?: Record<string, unknown> | Array<Record<string, unknown>>;
	}

	let {
		title = 'AI Ustaad — Zero Se Production Tak | Roman Urdu AI Engineering',
		description = 'South Asia ka pehla complete, production-grade Roman Urdu AI Engineering curriculum. Python, PyTorch, Transformers, Modern RAG, Anthropic MCP, DeepSeek-R1 GRPO aur Rust Axum.',
		canonical = 'https://ai-ustaad.pages.dev',
		ogType = 'website',
		ogImage = 'https://ai-ustaad.pages.dev/og-image.png',
		ogImageAlt = 'AI Ustaad — AI Mastery Zero Se Production Tak',
		twitterCard = 'summary_large_image',
		keywords = 'AI course in Urdu, Roman Urdu AI Engineering, AI Ustaad, DeepSeek-R1 GRPO, Unsloth QLoRA, Anthropic MCP, Rust Axum AI, PyTorch Urdu, Machine Learning Pakistan, Zero-GPU Google Colab',
		author = 'Bimo (isaim0011)',
		noindex = false,
		hreflangs,
		jsonLd
	}: SeoProps = $props();

	const baseUrl = 'https://ai-ustaad.pages.dev';

	const fullCanonical = $derived.by(() => {
		if (!canonical) return baseUrl;
		if (canonical.startsWith('http://') || canonical.startsWith('https://')) {
			return canonical;
		}
		const path = canonical.startsWith('/') ? canonical : `/${canonical}`;
		return `${baseUrl}${path}`;
	});

	const fullOgImage = $derived.by(() => {
		if (!ogImage) return `${baseUrl}/og-image.png`;
		if (ogImage.startsWith('http://') || ogImage.startsWith('https://')) {
			return ogImage;
		}
		const path = ogImage.startsWith('/') ? ogImage : `/${ogImage}`;
		return `${baseUrl}${path}`;
	});

	const formattedTitle = $derived.by(() => {
		if (!title) return 'AI Ustaad — Zero Se Production Tak';
		if (title.includes('AI Ustaad')) return title;
		return `${title} | AI Ustaad`;
	});

	const robotsValue = $derived(noindex ? 'noindex, nofollow' : 'index, follow');

	const effectiveHreflangs = $derived.by(() => {
		if (hreflangs && hreflangs.length > 0) return hreflangs;
		return [
			{ lang: 'ur-Latn', href: fullCanonical },
			{ lang: 'en', href: fullCanonical },
			{ lang: 'x-default', href: fullCanonical }
		];
	});

	const serializedJsonLd = $derived.by(() => {
		if (!jsonLd) return null;
		const jsonString = JSON.stringify(jsonLd).replace(/</g, '\\u003c');
		return `<script type="application/ld+json">${jsonString}<\/script>`;
	});
</script>

<svelte:head>
	<title>{formattedTitle}</title>
	<meta name="description" content={description} />
	<meta name="keywords" content={keywords} />
	<meta name="author" content={author} />
	<meta name="robots" content={robotsValue} />
	<link rel="canonical" href={fullCanonical} />

	{#each effectiveHreflangs as link (link.lang)}
		<link rel="alternate" hreflang={link.lang} href={link.href} />
	{/each}

	<!-- OpenGraph -->
	<meta property="og:type" content={ogType} />
	<meta property="og:site_name" content="AI Ustaad" />
	<meta property="og:title" content={formattedTitle} />
	<meta property="og:description" content={description} />
	<meta property="og:url" content={fullCanonical} />
	<meta property="og:image" content={fullOgImage} />
	<meta property="og:image:alt" content={ogImageAlt} />

	<!-- Twitter -->
	<meta name="twitter:card" content={twitterCard} />
	<meta name="twitter:title" content={formattedTitle} />
	<meta name="twitter:description" content={description} />
	<meta name="twitter:image" content={fullOgImage} />
	<meta name="twitter:creator" content="@isaim0011" />

	{#if serializedJsonLd}
		<!-- eslint-disable-next-line svelte/no-at-html-tags -->
		{@html serializedJsonLd}
	{/if}
</svelte:head>

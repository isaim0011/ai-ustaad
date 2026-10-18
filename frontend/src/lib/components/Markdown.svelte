<script lang="ts">
	import { marked, Renderer } from 'marked';
	import { highlightCode } from '$lib/utils/highlighter';

	interface Props {
		content: string;
		class?: string;
	}

	let { content = '', class: className = '' }: Props = $props();

	// Custom renderer for edge-safe code highlighting
	const renderer = new Renderer();
	renderer.code = function (arg: any, langStr?: string) {
		const text = typeof arg === 'string' ? arg : arg?.text || '';
		const lang = (typeof arg === 'string' ? langStr : arg?.lang) || 'text';
		return highlightCode(text, lang);
	};

	// Configure marked for clean GFM rendering
	const html = $derived(
		marked.parse(content, {
			renderer,
			async: false,
			gfm: true,
			breaks: true
		}) as string
	);
</script>

<div
	class="prose prose-neutral dark:prose-invert max-w-none
	prose-headings:font-serif prose-headings:font-semibold prose-headings:tracking-tight prose-headings:text-[#141413] dark:prose-headings:text-[#f5f4ed]
	prose-h1:text-2xl sm:prose-h1:text-3xl prose-h1:mb-4 prose-h1:mt-8
	prose-h2:text-xl sm:prose-h2:text-2xl prose-h2:mb-3 prose-h2:mt-6
	prose-h3:text-lg sm:prose-h3:text-xl prose-h3:mb-2 prose-h3:mt-4
	prose-p:text-[#2c2b28] dark:prose-p:text-[#dcd9ce] prose-p:leading-relaxed prose-p:my-3
	prose-a:text-[#c96442] prose-a:underline-offset-4 hover:prose-a:text-[#d97757]
	prose-blockquote:border-l-2 prose-blockquote:border-[#c96442] prose-blockquote:bg-[#f0eee6]/60 dark:prose-blockquote:bg-[#262624]/60 prose-blockquote:py-2 prose-blockquote:px-4 prose-blockquote:rounded-r-lg prose-blockquote:not-italic
	prose-strong:text-[#141413] dark:prose-strong:text-[#f5f4ed] prose-strong:font-semibold
	prose-code:font-mono prose-code:text-[#c96442] prose-code:bg-[#f0eee6] dark:prose-code:bg-[#262624] prose-code:px-1.5 prose-code:py-0.5 prose-code:rounded prose-code:before:content-none prose-code:after:content-none prose-code:text-xs
	prose-pre:bg-[#191918] prose-pre:border prose-pre:border-[#343330] prose-pre:rounded-xl prose-pre:p-4
	prose-li:my-1 prose-li:text-[#2c2b28] dark:prose-li:text-[#dcd9ce]
	{className}"
>
	{@html html}
</div>

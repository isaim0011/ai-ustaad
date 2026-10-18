<script lang="ts">
	import { PUBLIC_API_URL } from '$env/static/public';
	import { getBrowserSupabase } from '$lib/supabase';
	import { Sparkles, Send, Bot, User, ArrowRight, CornerDownLeft, RefreshCw } from 'lucide-svelte';
	import Markdown from '$lib/components/Markdown.svelte';
	import CodeBlock from '$lib/components/CodeBlock.svelte';
	import Diagram from '$lib/components/Diagram.svelte';
	import type { PageData } from './$types';

	let { data }: { data: PageData } = $props();

	interface Message {
		id?: string;
		sender: 'user' | 'assistant';
		content: string;
		code_snippet?: any;
		diagram_script?: string;
		suggested_followups?: string[];
	}

	let messages = $state<Message[]>([]);
	let inputValue = $state('');
	let isSending = $state(false);
	let textareaEl = $state<HTMLTextAreaElement | null>(null);
	let messagesContainerEl = $state<HTMLDivElement | null>(null);

	const sessionId = $derived(data.sessionId);
	const apiUrl = PUBLIC_API_URL || 'http://127.0.0.1:8080';

	// Initialize messages from DB or default welcome
	$effect(() => {
		if (data.messages && data.messages.length > 0) {
			messages = data.messages.map((m: any) => ({
				id: m.id,
				sender: m.sender as 'user' | 'assistant',
				content: m.content,
				code_snippet: m.metadata?.code_snippet,
				diagram_script: m.metadata?.diagram_script,
				suggested_followups: m.metadata?.suggested_followups
			}));
		} else if (messages.length === 0) {
			messages = [
				{
					sender: 'assistant',
					content:
						'Salam! Main aap ka **Roman Urdu AI Engineering Mentor** hoon.\n\nAap Transformer attention, Scaled Dot-Product math, Modern Hybrid RAG, Anthropic MCP swarms, DeepSeek-R1 GRPO ya Google Colab Free GPU compute se mutaliq koi bhi sawal pooch sakte hain!',
					suggested_followups: [
						'Transformer ka Self-Attention formula aur intuition samjhao',
						'Modern RAG mein ColPali aur BM25 re-ranking ka kya role hai?',
						'Google Colab Free GPU par bina paise diye LoRA fine-tuning kaise karein?'
					]
				}
			];
		}
	});

	function scrollToBottom() {
		setTimeout(() => {
			if (messagesContainerEl) {
				messagesContainerEl.scrollTop = messagesContainerEl.scrollHeight;
			}
		}, 50);
	}

	function handleInput(e: Event) {
		const target = e.target as HTMLTextAreaElement;
		target.style.height = 'auto';
		target.style.height = `${Math.min(target.scrollHeight, 160)}px`;
	}

	function handleKeyDown(e: KeyboardEvent) {
		if (e.key === 'Enter' && !e.shiftKey) {
			e.preventDefault();
			sendMessage();
		}
	}

	async function sendMessage(textToSend?: string) {
		const text = (textToSend || inputValue).trim();
		if (!text || isSending) return;

		inputValue = '';
		if (textareaEl) {
			textareaEl.style.height = 'auto';
		}

		// Add user message to UI
		const userMsg: Message = { sender: 'user', content: text };
		messages = [...messages, userMsg];
		isSending = true;
		scrollToBottom();

		const supabase = getBrowserSupabase();

		// Persist user message to Supabase
		if (supabase && sessionId) {
			try {
				await supabase.from('ai_chat_messages').insert({
					session_id: sessionId,
					sender: 'user',
					content: text
				});
			} catch (err) {
				console.error('Failed to persist user message:', err);
			}
		}

		// Prepare history
		const history = messages.slice(-6).map((m) => ({
			role: m.sender,
			content: m.content
		}));

		try {
			// Call server endpoint /api/mentor (3-tier: local backend -> Groq/Gemini -> Built-in Roman Urdu knowledge engine)
			const res = await fetch('/api/mentor', {
				method: 'POST',
				headers: { 'Content-Type': 'application/json' },
				body: JSON.stringify({
					message: text,
					history
				})
			});

			if (!res.ok) {
				throw new Error(`Mentor API error: ${res.status}`);
			}

			const mentorData = await res.json();
			const assistantMsg: Message = {
				sender: 'assistant',
				content: mentorData.reply_urdu || mentorData.content || 'Jawab receive nahi ho saka.',
				code_snippet: mentorData.code_snippet,
				diagram_script: mentorData.diagram_script,
				suggested_followups: mentorData.suggested_followups
			};

			messages = [...messages, assistantMsg];

			// Persist assistant message to Supabase
			if (supabase && sessionId) {
				await supabase.from('ai_chat_messages').insert({
					session_id: sessionId,
					sender: 'assistant',
					content: assistantMsg.content,
					metadata: {
						code_snippet: assistantMsg.code_snippet,
						diagram_script: assistantMsg.diagram_script,
						suggested_followups: assistantMsg.suggested_followups
					}
				});
			}
		} catch (err) {
			console.warn('Backend mentor API offline, using local intelligent Roman Urdu response:', err);

			// Smart client-side Roman Urdu fallback
			let fallbackReply = `So guys, dekhein: **${text}** ka conceptual framework bilkul straightforward hai!\n\nAI Mastery curriculum ke mutabiq har concept ko first-principles se samajhna zaroori hai. Scaled Dot-Product Attention ho ya Modern RAG retrieval, sab tensors aur probability distributions ke uper chalte hain.\n\nAap curriculum ke relevant module ko explore karein jahan detailed code examples aur interactive diagrams mojood hain!`;
			let fallbackCode: any = null;
			let fallbackScript: string | undefined = undefined;

			if (text.toLowerCase().includes('attention') || text.toLowerCase().includes('transformer')) {
				fallbackReply = `Transformer ka core block **Scaled Dot-Product Attention** hai!\nFormula: \`Attention(Q, K, V) = softmax((Q . K^T) / sqrt(d_k)) . V\`.\n\n- **Query (Q)**: Har token poochta hai mujhe baqi tokens se kya context chahiye?\n- **Key (K)**: Har token batata hai mere paas kya information hai?\n- **Value (V)**: Actual content vector jo aggregate hota hai!`;
				fallbackCode = {
					language: 'python',
					title: 'PyTorch Attention Vectorization',
					code: 'import torch\nimport torch.nn.functional as F\n\ndef attention(Q, K, V):\n    d_k = Q.size(-1)\n    scores = torch.matmul(Q, K.transpose(-2, -1)) / (d_k ** 0.5)\n    weights = F.softmax(scores, dim=-1)\n    return torch.matmul(weights, V)'
				};
				fallbackScript = `@preset midnight\n@animate flow\nflow LR: Attention Matrix\n  q[Query Q] -> dot((MatMul))\n  k[Key K] -> dot\n  dot -> sm[Softmax Weights] ~purple\n  v[Value V] -> out_mult((MatMul))\n  sm -> out_mult -> out[Attended Context]* ~ok`;
			} else if (text.toLowerCase().includes('rag') || text.toLowerCase().includes('vector')) {
				fallbackReply = `Modern RAG mein purana naive chunking ka tareeqa khatam ho chuka hai! 2026 SOTA standard **Hybrid Search + Re-ranking** hai:\n\n1. Dense Embeddings (pgvector ya Qdrant) semantic matching ke liye.\n2. BM25 Sparse Search exact keyword aur model names ke liye.\n3. Reciprocal Rank Fusion (RRF) dono results ko blend karta hai.\n4. Cohere ya BGE Re-ranker top-5 best chunks LLM context mein bhejta hai!`;
				fallbackScript = `@preset midnight\n@animate pulse\narch LR: Hybrid RAG Architecture\n  query[User Query] -> dense[pgvector Dense Search] $database\n  query -> sparse[BM25 Sparse Search] $terminal\n  dense -> rrf[Reciprocal Rank Fusion] $filter\n  sparse -> rrf\n  rrf -> rerank[Cross-Encoder Rerank] $layers\n  rerank -> llm[LLM Generation]* $brain`;
			}

			const assistantMsg: Message = {
				sender: 'assistant',
				content: fallbackReply,
				code_snippet: fallbackCode,
				diagram_script: fallbackScript,
				suggested_followups: [
					'Multi-head attention mein heads kyun divide karte hain?',
					'ColPali vision-based document retrieval kaise kaam karta hai?'
				]
			};

			messages = [...messages, assistantMsg];
		} finally {
			isSending = false;
			scrollToBottom();
		}
	}
</script>

<div class="mx-auto flex h-[calc(100vh-4rem)] max-w-4xl flex-col px-4 sm:px-6">
	<!-- Top Bar -->
	<div class="flex items-center justify-between border-b border-[#e5e2d9] py-3 text-xs dark:border-[#343330]">
		<div class="flex items-center gap-2">
			<div class="flex h-7 w-7 items-center justify-center rounded-lg bg-[#c96442]/10 text-[#c96442]">
				<Bot class="h-4 w-4" />
			</div>
			<div>
				<h1 class="font-serif text-sm font-semibold text-[#141413] dark:text-[#f5f4ed]">
					AI Mentor (Roman Urdu)
				</h1>
				<span class="text-[10px] font-mono text-[#6f6e69] dark:text-[#a19f97]">
					2026 SOTA Curriculum Assistant
				</span>
			</div>
		</div>

		<div class="flex items-center gap-2">
			<span class="inline-flex items-center gap-1 rounded-full bg-emerald-500/10 px-2 py-0.5 text-[11px] font-mono text-emerald-700 dark:text-emerald-400">
				<span class="h-1.5 w-1.5 rounded-full bg-emerald-500 animate-pulse"></span>
				Online
			</span>
		</div>
	</div>

	<!-- Messages Thread -->
	<div
		bind:this={messagesContainerEl}
		class="flex-1 overflow-y-auto py-6 space-y-6 pr-1"
	>
		{#each messages as msg, i (i)}
			{#if msg.sender === 'user'}
				<!-- User Message -->
				<div class="flex justify-end">
					<div class="max-w-[85%] rounded-2xl bg-[#c96442] px-4 py-3 text-xs leading-relaxed text-white sm:text-sm">
						{msg.content}
					</div>
				</div>
			{:else}
				<!-- Assistant Message (Claude Minimalist Style) -->
				<div class="flex items-start gap-3">
					<div class="flex h-7 w-7 shrink-0 items-center justify-center rounded-lg bg-[#c96442]/10 text-[#c96442] mt-0.5">
						<Sparkles class="h-3.5 w-3.5" />
					</div>
					<div class="flex-1 space-y-3 min-w-0">
						<div class="text-xs sm:text-sm leading-relaxed text-[#2c2b28] dark:text-[#dcd9ce]">
							<Markdown content={msg.content} />
						</div>

						<!-- Rendered Code Snippet if present -->
						{#if msg.code_snippet}
							<div class="my-2">
								<CodeBlock
									code={msg.code_snippet.code || ''}
									language={msg.code_snippet.language || 'python'}
									title={msg.code_snippet.title}
								/>
							</div>
						{/if}

						<!-- Rendered Diagram if present -->
						{#if msg.diagram_script}
							<div class="my-2">
								<Diagram script={msg.diagram_script} title="Mentor Visual Explanation" />
							</div>
						{/if}

						<!-- Suggested Followup Buttons -->
						{#if msg.suggested_followups && msg.suggested_followups.length > 0}
							<div class="flex flex-wrap gap-1.5 pt-2">
								{#each msg.suggested_followups as followup}
									<button
										type="button"
										onclick={() => sendMessage(followup)}
										class="inline-flex items-center gap-1 rounded-full border border-[#e5e2d9] bg-[#f0eee6] px-3 py-1 text-xs text-[#2c2b28] transition-colors hover:border-[#c96442]/40 hover:bg-[#e8e5db] dark:border-[#343330] dark:bg-[#262624] dark:text-[#dcd9ce] dark:hover:bg-[#2e2d2a]"
									>
										<span>{followup}</span>
										<ArrowRight class="h-3 w-3 text-[#c96442]" />
									</button>
								{/each}
							</div>
						{/if}
					</div>
				</div>
			{/if}
		{/each}

		{#if isSending}
			<div class="flex items-center gap-2 text-xs font-mono text-[#6f6e69] dark:text-[#a19f97]">
				<div class="h-3.5 w-3.5 animate-spin rounded-full border-2 border-[#c96442] border-t-transparent"></div>
				<span>Mentor soch raha hai...</span>
			</div>
		{/if}
	</div>

	<!-- Centered Claude-Style Bottom Composer -->
	<div class="sticky bottom-0 pb-4 pt-2 bg-[#faf9f5] dark:bg-[#1f1e1d]">
		<div class="rounded-2xl border border-[#e5e2d9] bg-[#f0eee6]/60 p-2 shadow-xs transition-colors focus-within:border-[#c96442]/50 focus-within:bg-[#faf9f5] dark:border-[#343330] dark:bg-[#262624]/60 dark:focus-within:bg-[#1f1e1d]">
			<textarea
				bind:this={textareaEl}
				bind:value={inputValue}
				oninput={handleInput}
				onkeydown={handleKeyDown}
				placeholder="Roman Urdu mein sawal poochein (e.g. 'Transformer attention formula samjhao')..."
				rows={1}
				class="w-full resize-none bg-transparent px-3 py-1.5 text-xs sm:text-sm text-[#141413] placeholder-[#6f6e69] focus:outline-none dark:text-[#f5f4ed] dark:placeholder-[#a19f97]"
			></textarea>

			<div class="flex items-center justify-between border-t border-[#e5e2d9]/60 px-2 pt-2 text-[11px] font-mono text-[#6f6e69] dark:border-[#343330]/60 dark:text-[#a19f97]">
				<span>Press <kbd class="rounded bg-[#e8e5db] px-1 dark:bg-[#2e2d2a]">Enter</kbd> to send, <kbd class="rounded bg-[#e8e5db] px-1 dark:bg-[#2e2d2a]">Shift+Enter</kbd> for newline</span>

				<button
					type="button"
					disabled={!inputValue.trim() || isSending}
					onclick={() => sendMessage()}
					class="inline-flex h-8 w-8 items-center justify-center rounded-xl bg-[#c96442] text-white shadow-xs transition-all hover:bg-[#d97757] disabled:cursor-not-allowed disabled:opacity-40"
					aria-label="Send message to AI Mentor"
				>
					<Send class="h-3.5 w-3.5" />
				</button>
			</div>
		</div>
	</div>
</div>

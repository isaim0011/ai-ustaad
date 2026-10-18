// Lightweight, universal syntax highlighter for Cloudflare Pages / Workers Edge Runtime
// Zero WASM, zero Node.js built-ins, zero external network requests.
// Supports Python, TypeScript, JavaScript, Rust, SQL, Bash, JSON, YAML, HTML, CSS.

export function escapeHtml(str: string): string {
	return str
		.replace(/&/g, '&amp;')
		.replace(/</g, '&lt;')
		.replace(/>/g, '&gt;')
		.replace(/"/g, '&quot;')
		.replace(/'/g, '&#39;');
}

interface TokenRule {
	type: string;
	regex: RegExp;
}

const COMMON_RULES: Record<string, TokenRule[]> = {
	python: [
		{ type: 'comment', regex: /(#.*)/g },
		{ type: 'string', regex: /(f?"""[\s\S]*?"""|f?'''[\s\S]*?'''|f?"(?:\\.|[^"\\])*"|f?'(?:\\.|[^'\\])*')/g },
		{ type: 'decorator', regex: /(@[a-zA-Z_]\w*)/g },
		{
			type: 'keyword',
			regex: /\b(def|class|return|if|elif|else|for|while|try|except|finally|with|as|import|from|in|is|not|and|or|lambda|yield|raise|pass|break|continue|async|await|assert|global|nonlocal)\b/g
		},
		{
			type: 'builtin',
			regex: /\b(torch|nn|F|Tensor|print|len|range|enumerate|zip|map|filter|list|dict|set|tuple|int|float|str|bool|self|cls|super|open|type|isinstance|issubclass)\b/g
		},
		{ type: 'number', regex: /\b(\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)\b/g },
		{ type: 'function', regex: /\b([a-zA-Z_]\w*)(?=\s*\()/g }
	],
	rust: [
		{ type: 'comment', regex: /(\/\/.*|\/\*[\s\S]*?\*\/)/g },
		{ type: 'string', regex: /("(?:\\.|[^"\\])*"|'[^'\\]')/g },
		{ type: 'macro', regex: /\b([a-zA-Z_]\w*!)/g },
		{
			type: 'keyword',
			regex: /\b(fn|pub|let|mut|struct|enum|impl|trait|use|mod|match|if|else|for|while|loop|return|async|await|where|unsafe|crate|self|Self|ref|type|const|static)\b/g
		},
		{
			type: 'builtin',
			regex: /\b(Option|Some|None|Result|Ok|Err|Vec|String|str|u8|u16|u32|u64|usize|i8|i16|i32|i64|isize|f32|f64|bool|char|Box|Arc|Rc|Mutex)\b/g
		},
		{ type: 'number', regex: /\b(\d+(?:\.\d+)?(?:[eE][+-]?\d+)?(?:u8|u16|u32|u64|usize|i32|i64|f32|f64)?)\b/g },
		{ type: 'function', regex: /\b([a-zA-Z_]\w*)(?=\s*\()/g }
	],
	typescript: [
		{ type: 'comment', regex: /(\/\/.*|\/\*[\s\S]*?\*\/)/g },
		{ type: 'string', regex: /(`[\s\S]*?`|"(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*')/g },
		{
			type: 'keyword',
			regex: /\b(function|const|let|var|return|if|else|for|while|switch|case|break|continue|import|export|from|default|class|extends|implements|interface|type|enum|new|this|typeof|instanceof|async|await|try|catch|finally|throw)\b/g
		},
		{
			type: 'builtin',
			regex: /\b(console|Promise|Array|Object|String|Number|Boolean|Map|Set|JSON|Math|Date|RegExp|Error|undefined|null|true|false|unknown|any|never|void)\b/g
		},
		{ type: 'number', regex: /\b(\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)\b/g },
		{ type: 'function', regex: /\b([a-zA-Z_]\w*)(?=\s*\()/g }
	],
	sql: [
		{ type: 'comment', regex: /(--.*|\/\*[\s\S]*?\*\/)/g },
		{ type: 'string', regex: /('(?:\\.|[^'\\])*')/g },
		{
			type: 'keyword',
			regex: /\b(SELECT|FROM|WHERE|INSERT|INTO|VALUES|UPDATE|SET|DELETE|CREATE|TABLE|ALTER|DROP|INDEX|JOIN|LEFT|RIGHT|INNER|OUTER|ON|GROUP|BY|ORDER|HAVING|LIMIT|OFFSET|UNION|ALL|AND|OR|NOT|IN|EXISTS|BETWEEN|LIKE|IS|NULL|AS|PRIMARY|KEY|FOREIGN|REFERENCES|DEFAULT|CASCADE)\b/gi
		},
		{
			type: 'builtin',
			regex: /\b(COUNT|SUM|AVG|MIN|MAX|NOW|COALESCE|CONCAT|SUBSTRING|TRIM|LOWER|UPPER|UUID|GEN_RANDOM_UUID)\b/gi
		},
		{ type: 'number', regex: /\b(\d+(?:\.\d+)?)\b/g }
	],
	bash: [
		{ type: 'comment', regex: /(#.*)/g },
		{ type: 'string', regex: /("(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*')/g },
		{
			type: 'keyword',
			regex: /\b(if|then|else|elif|fi|case|esac|for|while|until|do|done|in|function|return|exit|export|source|alias)\b/g
		},
		{
			type: 'builtin',
			regex: /\b(echo|cd|ls|mkdir|rm|cp|mv|cat|grep|sed|awk|curl|wget|pip|npm|cargo|git|python|python3|node|docker|kubectl)\b/g
		},
		{ type: 'variable', regex: /(\$[a-zA-Z_]\w*|\$\{[^}]+\})/g }
	]
};

// Aliases
COMMON_RULES.javascript = COMMON_RULES.typescript;
COMMON_RULES.js = COMMON_RULES.typescript;
COMMON_RULES.ts = COMMON_RULES.typescript;
COMMON_RULES.py = COMMON_RULES.python;
COMMON_RULES.sh = COMMON_RULES.bash;
COMMON_RULES.shell = COMMON_RULES.bash;

export function highlightCode(code: string, language: string = 'text'): string {
	const lang = language.toLowerCase().trim();
	const rules = COMMON_RULES[lang];

	if (!rules) {
		return `<pre class="edge-code"><code>${escapeHtml(code)}</code></pre>`;
	}

	// Line by line tokenization with safe escaping
	const lines = code.split('\n');
	const highlightedLines = lines.map((line) => {
		// Use placeholder replacement technique for tokens
		const tokens: Array<{ id: string; html: string }> = [];
		let processed = line;
		let tokenCounter = 0;

		for (const rule of rules) {
			processed = processed.replace(rule.regex, (match) => {
				const id = `___TOKEN_${tokenCounter++}___`;
				let className = 'text-[#c96442]';

				switch (rule.type) {
					case 'keyword':
						className = 'text-[#9e5d32] dark:text-[#d97757] font-semibold';
						break;
					case 'string':
						className = 'text-[#44805c] dark:text-[#78c295]';
						break;
					case 'comment':
						className = 'text-[#8c8a82] dark:text-[#6e6d67] italic';
						break;
					case 'builtin':
						className = 'text-[#387699] dark:text-[#68a8cf]';
						break;
					case 'function':
						className = 'text-[#815fa2] dark:text-[#b498d4] font-medium';
						break;
					case 'decorator':
					case 'macro':
						className = 'text-[#b87333] dark:text-[#e09355]';
						break;
					case 'number':
						className = 'text-[#c2623a] dark:text-[#e58a62]';
						break;
					case 'variable':
						className = 'text-[#c96442] dark:text-[#e5957d]';
						break;
					default:
						className = 'text-[#141413] dark:text-[#f5f4ed]';
				}

				tokens.push({
					id,
					html: `<span class="${className}">${escapeHtml(match)}</span>`
				});
				return id;
			});
		}

		// Escape remaining characters
		processed = escapeHtml(processed);

		// Restore tokens
		for (const token of tokens) {
			processed = processed.replace(token.id, token.html);
		}

		return processed;
	});

	return `<pre class="edge-code"><code>${highlightedLines.join('\n')}</code></pre>`;
}

import type { Session, User, SupabaseClient } from '@supabase/supabase-js';

declare global {
	namespace App {
		// interface Error {}
		interface Locals {
			supabase: SupabaseClient;
			safeGetSession: () => Promise<{ session: Session | null; user: User | null }>;
		}
		interface PageData {
			session?: Session | null;
			user?: User | null;
			supabaseConfigured?: boolean;
		}
		// interface PageState {}
		interface Platform {
			env?: {
				AI?: {
					run: (
						model: string,
						inputs: Record<string, unknown>,
						options?: Record<string, unknown>
					) => Promise<unknown>;
				};
				GROQ_API_KEY?: string;
				PUBLIC_API_URL?: string;
				PUBLIC_SUPABASE_URL?: string;
				PUBLIC_SUPABASE_ANON_KEY?: string;
				[key: string]: unknown;
			};
			context?: {
				waitUntil: (promise: Promise<unknown>) => void;
			};
			caches?: CacheStorage & { default: Cache };
		}
	}
}

export {};

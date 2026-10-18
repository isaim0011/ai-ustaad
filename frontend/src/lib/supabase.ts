import { createBrowserClient, createServerClient, isBrowser } from '@supabase/ssr';
import { PUBLIC_SUPABASE_URL, PUBLIC_SUPABASE_ANON_KEY } from '$env/static/public';
import type { SupabaseClient } from '@supabase/supabase-js';

export function isSupabaseConfigured(): boolean {
	if (!PUBLIC_SUPABASE_URL || !PUBLIC_SUPABASE_ANON_KEY) return false;
	if (PUBLIC_SUPABASE_URL.includes('your-project') || PUBLIC_SUPABASE_URL === '') return false;
	if (PUBLIC_SUPABASE_ANON_KEY.includes('your-anon') || PUBLIC_SUPABASE_ANON_KEY === '') return false;
	return true;
}

export function getBrowserSupabase(): SupabaseClient | null {
	if (!isSupabaseConfigured()) return null;
	return createBrowserClient(PUBLIC_SUPABASE_URL, PUBLIC_SUPABASE_ANON_KEY);
}

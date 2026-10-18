use std::env;

#[derive(Debug, Clone)]
pub struct Config {
    pub host: String,
    pub port: u16,
    pub database_url: Option<String>,
    pub supabase_url: Option<String>,
    pub supabase_anon_key: Option<String>,
    pub supabase_service_role_key: Option<String>,
    pub supabase_jwt_secret: Option<String>,
    pub environment: String,
    pub cors_origins: Vec<String>,
}

impl Config {
    pub fn from_env() -> Self {
        dotenvy::dotenv().ok();

        let host = env::var("HOST").unwrap_or_else(|_| "127.0.0.1".to_string());
        let port = env::var("PORT")
            .ok()
            .and_then(|p| p.parse::<u16>().ok())
            .unwrap_or(8080);

        let database_url = env::var("DATABASE_URL").ok().filter(|s| !s.trim().is_empty());
        let supabase_url = env::var("SUPABASE_URL").ok().filter(|s| !s.trim().is_empty());
        let supabase_anon_key = env::var("SUPABASE_ANON_KEY").ok().filter(|s| !s.trim().is_empty());
        let supabase_service_role_key = env::var("SUPABASE_SERVICE_ROLE_KEY").ok().filter(|s| !s.trim().is_empty());
        let supabase_jwt_secret = env::var("SUPABASE_JWT_SECRET").ok().filter(|s| !s.trim().is_empty());
        let environment = env::var("ENVIRONMENT").unwrap_or_else(|_| "development".to_string());

        let cors_origins = env::var("CORS_ORIGIN")
            .unwrap_or_else(|_| "*".to_string())
            .split(',')
            .map(|s| s.trim().to_string())
            .filter(|s| !s.is_empty())
            .collect();

        Self {
            host,
            port,
            database_url,
            supabase_url,
            supabase_anon_key,
            supabase_service_role_key,
            supabase_jwt_secret,
            environment,
            cors_origins,
        }
    }
}

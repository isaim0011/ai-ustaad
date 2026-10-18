use axum::{
    extract::FromRequestParts,
    http::{header::AUTHORIZATION, request::Parts},
};
use jsonwebtoken::{decode, DecodingKey, Validation};
use serde::{Deserialize, Serialize};
use std::sync::Arc;

use crate::{config::Config, error::AppError};

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct SupabaseClaims {
    pub sub: String,
    pub email: Option<String>,
    pub role: Option<String>,
    pub exp: Option<usize>,
    pub aud: Option<String>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct AuthenticatedUser {
    pub user_id: String,
    pub email: Option<String>,
    pub is_guest: bool,
}

impl Default for AuthenticatedUser {
    fn default() -> Self {
        Self {
            user_id: "guest-user".to_string(),
            email: Some("student@aimastery.local".to_string()),
            is_guest: true,
        }
    }
}

pub fn verify_token(token: &str, config: &Config) -> Result<AuthenticatedUser, AppError> {
    let token = token.trim();
    if token.is_empty() || token == "guest" || token.starts_with("guest-") || token == "dev-token" {
        return Ok(AuthenticatedUser {
            user_id: if token.starts_with("guest-") { token.to_string() } else { "guest-user".to_string() },
            email: Some("guest@aimastery.local".to_string()),
            is_guest: true,
        });
    }

    if let Some(secret) = &config.supabase_jwt_secret {
        let key = DecodingKey::from_secret(secret.as_bytes());
        let mut validation = Validation::default();
        validation.validate_exp = true;
        // In Supabase, aud can be "authenticated"
        validation.set_audience(&["authenticated"]);

        match decode::<SupabaseClaims>(token, &key, &validation) {
            Ok(token_data) => Ok(AuthenticatedUser {
                user_id: token_data.claims.sub,
                email: token_data.claims.email,
                is_guest: false,
            }),
            Err(_) => {
                // Try without audience check
                let mut fallback_validation = Validation::default();
                fallback_validation.validate_aud = false;
                match decode::<SupabaseClaims>(token, &key, &fallback_validation) {
                    Ok(data) => Ok(AuthenticatedUser {
                        user_id: data.claims.sub,
                        email: data.claims.email,
                        is_guest: false,
                    }),
                    Err(e) => {
                        if config.environment == "development" {
                            tracing::warn!("JWT decode error: {e}, falling back to guest in dev mode");
                            Ok(AuthenticatedUser::default())
                        } else {
                            Err(AppError::Unauthorized(format!("Invalid token: {e}")))
                        }
                    }
                }
            }
        }
    } else {
        // If no JWT secret is configured, allow guest / demo usage
        Ok(AuthenticatedUser {
            user_id: "demo-user".to_string(),
            email: Some("demo@aimastery.local".to_string()),
            is_guest: true,
        })
    }
}

impl<S> FromRequestParts<S> for AuthenticatedUser
where
    S: Send + Sync,
{
    type Rejection = AppError;

    async fn from_request_parts(parts: &mut Parts, _state: &S) -> Result<Self, Self::Rejection> {
        let auth_header = parts
            .headers
            .get(AUTHORIZATION)
            .and_then(|h| h.to_str().ok());

        let token = match auth_header {
            Some(val) if val.starts_with("Bearer ") => &val[7..],
            Some(val) => val,
            None => return Ok(AuthenticatedUser::default()), // Default to guest if unauthenticated
        };

        // Extract config if stored in extensions, or construct default
        let config = parts
            .extensions
            .get::<Arc<Config>>()
            .cloned()
            .unwrap_or_else(|| Arc::new(Config::from_env()));

        verify_token(token, &config)
    }
}

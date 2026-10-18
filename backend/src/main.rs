pub mod auth;
pub mod config;
pub mod db;
pub mod error;
pub mod models;
pub mod routes;
pub mod services;

#[cfg(test)]
pub mod tests;

use std::sync::Arc;
use axum::Extension;
use tower_http::cors::{Any, CorsLayer};
use tracing_subscriber::{layer::SubscriberExt, util::SubscriberInitExt};

use crate::{config::Config, db::AppState, routes::create_router};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Initialize tracing logging
    tracing_subscriber::registry()
        .with(
            tracing_subscriber::EnvFilter::try_from_default_env()
                .unwrap_or_else(|_| "ai_mastery_backend=debug,tower_http=debug,axum=trace".into()),
        )
        .with(tracing_subscriber::fmt::layer())
        .init();

    let banner = r#"
   ___    ____   __  ___           __                 
  /   |  /  _/  /  |/  /___ ______/ /____  _______  __
 / /| |  / /   / /|_/ / __ `/ ___/ __/ _ \/ ___/ / / /
/ ___ |_/ /   / /  / / /_/ (__  ) /_/  __/ /  / /_/ / 
/_/  |_/___/  /_/  /_/\__,_/____/\__/\___/_/   \__, /  
                                             /____/   
==> AI Mastery Platform: Zero to Production Backend
==> Powered by Axum 0.8 + SQLx + DiagramKit (Native Rust)
    "#;
    println!("{banner}");

    // Load configuration
    let config = Arc::new(Config::from_env());
    let addr = format!("{}:{}", config.host, config.port);

    // Initialize AppState (Postgres connection pool or in-memory fallback + Syllabus store)
    let state = AppState::new(config.clone()).await;

    // CORS configuration
    let cors = CorsLayer::new()
        .allow_origin(Any)
        .allow_methods(Any)
        .allow_headers(Any);

    let app = create_router(state)
        .layer(cors)
        .layer(Extension(config.clone()));

    tracing::info!("Server listening on http://{}", addr);
    println!("Server running at: http://{addr}");
    println!("API Health:        http://{addr}/api/health");
    println!("Course Overview:   http://{addr}/api/course");
    println!("Diagram Gallery:   http://{addr}/api/diagrams/gallery");

    let listener = tokio::net::TcpListener::bind(&addr).await?;
    axum::serve(listener, app).await?;

    Ok(())
}

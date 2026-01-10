"""アプリケーション設定."""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """アプリケーション設定."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    # アプリケーション設定
    app_name: str = "Historical Travel Agent"
    debug: bool = False

    # CORS設定
    cors_origins: list[str] = ["http://localhost:3000"]

    # データベース設定
    database_url: str = "postgresql://postgres:postgres@localhost:5432/travel_agent"

    # Redis設定
    redis_url: str = "redis://localhost:6379/0"

    # Google Cloud設定
    google_cloud_project: str = ""
    google_cloud_location: str = "asia-northeast1"

    # ストレージ設定
    upload_dir: str = "./uploads"
    max_upload_size: int = 10 * 1024 * 1024  # 10MB


@lru_cache
def get_settings() -> Settings:
    """設定のシングルトンインスタンスを取得."""
    return Settings()

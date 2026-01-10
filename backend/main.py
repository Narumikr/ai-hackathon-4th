"""FastAPI application entry point."""

from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config.settings import get_settings


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """アプリケーションのライフサイクル管理."""
    # 起動時の処理
    print("Starting up...")
    yield
    # 終了時の処理
    print("Shutting down...")


# 設定の読み込み
settings = get_settings()

# FastAPIアプリケーション作成
app = FastAPI(
    title="Historical Travel Agent API",
    description="歴史学習特化型旅行AIエージェント - REST API",
    version="0.1.0",
    lifespan=lifespan,
)

# CORS設定（ローカル開発環境）
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root() -> dict[str, str]:
    """ルートエンドポイント."""
    return {"message": "Historical Travel Agent API"}


@app.get("/health")
async def health() -> dict[str, str]:
    """ヘルスチェックエンドポイント."""
    return {"status": "ok"}

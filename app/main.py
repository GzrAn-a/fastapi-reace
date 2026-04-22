from contextlib import asynccontextmanager

from fastapi import FastAPI

from sqlmodel import SQLModel
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

from app.src.db import engine
from app.src.api import api_my, api_ws,api_create_yzm


@asynccontextmanager
async def lifespan(app: FastAPI):
    # 👉 startup
    SQLModel.metadata.create_all(engine)
    print("DB initialized")

    yield  # 👉 application runs here

    # 👉 shutdown
    print("App shutting down")


app = FastAPI(
    lifespan=lifespan,
    title="My API",
    description="My API",
    version="1.0",
    # openapi_url=None,
    # docs_url=None,
    # redoc_url=None,
)

app.mount("/assets", StaticFiles(directory="assets"), name="static")
# # --- 关键：添加 CORS 中间件 ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*",
        # "http://192.168.20.236:8000",  # 允许局域网 IP 访问
        # "http://localhost:8000",  # 允许本地访问
        # "http://127.0.0.1:8000",
        #  "http://localhost:5173/"

    ],  # 允许所有来源
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

s = """
我佛糍粑
"""
print(s)

app.include_router(api_ws.router, prefix="/api_ws")
app.include_router(api_my.router, prefix="/api_v1")
app.include_router(api_create_yzm.router, prefix="/api_create_yzm")
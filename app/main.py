from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlmodel import SQLModel
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

from app.src.api.user_api.api_create_order import api_create_order
from app.src.db import engine
from app.src.api.user_api import api_ws, api_create_yzm, api_my
from app.src.api.user_api.api_index import api_get_order
from app.src.api.user_api.api_user import api_user_login


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan events."""
    SQLModel.metadata.create_all(engine)
    print("DB initialized")
    yield
    print("App shutting down")


app = FastAPI(
    lifespan=lifespan,
    title="My API",
    description="My API",
    version="1.0",
)

app.mount("/assets", StaticFiles(directory="assets"), name="static")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(api_ws.router, prefix="/api_ws")
app.include_router(api_my.router, prefix="/api_v1")
app.include_router(api_create_yzm.router, prefix="/api_v1/api_create_yzm")
app.include_router(
    api_create_order.router,
    prefix="/api_v1/api_create_order",
    tags=["订单页面"]
)
app.include_router(
    api_get_order.router,
    prefix="/api_v1/get_order",
    tags=["小程序首页"]
)
app.include_router(
    api_user_login.router,
    prefix="/api_v1/user_login",
    tags=["用户相关"]
)
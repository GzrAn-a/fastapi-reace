from typing import Optional

from fastapi import UploadFile, File, APIRouter

from src.services.server_auth import server_auth

router = APIRouter()

@router.post("/login")
async def user_login(
        file: Optional[UploadFile] = File(default=None)
):
    data = await server_auth(file)
    
    return {"message": data}

@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

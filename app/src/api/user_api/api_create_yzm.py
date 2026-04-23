from fastapi import APIRouter, BackgroundTasks

from app.src.services.server_create_yzm import server_create_yzm, delete_file

router = APIRouter()


@router.get("/create_yzm",summary="创建验证码")
def captcha(background_tasks: BackgroundTasks):
    """生成验证码"""
    img = server_create_yzm()

    background_tasks.add_task(delete_file, img["img_rul"])

    return {"id": img["captcha_id"], "img_url": img["img_rul"]}

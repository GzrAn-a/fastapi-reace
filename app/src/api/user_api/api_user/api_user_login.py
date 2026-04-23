import random

from fastapi import FastAPI, APIRouter,Depends
from pydantic import BaseModel
from app.src.db import get_session
from app.src.models.ModelUser import ModelUser
from sqlmodel import Session, select
import time

router = APIRouter()
"""
{
  "access_token": "ACCESS_TOKEN",
  "expires_in": 7200,
  "refresh_token": "REFRESH_TOKEN",
  "openid": "OPENID",
  "scope": "SCOPE",
  "unionid": "UNIONID"
}
"""

# 接收前端数据
class RequestUserLogin(BaseModel):
    openid: str

@router.post("/user_login",summary="微信登录")
async def user_login(
        login_data:RequestUserLogin,
        session:Session=Depends(get_session)
):
    # 1 尝试查询用户
    statement = select(ModelUser).where(ModelUser.openid == login_data.openid)
    user:ModelUser = session.exec(statement).first()

    # 如果不存在就创建
    if not user:
        user = ModelUser(
            openid=login_data.openid,
            nick_name="用户名",  #
            user_avatar="https://123412",  # 头像
            student_id=random.randint(1000,2000),
            school_image="https://123412", # 学生证照片
            school_id=0,  # 学校id, 上传学生证 审核通过后，由 管理员设置
            dorm_building="宿舍楼",
            created_at=int(time.time()),
        )
        session.add(user)
        session.commit()
        session.refresh(user)
        print(f"新用户注册成功: {user.openid}")
    else:
        print(f"用户已登录: {user.openid}")
    return {
        "status": "success",
        "user":user
    }
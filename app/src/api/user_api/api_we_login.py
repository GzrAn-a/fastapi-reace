import os
import secrets
import httpx
from fastapi import APIRouter
from fastapi import HTTPException
from pydantic import BaseModel

router = APIRouter()

class LoginRequest(BaseModel):
    code: str


@router.post("/api/login/wechat")
async def wechat_login(req: LoginRequest):
    # 微信登录凭证校验接口
    # grant_type 固定为 'authorization_code'
    url = "https://api.weixin.qq.com/sns/jscode2session"
    params = {
        "appid": os.getenv("AppID"),
        "secret": os.getenv("AppSecret"),
        "js_code": req.code,
        "grant_type": "authorization_code"
    }
    
    try:
        async with httpx.AsyncClient() as client:
            # 1. 请求微信服务器换取 openid
            response = await client.get(url, params=params)
            data = response.json()
        
        # 2. 处理微信返回的错误
        if "errcode" in data:
            raise HTTPException(status_code=400, detail=f"微信接口错误: {data['errmsg']}")
        
        openid = data["openid"]  # 用户 ID
        session_key = data["session_key"]   # 微信返回 解密用户数据的 密钥 不能返回给前端
        
        # 3. (可选) 获取用户信息
        # 注意：从2021年起，获取头像昵称需要用户点击按钮授权，
        # 这里仅返回 openid，具体用户信息建议前端通过 <button open-type="chooseAvatar"> 获取
        # 或者使用新版头像昵称填写能力
        
        # 4. 生成自定义登录态 (Token)
        # 实际项目中应使用 JWT (如 python-jose) 并绑定 openid 存入数据库
        custom_token = secrets.token_urlsafe(32)
        
        # TODO: 将 openid 和 token 存入数据库 (Redis/MySQL)
        
        return {
            "success": True,
            "data": {
                "token": custom_token,
                "user": {
                    "openid": openid, # 用户 id
                    "nickname": "新用户"  # 这里可以是数据库中查询到的昵称
                }
            }
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
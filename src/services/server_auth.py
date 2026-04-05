# server/auth_service.py
import base64
from fastapi import UploadFile


# 这里可以放复杂的业务逻辑，比如数据库查询、密码校验等
async def server_auth(file: UploadFile):
    file_content = None
    if file:
        contents = await file.read()
        encoded_str = base64.b64encode(contents).decode('utf-8')
        file_content = f"data:image/png;base64,{encoded_str}"
    return {
        "file_base64": file_content,
        "original_filename": file.filename if file else None
    }

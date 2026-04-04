# server/auth_service.py
import base64
from fastapi import UploadFile


# 这里可以放复杂的业务逻辑，比如数据库查询、密码校验等
async def server_auth(file: UploadFile):
    file_content = None
    
    if file:
        # 1. 读取二进制流
        contents = await file.read()
        
        # 2. 处理 Base64 编码
        # 注意：这里为了演示保留了你之前的逻辑，但在生产环境中
        # 大文件转 Base64 会占用大量内存，建议直接上传到对象存储(S3/MinIO)
        encoded_str = base64.b64encode(contents).decode('utf-8')
        
        # 3. 拼接 Data URI (根据实际文件类型动态判断更好)
        file_content = f"data:image/png;base64,{encoded_str}"
        
        # 记得要把文件指针归位，如果后面还要读取的话
        # await file.seek(0)
    
    return {
        "file_base64": file_content,
        "original_filename": file.filename if file else None
    }

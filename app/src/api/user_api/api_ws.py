import subprocess
import os
from fastapi import APIRouter, WebSocket, WebSocketDisconnect

router = APIRouter()


@router.websocket('/ws')
async def my_socker(websocket: WebSocket):
    await websocket.accept()
    print("Remote Shell Connected.")

    try:
        while True:
            # 1. 接收命令
            request = await websocket.receive_text()

            # 2. 执行系统命令
            try:
                # 注意：subprocess.run 是同步阻塞的，在生产环境建议用 asyncio.create_subprocess_shell
                result = subprocess.run(
                    request,
                    shell=True,
                    capture_output=True,
                    text=True,
                    # 自动处理编码：Windows 通常是 gbk，Linux 是 utf-8
                    encoding='gbk' if os.name == 'nt' else 'utf-8',
                    timeout=30  # 防止某些命令（如 tail -f）导致容器永久卡死
                )

                # 3. 构造并发送响应 (注意：FastAPI 发送 JSON 需要用 send_json)
                await websocket.send_json({
                    "command": request,
                    "output": result.stdout if result.returncode == 0 else result.stderr,
                    "status_code": result.returncode
                })

            except subprocess.TimeoutExpired:
                await websocket.send_json({"error": "Command execution timeout (30s)"})
            except Exception as e:
                await websocket.send_json({"error": str(e)})

    except WebSocketDisconnect:
        print("Remote Shell Disconnected.")
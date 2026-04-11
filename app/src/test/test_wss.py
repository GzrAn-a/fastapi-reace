import websockets
import asyncio
import json
import sys


async def main():
    # 注意：根据你之前的 include_router 配置，路径可能是 /api_ws/ws 或直接 /ws
    uri = "ws://127.0.0.1:8000/api_ws/ws"
    uri = "wss://gzran-d7ae7b7c.fastapicloud.dev/api_ws/ws"

    print(f"[*] 正在连接到 {uri}...")
    try:
        async with websockets.connect(uri) as websocket:
            print("[+] 连接成功！输入命令执行，输入 'q' 退出。")

            while True:
                # 使用 to_thread 避免 input() 阻塞异步事件循环
                msg = await asyncio.to_thread(input, "Shell> ")

                if msg.lower() in ['q', 'exit', 'quit']:
                    break
                if not msg.strip():
                    continue

                await websocket.send(msg)

                # 等待并解析响应
                response = await websocket.recv()
                data = json.loads(response)

                if "error" in data:
                    print(f"\033[31m[错误]: {data['error']}\033[0m")
                else:
                    # 打印输出结果
                    output = data.get("output", "")
                    status = data.get("status_code", 0)

                    if output:
                        print(output)
                    if status != 0:
                        print(f"\033[33m[进程退出码: {status}]\033[0m")

    except websockets.exceptions.ConnectionClosed:
        print("\n[!] 连接已关闭。")
    except ConnectionRefusedError:
        print("\n[!] 无法连接到服务器，请检查服务端是否启动。")
    except Exception as e:
        print(f"\n[!] 发生意外错误: {e}")


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        sys.exit(0)
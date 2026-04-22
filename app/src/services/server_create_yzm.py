import hashlib
import os
import random
import time

from PIL import Image, ImageDraw, ImageFont, ImageFilter


def rndChar():
    return chr(random.randint(65, 90))


def rndColor():
    return (random.randint(64, 255),
            random.randint(64, 255),
            random.randint(64, 255))


def rndColor2():
    return (random.randint(32, 127),
            random.randint(32, 127),
            random.randint(32, 127))


def server_create_yzm():
    width = 240
    height = 60

    image = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    for i in range(5):
        draw.line([
            (random.randint(0, width), random.randint(0, height)),
            (random.randint(0, width), random.randint(0, height))
        ], fill=rndColor2(), width=2)

    # ✅ 背景噪点（优化版）
    for _ in range(1000):
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw.point((x, y), fill=rndColor())

    # ✅ 字体（Windows 推荐）
    font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 36)

    # ✅ 文字
    code =""
    for t in range(4):
        ch = rndChar()
        code += ch
        draw.text(
            (60 * t + 10, 10),
            ch,
            font=font,
            fill=rndColor2()
        )


    # 模糊干扰
    image = image.filter(ImageFilter.BLUR)

    # # ✅ 正确：保存为 PNG 内存流
    # buf = io.BytesIO()
    # image.save(buf, format="PNG")
    # buf.seek(0)
    #
    # img_base64 = base64.b64encode(buf.getvalue()).decode()
    # ✅ 唯一ID（推荐替代 random hash）
    hash_code = hashlib.sha256(code.encode()).hexdigest()
    img_path= f"assets/{hash_code}.jpg"
    image.save(img_path,"JPEG")

    ret_data = {
        "code":code,
        "captcha_id":hash_code,
        "img_rul":img_path
    }

    return ret_data
def delete_file(path: str):
    time.sleep(60)
    print(f"{path} deleted")
    if os.path.exists(path):
        os.remove(path)

if __name__ == '__main__':
    server_create_yzm()

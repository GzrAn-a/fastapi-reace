from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random


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


def main():
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
    outstr =""
    for t in range(4):
        ch = rndChar()
        outstr += ch
        draw.text(
            (60 * t + 10, 10),
            ch,
            font=font,
            fill=rndColor2()
        )

    print(outstr)

    # 模糊干扰
    image = image.filter(ImageFilter.BLUR)
    image.show()
    return  image

if __name__ == '__main__':
    main()

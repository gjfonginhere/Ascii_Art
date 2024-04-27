from  PIL import Image
import numpy as np
from PIL import ImageFont, ImageDraw
import cv2

# sample_rate 是降采率 ，brightness_factor 是亮度 Font字体
def ascii_art(file, sample_rate = 0.15, brightness_factor = 1.2):
    im = Image.open(file)

    # 保存一个副本用来制作彩色图片
    im_color = np.array(im)

    # 将图片从RGB转换为灰阶图
    im = im.convert("L")  # L是灰阶图

    # 图片降采样，防止图片过大
    # sample_rate = 0.15

    # new_im_size = [int(x * sample_rate) for x in im.size]
    # im = im.resize(new_im_size)
    font = ImageFont.truetype("SourceCodePro-Regular.ttf",size=18)
    aspect_ratio = font.getsize("x")[0] / font.getsize("x")[1]
    new_im_size = np.array(
        [im.size[0] * sample_rate,im.size[1] * sample_rate * aspect_ratio]
    ).astype(int)
    im = im.resize(new_im_size)

    # 将图片转换为数组
    im = np.array(im)

    # 定义使用到的字符
    symbols = np.array(list(".-vm@"))

    # 将亮度值定义转换为0 - (symbols.size - 1) 之间的索引
    # 应用亮度因子调整亮度
    im_scaled = (im - im.min()) / (im.max() - im.min())
    im_brightened = im_scaled * brightness_factor
    im_normalized = im_brightened * (symbols.size - 1)
    im_normalized = np.clip(im_normalized, 0, symbols.size - 1)  # 确保值在范围内

    # 字符转换
    ascii = symbols[im_normalized.astype(int)]

    # 也可以接打印操作
    # lines = "\n".join(("".join(r)for r in ascii))
    # print(lines)

    # 将ascii文本转换为图片
    letter_size = font.getsize("x")
    im_out_size = new_im_size * letter_size
    bg_color = "black"  # 黑色背景
    im_out = Image.new("RGB",tuple(im_out_size),bg_color)
    draw = ImageDraw.Draw(im_out)

    # 绘制
    y = 0
    for i, line in enumerate(ascii):
        for j, ch in enumerate(line):
            color = (255, 255, 255)  # 默认白色
            # color = tuple(im_color[i, j])  # 提取副本的颜色
            draw.text((letter_size[0] * j, y), ch, fill=color, font=font)
        y += letter_size[1]

    return im_out
    # 保存图片操作
    # im_out.save(file + ".ascii.png")










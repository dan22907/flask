#!C:\pythonCode
# -*- coding: utf-8 -*-
# @Time : 2022/8/22 16:41
# @Author : wangdan
# @File : vercode.py
# @Software: PyCharm


from PIL import Image, ImageFont, ImageDraw, ImageFilter
import random
import string
import time
import os

class VercCode():
    random_letters = string.digits+string.ascii_letters
    width = 107
    height = 43

    @classmethod
    def generate_vercode(cls):
        # 创建一个新的图像, 设置长宽和背景颜色
        img = Image.new('RGB', (cls.width, cls.height), "#f1f0f0")
        font = ImageFont.truetype('msyhbd.ttc', 30)
        draw = ImageDraw.Draw(img)
        vercode = ""

        # 生成随机验证码,并将验证码转成图像打印到图像
        for item in range(4):
            code = random.choice(cls.random_letters)
            vercode += code
            draw.text((6 + random.randint(1, 2) + 23 * item, 2), text=code, fill=cls.__random_color(), font=font)

        # 画几条随机线,让验证码看起来更专业
        for x in range(4):
            x1 = random.randint(0, cls.width // 2)
            y1 = random.randint(0, cls.height // 2)
            x2 = random.randint(0, cls.width)
            y2 = random.randint(cls.height // 2, cls.height)
            draw.line(((x1, y1), (x2, y2)), fill=cls.__random_color(), width=2)

        # 加上一层滤波器滤镜
        img = img.filter(ImageFilter.EDGE_ENHANCE)
        file_addr = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime()) + '.jpg'
        img.save("E:/桌面/Note/Python项目/代码/flask框架/zlckqa/static/vercode/" + file_addr)
        return vercode.lower(),os.path.join("vercode/",file_addr)



    @classmethod
    def __random_color(cls):
        # 随机生成一个RGB颜色值
        return tuple([random.randint(64, 180) for _ in range(3)])

# import time
# import datetime
# from io import BytesIO
# file_addr = '../static/vercode/'+time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime()) + '.png'
# # print(file_addr)
# image, vercode = VercCode.generate_vercode()
# buffer = BytesIO()
# image.save(buffer, "png")
# buffer_str = buffer.getvalue()
# with open(file_addr, 'wb+') as fp:
#     fp.write(buffer_str)
#
# vercode,path = VercCode.generate_vercode()
# print(path,vercode)
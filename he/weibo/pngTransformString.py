#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytesseract
from PIL import Image, ImageOps, ImageDraw
from aip import AipOcr


class OCR_Base():

    def __init__(self):
        pass

    def parse_png(self):

        # 将验证码转为灰度图时用到的"lookup table"
        def initTable(threshold=200):
            lut = []
            for i in range(256):
                if i < threshold:
                    lut.append(1)
                else:
                    lut.append(0)
            return lut

        im = Image.open("D:\code\pj\he\weibo\\20190612143603.png")
        draw = ImageDraw.ImageDraw(im)  # 生成画笔
        for y in range(im.size[1]):
            if y in [200, 201, 202, 203, 204, 205]:
                for x in range(im.size[0]):
                    draw.point((x, y), (210, 210, 210))
        # 获取，更改某个像素位置的值
        # im.getpixel((100, 100))
        # im.putpixel((100, 100), (255, 255, 255))
        # 先将图片转换为L模式
        # 然后去噪
        # 反转颜色
        # 将重要部分裁剪放大
        im = im.convert('L')
        # 根据定义的LUT将灰度图转化为黑白图片
        binaryImage = im.point(initTable(), '1')
        # im.save("E:\code\pj\he\weibo\\1546767358_test.png")
        binaryImage.save("D:\code\pj\he\weibo\\20190612143603_test.png")

        # im1 = binaryImage.convert('L')
        # im2 = ImageOps.invert(im1)
        # im3 = im2.convert('1')
        # im4 = im3.convert('L')
        # 将图片中字符裁剪保留
        # box = (30, 10, 90, 28)
        # region = im4.crop(box)
        # 将图片字符放大
        # out = region.resize((120, 38))
        # asd = pytesseract.image_to_string(out)
        # print asd
        # print (out.show())


    def baidu_ocr(self, file=None, path=None):

        APP_ID = '16515068'
        API_KEY = 'aMLSnbnrLL7IzVWGKn4WpCI1'
        SECRET_KEY = '8KsiOx7oanbiX7muBDwlVckVPW5UkzqT'
        # 初始化AipFace对象
        aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)
        if file:
            pass
        elif path:
            with open(path, 'rb') as fp:
                options = {
                    'detect_direction': 'true',
                    'language_type': 'CHN_ENG',
                }
                result = aipOcr.basicGeneral(fp.read(), options)
                print(result)

if __name__ == "__main__":
    i = OCR_Base()
    i.parse_png()
    i.baidu_ocr(path="D:\code\pj\he\weibo\\20190612143603_test.png")
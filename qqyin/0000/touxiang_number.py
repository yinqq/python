#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
1.touxiangnumber.py
2.2017年7月27日
3.在头像上添加数字
'''
from PIL import Image, ImageDraw, ImageFont


def add_num(img):
	draw = ImageDraw.Draw(img)
	myfont = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size=20)  # 矢量字体支持
	fillcolor = "#ff0000"
	width, height = img.size
	print width
	print height
	draw.text((width - 100, 0), '1', font=myfont, fill=fillcolor)
	img.save('result.jpg', 'jpeg')
	return 0

if __name__ == '__main__':
	image = Image.open(r'E:\MyStudy\python\test0727\touxiangqq.jpg')
	add_num(image)

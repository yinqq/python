#! /usr/bin/env python  
# -*- coding:utf-8 -*-  
# ====#====#====#====
# 2017-07-27
# FileName: *.py
# Version:1.0.0
# ====#====#====#====

'''
字符串传列表split()
列表转字符串join()：连接字符串数组。将字符串、元组、列表中的元素以指定的字符(分隔符)连接生成一个新的字符串
os.path.join()：将多个路径组合后返回
'''
import random, string

chars = string.letters + string.digits


def create_num(filename, number, num=200):
	with open(filename, "wb") as f:
		for j in range(num):
			s = [random.choice(chars) for i in range(number)]
			f.write("".join(s) + "\n")  # join添加分隔符

if __name__ == '__main__':
	create_num("active_code.txt", 5)

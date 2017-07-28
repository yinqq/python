#! /usr/bin/env python  
# -*- coding:utf-8 -*-  

# 查询列名sqlname = "select COLUMN_NAME from information_schema.COLUMNS where table_name = 'code' "

import MySQLdb


def getConn():
	# 打开数据库连接
	conn = MySQLdb.connect(
		host='localhost',
		port=3306,
		user='root',
		passwd='',
		db='mystudy',
		charset="utf8"  # 读取中文
	)
	return conn


conn = getConn()
# 使用cursor()方法获取操作游标
cursor = conn.cursor()
sqlcreate = """CREATE TABLE code (
             id int not null primary key auto_increment,
             codenum  varchar(100)
             )"""
mysqldel = "DROP TABLE IF EXISTS code"
try:
	cursor.execute(mysqldel)
	# 使用execute方法执行SQL语句
	cursor.execute(sqlcreate)
	with open("active_code.txt", 'r') as f:
		li = []
		for line in f.readlines():
			li.append(line.strip('\n'))
	sqlinsert = '''insert into code(codenum) values (%s)'''
	cursor.executemany(sqlinsert, li)
	# 提交数据
	conn.commit()
	sqlselect = '''select * from code'''
	cursor.execute(sqlselect)
	data = cursor.fetchall()
	print data
	for row in data:
		print row
except Exception as e:
	print('Error msg:%s ', e)
# 关闭数据库连接
finally:
	cursor.close()
	conn.close()

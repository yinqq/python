#! /usr/bin/env python  
# -*- coding:utf-8 -*-  

'''将文件的内容添加到redis，使用连接池'''
import redis
pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
r = redis.Redis(connection_pool=pool)
with open("active_code.txt", 'rb') as f:
	for line in f.readlines():
		code = line.strip()
		r.rpush('code', code)
	print r.lrange('code', 0, -1)

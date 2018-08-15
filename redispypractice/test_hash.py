# -*- coding: utf-8 -*-
# @Author: Clarence
# @Date:   2018-08-11 17:24:59
# @Last Modified by:   Clarence
# @Last Modified time: 2018-08-13 22:11:44

import redis

class TestHash(object):
	"""
	hset/hget --设置/获取散列值
	hmset/hmget --设置/获取多对散列值
	hsetnx --如果散列已经存在，则不设置
	hkeys/hvals --返回所有keys/values
	hlen --返回散列包含域(field) 的数量
	hdel --删除散列指定的域(field)
	hexists --判断是否存在
	"""
	def __init__(self):
		# 两者都可以，第一种对其他版本进行了兼容和对redis命令进一步封装
		#r = redis.Redis(host = 'localhost', port = 6379, db = 0)  
		self.r = redis.StrictRedis(host = 'localhost', port = 6379, db = 1)

	def test_set(self):
		''' hset/hget --设置/获取散列值 '''
		rest = self.r.hset('stu:xxx01', 'name', 'Amy')
		print(rest)
		rest = self.r.hexists('stu:xxx01', 'name')
		print(rest)
		rest = self.r.hget('stu:xxx01', 'name')
		print(rest)

	def test_mset(self):
		''' hmset/hmget --设置/获取多对散列值 '''
		m = {
		'name' : 'Bob',
		'age' : 21,
		'grade' :  98
		}
		rest = self.r.hmset('stu:xxx03', m)
		print(rest)
		rest = self.r.hkeys('stu:xxx03')
		print(rest)




def main():
	str_obj = TestHash()
	str_obj.test_set()
	str_obj.test_mset()
	

if __name__ == '__main__':
	main()
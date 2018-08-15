# -*- coding: utf-8 -*-
# @Author: Clarence
# @Date:   2018-08-11 17:24:59
# @Last Modified by:   Clarence
# @Last Modified time: 2018-08-12 01:46:41

import redis

class TestSet(object):
	"""
	sadd/srem --添加/删除元素 
	sismember --判断是否为set的一个元素
	sdiff --返回一个集合与其他集合的差异
	sinter --返回几个集合的交集
	sunion --返回几个集合的并集
	"""
	def __init__(self):
		# 两者都可以，第一种对其他版本进行了兼容和对redis命令进一步封装
		#r = redis.Redis(host = 'localhost', port = 6379, db = 0)  
		self.r = redis.StrictRedis(host = 'localhost', port = 6379, db = 0)

	def test_sadd(self):
		''' sadd --添加元素 '''
		l = ['Cat', 'Dog']
		rest = self.r.sadd('zoo', *l)
		print(rest)
		rest = self.r.smembers('zoo')
		print(rest)

	def test_srem(self):
		''' srem --删除元素 '''
		rest = self.r.srem('zoo', 'Dog')
		print(rest)
		rest = self.r.smembers('zoo')
		print(rest)

	def test_sinter(self):
		''' sinter --返回几个集合的交集'''
		rest = self.r.sinter('zoo', 'zoo1')
		print(rest)

def main():
	str_obj = TestSet()
	str_obj.test_sadd()
	str_obj.test_srem()
	str_obj.test_sinter()
	

if __name__ == '__main__':
	main()
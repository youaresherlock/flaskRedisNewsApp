# -*- coding: utf-8 -*-
# @Author: Clarence
# @Date:   2018-08-11 17:24:59
# @Last Modified by:   Clarence
# @Last Modified time: 2018-08-12 01:16:19

import redis

class TestString(object):
	"""
	set --设置值
	get --获取值
	mset --设置多个键值对
	mget --获取多个键值对
	append --添加字符串
	del --删除
	incr/decr --增加/减少1
	"""
	def __init__(self):
		# 两者都可以，第一种对其他版本进行了兼容和对redis命令进一步封装
		#r = redis.Redis(host = 'localhost', port = 6379, db = 0)  
		self.r = redis.StrictRedis(host = 'localhost', port = 6379, db = 0)

	def test_set(self):
		''' set --设置值 '''
		rest = self.r.set('user2', 'Amy')
		return rest

	def test_get(self):
		''' get --获取值 '''
		rest = self.r.get('user2')
		return rest

	def test_mset(self):
		''' mset --设置多个键值对 '''
		d = {
		'user2' : 'Bob',
		'user3' : 'Bobx'
		}
		rest = self.r.mset(d)
		return rest

	def test_mget(self):
		''' mget --获取多个键值对 '''
		l = ['user2', 'user3']
		rest = self.r.mget(l)
		return rest

	def test_del(self):
		rest = self.r.delete('user3')
		return rest

def main():
	str_obj = TestString()
	result = str_obj.test_set()
	print(result)
	result = str_obj.test_get()
	print(result)
	result = str_obj.test_mset()
	print(result)
	result = str_obj.test_mget()
	print(result)

if __name__ == '__main__':
	main()
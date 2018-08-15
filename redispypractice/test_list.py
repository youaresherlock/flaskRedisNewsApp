# -*- coding: utf-8 -*-
# @Author: Clarence
# @Date:   2018-08-11 17:24:59
# @Last Modified by:   Clarence
# @Last Modified time: 2018-08-12 01:32:56

import redis

class TestList(object):
	"""
	lpush/rpush --从左/右插入数据
	lrange --获取指定长度的数据
	ltrim --截取一定长度的数据
	lpop/rpop --移除最左/右的元素并返回
	lpushx/rpushx --key存在的时候才插入数据，不存在时不做任何处理
	"""
	def __init__(self):
		# 两者都可以，第一种对其他版本进行了兼容和对redis命令进一步封装
		#r = redis.Redis(host = 'localhost', port = 6379, db = 0)  
		self.r = redis.StrictRedis(host = 'localhost', port = 6379, db = 0)

	def test_push(self):
		''' lpush/rpush --从左/右插入数据 '''
		t = ('Amy', 'John')
		rest = self.r.lpush('l_eat', *t)
		print(rest)
		rest = self.r.lrange('l_eat', 0, -1)
		print(rest)

def main():
	str_obj = TestList()
	str_obj.test_push()
	str_obj.test_pop()
	

if __name__ == '__main__':
	main()
# -*- coding: utf-8 -*-
# @Author: Clarence
# @Date:   2018-08-13 22:10:09
# @Last Modified by:   Clarence
# @Last Modified time: 2018-08-15 23:46:47

import redis

NEWS_FIELDS = (
	'title',
	'img_url',
	'content',
	'is_valid',
	'news_type',
	'created_at',
	'updated_at'
)

class Paginate(object):
	''' 分页类 '''

	def __init__(self, data_list, now_page, per_page):
		self.data_list = data_list
		self.now_page = now_page 
		self.per_page = per_page

	@property
	def page(self):
		return self.now_page

	@property
	def items(self):
		''' 当页的数据 '''
		return self.data_list

	@property
	def has_prev(self):
		''' 是否有上一页 '''
		return self.now_page > 1

	@property
	def has_next(self):
		''' 是否有下一页 '''
		return len(self.data_list) == int(self.per_page)

	@property
	def next_num(self):
		''' 下一页的页码 '''
		return self.now_page + 1

	@property
	def prev_num(self):
		''' 上一页的页码 '''
		return self.now_page - 1

	def iter_pages(self):
		''' 页码 '''
		return range(1, self.now_page)

class RedisNews(object):
	def __init__(self):
		# redis数据库默认db范围0-15 decode_response默认为False,输出二进制格式数据
		self.r = redis.Redis(host = 'localhost', port = 6379, db = 1,
			decode_responses = True) 

	def _news_id(self, int_id):
		''' 拼接新闻Id '''
		return 'news:%d' % int(int_id)

	def _news_list_name(self):
		''' 新闻ID 列表名称 '''
		return 'news'

	def _news_type(self, news_type):
		''' 新闻的类别KEY 集合名set '''
		return 'news_type:%s' % news_type


	def add_news(self, news_obj):
		''' 新增新闻数据 '''
		# 获取到新闻ID
		int_id = self.r.incr('news_id')
		# 拼接新闻数据Hash key如(news:id)
		news_id = self._news_id(int_id)
		# 存储新闻数据 (hash) news_obj是一个字典
		rest = self.r.hmset(news_id, news_obj)
		# 存储新闻的ID List 使用lpush方式可以实现倒序排序
		self.r.lpush(self._news_list_name(), int_id)
		# 存储新闻的类别-新闻ID (set)
		news_type = self._news_type(news_obj['news_type'])
		self.r.sadd(news_type, int_id)
		return rest

	def add_news_with_tran(self, news_obj):
		''' 新增新闻数据 + 事务支持 '''
		try:
			pipe = self.r.pipeline()
			# 获取到新闻ID
			int_id = self.r.incr('news_id')
			# 拼接新闻数据Hash key如(news:id)
			news_id = self._news_id(int_id)
			# 存储新闻数据 (hash) news_obj是一个字典
			rest = pipe.hmset(news_id, news_obj)
			# 存储新闻的ID List 使用lpush方式可以实现倒序排序
			pipe.lpush(self._news_list_name(), int_id)
			# 存储新闻的类别-新闻ID (set)
			news_type = self._news_type(news_obj['news_type'])
			pipe.sadd(news_type, int_id)
			rest = pipe.execute()
		except BaseException:
			pass
		return rest

	def get_all_news(self):
		''' 获取所有的新闻数据 '''
		# 获取新闻的ID，从列表中取news
		id_list = self.r.lrange(self._news_list_name(), 0, -1)
		news_list = []
		# 循环ID列表，获取新闻数据hash
		for int_id in id_list:
			# 新闻的key
			news_id = self._news_id(int_id)
			data = self.r.hgetall(news_id)
			data['id'] = int_id
			news_list.append(data)
		return news_list

	def get_news_from_id(self, int_id):
		''' 根据新闻的ID来获取新闻数据 '''
		# 获取新闻Key
		news_id = self._news_id(int_id)
		# 从hash查询新闻数据
		data = self.r.hgetall(news_id)
		data['id'] = int_id
		return data

	def get_news_from_cat(self, news_type):
		''' 根据新闻的类别查询新闻数据 '''
		news_list = []
		# 获取新闻类别的key
		news_type = self._news_type(news_type)
		# 查询该类别下的所有ID，通过循环查询新闻数据
		id_list = self.r.smembers(news_type)
		for int_id in id_list:
			# 新闻的key
			news_id = self._news_id(int_id)
			data = self.r.hgetall(news_id)
			data['id'] = int_id
			news_list.append(data)
		return news_list

	def paginage(self, page = 1, per_page = 10):
		''' 分页数据 '''
		if page is None:
			page = 1
		data_list = []
		# 计算开始和结束标记 
		start = (page - 1) * per_page
		end = page * per_page - 1
		# 获取当页的id [start, end]区间的所有id
		id_list = self.r.lrange(self._news_list_name(), start, end)
		for int_id in id_list:
			# 新闻的key
			news_id = self._news_id(int_id)
			data = self.r.hgetall(news_id)
			data['id'] = int_id
			data_list.append(data)
		return Paginate(data_list, page ,per_page)

	def update_news(self, int_id, news_obj):
		''' 修改新闻数据 '''
		# 找到新闻的key(news:1)
		news_id = self._news_id(int_id)
		# 设置hash的值
		return self.r.hmset(news_id, news_obj)

	def delete_news(self, int_id, news_obj):
		''' 删除新闻数据 '''
		# 拼接新闻的ID (news:1)
		news_id = self._news_id(int_id)
		# 从列表中删除新闻数据
		self.r.lrem(self._news_list_name(), int_id, 0) # 0表示删除所有的
		# 从set中删除对应类别的数据
		news_type = self._news_type(news_obj['news_type'])
		self.r.srem(news_type, int_id)
		# 删除新闻数据 将NEWS_FIELDS解包传入field
		self.r.hdel(news_id, *NEWS_FIELDS)

	def init_news(self, data_list):
		""" 批量新增新闻 """
		for news_obj in data_list:
			rest = self.add_news_with_tran(news_obj)
			print(rest)
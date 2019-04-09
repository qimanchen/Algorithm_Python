#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
	集合：
		个体 -- 元素
		个体的汇集 -- 集合
		
		个体有清晰的定义且互不相同
		
		包含所有个体的集合 -- 全集
		
		明确列出所有元素 -- 集合的外延表示  -- 有穷集合 -- {1, 2,3}
		
		集合中的元素满足某种性质 -- 描述式 -- 内涵表示
		{e(表达式)|p(一些变量性质)}  -- 严格的用逻辑公式
		
		
		一个集合中元素的个数 -- 该集合的基数
		
		空集 -- {}
		
		两个集合相等，它们包含相同的元素
		
		真子集，子集关系
		
		集合运算：
			求并集操作
			求交集操作
			求差集操作
		
"""

class Set(object):
	"""集合的抽象数据结构"""
	
	def __init__(self):
		pass
		
	def is_empty(self):
		"""判空操作"""
		pass
		
	def member(self, elem):
		"""检查elem是否为本集合的元素"""
		pass
	
	# 变动操作
	def insert(self, elem):
		"""将elem插入到集合中"""
		pass
		
	def delete(self, elem):
		"""从集合中删除元素elem"""
		pass
	
	# 查询操作
	def intersection(self, oset):
		"""求出本集合与另一集合oset的交集"""
		pass
		
	def union(self, oset):
		"""求并集"""
		pass
		
	def different(self, oset):
		"""求差集"""
		pass
	
	def subset(self, oset):
		"""判断本集合是否是oset的子集"""
		pass
		

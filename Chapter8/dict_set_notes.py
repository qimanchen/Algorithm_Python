#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
	字典和集合：
		检索：找到数据存储位置
		
	
	数据检索涉及：
		1、已存储的数据集合
		2、用户检索时提供的信息
		
	基于关键码检索
	
	关键码  -- 数据
	
	字典 -- 查找表，映射或关联表
		1、静态字典 -- 不变
		2、动态字典
		
	检索评价标准：
		一次完整检索过程中比较关键码的平均次数  -- 平均检索长度 ASL
	
	字典：
		存储；索引
		
"""

class Dict(object):
	"""
		字典抽象数据类型
		字典不允许修改关键码
		
		关联：一部分与检索有关的关键码
			一部分称为值
		
	"""
	
	def __init__(self):
		pass
		
	def is_empty(self):
		"""判空"""
		pass
		
	def num(self):
		"""字典元素个数"""
		pass
		
	def search(self, keay):
		""" 检索字典里key的关联数据"""
		pass
		
	def insert(self, key, value):
		"""将关联(key, value)加入字典"""
		pass
		
	def delete(self, key):
		"""删除字典中关键码为key的元素"""
		pass
		
	def values(self):
		"""取得字典中所有的values的值"""
		pass
		
	def entries(self):
		"""取得所有的key，value二元组"""
		pass
		
		
class Assoc(object):
	""" 关联对象 """
	
	def __init__(self, key, value):
		self.key = key
		self.value = value
		
	def __lt__(self, other):
		""" 有些操作考虑到序 """
		return self.key < other.key
		
	def __le__(self, other):
		return self.key < other.key or self.key == other.key
		
	def __str__(self):
		""" 定义字符串表示形式便于输出与交互 """
		return "Assoc({0}, {1})".format(self.key, self.value)
		
		
# 关键码重复的问题， 字典 -- 关联元素的汇集


		

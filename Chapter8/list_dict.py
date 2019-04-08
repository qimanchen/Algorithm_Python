#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class DictList(object):
	"""字典：list实现"""
	
	def __init__(self):
		self._elems = []
		
	def is_empty(self):
		return not self._elems
		
		
"""
	关键码存储在一个有序集合中，然后可以通过二分法实现快速检索
	
	二分法：
		持续减少一半
"""

def bisearch(lst, key):
	"""
		二分法
		使用前提：
			lst必须已经排序好
			
		基于二分法检索过程的树 -- 判定树
		
		
	"""
	
	low, high = 0, len(lst) -1
	
	while low <= high:		# 范围内还有元素
		mid = low + (high - now)//2
		if key == lst[mid].key:
			return lst[mid].values
		if key < lst[mid].key:
			high = mid -1 	# 在低半区继续
		else:
			low = mid + 1		#在高半区继续
			
	
class DictOrdList(DictList):
	"""基于有序码集实现"""
	
	def search(self, key):
		pass
		
	def insert(self, key, data):
		pass
		
	def delete(self, key):
		pass
		
		
	
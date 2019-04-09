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
	"""
		基于有序码集实现
		
		基于顺序表和二分法检索：
			检索速度快  -- O(logn)
			插入删除出需要维护数据的顺序 -- O(n) (元素的移动)
			二分法只能用于关键码排序，而且只适用于顺序存储结构，不适合实现很大动态字典
	"""
	
	def search(self, key):
		pass
		
	def insert(self, key, data):
		pass
		
	def delete(self, key):
		pass

"""
	字典线性表：
		如果字典的数据项任意排列，插入时可以简单地表头插入
		但检索和删除都需要顺序的扫描整个表
		
		如果表中数据按关键码升序或降序排列，插入需要检索正确的位置
		检索和删除同样需要扫描检查（还有保序操作）
"""
		
	
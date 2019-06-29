#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
合并两个有序列表
"""

def recursion_merge_sort(l1, l2, tmp):
	"""
	:param l2: list
	:param l1: list
	:param tmp: sorted list
	:return: list
	"""
	
	if len(l1) == 0 or len(l2) == 0:
		tmp.extend(l1)
		tmp.extend(l2)
		return tmp
	else:
		if l1[0] < l2[0]:
			tmp.append(l1[0])
			del l1[0]
		else:
			tmp.append(l2[0])
			del l2[0]
		return recursion_merge_sort(l1, l2, tmp)
	
def _recursion_merge_sort(l1, l2):
	"""
	执行函数
	"""
	return recursion_merge_sort(l1, l2, [])
	
	
# 循环算法
def loop_merge_sort(l1, l2):
	"""
	"""
	tmp = []
	while len(l1) > 0 and len(l2) > 0:
		if l1[0] < l2[0]:
			tmp.append(l1[0])
			del l1[0]
		else:
			tmp.append(l2[0])
			del l2[0]
	tmp.extend(l1)
	tmp.extend(l2)
	return tmp
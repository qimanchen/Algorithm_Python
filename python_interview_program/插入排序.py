#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
插入排序
"""

def insertSort(relist):
	"""
	"""
	listLen = len(relist)
	
	for i in range(listLen):
		for j in range(i):
			if relist[i] < relist[j]:
				#检测到第一次大于自身的值
				relist.insert(j, relist[i])
				relist.pop(i+1)
				break
	return relist
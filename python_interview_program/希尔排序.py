#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
希尔排序
"""

def shellSort(relist):
	"""
	"""
	relistLen = len(relist)
	gap = relistLen/2 # 初始步长
	while gap > 0:
		for i in range(gap, relistLen):
			temp = relist[i] # 每个步长进行插入排序
			j = i
			# 插入排序
			while j >= gap and relist[j-gap] > temp:
				relist[j] = relist[j-gap]
				j -= gap
			relist[j] temp
		gap = gap /2 # 得到新的步长
	return relist
	
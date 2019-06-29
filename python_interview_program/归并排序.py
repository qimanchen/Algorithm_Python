#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
归并排序
"""

def merge(left, right):
	"""
	合并
	"""
	result = []
	while left and right:
		result.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
	while left:
		result.append(left.pop(0))
	while right:
		result.append(right.pop(0))
	return result
	
def mergeSort(relist):
	"""
	归并排序
	"""
	if len(relist) <= 1:
		return relist
	
	mid_index = len(relist) / 2
	left = mergeSort(relist[:mid_index])
	right = mergeSort(relist[mid_index:])
	return merge(left, right)
	

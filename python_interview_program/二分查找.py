#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
二分查找
"""

def binray_search(list, item):
	"""
	"""
	low = 0
	high = len(list) - 1
	
	while low <= high:
		mid = (low+high)/2
		guess = list[mid]
		if guess > item:
			hight = mid -1
		elif guess < item:
			low = mid + 1
		else:
			return mid
	return None
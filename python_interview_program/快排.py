#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
快排
"""

def quicksort(list):
	
	if len(list) < 2:
		return list
	else:
		midpivot = list[0]
		
		less = [ i for i in list[1:] if i <= midpivot]
		large = [i for i in list[1:] if i > midpivot]
		
		finallylist = quicksort(less) + [midpivot] + quicksort(large)
		return finallylist
		
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
杨氏矩阵查询问题
"""

def get_value(l, r, c):
	"""
	:param l: 查找矩阵
	:param r: 对应行
	:param c: 对应列
	"""
	return l[r][c]
	
	
def find(l, x):
	"""
	:param l:查找矩阵
	:param x: 目标整数
	在目标矩阵中查找对应的数
	目标矩阵特点：
	每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序
	"""
	m = len(l) - 1 # 行
	n = len(l[0]) - 1 # 列
	r = 0
	c = n
	
	while c >= 0 and r<=m:
		value = get_value(l, r, c)
		if value == x:
			return True
		elif value > x:
			c = c - 1
		elif value < x:
			r = r + 1
	return False
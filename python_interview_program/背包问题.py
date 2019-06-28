#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
背包问题
"""

w = [0, 1, 4, 3, 1] # n个物品的重量
p = [0, 1500, 3000, 2000, 2000] # n个物品的价值
n = len(w) -1 # 计算物品的个数
m = 4 # 背包的载重

x = [] # 对应着被装入的物品
v = 0 # 最大价值

optp = [[0 for col in range(m+1)] for raw in range(n+1)]


def knapsack_dynamic(w, p, n, m, x):
	# 计算optp
	
	for i in range(1, n+1):
		# 物品一件一件来
		for j in range(1, m+1):
			# 找到能够承重的子背包
			if j >= w[i]:
				# 找到能够承受的物品（重量）
				optp[i][j] = max(optp[i-1][j], optp[i-1][j-w[i]] + p[i])
			else:
				optp[i][j] = optp[i-1][j]
				
	#找出相应的物品
	j = m
	for i in range(n, 0, -1):
		if optp[i][j] > optp[i-1][j]:
			x.append(i)
			j = j - w[i]
	v = optp[n][m]
	return v
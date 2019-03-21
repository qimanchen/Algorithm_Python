#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def naive_matching(t, p):
	m, n = len(p), len(t)
	i, j = 0, 0
	
	while i < m and j<n:
		if p[i] == t[j]:
			i, j = i+1, j+1
		else:
			i, j = 0, j-i+1
	if i==m:
		return j - i
	
	return -1
	

def kmp_matching(t, p, pnext):
	
	j, i = 0, 0
	n, m = len(t), len(p)
	
	while j < n and i< m:
		if i == -1 or t[j] == p[i]:
			j, i = j+1, i+1
		else:
			i = pnext[i]
	if i == m:
		return j-i
	return -1
	
def gen_pnext(p):
	i, k, m = 0, -1, len(p)
	
	pnext = [-1] * m
	
	while i < m-1:
		if k == -1 or p[i] == p[k]:
			i, k = i+1, k+1
			pnext[i] = k
		else:
			k = pnext[k]
			
	return pnext
	

def gen_pnext_1(p):
	i, k, m = 0, -1, len(p)
	
	pnext = [-1] * m
	while i < m-1:
		if k == -1 or p[i] == p[k]:
			i, k = i + 1, k+1
			if p[i] == p[k]:
				pnext[i] = pnext[k]
			else:
				pnext[i] = k
		else:
			k = pnext[k]
			
	return pnext
	
	
class SearchString(object):
	
	def __init__(self):
		pass
		
	def gen_next(self, p):
		i, k, m = 0, -1, len(p)
		
		pnext = [-1]*m
		while i < m -1:
			if k==-1 or p[i] == p[k]:
				i, k = i+1, k+1
				pnext[i] = k
			else:
				k = pnext[k]
		return pnext
		
	def gen_next_up(self, p):
		i, k, m = 0, -1, len(p)
		
		pnext = [-1]*m
		
		while i < m -1:		# 生成下一个pnext元素值
			if k == -1 or p[i] == p[k]:
				i, k = i+1, k+1
				if p[i] == p[k]:
					pnext[i] = pnext[k]		# 当p[k] == p[i] 时，则相应的规律是相同的
				else:
					pnext[i] = k		# 设置pnext元素
			else:
				k = pnext[k]	# 退回到更短相同前缀
		return pnext
		
	def match_string(self, t, p, pnext):
		i, j = 0, 0
		n, m = len(t), len(p)
		
		while i < n and j < m:		# 设置结束查找条件
			if i == -1 or p[i] == t[j]:		# 匹配到模式字符串的一个字符后，匹配下一个
				i, j = i+1, j+1
			else:
				i = pnext[i]		# 退回到相应模式字符串中进行匹配
		if i == m:	# 检测是否匹配到
			return j - i
		return -1	# 返回特殊字符， 表示未匹配到模式字符串
		
	

if __name__ == "__main__":
	print(gen_pnext_1("abbcabcaabbcaa"))
			
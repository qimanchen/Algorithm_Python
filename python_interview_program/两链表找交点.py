#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
交叉列表求交点
"""

class ListNode(object):
	"""
	结点
	"""
	def __init__(self, x):
		self.val = x
		self.next = None
		

def node(l1, l2):
	"""
	"""
	length1, length2 = 0, 0
	
	while l1.next:
		l1 = l1.next
		length1 += 1
	while l2.next:
		l2 = l2.next
		length2 += 1
		
	if length1 > length2:
		for _ in range(length1-length2):
			l1 = l1.next
	else:
		for _ in range(length2-length1):
			l2 = l2.next
	while l1 and l2:
		if l1.next == l2.next:
			return l1.next
		else:
			l1 = l1.next
			l2 = l2.next
#!/usr/bin/env python3
# -*- coding utf-8 -*-

"""
单链表逆置
"""

class Node(object):
	"""
	结点
	"""
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next
		

def rev(link):
	"""
	翻转链表
	"""
	if not link:
		return link
	pre = link
	cur = link.next
	pre.next = None
	while cur:
		tmp = cur.next
		cur.next = pre
		pre = cur
		cur = tmp
	return pre
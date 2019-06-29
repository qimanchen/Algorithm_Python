#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
链表对调
"""

class ListNode(object):
	"""
	结点
	"""
	def __init__(self, x):
		self.val = x
		self.next = None
		

class Solution(object):
	"""
	链表成队翻转
	"""
	def swapPairs(self, head):
		"""
		:param head: ListNode
		: return: ListNode
		"""
		
		if head != None and head.next != None:
			mid = head.next
			head.next = self.swapPairs(mid.next)
			mid.next = head
			return mid
		return head
		
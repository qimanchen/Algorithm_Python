#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
树遍历
"""

class Node(object):
	"""
	树结点
	"""
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right
		
	
# 层次遍历
def lookUp(root):
	"""
	"""
	row = [root]
	while row:
		print(row)
		row = [kid for item in row for kid in (item.left, item.right) if kid]
		
# 求最大树深
def maxDepth(root):
	"""
	"""
	if not root:
		return 0
	return max(maxDepth(root.left), maxDepth(root.right)) + 1
	
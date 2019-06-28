#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
前中求后
"""

def rebuild(pre, center):
	"""
	通过前序和中序求后序
	重构二叉树
	"""
	if not pre:
		return
		
	cur = Node(pre[0])
	index = center.index(pre[0]) # 找出中间分割点
	cur.left = rebuild(pre[1:index+1], center[:index])
	cur.right = rebuild(pre[index+1:], center[index+1:])
	return cur
	
def deepSearch(root):
	"""
	后序遍历
	"""
	if not root:
		return
	deep(root.left)
	deep(root.right)
	print(root.data)
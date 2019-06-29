#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
二叉树非递归遍历算法
"""
# 先序
def pre_binary_tree(root):
	"""
	先序遍历非递归
	"""
	if not root:
		return
	stack = []
	# node = root # 最好使用复制 -- 防止改变原树
	while stack or root:
		while root:
			print(root.data)
			stack.append(root)
			root = root.left
		root = stack.pop()
		root = root.right
		
def mid_binary_tree(root):
	# 中序
	stack = []
	while stack or root:
		while root:
			stack.append(root)
			root = root.left
		root = stack.pop()
		print(root.data)
		root = root.right
		
def last_binary_tree(root):
	# 后序
	stack1 = []
	stack2 = []
	while stack1 or root:
		while root:
			stack2.append(root)
			stack1.append(root)
			root = root.right
		root = stack1.pop()
		root = root.left
	while stack2:
		print(stack2.pop().data)
		
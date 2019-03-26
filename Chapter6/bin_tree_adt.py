#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class BinTree(object):
	"""
		二叉树实现数据结构
		
		实际中，常用根结点表示某棵二叉树，即左右子树通过它们的根结点表示
		
		二叉树的唯一标志：树根结点
		
		遍历的两种选择：
			1、深度优先  -- 沿一条路直到走到头：
				3中工作：遍历左子树，遍历右子树，访问根结点
					a、中 -> 左 -> 右	先根序
					b、左 -> 根 -> 右	对称序
					c、左 -> 右 -> 根	后根序
				如果确定对称序，又知道另一种序列，就可以唯一确定这个二叉树
			2、广度优先  -- 所有路径齐头并进
				按层次进行： 上 -> 下 左 -> 右  二叉树的层次序列
			
		
	"""
	
	def __init__(self, data, left, right):		#构造操作，创建一个新二叉树
		pass
		
	def is_empty(self):
		"""判断self是否为空二叉树"""
		pass
		
	def num_nodes(self):
		"""求二叉树结点个数"""
		pass
		
	def data(self):
		"""获取二叉树根存储的数据"""
		pass
		
	def left(self):
		"""获取二叉树的左子树"""
		pass
		
	def right(self):
		"""获取二叉树的右子树"""
		pass
		
	def set_left(self, btree):
		"""用btree取代原来的左子树"""
		pass
		
	def set_right(self, btree):
		"""用btree取代原来的右子树"""
		pass
		
	def traversal(self):
		"""遍历二叉树中各结点数据的迭代器"""
		pass
		
	def forall(self, op=None):
		"""对二叉树中的每个结点的数据执行操作op"""
		pass
		
	
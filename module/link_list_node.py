#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class LNode(object):
	"""
		单链表节点类
		
		使用：
			node_object = LNode(elem, next_)
			elem:	该节点的值
			next_:		该节点的下一节点，默认为None
	"""
	
	def __init__(self, elem, next_=None):
		self.elem = elem
		self.next = next_
		

class LinkedListUnderflow(ValueError):
	"""
		链表的异常定制类
	"""
	pass
	
	
class DLNode(LNode):
	"""
		双链表节点类：
		使用：
			node_object = DLNode(elem, prev, next_)
			elem: 该节点的值
			prev: 该节点的前一节点对象
			next_: 该节点的下一节点对象
	"""
	def __init__(self, elem, prev=None, next_=None):
		LNode.__init__(self, elem, next_)		# 使用LNode类初始化
		# super(DLNode, self).__init__(elem, next_)
		self.prev = prev
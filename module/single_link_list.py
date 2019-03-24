#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 非package不可以这样使用
# import link_list_node.LNode
# import link_list_node.LinkedListUnderflow

from link_list_node import LNode, LinkedListUnderflow

class SingleLinkList(object):
	"""
		单链表数据结构实现类
	"""
	
	def __init__(self):
		self._head = None
		
	def is_empty(self):
		"""判断链表是否为空"""
		return self._head is None
		
	def sort_elem(self):
		pass
	
	def sort_place(self):
		pass
		
	def rev(self):
		"""
			翻转单链表
			通过新建一个链表，来实现链表的翻转
		"""
		
		p = None
		while self._head is not None:
			q = self._head
			self._head = q.next
			q.next = p
			p = q
			
		self._head = p
		
	def prepend(self, elem):
		"""
			在链表开头插入新节点
		"""
		self._head = LNode(elem, self._head)
		
	def append(self, elem):
		"""
			从节点结尾插入新节点
		"""
		if self._head is None:
			self._head = LNode(elem)
			return
		p = self._head
		while p.next is not None:
			p = p.next
			
		p.next = LNode(elem)
		
	def insert(self, elem, pred=None):
		"""
			在链表的任意位置插入新节点
		"""
		if self._head is None:
			self._head = LNode(elem)
		
		q = LNode(elem)
		q.next = pred.next
		pred.next = q
		
	def pop(self):
		"""
			从链表首部删除链表元素
		"""
		if self._head is None:
			raise LinkedListUnderflow(" in single_link_list pop")
			
		e = self._head.elem
		self._head = self._head.next
		return e
		
	def pop_last(self):
		"""
			从链表结尾删除节点
		"""
		if self._head is None:
			raise LinkedListUnderflow(" in single_link_list pop_last")
			
		p = self._head
		if p.next is None:
			e = p.elem
			self._head = None
			return e
		
		while p.next.next is not None:
			p = p.next
		e = p.next.elem
		p.next = None
		return e
		
	def find(self, pred):
		"""从链表中查找指定元素"""
		p = self._head
		while p is not None:
			if pred(p.elem):
				return p.elem
			p = p.next
			
	def printall(self):
		"""打印链表中所有节点的值"""
		p = self._head
		while p is not None:
			print(p.elem, end=' ')
			if p.next is not None:
				print(", ", end=' ')
			p = p.next
		print(' ')
		
	def for_each(self, proc):
		"""遍历链表"""
		p = self._head
		while p is not None:
			proc(p.elem)
			p = p.next
			
	def elements(self):
		"""链表迭代器"""
		p = self._head
		while p is not None:
			yield p.elem
			p = p.next
			
	def filter(self, pred):
		"""链表迭代器"""
		p = self._head
		while p is not None:
			if pred(p.elem):
				yield p.elem
			p = p.next
		
	
def test_LList():
	mlist1 = SingleLinkList()
		
	for i in range(10):
		mlist1.prepend(i)
		
	for i in range(11, 20):
		mlist1.append(i)
	mlist1.printall()
	
	
if __name__ == "__main__":
	test_LList()

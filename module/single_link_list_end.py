#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint

from link_list_node import LNode, LinkedListUnderflow
from single_link_list import SingleLinkList

class SingleLinkListEnd(SingleLinkList):
	"""
		单链表添加尾节点记录
	"""
	
	def __init__(self):
		SingleLinkList.__init__(self)
		self._rear = None
		
	def prepend(self, elem):
		# self._head = LNode(elem, self._head)
		# if self._rear is None:
		# self._rear = self._head
		if self._head is None:
			self._head = LNode(elem, self._head)
			self._rear = self._head
		else:
			self._head = LNode(elem, self._head)
			
	def rev(self):
		p = None
		
		rear_change = True
		
		while self._head is not None:	
			q = self._head
			self._head = q.next
			q.next = p
			p = q
			if rear_change:
				self._rear = p
				rear_change = False
			
		self._head = p
		
	def append(self, elem):
		if self._head is None:
			self._head = LNode(elem, self._head)
			self._rear = self._head
			
		else:
			self._rear.next = LNode(elem)
			self._rear = self._rear.next
			
	def pop_last(self):
		if self._head is None:
			raise LinkedListUnderflow("in pop_last")
			
		p = self._head
		if p.next is None:
			e = p.elem
			self._head = None
			return e
		
		while p.next.next is not None:
			p = p.next
			
		e = p.next.elem
		p.next = None
		self._rear = p
		return e
		
def test_LListEnd():
	mlist1 = SingleLinkListEnd()
	mlist1.prepend(99)
	
	for i in range(11, 20):
		mlist1.append(randint(1, 20))
		
	mlist1.printall()
	mlist1.rev()
	mlist1.printall()
	print(mlist1.pop_last())
	

if __name__ == "__main__":
	test_LListEnd()

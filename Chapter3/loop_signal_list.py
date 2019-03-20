#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 链表变形


class LNode(object):
	
	def __init__(self, elem, next_=None):
		self.elem = elem
		self.next = next_

		
class LinkedListUnderflow(ValueError):
	pass		


class LCList(object):
	def __init__(self):
		self._rear = None
		
	def is_empty(self):
		return self._rear is None
		
	def prepend(self, elem):
		p =LNode(elem)
		if self._rear is None:
			p.next = p
			self._rear = p
		else:
			p.next = self._rear.next
			self._rear.next = p
			
	def append(self, elem):
		# 尾端插入
		self.prepend(elem)
		self._rear  = self._rear.next
		
	def pop(self):
		if self._rear is None:
			raise LinkedListUnderflow(" in pop of  LCList.")
		
		p = self._rear.next
		
		if self._rear is p:
			self._rear = None
		else:
			self._rear.next = p.next
			
		return p.elem
		
	def printall(self):
		if self.is_empty():
			return
		p = self._rear.next
		while True:
			print(p.elem, end=" ")
			if p is self._rear:
				break
			p = p.next
			

class DLNode(LNode):
	def __init__(self, elem, prev = None, next_=None):
		LNode.__init__(self, elem, next_)
		self.prev = prev
		

	
def test_LCLlist():
	mlist1 = LCList()
		
	for i in range(10):
		mlist1.prepend(i)
		
	for i in range(11, 20):
		mlist1.append(i)
	mlist1.printall()
	
	
if __name__ == "__main__":
	test_LCLlist()
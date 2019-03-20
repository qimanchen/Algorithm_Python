#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from random import randint


class LNode(object):
	
	def __init__(self, elem, next_=None):
		self.elem = elem
		self.next = next_
		
		
"""
def add_in_head():
	q = LNode(13)
	q.next = head.next
	head = q

def add_in_any():
	q = LNode(13)
	q.next = pre.next
	pre.next = q
	
def length(head):
	p, n = head, 0
	while p is not None:
		n += 1
		p = p.next
	return n
"""


class LinkedListUnderflow(ValueError):
	pass
	
	
class LList(object):
	
	def __init__(self):
		self._head = None
		
	def is_empty(self):
		return self._head is None
		
	def sort1(self):
		if self._head is None:
			return
		crt = self._head.next
		
		while crt is not None:
			x = crt.elem
			p = self._head
			while p is not crt and p.elem <=x:
				p = p.next
			while p is not crt:
				y = p.elem
				p.elem = x
				x = y
				p = p.next
			crt.elem = x
			
	def sort(self):
		p = self._head
		if p is None or p.next is None:
			return
		rem = p.next
		p.next = None
		
		while rem is not None:
			p = self._head
			q = None
			while p is not None and p.elem <= rem.elem:
				q = p
				p = p.next
			if q is None:
				self._head = rem
			else:
				q.next = rem
			
			q = rem
			rem = rem.next
			q.next = p
		
	def rev(self):
		p = None
		while self._head is not None:
			q = self._head
			self._head = q.next
			q.next = p
			p = q
			
		self._head = p
		
	def prepend(self, elem):
		self._head = LNode(elem, self._head)
		
	def pop(self):
		if self._head is None:
			raise LinkedListUnderflow("in pop")
		
		e = self._head.elem
		self._head = self._head.next
		return e
		
	def insert(self, elem, pred=None):
		if self._head is None:
			self._head = LNode(elem)
		q = LNode(elem)
		q.next = pred.next
		pred.next = q
		
	def append(self, elem):
		if self._head is None:
			self._head = LNode(elem)
			return
		p = self._head
		while p .next is not None:
			p = p.next
		p.next = LNode(elem)
		
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
		return e
		
	def find(self, pred):
		p = self._head
		while p is not None:
			if pred(p.elem):
				return p.elem
			p = p.next
			
	def printall(self):
		p = self._head
		while p is not None:
			print(p.elem, end=' ')
			if p.next is not None:
				print(", ", end=' ')
			p = p.next
		print(' ')
		
	def for_each(self, proc):
		p = self._head
		while p is not None:
			proc(p.elem)
			p = p.next
			
	def elements(self):
		p = self._head
		while p is not None:
			yield p.elem
			p = p.next
			
	def filter(self, pred):
		p = self._head
		while p is not None:
			if pred(p.elem):
				yield p.elem
			p = p.next
			
class LListEnd(LList):
	
	def __init__(self):
		LList.__init__(self)
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

		
class DLNode(LNode):
	def __init__(self, elem, prev = None, next_=None):
		LNode.__init__(self, elem, next_)
		self.prev = prev
		
class DLList(LListEnd):
	def __init__(self):
		LListEnd.__init__(self)
		
	def prepend(self, elem):
		p = DLNode(elem, None, self._head)
		if self._head is None:
			self._rear = partition
		else:
			p.next.prev = p
		self._head = p
		
	def append(self, elem):
		p = DLNode(elem, self._rear, None)
		if self._head is None:
			self._head = p
		else:
			p.prev.next = p
		self._rear = p
		
	def pop(self):
		if self._head is None:
			raise LinkedListUnderflow("in pop of DLList")
			
		e = self._head.elem
		self._head = self._head.next
		if self._head is not None:
			self._head.prev = None
		return e
		
	def pop_last(self):
		if self._head is None:
			raise LinkedListUnderflow(" in pop_last of DLList")
		e = self._rear.elem
		self._rear = self._rear.prev
		
		if self._rear is None:
			self._head = None
		else:
			self._rear.next = None
		return e
		
	
def test_LList():
	mlist1 = LList()
		
	for i in range(10):
		mlist1.prepend(i)
		
	for i in range(11, 20):
		mlist1.append(i)
	mlist1.printall()
	
	mlist1.sort()
	mlist1.printall()
	
	
def test_LListEnd():
	mlist1 = LListEnd()
	mlist1.prepend(99)
	
	for i in range(11, 20):
		mlist1.append(randint(1, 20))
		
	mlist1.printall()
	mlist1.rev()
	mlist1.printall()
	print(mlist1.pop_last())
		
	# for x in mlist1.filter(lambda y: y%2==0):
		# print(x)

def list_sort(lst):
	for i in range(1, len(lst)):
		x = lst[i]
		j = i
		while j > 0 and lst[j-1] >x:
			lst[j] = lst[j-1]
			j -= 1
			
		lst[j] = x
			
if __name__ == "__main__":
	
	test_LList()

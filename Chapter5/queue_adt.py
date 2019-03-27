#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class QueueUnderflow(ValueError):
	"""判断队列为空是，异常类"""
	pass
	

class Queue(object):
	"""对列实现数据结构"""
	
	def __init__(self):
		"""创建空队列"""
		pass
		
	def is_empty(self):
		"""判断队列是否为空，空时返回True，否则返回False"""
		q.head == q.rear		# 队列为空
		pass
		
	def is_full(self):
		"""判断队列是否已满"""
		(q.rear + 1) % q.len == q.head
		
	def enqueue(self, elem):
		"""将元素elem加入队列 -- 入队"""
		q.head = (q.head + 1) % q.len
		pass
		
	def dequeue(self):
		"""删除队列中最早进入的元素并将其删除 -- 出队"""
		q.rear = (q.rear + 1) % q.len
		pass
		
	def peek(self):
		"""查看队列里最早进入的元素，不删除"""
		pass
		

# list实现队列
class SQueue(object):
	"""队列实现数据结构"""
	
	def __init__(self, init_len=8):		# 默认队列初始长度为8
		"""创建空队列"""
		self._len = init_len		# 存储区长度
		self._elems = [0]*init_len	# 元素存储
		self._head = 0		# 表头元素下标
		self._num = 0		# 元素个数
		
	def is_empty(self):
		"""判断队列是否为空，空时返回True，否则返回False"""
		return self._num == 0
		
	def is_full(self):
		"""判断队列是否已满"""
		pass
		
	def enqueue(self, elem):
		"""将元素elem加入队列 -- 入队"""
		if self._num == self._len:
			self.__extend()
		self._elems[(self._head+self._num)%self._len] = e
		self._num += 1
		
	def __extend(self):
		"""当队列满时，对列进行扩容"""
		old_len = self._len
		self._len *= 2
		new_elems = [0] * self._len
		for i in range(old_len):
			new_elems[i] = self._elems[(self._head+i) % old_len]
		
		self._elems, self._head = new_elems, 0
		
	def dequeue(self):
		"""删除队列中最早进入的元素并将其删除 -- 出队"""
		if self._num == 0:
			raise QueueUnderflow
		e = self._elems[self._head]
		self._head = (self._head + 1) % self._len
		self._num -= 1
		return e
		
	def peek(self):
		"""查看队列里最早进入的元素，不删除"""
		if self._num == 0:
			raise QueueUnderflow
		return self._elems[self._head]
		
		
# 队列的应用：
# 1、文件打印
# 2、万维网服务器
# 3、Windows系统和消息队列
# 4、离散事件系统模拟


	
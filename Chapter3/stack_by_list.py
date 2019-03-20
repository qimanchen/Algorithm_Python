#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class TestQueue(object):
	
	def __init__(self, elems=None):
		self._queue = []
	
	def is_empty(self):
		return len(self._queue) == 0
		
	def in_queue(self, elem):
		self._queue.append(elem)
		
	def out_queue(self):
		return self._queue.pop()
		
	def print_queue(self):
		for i in self._queue:
			print(i, end=" ")
		print("")
		
if __name__ == "__main__":
	test_obj = TestQueue()
	for i in range(10):
		test_obj.in_queue(i)
		
	test_obj.print_queue()
	
	print("*"*10)
	
	while not test_obj.is_empty():
		print(test_obj.out_queue())
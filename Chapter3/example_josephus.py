#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from chain_list import LList
from loop_signal_list import LCList


class Josephus(LCList):
	def turn(self, m):
		for i in range(m):
			self._rear = self._rear.next
	def __init__(self, n, k, m):
		LCList.__init__(self)
		# 可以直接在init中调用父程序中的方法
		for i in range(n):
			self.append(i+1)
		self.turn(k-1)
		while not self.is_empty():
			self.turn(m-1)
			print(self.pop(), end=("\n" if self.is_empty() else ", "))
				
	
def josephus_A(n, k, m):
	people = list(range(1, n+1))
	
	i = k - 1
	
	for num in range(n):
		count = 0
		while count < m:
			if people[i] > 0:
				count += 1
			if count == m:
				print(people[i], end=" ")
				people[i] = 0
			# 当到达n时，设置为1
			i  = (i+1) % n
		if num < n-1:
			print(", ", end=" ")
		else:
			print(" ")
	return
	

def josephus_L(n, k, m):
	people = list(range(1, n+1))
	
	num, i = n, k-1
	
	for num in range(n, 0, -1):
		i = (i + m-1) % num
		print (people.pop(i),
				  end=(", " if num>1 else "\n"))
	return

def test(n, k, m):
	people = list(range(1, n+1))
	
	i = k-1
	
	num = n
	
	while num > 0:
		i = (i+m-1) % num
		print(people.pop(i), end=" ")
		num -= 1
	print(" ")
	return
	

if __name__ == "__main__":
	josephus_A(10, 2, 7)
	josephus_L(10, 2, 7)
	test(10, 2,7)
	Josephus(10, 2, 7)

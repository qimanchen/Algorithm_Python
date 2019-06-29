#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
台阶问题
"""

def fog_step(n):
	"""
	"""
	if n <= 2:
		return n
	return fog_step(n-1) + fog_step(n-2)
	
def fog_step1(n):
	
	a, b = 0, 1
	
	while n > 0:
		a, b = b, a+b
		n -= 1
	return a

if __name__ == "__main__":
	print(fog_step(5))
	print(fog_step(5))
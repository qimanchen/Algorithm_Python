#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
	Firborach 
"""

def fib_ite(n):
	if n < 2:
		return 1
	else:
		return fib_ite(n-1) + fib_ite(n-2)
		
def fib_loop(n):
	f1 = f2 = 1
	for k in range(1, n):
		f1, f2 = f2, f2+f1
	return f2
	

if __name__ == "__main__":
	print(fib_ite(5))
	print(fib_loop(5))
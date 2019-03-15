#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Test add argument time for list
import time
from functools import wraps

def fn_timer(func):
	@wraps(func)
	def function_timer(*args, **kwargs):
		t0 = time.time()
		result = func(*args, **kwargs)
		t1 = time.time()
		print("Total time running %s : %s seconds" % (func.__name__, str(t1-t0)))
		
		return result
	return function_timer


@fn_timer
def test1(n):
	lst = []
	for i in range(n*10000):
		lst = lst + [i]
	return lst

@fn_timer
def test2(n):
	lst = []
	for i in range(n*10000):
		lst.append(i)
	return lst

@fn_timer
def test3(n):
	return [ i for i in range(n*10000)]

@fn_timer
def test4(n):
	return list(range(n*10000))
	

if __name__ == "__main__":
	test1(10)
	test2(10)
	test3(10)
	test4(10)
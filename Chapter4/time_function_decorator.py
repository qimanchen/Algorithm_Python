#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import time
from functools import wraps


def fn_timer(func):
	@wraps(func)
	def function_timer(*args, **kwargs):
		t0 = time.time()
		result = func(*args, **kwargs)
		t1 = time.time()
		print("Total time running %s: %s seconds" % (func.__name__, str(t1-t0)))
		
		return result
	return function_timer
	

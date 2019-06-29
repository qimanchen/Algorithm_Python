#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-06-04 23:04:13
# @Author  : Qiman Chen
# @Version : $Id$

"""
单例模式

"""

# 1
def singleton(cls):
	instances = {}
	def wrapper(*args, **kwargs):
		if cls not in instances:
			instances[cls] = cls(*args, **kwargs)
		return instances[cls]
	return wrapper

@singleton
class Foo(object):
	pass


foo1 = Foo()
foo2 = Foo()
print(foo1 is foo2)


class Singleton(object):
	"""
	单例模式
	"""
	def __new__(cls, *args, **kwargs):
		if not hasattr(cls, '_instance'):
			cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
		return cls._instance




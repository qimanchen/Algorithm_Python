#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Countable(object):
	
	# 类属性
	# 必须通过类名.属性  使用
	counter = 0
	
	# 静态方法
	@staticmethod
	def static_method():
		"""
			静态方法，可以在__init__ 中使用
			不用经过类的初始化
			调用：
				self.static_method()
				class.static_method()
		"""
		pass
		
	def __init__(self):
		Countable.counter += 1
	
	# 类方法
	@classmethod
	def get_count(cls):
		return Countable.counter
		
		
if __name__ == "__main__":
	x = Countable()
	y = Countable()
	z = Countable()
	
	print(Countable.get_count())


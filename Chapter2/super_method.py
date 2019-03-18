#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class C1(object):
	
	def __init__(self,  x,  y):
		self.x = x
		self.y = y
		
	def m1(self):
		print(self.x, self.y)
		
		
class C2(C1):

	def __init__(self)
		# 调用基类的初始化方法初始化
		super(C2, self).__init__()
	
	def m1(self):
		# 直接调用基类中的m1函数
		super().m1()
		print("Some special service.")
		

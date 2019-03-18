#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
	静态约束
		就是，在谁里面，就谁做主
	动态约束
		x = C()  # 实例类C
		x.f()   # f 为虚函数
		实际调用流程：
			1、先检查类C中是否有方法f
			2、若没有，则检查它的基类B中是否有相应的方法
			3、执行B中的f，但是其 self属性还是表示C的
	谁实例化，self就代表谁
		
"""


class B(object):
	
	def f(self):
		self.g()
	
	def g(self):
		print('B.g called.')
		

class C(B):
	
	def g(self):
		print('C.g called.')
		
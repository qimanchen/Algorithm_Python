#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
判断时间的装饰器
"""
import datetime


class TimeException(Exception):
	"""
	时间异常类
	"""
	def __init__(self, exception_info):
		super().__init__()
		self.info = exception_info
		
	def __str__(self):
		return self.info
		

def timeCheck(func):
	"""
	时间检测装饰器
	"""
	def wrapper(*args, **kwargs):
		if datetime.datetime.now().year == 2019:
			func(*args, **kwargs)
		else:
			raise TimeException("函数已过时")
	return wrapper
	
	
# 实例
@timeCheck
def test(name):
	print("Hello {}, 2019 Happy".format(name))
	
if __name__ == "__main__":
	test("backbp")

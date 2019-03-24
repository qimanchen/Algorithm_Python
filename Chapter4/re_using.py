#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
# 添加绝对路径
# 前面路径错误的原因，是没有切换到指定的工作路径中
os.chdir(sys.path[0])

print(sys.path)

sys.path.append(r"..\module")

# print(sys.path)
import single_link_list


# import link_list_node
""" 通过 '.' 和 '..' 这样相对路径是针对当前工作路径而言的"""
# from . import string_notes




"""
	re 正则表达式模块的使用：
		re_object = re.compile(pattern)	# 实际的模式串
		for mat in re_object.finditer(text):
			mat.group()	# 取得被匹配的字串，做所需操作
			text[mat.strart()]	text[mat.end()]
			
			mat.re	# 访问被匹配的模式串
			mat.string	# 访问被匹配的目标字符串
"""

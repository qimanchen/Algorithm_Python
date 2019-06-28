#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-06-04 21:43:51
# @Author  : Qiman Chen
# @Version : $Id$

"""
这个函数接收文件夹的名称作为输入参数
返回该文件夹中文件的路径
以及其包含文件夹中文件的路径
"""

import os


def print_directory_contents(s_path):
	"""
	:param s_path: 输入文件夹 -- 完整的路径
	输出该文件夹包含文件和文件夹的所有完整路径
	"""

	for s_child in os.listdir(s_path):
		s_child_path = os.path.join(s_path, s_child)
		if os.path.isdir(s_child_path):
			print_directory_contents(s_child_path)
		else:
			print(s_child_path)


def main():

	s_path = input("请输入需要操作的文件名")

	print_directory_contents(s_path)


if __name__ == "__main__":
	main()

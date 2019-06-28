#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-06-04 21:34:04
# @Author  : Qiman Chen
# @Version : $Id$

"""
有一个jsonline格式的文件大小约为10k

def get_lines():
	with open('file.txt', 'rb') as f:
		return f.readlines()

if __name__ == "__main__":
	for e in get_lines():
		process(e) # 处理每一行数据
"""

from mmap import mmap


def get_lines(fp):
	"""
	improved version
	"""

	with open(fp, 'r+') as f:
		m = mmap(f.fileno(), 0)
		tmp = 0
		for i, char in enumerate(m):
			if char == b"\n":
				yield m[tmp:i+1].decode()
				tmp = i+1


if __name__ == "__main__":
	for i in get_lines('fp_some_huge_file'):
		print(i)

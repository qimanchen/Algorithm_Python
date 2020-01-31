#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
判题系统的输入
"""

import sys
# python 2
try:
	while True:
		line = sys.stdin.readline().strip()
		if line == '':
			break
		lines = line.split()
		print int(lines[0]) + int(lines[1])
except:
	pass
	
# python 3
for line in sys.stdin:
	a = line.strip().split()
	print(int(a[0]) + int(a[1]))
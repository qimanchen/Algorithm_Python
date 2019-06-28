#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-06-04 21:53:55
# @Author  : Qiman Chen
# @Version : $Id$

"""
输入日期，判断这一条是这一年的第几天
"""


import datetime


def dayofyear():
	"""
	判断某一天是某年的第几天
	"""

	year = input('请输入年份：')
	month = input('请输入月份：')
	day = input('请输入天：')

	date1 = datetime.date(year=int(year), month=int(month), day=int(day))
	date2 = datetime.date(year=int(year), month=1, day=1)
	return (date1-date2).days + 1

if __name__ == "__main__":
	print(dayofyear())

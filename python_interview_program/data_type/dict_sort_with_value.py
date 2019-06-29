#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-06-04 22:11:52
# @Author  : Qiman Chen
# @Version : $Id$

"""
现有字典 d= {'a':24,'g':52,'i':12,'k':33}请按value值进行排序?
"""

# 字典按value排序
# dict.items() -- [(key, value), ...]
sorted(d.items(), key=lambda x: x[1])

# 字典推导式
d = {key:value for (key, value) in iterable}

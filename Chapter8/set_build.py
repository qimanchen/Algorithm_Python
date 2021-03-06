#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 将一个元素加入集合后，判断它存在于集合的结果为真
# 没加入的元素，或已经删除的元素，判断它存在于集合的结果为假

# 简单线性表实现集合
"""
集合插入与删除：
	1、插入元素时，检查它是否在集合中，保证集合中元素的唯一性
		  删除元素时，找到第一个相同的元素并将其删除
		  
	2、插入时，简单将其加入线性表
		  删除时，检查整个表，删除指定元素的所有拷贝
"""
# 简单线性表实现技术简单，元素判断和几个集合运算的操作效率低
# O(m*n)


# 采用排序表操作
# O(m+n)

# 采用hash表实现
# O(m+n)

# 集合特殊实现技术 -- 位向量实现

"""
具体实现方法：
	假定U包含n个元素，每个元素确定一个编号作为该元素的下标
	
	建立一个n位的二进制序列，对应值存在，二进制位取值为1，反之为0
	
	对于并集等运算操作快，直接对而进制求并
	
	
"""
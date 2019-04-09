#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
	python中字典类型 -- dict
	集合类型  -- set，frozenset
	
	都是基于hash表实现的
	
	dict：
		dict采用hash表技术实现，元素是 key-value 关键码是任意不变对象，值可以是任何对象
		
		创建空字典时，初始分配存储区可容纳8个元素
		
		dict对象在负载因子超过2/3时自动更换成更大的存储区 -- 4倍扩，超50000 -- 2倍扩
		
	frozenset是不变对象
	
	dict的关键码和set，frozenset的元素只能为不变对象
	
	hash函数都是对于不可变对象而言
	
	__hash__ 定义hash函数的操作
	
	

"""
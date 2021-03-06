#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
栈和队列：
	容器 包含 元素（其他数据结构）
	
	只支持数据项的存储和访问，不支持数据项之间的任何关系
	
	最重要的功能： 元素的存入和取出
	
	两种访问顺序：
		先进先出
		后进先出
		
	栈概念：
		元素之间只有时间的先后顺序关系，而无其他关系
		后进先出
		
		应用：
			前缀表达式： 每个运算符的运算对象，就是它后面出现的几个完整表达式
			后缀表达式： 与前面相反
		
		栈与函数调用：
			1、进入新的函数调用之前，保存一些信息  -- 函数调用的前序动作
			2、退出上一次函数调用，需要恢复调用前的状态  -- 函数调用的后序动作
			
			因此函数调用是有代价的
			
	任何一个递归定义的函数，都可以通过引入一个栈保存中间结果的方式，翻译为一个非递归的过程
	
	递归 -- 涉及函数的调用（消耗资源）
	转化
	非递归 -- 减少函数调用的开销
	
	任何包含循环的程序翻译为不包含循环的递归定义
			
队列：
	queue -- 容器
	 
	单链表可以直接实现 -- 先进先出（直接首端操作）
	
	假性溢出
	
	
	通过顺序表实现队列 -- 通过循环队列实现
	
	简单实现通过固定大小的list
	
	数据不变式：维护对象属性间的正确关系
	
基于栈的搜索  -- 深度优先搜索 -- 单条路径找个遍
基于队列的搜索 -- 广度优先搜索 -- 多条路径的进行

深度优先：
	总是沿着遇到的搜索路径一路前行
	
	当分支节点对不同分支的选择非常重要；问题简单，没有其他额外的帮助信息
	
	状态空间小时使用
	
	解：
		可以通过栈来保存
	
广度优先：
	只要存在达解的有穷长路径 -- 必定找到最短的路径（最近的解)
	
	解：
		需要额外的方法进行记录
		
时间开销 -- 访问的状态个数


几种特殊的栈与对列：
	1、双端对列  --- python 中的collections包中定义了一种deque类型 -- python版的双端队列
	
链接表带来灵活性，但是失去了一定的效率
cpu需要整块的分级缓存单元


		
	
	
	
	


			
			
		
"""
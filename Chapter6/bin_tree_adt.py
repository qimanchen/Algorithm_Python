#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class BinTree(object):
	"""
		二叉树实现数据结构
		
		实际中，常用根结点表示某棵二叉树，即左右子树通过它们的根结点表示
		
		二叉树的唯一标志：树根结点
		
		遍历的两种选择：
			1、深度优先  -- 沿一条路直到走到头：
				3中工作：遍历左子树，遍历右子树，访问根结点
					a、中 -> 左 -> 右	先根序
					b、左 -> 根 -> 右	对称序
					c、左 -> 右 -> 根	后根序
				如果确定对称序，又知道另一种序列，就可以唯一确定这个二叉树
			2、广度优先  -- 所有路径齐头并进
				按层次进行： 上 -> 下 左 -> 右  二叉树的层次序列
			搜索树
			
		二叉树：
			三元组： 左右子树和本结点数据
			
		使用list实现二叉树：
			None -- 空树
			[d, l, r] - 非空二叉树：
				d -- 根结点的元素
				l, r -- 子树，整个二叉树同样结构的list实现
			使用嵌套括号表示形式
			
		
		
	"""
	
	def __init__(self, data, left, right):		#构造操作，创建一个新二叉树
		pass
		
	def is_empty(self):
		"""判断self是否为空二叉树"""
		pass
		
	def num_nodes(self):
		"""求二叉树结点个数"""
		pass
		
	def data(self):
		"""获取二叉树根存储的数据"""
		pass
		
	def left(self):
		"""获取二叉树的左子树"""
		pass
		
	def right(self):
		"""获取二叉树的右子树"""
		pass
		
	def set_left(self, btree):
		"""用btree取代原来的左子树"""
		pass
		
	def set_right(self, btree):
		"""用btree取代原来的右子树"""
		pass
		
	def traversal(self):
		"""遍历二叉树中各结点数据的迭代器"""
		pass
		
	def forall(self, op=None):
		"""对二叉树中的每个结点的数据执行操作op"""
		pass
		

# list内部的嵌套层次等于树的高度
# 二叉树的简单list实现
def BinTree(data, left=None, right=None):
	return [data, left, right]
	
def is_empty_BinTree(btree):
	return btree is None

# 输出根，左，右结点
def root(btree):
	return btree[0]
	
def left(btree):
	return btree[1]
	
def right(btree):
	return btree[2]

# 设置根，左，右结点	
def set_root(btree, data):
	btree[0] = data
	
def set_left(btree, left):
	btree[1] = left
	
def set_right(btree, right):
	btree[2] = right
	
# 表达式树
# 运算符表达式，二元表达式
"""
	二元表达式：
		基本运算对象（数和变量）作为页结点的数据
		以运算符作为分支结点的数据：
			两颗子树它的运算对象
			子树可以是基本运算对象，也可以是任意复杂的二元表达式
	
	tuple -- 运算符作用于运算对象的复合表达式
	否则就是基本表达式 -- 数或变量
"""
def make_sum(a, b):
	return('+', a, b)
	
def make_prod(a, b):
	return ('*', a, b)
	
def make_diff(a, b):
	return ('-', a, b)
	
def make_div(a, b):
	return ('/', a, b)
	
def is_basic_exp(a):
	"""区分基本表达式（直接处理），复合表达式（递归处理）"""
	return not isinstance(a, tuple)
	
def is_number(x):
	"""判断是否是数值（int，float，complex）"""
	return (isinstance(x, int) or isinstance(x, float) or isinstance(x, complex)
	
e1 = make_prod(3, make_sum(2, 5))

# make_sum(make_prod('a', 2), make_prod('b', 7))

"""数学表达式求值规则：
	1、对表达式里的数，其值就是它们本身
	2、其它表达式根据运算符的情况处理，可以定义专门的处理函数
	3、当一个运算符的两个运算对象都是数时，就可以求出一个数值
"""

# 求值函数
def eval_exp(e):
	if is_basic_exp(e):
		return e
	# 通过本函数的递归调用，处理子树的运算
	op, a, b = e[0], eval_exp(e[1]), eval_exp(e[2])
	
	if op == '+':
		return eval_sum(a, b)
	elif op == '-':
		return eval_diff(a, b)
	elif op == '*':
		return eval_prod(a, b)
	elif op == '/':
		return eval_div(a, b)
	else:
		raise ValueError("Unknown operator:", op)

# 具体求值函数
def eval_sum(a, b):
	if is_number(a) and is_number(b):
		return a + b
	if is_number(a) and a == 0:
		return b
	if is_number(b) and b == 0:
		return a
	return make_sum(a, b)
	
def eval_div(a, b):
	if is_number(a) and is_number(b):
		return a/b
	if is_number(a) and a == 0:
		return 0
	if is_number(b) and b == 1:
		return a
	if is_number(b) and b == 0:
		raise ZeroDivisionError
	return make_div(a, b)
	


		




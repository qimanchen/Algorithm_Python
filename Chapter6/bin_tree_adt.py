#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from discrete_event_system import SQueue

class StackUnderflow(ValueError):
	""" 栈下溢 -- 空栈访问"""
	pass
	
	
class LNode(object):
	
	def __init__(self, elem, next_=None):
		self.elem = elem
		self.next = next_

class SStack(object):
	"""
		栈的ADT
		基于顺序表实现栈类
	"""
	
	def __init__(self):
		"""
			创建空栈
			使用list对象 _elems存储栈中元素
			所有的栈操作都映射到list操作
		"""
		self._elems = []
		
	def is_empty(self):
		"""判断栈是否未空，空时返回True，否则返回False"""
		return self._elems == []
		
	def push(self, elem):
		"""将elem加入栈 -- 压栈，入栈"""
		self._elems.append(elem)
		
	def pop(self):
		"""删除栈中最后压入的元素，出栈"""
		if self._elems == []:
			raise StackUnderflow("in SStack.pop() ")
		return self._elems.pop()
		
	def top(self):
		"""取得栈内最后压入的元素，但不删除"""
		if self._elems == []:
			raise StackUnderflow("in SStack.top()")
		return self._elems[-1]


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
	return (isinstance(x, int) or isinstance(x, float) or isinstance(x, complex))
	
# e = make_prod(3, make_sum(2, 5))

# make_sum(make_prod('a', 2), make_prod('b', 7))

# 数学表达式求值规则：
# 1、对表达式里的数，其值就是它们本身
# 2、其它表达式根据运算符的情况处理，可以定义专门的处理函数
# 3、当一个运算符的两个运算对象都是数时，就可以求出一个数值
def eval_exp(e):
	# 求值函数
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

	
"""
	二叉树的实现方案:
		1、通过前面实现的list和tuple技术，以其作为二叉树类型内部表示方式
		2、链接实现：
			用一个数据单元表示一个二叉树的结点，通过子结点链接（指针）建立结点之间的联系
"""


class BinTNode(object):
	"""
		二叉树结点类
		没有子结点用None表示
		空二叉树直接用None表示
	"""
	
	def __init__(self, dat, left=None, right=None):
		self.data = dat		# 结点数据
		self.left = left		# 左结点
		self.right = right	# 右结点

"""
	1、描述空树处理，直接给出结果
	2、描述非空树处理：
		a、如何处理根结点
		b、通过递归调用分别处理左右子树
		c、基于上述三部分处理的结果得到整个树的处理结果

"""
# 统计树中结点个数
def count_BinTNodes(t):
	if t is None:
		return 0
	else:
		return 1 + count_BinTNodes(t.left) + count_BinTNodes(t.right)

# 如果结点中保存数值，求二叉树中所有数值和:
def sum_BinTNodes(t):
	if t is None:
		return 0
	else:
		return t.data + sum_BinTNodes(t.left) + count_BinTNodes(t.right)

# 实现二叉树遍历及做出相关操作
# 广度优先		
def preorder(t, proc):
	"""
		二叉树的递归遍历实现
		proc是具体结点数据的操作
	"""
	
	if t is None:
		return		
	proc(t.data)
	preorder(t.left)
	preorder(t.right)
	
# 输出二叉树
def print_BinTNodes(t):
	if t is None:
		print("^", end=" ")		# 空树输出 ^
		return
	print("(" + str(t.data), end=" ")
	print_BinTNodes(t.left)
	print_BinTNodes(t.right)
	print(")", end=" ")
		

# 深度优先实现
def levelorder(t, proc=None):
	# 建立缓存处理队列
	qu = SQueue()
	qu.enqueue(t)
	while not qu.is_empty():
		t = qu.dequeue()
		if t is None:		# 弹出的树为空则直接跳过
			continue
		# 判空操作
		# 根 -- 左 -- 右
		if not t.left is None:
			qu.enqueue(t.left)
		if not t.right is None:
			qu.enqueue(t.right)
		proc(t.data)
# 不能直接通过迭代修改为生成器
# 由于每次迭代返回的都是None

# 非递归的先根序遍历函数
"""
	非递归遍历：
		1、递归与非递归的关系
		2、清楚二叉树遍历的具体过程和相关性质
		3、分析问题和设计算法
		
	实现：
		先根序， 遇到结点就访问，下一步沿着树的左支下行
		结点的右分支入栈
		遇空树回溯，取出栈中保存的一个右分支，像二叉树一样遍历它
	
	循环不变关系：
		只要前树不为空或栈不为空
		
		内部遇到空树就回溯
"""
def preorder_nonrec_root(t, proc):
	# 先根序
	s = SStack()		# 建立栈
	while t is not None or not s.is_empty():
		while t is not None:		# 回溯条件
			proc(t.data)		# 先根序先处理根数据
			s.push(t.right)	# 右分支入栈
			t = t.left		# 沿左分支下行
		t = s.pop()		# 遇到空树，回溯

def preorder_nonrec_mid(t, proc):
	""" 
		中根序
		
		分析：
			左 -- 根 -- 右
			先查看左结点是否为空，不为空则
			查看其左结点的左结点是否为空：
			若为空，则 proc(t.left.data), proc(t.data)
			s.push(t.right)
			若不为空:
				s.push(t)
				t = t.left
			若为空，proc(t.data)
			同时检测t.right是否为空，若不为空
				s.push(t.right)
			若为空 continue

	"""
	s = SStack()
	while t is not None or not s.is_empty():
		while t is not None:
			if t.left is None and t.right is not None:
				proc(t.data)
				t = t.right
			elif t.left is None and t.right is None:
				proc(t.data)
				break
			else:
				s.push(t)
				t = t.left
		if s.is_empty():
			break
		
		t = s.pop()
		proc(t.data)	# 根结点处理
		if t.right is not None:
			t = t.right

def preorder_nonrec_last(t, proc):
	"""
		函数定义中的下行循环 -- 内层循环
		
	"""
	s = SStack()
	while t is not None or not s.is_empty():
		while t is not None:		# 下行循环，指导栈顶的两子树为空
			s.push(t)
			t = t.left if t.left is not None else t.right
			
		t = s.pop()		# 栈顶就是应该访问的结点
		proc(t.data)
		
		if not s.is_empty() and s.top().left == t:
			t = s.top().right
		else:
			t = None
	
# 通过生成器函数遍历
# 非递归算法，实现迭代器的基础
def preorder_elements(t):
	s = SStack()
	while t is not None or not s.is_empty():
		while t is not None:
			s.push(t.right)
			yield t.data
			t = t.left
		t = s.pop()
		
		
# 二叉树类
class BinTree(object):
	"""
		二叉树类：
			为解决基于结点构造的二叉树的None非BinTNode类型
			同样为保持好二叉树解决方法的封装性
	"""
	
	def __init__(self):
		# 空树
		self._root = None
		
	def is_empty(self):
		"""判空"""
		return self._root is None
		
	def root(self):
		# 查询根结点
		return self._root
	
	def leftchild(self):
		"""
			查询左结点
		"""
		return self._root.left
		
	def rightchild(self):
		"""
			查询右结点
		"""
		return self._root.right
		
	def set_root(self, rootnode):
		"""
			操作根结点
		"""
		self._root = rootnode
		
	def set_left(self, leftchild):
		"""
			操作左结点
		"""
		self._root.left = leftchild
		
	def set_right(self, rightchild):
		"""
			操作右结点
		"""
		self._root.right = rightchild
		
	def preorder_elements(self):
		"""
			元素迭代器
			先根序实现类
		"""
		t, s = self._root, SStack()
		while t is not None or not s.is_empty():
			while t is not None:
				s.push(t.right)
				yield t.data
				t = t.left
			t = s.pop()

			
class BinPNode(object):
	""" 
		可查询结点的结点类
	"""
	def __init__(self, dat, parent=None, left=None, right=None):
		self.data = dat
		self.parent = parent
		self.left = left
		self.right = right
			
class BinTreeParent(object):
	"""
		增加结点的父结点域
		方便父结点的查询
	"""
	def __init__(self):
		# 空树
		self._root = None
		
	def is_empty(self):
		"""判空"""
		return self._root is None
		
	def root(self):
		# 查询根结点
		return self._root
	
	def leftchild(self):
		"""
			查询左结点
		"""
		return self._root.left
		
	def rightchild(self):
		"""
			查询右结点
		"""
		return self._root.right
		
	def set_root(self, rootnode):
		"""
			操作根结点
		"""
		self._root = BinPNode(rootnode)
		
	def set_left(self, leftchild):
		"""
			操作左结点
		"""
		self._root.left = BinPNode(leftchild, self._root)
		
	def set_right(self, rightchild):
		"""
			操作右结点
		"""
		self._root.right = BinPNode(rightchild, self._root)
		
	def preorder_elements(self):
		"""
			元素迭代器
			先根序实现类
		"""
		t, s = self.root(), SStack()
		while t is not None or not s.is_empty():
			while t is not None:
				s.push(t.right)
				yield t.data
				t = t.left
			t = s.pop()
			
		
# test函数	
def test():
	a = BinTNode('A', BinTNode('B', BinTNode('D', None, BinTNode('H')), BinTNode('E', None, BinTNode('I'))), BinTNode('C', BinTNode('F', BinTNode('J'), BinTNode('K')), BinTNode('G')))
	levelorder(a, print)
	print_BinTNodes(a)
	print()
	preorder_nonrec_root(a, lambda x: print(x, end=" "))
	print()
	preorder_nonrec_last(a, lambda x: print(x, end=" "))
	print()
	preorder_nonrec_mid(a, lambda x: print(x, end=" "))
	
def test_BinTreeParent():
	"""
		测试BinTreeParent类
	"""
	ptree = BinTreeParent()
	ptree.set_root(10)
	ptree.set_right(20)
	ptree.set_left(20)
	
	print(ptree.root().data, ptree.leftchild().data, ptree.rightchild().data)
	for i in ptree.preorder_elements():
		print(i)

if __name__ == "__main__":
	test_BinTreeParent()
		
	


		




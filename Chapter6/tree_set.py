#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
	树的集合：树林
	
	树：
		层次结构：通过将上下层元素之间的联系抽象为结点之间的联系
		
	使用括号嵌套的格式表示
	
	
	树的定义和相关概念：
		一棵树是n各结点的有限集  -- n >= 0
		当 n>0时：
			有且只有一个根结点
			
		空树
		
		单结点树
		
		有序树：每个结点的子树都有明确规定的顺序， 从左到右
		
		无序树：一个结点的不同子树没有顺序关系
		
		树的度数：树中度数最大的结点的度数
		
		树林：0棵树或多棵树的集合

"""


class Tree(object):
	"""
		一个树的抽象数据类型
	"""
	
	def __init__(self, data, forest):
		"""
			构造操作，基于树根数据和一组子树
		"""
		pass
		
	def is_empty(self):
		"""
			判断是否为一颗空树
		"""
		pass
		
	def num_nodes(self):
		"""
			树中结点的个数
		"""
		pass
		
	def data(self):
		"""
			取出树根中存储的数据
		"""
		pass
		
	def first_child(self, node):
		"""
			取出树中结点node的第一颗子树
		"""
		pass
		
	def children(self, node):
		"""
			取出树中结点node的各子树的迭代器
		"""
		pass
	
	def set_first(self, tree):
		"""
			用tree取代原来的第一颗子树
		"""
		pass
		
	def insert_child(self, i, tree):
		"""
			将tree设置为第i棵子树，其他子树顺序后移
		"""
		pass
		
	def traversal(self):
		"""
			遍历树中各结点之数据的迭代器
		"""
		pass
		
	def forall(self, op):
		"""
			对树中的每个结点的数据执行操作op
		"""
		pass
		

"""
	遍历树：
		开始：将树根加入队列
		过程：重复以下动作直到队列为空
			1、弹出队列里的首结点并访问
			2、将该结点的子结点顺序加入队列
			
	深度搜索：
		先根序列
		后根序列
	
	广度搜索：
"""


"""
	树表示方法：
		子结点引用表示法：
			子指针表示法：
				用一个数据单元表示结点，通过结点间的链接表示树结构
				考虑支持度数不超过m的
			实现：
				每个结点用一个list对象实现
		
		父结点引用表示法：
			利用除根结点外，每个结点只有一个父结点的特性
			
			实现：
				用一个顺序表表示树，每个表元素对应于一个结点，包含两部分：
					结点数据和父结点引用
		
		子结点表表示法：
			每个结点关联一个子结点表，记录树的结构
			
			实现：
				一种单元表示结点：结点数据和子结点表头指针的二元组
				另一种子结点表的结点单元
		
		长子 - 兄弟表示法：
			树的二叉树表示
			每个树结点对应二叉树的一个结点
			特性：
				二叉树中结点d的左子结点是原树中d的第一个子结点
				二叉树中右子结点是原树中d的下一个兄弟结点
"""

# 树的具体实现
# 包含两个成员的表（结点，子树序列）

class SubtreeIndexError(ValueError):
	pass
	

# 树结点表示类
def Tree(data, *subtrees):
	"""
		subtrees:序列参数
	"""
	# !!! extend内部实现没有返回值
	data = list(data)
	data.extend(subtrees)
	return data
	
# 其他操作参数
# None表示空树

# 判断空树操作
def is_empty_tree(tree):
		return tree is None
		
# 查根结点数据
def root(tree):
	return tree[0]
	
def subtree(tree, i):
	if i<1 or i>len(tree):
		raise SubtreeIndexError
	return tree[i+1]
	
def set_root(tree, data):
	tree[0] = data
	
def set_subtree(tree, i, subtree):
	if i<1 or i> len(tree):
		raise SubtreeIndexError
	tree[i+1] = subtree
	

# 树的类实现
class TreeNode(object):
	"""树结点类：
		数据域+子结点域
	"""
	
	def __init__(self, data, subs=[]):
		self._data = data
		self._subtrees = list(subs)
		
	def __str__(self):
		return "[Treenode {0} {1}]".format(self._data, self.subtrees)
	
def test_list_tree():
	tree1 = Tree('+', 1, 2, 3)
	
	print(tree1)
	
	tree2 = Tree('*', tree1, 6,8)
	print(tree2)
	
	set_subtree(tree1, 2, Tree('+', 3, 5))
	print(tree1)
	
def test_tree_class():
	pass
	

if __name__ == "__main__":
	test_list_tree()
	

		
		
		

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
二叉排序树：
	左子树的所有结点中保存的关键码值小于根结点的值
	右子树的所有结点中保存的关键码值大于根结点的值
	
	
	通过中根序的递增序列
"""

def bt_search(btree, key):
	"""基于二叉树查询操作"""
	
	bt = btree
	
	while bt is not None:
		entry = bt.data
		
		if key < entry.key:
			bt = bt.left
		elif key > entry.key:
			bt = bt.right
		else:
			return entry.values
	return None

	

class BinTNode(object):
	"""
		二叉树结点类
		没有子结点用None表示
		空二叉树直接用None表示
	"""
	
	def __init__(self, dat, left=None, right=None):
		self.data = dat		# 结点数据 key -- values
		self.left = left		# 左结点
		self.right = right	# 右结点
	
class Assoc(object):
	""" 关联对象
		data数据对象
	"""
	
	def __init__(self, key, value):
		self.key = key
		self.value = value
		
	def __lt__(self, other):
		""" 有些操作考虑到序 """
		return self.key < other.key
		
	def __le__(self, other):
		return self.key < other.key or self.key == other.key
		
	def __str__(self):
		""" 定义字符串表示形式便于输出与交互 """
		return "Assoc({0}, {1})".format(self.key, self.value)
		

class DictBinTree(object):
	""" """
	
	def __init__(self):
		self._root = None
		
	def is_empty(self):
		""" 判空 """
		return self._root is None
		
	def search(self, key):
		""" 查询操作 """
		
		bt = self._root
		while bt is not None:
			entry = bt.data
			if key < entry.key:
				bt = bt.left
			elif key > entry.key:
				bt = bt.right
			else:
				return entry.values
		return None
		
	def insert(self, key, value):
		"""
			插入操作
			当关键码相同时替换其对应的关联值
		"""
		bt = self._root
		if bt is None:
			self._root = BinTNode(Assoc(key, value))
			return
		while True:
			entry = bt.data
			if key < entry.key:
				if bt.left is None:
					bt.left = BinTNode(Assoc(key, value))
					return
				bt = bt.left
			elif key > entry.key:
				if bt.right is None:
					bt.right = BinTNode(Assoc(key, value))
					return
				bt = bt.right
			else:
				bt.data.value = value		# 这样干是不合理的
				return
			
	def values(self):
		""" 遍历值生成器 """
		t, s = self._root, SStack()
		
		while t is not None or not s.is_empty():
			while t is not None:
				s.push(t)
				t = t.left
			t = s.pop()
			yield t.data.value
			t = t.right
			
	def entries(self):
		""" 遍历字典序对(key-value) """
		t, s = self._root, SStack()
		
		while t is not None or not s.is_empty():
			while t is not None:
				s.push(t)
				t = t.left
			t = s.pop()
			yield t.data.key, t.data.value
			t = t.right
			
	# 删除操作
	def delete(self, key):
		"""删除操作"""
		p, q = None, self._root			# 维持p为q的父结点
		while q is not None and q.data.key != key:
			p = q
			if key < q.data.key:
				q = q.left
			else: 
				q = q.right
		if q is None:		# 树中没有关键码key
			return
		# q引用要删除结点， p是其父结点或None（这时q是根结点）
		if q.left is None:		# 如果q没有左子结点
			if p is None:			# q是根结点，修改_root
				self._root = q.right
			elif q is p.left:		# 根据q和p的关系修改p的子树引用
				p.left = q.right  #TODO 这里不能保证其值一定小于其值？？？？？
			else:
				p.right = q.right
				
			return
		r = q.left			# 找到q左子树的最右结点
		
		while r.right is not None:
			r = r.right
		r.right = q.right
		if p is None:			# q是根结点，修改_root
			 self._root = q.left
		elif p.left is q:
			p.left = q.left
		else:
			p.right = q.left
			
	def print(self):
		for k, v in self.entries():
			print(k, v)
			
def build_dictBinTree(entries):
	""" 建立一棵二叉排序数 """
	dic = DictBinTree()
	for k, v in entries:
		dict.insert(k, v)
	return dic
			
			
# 最佳二叉排序树 -- 比较最少

# 平均检索长度

# 扩充二叉排序树的对称序列

class DictOptBinTree(DictBinTree):
	""" 最佳二叉排序树 """
	
	def __init__(self, seq):
		DictBinTree.__init__(self)
		data = sorted(seq)
		self._root = DictOptBinTree.buildOBT(data, 0, len(data) -1)
		
	@staticmethod
	def buildOBT(data, start, end):
		if start > end:
			return None
		mid = (end + start) // 2
		left = DictOptBinTree.buildOBT(data, start, mid-1)
		right = DictOptBinTree.buildOBT(data, mid+1, end)
		return BinTNode(Assoc(*data[mid]), left, right)
		
		
			
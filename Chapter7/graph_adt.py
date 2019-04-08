#!/usr/bin/env python3
# -*- coding:utf-8 -*-


class GraphAdt(object):
	"""
		图的抽象数据类型
		出度
		入度
		
		遍历：
			1、图中可能存在回路
			2、图有可能不连通，要考虑初始顶点不可达的部分
			
		主要考虑边与顶点的邻接关系和顶点间的邻接关系
	"""
	
	def __init__(self):
		# 可以根据需要添加一些初始化操作
		pass
		
	def is_empty(self):
		"""
			判空
		"""
		pass
		
	def vertex_num(self):
		"""
			取图中顶点的个数
		"""
		pass
		
	def edge_num(self):
		"""
			取图中边的条数
		"""
		pass
		
	def vertices(self):
		"""
			取得图中顶点的集合
		"""
		pass
		
	def edges(self):
		"""
			取得图中边的集合
		"""
		pass
		
	def add_vertex(self, vertex):
		"""
			将顶点vertex加入此图中
		"""
		pass
		
	def add_edge(self, v1, v2):
		"""
			将从v1到v2的边加入图中
		"""
		pass
		
	def get_edge(self, v1, v2):
		"""
			查询v1到v2的边相关的信息，没有时返回特殊值
		"""
		pass
		
	def out_edges(self, v):
		"""
			取得从v出发的所有的边
		"""
		pass
	
	def degree(self, v):
		"""
			检查v的度
		"""
		pass
		
"""
	图表示方法：
		邻接矩阵：V*V的矩阵：特殊值表示无边
			矩阵中的行对应出边，列对应入边
			非零的个数对应出度和入度
			缺点：存储太多的无用信息
			
		邻接矩阵压缩版：
			邻接表表示法：	只是记录它的出边
				每个顶点关联一个边表，结点里记录该边终点的下标
				一个边关联的边的表长度就是它的长度
				
			
			邻接多重表表示法
			
			图的十字链表表示法
			
"""

# 定义两个表示图的类
# inf = float("inf") 	# inf的值大于任何float类型的值

# 邻接矩阵的实现

class Graph(object):
	"""
		图的邻接矩阵的实现
	"""
	
	def __init__(self, mat, unconn=0):
		"""
			mat: 传入的二维表参数
			unconn: 表示无边
		"""
		vnum = len(mat)
		
		for x in mat:
			if len(x) != vnum:		# 检查是否为方阵
				raise ValueError("Argument for 'Graph'")
		self._mat = [mat[i][:] for i in range(vnum)]		# 拷贝
		self._unconn = unconn
		self._vnum = vnum
		
	def vertex_num(self):
		"""
			顶点的个数
		"""
		return self._vnum
		
	def _invalid(self, v):
		# 检查下标的合法性
		return 0 > v or v >= self._vnum
		
	def add_vertex(self):
		# 目前不支持增加新的结点
		# 由于矩阵方式实现时，插入复杂度较高
		raise ValueError("Adj - Matrix does not support 'add_vertex'.")
		
	def add_edge(self, vi, vj, val=1):
		# 增加一条新的链路
		if self._invalid(vi) or self._invalid(vj):
			raise ValueError(str(vi) + 'or' + str(vj) + " is not a valid vertex.")
		self._mat[vi][vj] = val
		
	def get_edge(self, vi, vj):
		# 读取两结点的链接关系状态
		if self._invalid(vi) or self._invalid(vj):
			raise ValueError(str(vi) + 'or' + str(vj) + " is not a valid vertex.")
			
		return self._mat[vi][vj]
	
	def out_edges(self, vi):
		if self._invalid(vi):
			raise ValueError(str(vi) + " is not valid vertex.")
		return self._out_edges(self._mat[vi], self._unconn)
		
	@staticmethod
	def _out_edges(row, unconn):
		# 读取图的边具体实现
		edges = []
		for i in range(len(row)):
			if row[i] != unconn:
				edges.append((i, row[i]))
		return edges
		
	def __str__(self):
		# 类对象输出时的格式
		return "[\n" + ", \n".join(map(str, self._mat)) + "\n]" + "\nUnconnected: " + str(self._unconn)
		

"""
	邻接表的实现：
		1、每个顶点的邻接边用一个list对象表示
		2、元素形式为：(v,w) w为边的权重信息
		
"""

class GraphAL(Graph):
	"""
		图的邻接表的实现
	"""
	
	def __init__(self, mat=[], unconn=0):
		"""
			支持通过空图构建所需图对象
		"""
		vnum = len(mat)
		
		for x in mat:
			if len(x) != vnum:
				raise ValueError("Argument for 'GraphAL'.")
		self._mat = [Graph._out_edges(mat[i], unconn) for i in range(vnum)]
		self._vnum = vnum
		self._unconn = unconn
		
	def add_vertex(self):		# 增加新顶点时安排一个编号
		"""
			增加一个新的顶点到图中
		"""
		self._mat.append([])
		self._vnum += 1
		return self._vnum - 1
		
	def add_edge(self, vi, vj, val=1):
		"""
			增加一条新的边
			加入的新边按照邻接矩阵的下标顺序排列
		"""
		if self._vnum == 0:
			raise ValueError("Cannot add edge to empty graph.")
		if self._invalid(vi) or self._invalid(vj):
			raise ValueError(str(vi) + 'or' + str(vj) + " is not valid vertex.")
			
		row = self._mat[vi]
		i = 0
		while i < len(row):
			if row[i][0] == vj:		# 修改mat[vi][vj]的值
				self._mat[vi][i] = (vj, val)
				return
			if row[i][0] > vj:		# 原来没有到vj的边，退出循环后加入边
				break
		self._mat[vi].insert(i, (vj, val))
		
	def get_edge(self, vi, vj):
		"""
			取得两点之间的边
		"""
		if self._invalid(vi) or self._invalid(vj):
			raise ValueError(str(vi) + ' or ' + str(vj) + "  is not a valid vertex.")
			
		for i, val in self._mat[vi]:
			if i == vj:
				return val
		return self._unconn
		
	def out_edges(self, vi):
		"""
			输出一个顶点的所有的边（对应的list对象）
		"""
		if self._invalid(vi):
			raise ValueError(str(vi) + " is not a valid vertex.")
			
		return self._mat[vi]
		
		
		

		
		
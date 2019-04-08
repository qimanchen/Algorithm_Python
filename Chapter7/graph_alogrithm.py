#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from stack_adt import SStack

"""
	图的遍历：
		深度优先遍历：从指定顶点v出发
			1、先访问顶点v，并标记
			2、检查v的邻接顶点，从中选择一个尚未访问的顶点
			从它出发继续执行搜索算法，不存在这种邻接顶点时，回溯
			3、重复执行以上的操作，直到从v出发可达所有顶点都已访问
			4、如果图中还有未访问的顶点，则选出一个未访问顶点，由它出发
			直到访问到所有结点
			
		DFS序列
		
		宽度优先遍历 BFS
			1、先访问顶点v，并标记
			2、依次访问v的所有的相邻顶点，再依次访问这些相邻顶点
			所邻接的所有未访问过的顶点，直到所有的顶点都被访问了
			3、如果图中还存在未访问的顶点，选择一个顶点，重复以上的操作
			直到所有的结点访问完毕
			
	
"""

# DFS序列实现
def DFS_graph(graph, v0):
	"""
		非递归实现
		graph: 图实例化对象
		v0：指定的起始顶点
	"""
	vnum = graph.vertex_num()
	visited = [0] * vnum		# visited记录已访问顶点
	visited[v0] = 1
	
	DFS_seq = [v0]		# 记录遍历序列
	
	st = SStack()
	st.push((0, graph.out_edges(v0)))		# 入栈(i, edegs), 说明
	while not st.is_empty():		# 下次应访问边edges[i]
		i, edges = st.pop()
		
		if i < len(edges):
			v, e = edges[i]
			st.push((i+1, edges))		# 下次回来将访问edges[i+1]
			if not visited[v]:			# v未访问，访问并记录其可达顶点
				DFS_seq.append(v)
				visited[v] = 1
				st.push((0, graph.out_edges(v)))
				# 下面访问的边组
	return DFS_seq
	
"""
	生成树：
		从有根有向图任意顶点出发，到图中其他各个顶点都存在路径
	
	性质：
		G中有n个顶点，必然有一个包含n-1条边的边集合，它包含了从v0到其他所有顶点的路径
		
		如果一个图有生成树，则其生成树可能不唯一
		
		n个顶点的连通图G的生成树包含恰好n-1条边，无向图就是G的一个最小连通子图 -- 无环图
		有向图的生成树中所有的边都位于从根到其他顶点的路径上
		
	生成树的边：
		一个顶点可能有多个”下一顶点“
		每个顶点至多有一个”前一顶点“
		假设有vnum个元素：
			表项 span_forest[vi] -- (vj, e) vj为从v0到vi的前一顶点，e是vj到vi的邻接边的信息
			
"""

# DFS生成树：递归算法
def DFS_span_forest(graph):
	""" """
	
	vnum = graph.vertex_num()
	span_forest = [None]*vnum
	
	def dfs(graph, v):		# 递归遍历函数， 在递归中记录经由边
		nonlocal span_forest		# span_forest是nonlocal变量
		for u, w in graph.out_edges(v):		# 针对v顶点的边操作
			if span_forest[u] is None:
				span_forest[u] = (v, w)
				dfs(graph, u)
	for v in range(vnum):
		if span_forest[v] is None:
			span_forest[v] = (v, 0)
			dfs(graph, v)
	return span_forest


"""
	最小生成树：
		一颗生成树中各条边的权值之和称为：该生成树的权
		
		权值最小的生成树：最小生成树
		
		各顶点到自身：0
		无边时权值：inf
		
	Kruskal算法：
		1：取G中所有n个顶点，构造没有任何边的孤立顶点子图 T = (V, {})
		
		2：将E中的边按权值递增的顺序排序，取权值最小且最短的边加入到T中
			  
		3：重复第2步，直到T中所有顶点都包含在一个连通分量里
		
		T = (V, {})
		while T中所含边数小于n-1：
			从e中选取当前最小边（u，v), 将它从E中删除
			if (u, v)两端点属于T的不同连通分量：
				将边加入T
				
		需要解决的问题：
			1、最短边的选取：
				每次扫描剩下的边，选出最短的边
				先将边排序后顺序选取
				使用一个优先对列
			2、如何判断两个顶点在当时T里属于不同连通分量：
				检查两顶点之间是否存在路径
				
				每个连通分量确定一个代表元，代表元相同则属于同一连通分量
				
		
		
		
"""

# Kruskal算法：
def Kruskal(graph):
	""" 最小生成树实现"""
	
	vnum = graph.vertex_num()
	
	reps = [ i for i in range(vnum)]
	
	mst, edges = [], []
	
	for vi in range(vnum):		# 所有边加入表edges
		for v, w in graph.out_edges(vi):
			edges.append((w, vi, v))
			
	edges.sort()		# 边按权值排序，O(nlogn)时间
	for w, vi, vj in edges:
		if reps[vi] != reps[vj]:		# 两端点属于不同连通分量
			mst.append(((vi, vj), w)	)	# 记录这条边
			if len(mst) == vnum -1:		# V -1条边，构造完成
				break
			rep, orep = reps[v], reps[vj]
			for i in range(vnum):		# 合并连通分量，统一代表元
				if reps[i] == orep:
					reps[i] = rep
					
	return mst
	
"""

	Prim算法：
		1、构造子集U，边集合E
		2、检查出权值最小，并且另一端点不属于U，将它加入到U和E中
		3、直到len(U) == len(V)
		
	
"""

def Prim(graph):
	""" Prim算法实现"""
	vnum = graph.vertex_num()
	
	mst = [None] *vnum
	
	cands = PrioQueue([(0, 0, 0)])		# 记录候选边 (w, vi, vj)
	
	count = 0
	
	while count < vnum and not cands.is_empty():
		w, u, v = cands.dequeue()		# 取当时的最短边
		if mst[v]:
			continue		# 邻接顶点v已在mst，继续
		mst[v] = ((u,v), w)		# 记录新的mst边和顶点
		count += 1
		
		for vi, w in graph.out_edges(v):			# 考虑v的邻接顶点vi
			if not mst[vi]:		# 如果vi不在mst则这条边是候选边
				cands.enqueue((w, v, vi))
				
	return mst
	

"""
	Prim算法的改进：
		避免将一些无效的边加入优先对列中
		
"""

def PrimProv(graph):
	vnum = graph.vertex_num()
	
	wv_seq = [ [ graph.get_edge(0, v), v, 0] for v in range(vnum)]
	
	connects = DecPrioHeap(wv_seq)		# 连接的顶点堆，V个元素
	mst = [None] * vnum
	
	while not connects.is_empty():
		w, mv, u = connects.getmin()		# 取得最近顶点和连接边
		if w == infinity:			# 最近顶点不连通，该图没有生成树
			break
		mst[mv] = ((u, mv), w)		# 新的mst边
		
		for v, w in graph.out_edges(mv):		# 检查mv的邻接边
			if not mst[v] and w < connects.weight(v):
				connects.dec_weight(v, w, mv)		# 更短就修改
				
	return mst
	
	

		
		

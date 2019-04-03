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

	
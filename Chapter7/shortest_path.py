#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
	最短路径：
		从顶点vi到vj的一条路径上各条边的长度之和称为该路径的长度
		
		而长度最短的为最短路径
		
	
	Dijkstra算法：
		要求图中所有边的权不小于0
		
		将图中的顶点分为两个集合：
			当时已知最短路径的顶点集合 U，以及顶点集合V-U（不知道最短路径）
			
			算法执行过程中不断的扩充集合U（最短的路径的顶点更新）
			
	算法执行：
		1、 集合U中存入初始顶点v0
		2、对V-U中的每个顶点 v，如果存在直接的边，则到v的已知最短路径设为w(v0, v)
			  否则设置为inf
		3、congV-U中选出当时已知最短路径长度最小的顶点Vmin加入，测试最短 （重复执行）
		4、若发现新发现的路径比原来的更短，则更新最短路径，重复执行直到所有的顶点都在U中
		如果直到最后还存在未加入U中顶点，则说明，被处理的图不连通
		
	最短路径中前段也是最短路径
		
"""

def Dijkstra(graph, v0):
	"""
		如何记录从v0到各顶点的最短路径
	"""
	vnum = graph.vertex_num()
	
	assert 0 <= v0 < vnum
	paths = [None] * vnum
	
	count = 0
	
	cands = PrioQueue([(0, v0, v0)])		# 初始队列
	while count < vnum and not cands.is_empty():
		plen, u, vmin = cands.dequeue()		# 取路径最短顶点
		if paths[vmin]:
			continue		# 如果其最短路径已知则继续
		paths[vmin] = (u, plen)
		
		for v, w in graph.out_edges(vmin):		# 考察经由新U顶点的路径
			if not paths[v]:		# 是到尚未知最短路径的顶点的路径，记录它
				cands.enqueue((plen+w, vmin, v))
				
		count += 1
	return paths
	
	
"""
	Floyd算法
		
"""

def all_shortest_paths(graph):
	
	vnum = graph.vertex_num()
	
	a = [ [ graph.get_edge(i, j) for j in range(vnum)] for i in range(vnum)]		# create a copy
	
	nvertex = [ [-1 if a[i][j] == inf else j for j in range(vnum)] for i in range(vnum)]
	
	for k in range(vnum):
		for i in range(vnum):
			for j in range(vnum):
				if a[i][j] > a[i][k] + a[k][j]:
					a[i][j] = a[i][k] + a[k][j]
					nvertex[i][j] = nvertex[i][k]
					
	return (a, nvertex)
	
	
	
	
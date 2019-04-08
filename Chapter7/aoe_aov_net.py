#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from graph_adt import GraphAL

"""
	有向图：图中顶点表示某个有一定规模的”工程“里的不同活动，
					 图中的边表示各项活动之间的先后顺序关系
	顶点活动图：AOV
	
	拓扑排序
	拓扑序列
	
	拓扑序列反向得到的序列 -- 逆网
	
	任何无环的AOV网N都可以做出拓扑序列：
		1、从N中选出一个入度为0的顶点作为序列的下一顶点
		2、从N网中删除所选顶点及其所有的出边
		3、反复执行上面两步，直到选出所有图中结点，或者再也找不到入度非0的顶点时算法结束
		
		

"""

def toposort(graph):
	""" """
	vnum = graph.vertex_num()
	
	indegree, toposeq = [0]*vnum,  []
	
	zerov = -1
	
	for vi in range(vnum):		# 建立初始入度表
		for v, w in graph.out_edges(vi):
			indegree[v] += 1
			
	for vi in range(vnum):		# 建立初始的0度表
		if indegree[vi] == 0:
			indegree[vi] = zerov
			zerov = vi
			
	for n in range(vnum):		# 不存在拓扑序列
		if zerov == -1:
			return False
		vi = zerov		# 从0度表弹出顶点vi
		zerov = indegree[zerov]
		
		toposeq.append(vi)			# 把一个vi加入拓扑序列
		for v, w in graph.out_edges(vi):		# 检查vi的出边
			indegree[v] -= 1
			
			if indegree[v] == 0:
				indegree[v] = zerov
				zerov = values
	return toposeq
	
def test_toposort():
	
	graph = GraphAL()
	
	for i in mat:
		graph.add_vertex()
	
	# 增加对应的边
	graph.add_edge(1, 5)
	graph.add_edge(1, 4)
	graph.add_edge(1, 3)
	
	graph.add_edge(2, 3)
	graph.add_edge(2, 6)
	
	graph.add_edge(3,6)
	graph.add_edge(3, 8)

	graph.add_edge(4, 6)
	graph.add_edge(4, 7)
	graph.add_edge(4, 8)
	
	graph.add_edge(5,7)
	
	graph.add_edge(6, 8)
	
	graph.add_edge(7, 9)
	graph.add_edge(7, 10)
	
	graph.add_edge(8, 8)
	graph.add_edge(8, 10)
	
	print(toposort(graph))
	
	
	
	
"""

	AOE网：带权有向图
	
		顶点表示事件，有向边表示活动，边上的权值表示活动的持续时间
		入边表示的活动已经完成，出边表示活动可以开始的那个状态 -- 事件
		
	AOE网中描述的活动可以并行的进行，只要活动的前提事件均已发生
	
	
	从开始顶点到完成顶点最长路径的长度  -- AOE网的关键路径
	
	
"""



if __name__ == "__main__":
	test_toposort()
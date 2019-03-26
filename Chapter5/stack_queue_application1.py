#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from stack_adt import SStack
from queue_adt import SQueue

"""
	迷宫求解:
		
	状态空间搜索问题：
		1、存在一集可能状态 -- 迷宫中所有的位置
		2、有一个初始状态，一个或多个结束状态，或有判断成功结束的方法 --迷宫入口：初始状态，出口：结束状态
		3、对于每个状态s，都有临近的一组状态 -- 迷宫中相邻的四个方向
		4、有一个判断函数判断s是否可行 -- 迷宫中的passable函数
		5、问题：找出从s0出发到某个结束状态的路径，或找到全部的解
		
	后进先出 -- 栈 -- 回溯
	先进先出 -- 齐头并进
	
"""

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]		# (i, j) -- E, S, W, N
	
	
def mark(maze, pos):		# 给迷宫maze的位置pos标2，表示 ”到过了“
	maze[pos[0]][pos[1]] = 2
		
def passable(maze, pos):		# 检查迷宫maze的位置pos是否可行
	return maze[pos[0]][pos[1]] == 0
		
		
# 递归求解
def find_path(maze, pos, end):
	mark(maze, pos)
		
	if pos == end:		# 已到达出口
		print(pos, end=" ")		# 输出这个位置
		return True		# 成功结束
	for i in range(4):		# 是否按四个方向顺序探查
		nextp = pos[0] + dirs[i][0], pos[1] + dirs[i][1]
		# 考虑下一个可能的方向
		if passable(maze, nextp):		# 不可行的相邻位置不管
			if find_path(maze, nextp, end):		# 从nextp可达出口
				print(pos, end=" ")		# 输出这个点
				return True		# 成功结束
				
	return False
	
	
# 栈与回溯法
def maze_solver(maze, start, end):
	if start == end:
		print(start)
		return
	st = SStack()
	mark(maze, start)
	
	st.push((start, 0))		# 入口和方向0的序对入栈
	
	while not st.is_empty():		# 走不通时回退
		pos, nxt = st.pop()
		for i in range(nxt, 4):		# 依次检查未探查的方向
			nextp = (pos[0] + dirs[i][0], pos[1] + dirs[i][1])		# 计算出下一位置
			if nextp == end:		# 到达出口，打印路径
				print_path(end, pos, st)
			
			if passable(maze, nextp): 		# 遇到未探查的新位置
				st.push((pos, i+1))		# 原位置和下一方向入栈
				mark(maze, nextp)
				st.push((nextp, 0))		# 新位置入栈
				break		# 退出内存循环，下次迭代将以新栈顶为当前位置继续
				
	print("No path found. ")
	
def print_path(end, pos, st):
	"""打印出寻找得到的路径"""
	pass
	
# 队列与迷宫
def maze_solver(maze, start, end):
	if start == end:		# 特殊情况
		print("Path finds.")
		return
	qu = SQueue()
	mark(maze, start)
	
	qu.enqueue(start)		# start位置入队
	
	while not qu.is_empty():		# 还有侯选位置
		pos = qu.dequeue()		# 取出下一个位置
		for i in range(nxt, 4):		# 依次检查未探查的方向
			nextp = (pos[0] + dirs[i][0], pos[1] + dirs[i][1])		# 计算出下一位
			
			if passable(maze, nextp): 		# 遇到未探查的新位置
				if nextp == end:		# 到达出口，打印路径
					print("Path find.")		# 成功
					return
				mark(maze, nextp)
				qu.enqueue(nextp)		# 新位置入栈
				
	print("No path found. ")		# 没有找到路径，失败
	
	

	
	
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
	优先队列
		队列中的每项数据都另外赋有一个数值 -- 优先级
		
		保证每次弹出的都是优先级最高的
		
		相同优先级的根据内部实现操作
		
	实现：
		创建，判断空（清空内容，确定当前元素的个数）
		插入元素，访问和删除优先队列（当时最优先）的元素
"""


# 基于连续表实现
"""
	两种实现方案：
		1、采用有组织（顺序）存放，存入元素麻烦，但访问和弹出方便
		2、无组织，存入快，但访问和弹出不方便
		
"""

# 效率低的原因：
"""
	沿着顺序检索插入位置必然需要检索，而检索的长度为O(n)
	使用线性表，必然遇到此种问题
"""

# 基于list实现优先队列
class PrioQueueError(ValueError):
	pass
	

class PrioQue(object):
	"""
		list实现
		优先队列类
	"""
	
	def __init__(self, elist=[]):
		# 对实参表做拷贝，避免共享
		# 实参可以时任何可迭代对象
		self._elems = list(elist)
		
		# 使用reverse表示从大到小排序 -- 较小的优先
		self._elems.sort(reverse=True)
		
	def enqueue(self, e):
		i = len(self._elems) - 1
		while i >= 0:
			if self._elems[i] <= e:
				i -= 1
			else:
				break
		# insert 插入表示在指定位置插入
		# 当 index值等于len(list)时，表示插入到list结尾
		self._elems.insert(i+1, e)
		
	def is_empty(self):
		"""判空"""
		return not self._elems
		
	def peek(self):
		"""弹出队列中优先度高的元素,但不删除"""
		if self.is_empty():
			raise PrioQueueError(" in top")
		return self._elems[-1]
		
	def dequeue(self):
		"""弹出队列中优先度高的元素，同时删除"""
		if self.is_empty():
			raise PrioQueueError(" in pop ")
		return self._elems.pop()
		
	
# 堆及其性质
"""
	采用树形结构实现优先队列的技术  --  堆
	
	结构上： 堆就是存储数据的完全二叉树
	
	堆中的数据的存储满足一种特殊顺序：
		任意结点里所存的数据先于或等于其子结点（如果存在）里的数据
		
	性质：
		1、堆中树根到任意叶结点的路径上，各结点所存储的数据按规定的优先关系（非严格）递减
		2、堆中最优先的元素必定位于二叉树的根结点（堆顶）， O(1)时间
		3、位于树中不同路径上的元素，不必关心其顺序关系
	
	小顶堆：
		小元素优先，堆顶为小元素，每个结点的数据小于或等于其子结点的数据
	
	大堆顶：
		大元素优先，堆顶为大元素，每个结点的数据大于或等于其子结点的数据
		
	堆和完全二叉树的性质;
	连续表中的存储，通过广度优先存储
		1、在堆的最后添加一个元素（连续表最后），整个结构还可以看作一颗完全二叉树，但不一定是堆
		2、一个堆去掉堆顶（表中位置为0的元素），其余元素形成的子堆，下标计算规则任然可用，堆序任然成立
		3、由2得到的表（子堆）加入一个根元素，得到的结点序列又可以看作完全二叉树，但未必是堆
		4、去掉堆中最后的元素，剩下的元素仍然为堆
"""


# 堆实现优先队列

"""
	问题：以下两个操作都是 O(log n)时间内完成的
		1、如何实现插入元素：向堆中加入一个新元素，通过相应的操作，
			   得到一个包含了所有原有元素和新添加元素的堆
		
		2、如何实现弹出元素的操作：从堆中弹出最小元素，必须把剩余元素重新构成堆
	
	解决方法：
		筛选：
			1、向上筛选：
				不断用新加入的元素（e）与其父结点的数据比较，如果e较小就交换两元素的位置；
				知道e的父结点的数据小于等于e，或e到达根结点
				
				操作：
					1、把新加入的元素加入到已有元素之后（连续表），执行一次向上筛选
					2、向上筛选操作中比较和交换的次数不超过最长路径的长度 
					O(log n)
					
			2、向下筛选:
				从原堆取出一个元素（堆顶），从对尾拿出一个元素加入到堆顶
				
				子堆A， B，加上根元素构成一个完全二叉树，重构成堆：
					1、用e与A、B两个子堆的顶元素比较，最小者作为堆顶
						a、若e不是最小，最小的必然为A或B的根，若A的根最小，将其移到堆顶
						b、把e放入A的堆顶，同样操作（规模更小）
						
					2、如果某次比较中e最小，以它为顶的局部树已成为堆，结束
					3、若e到底，结束
					
	三大步骤：
		1、弹出当时的堆顶
		2、从堆最后取出一个元素作为完全二叉树的根
		3、执行一次向下筛选 O(log n)
"""

class PrioQueue(object):
	"""
		通过堆技术实现优先队列
		小堆顶
	"""
	
	def __init__(self, elist=[]):
		# 插入的是任意的list（没有排序的）
		self._elems = list(elist)
		if elist:
			# 将elist变为堆
			self.buildheap()
			
	def is_empty(self):
		""" 空list，not [] 返回True"""
		return not self._elems
	
	def peek(self):
		if self.is_empty():
			raise PrioQueueError(" in peek ")
		return self._elems[0]
		
	# 插入操作
	def enqueue(self, e):
		self._elems.append(None)		# 增加一个尾部元素
		self.siftup(e, len(self._elems)-1)		# 向上筛选
		
	def siftup(self, e, last):
		elems, i, j = self._elems, last, (last-1)//2
		while i > 0 and e < elems[j]:
			elems[i] = elems[j]
			i, j = j, (j-1)//2
			
		elems[i] = e
		
	# 删除操作
	def dequeue(self):
		if self.is_empty():
			raise PrioQueueError(" in dequeue")
		elems = self._elems
		
		e0 = elems[0]		# 需要弹出的元素
		
		e = elems.pop()	# 从对尾提取出的元素，需要插入队尾，执行向下筛选操作
		
		if len(elems) > 0:
			self.siftdown(e, 0, len(elems))
		return e0
		
	def siftdown(self, e, begin, end):
		"""采用拿着元素进行匹配，找到后再插入"""
		elems, i, j = self._elems, begin, begin*2 + 1
		
		while j < end:		# invariant:  j == 2*i + 1
			if j+1 < end and elems[j+1] < elems[j]:		# 每个根结点只有两各子结点
				j += 1		# elems[j] 不大于其他兄弟结点的数据
			if e < elems[j]:		# e在三者中最小，已找到位置
				break
			elems[i] = elems[j]		# elems[j] 在三者中最小，上移
			i, j = j, 2*j + 1
		elems[i] = e
	
	# 将list转换成堆（满足堆定义的完全二叉树）
	def buildheap(self):
		"""创建操作的复杂度是O(n)"""
		end = len(self._elems)
		for i in range(end//2, -1, -1):
			self.siftdown(self._elems[i], i, end)
			
# 堆排序
"""
	排序需要解决的问题：
		1、连续表中的初始元素不满足堆序 -- buildheap解决
		2、选出的元素存放在何处，能不能不用其他空间
"""

def heap_sort(elems):
	def siftdown(elems, e, begin, end):
		i, j = begin, begin*2 + 1
		
		while j < end: 		# invariant: j == 2*i + 1
			if j+1 < end and elems[j+1] > elems[j]:
				j += 1		# elems[j] 小于等于其他兄弟结点的数据
			if e > elems[j]: 		# e在三者中最小
				break
			elems[i] = elems[j]		# elems[j] 最小，上移
			i, j = j, 2*j+1
		elems[i] = e
	end = len(elems)
	
	# 建堆
	for i in range(end//2, -1, -1):
		siftdown(elems, elems[i], i, end)
	# 取出最小元素
	for i in range((end-1), 0, -1):
		# 求出的是升序
		e = elems[i]
		elems[i] = elems[0]
		siftdown(elems, e, 0, i)	
		
	return elems		# 返回排序结果
		
		
if __name__ == "__main__":
	print(heap_sort([9, 10, 3, 5, 90, 8]))
	
	
	
	

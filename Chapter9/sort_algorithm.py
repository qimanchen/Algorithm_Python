#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 记录结构
class Record(object):
	""" """
	
	def __init__(self, key, datum):
		self.key = key
		self.datum = datum
		
# 几种简单排序算法

"""
插入排序：
	起点：需要一个初始的已知的排序序列（空序列 或 只有一个元素的序列）
	
	具体实现：
		找到第i个元素在前段的插入位置
	
	插入排序：每次都要移动元素
	
	最重要的简单排序算法：
		实现简单
		自然的稳定性和适应性
		
"""

def insert_sort(lst):
	"""
		插入排序
		从小到大 -- 递增
		lst：需要排序的list
		lst中的每个元素为Recode对象
	"""
	for i in range(1, len(lst)):		# 开始时片段[0:1]已排序
		x = lst[i]		# 初始位置
		j = i			# 检测位置
		while  j > 0 and lst[j-1].key > x.key:
			lst[j] = lst[j-1]		# 反序逐个后移元素，确定插入位置
			j -= 1
			
		lst[j] = x

"""
选择排序：
	实现：
		1、所有记录中最小的i个记录的已排序序列
		2、每次从未排序的记录中选取关键码最小的记录，将其放在已排序的后面
		3、以空序列开始，直到尚未排序的部分只有一个元素
		
	如何选择元素
	
	尽可能的利用现有序列的存储空间
	
	直接选择排序：将简单的交换选出元素和未排序元素的最小值
	
	
	算法无适应性和稳定性
	
	解决稳定性：
		找到最小记录后，逐次后移k个位置之前的那些尚未排序的元素
"""

def select_sort(lst):
	"""
		选择排序
		每次检测的步骤是固定的
		
	"""
	for i in range(len(lst)-1):		# 只需要循环len(lst) - 1次
		k = i
		for j in range(i, len(lst)):		# k是已知最小元素的位置
			if lst[j] .key < lst[k].key:
				k = j
		if i != k:			# lst[k] 是确定的最小元素，检查是否需要交换
			lst[i], lst[k] = lst[k], lst[i]
			
# 选择排序的改进 -- 利用每次比较中的信息
# 堆排序
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
	for i in range(end//2, -1, -1):		# O(n)
		siftdown(elems, elems[i], i, end)
	# 取出最小元素
	for i in range((end-1), 0, -1):		# O(log n)
		# 求出的是升序
		e = elems[i]
		elems[i] = elems[0]
		siftdown(elems, e, 0, i)	
		
	return elems		# 返回排序结果
	
"""
交换排序：
	通过不断减少序列中的逆序
	
	不同的确定逆序的方法和交换方法
	
	起泡排序：
		通过交换元素消除逆序
		
		每一遍检查，都可以将一个较大元素交换到大区
	
	交错排序
		
"""

def bubble_sort(lst):
	"""
		冒泡排序
	"""
	for i in range(len(lst)):
		for j in range(1, len(lst)-i):
			if lst[j-1].key > lst[j].key:
				lst[j-1], lst[j] = lst[j], lst[j-1]
				
def bubble_sort_c(lst):
	"""
		冒泡排序的改进
	"""
		for i in range(len(lst)):
			found = False
			for j in range(1, len(lst) - i):
				if lst[j-1].key > lst[j].key:
					lst[j-1], lst[j] = lst[j], lst[j-1]
					found = True
			if not found:
				break

# 非简单排序			
"""
快速排序：
	基本思路：
		发现逆序，交换记录位置
		
	实现：
		以某种标准将记录划分为 -- 小记录和大记录
		1、选择一种标准将被排序的序列分为大小两组
		2、采用同样的方式，递归划分得到的这两组记录，并继续划分
		3、直到每个记录组中最多只包含一个的时候
		
	快速排序表的实现：
		分为两段，小记录左侧，大记录右侧
		
		划分规则：
			取序列中的第一个记录，比它小的放左侧，比它大的放右侧
			
		两种操作：
			空位在哪一方，对哪一方的发方向进行操作
			
"""

def quick_sort(lst):
	"""
		快排递归调用函数
		
		复杂度：
			平均 O(n log n)
			
		排序低效，是因为：分段不均
		
		三者取中：
			每趟划分前比较分段中 第一个、最后一个、位置居中的三个记录关键码
			取其中值居中的记录与首记录交换位置，而后基于这个记录的关键码划分
	"""
	qsort_rec(lst, 0, len(lst) - 1)
	
def qsort_rec(lst, l, r):
	"""
		快排实现函数
		lst: 需要操作的目标list
		l: 低位
		r: 高位
	"""
	
	if l >= r: 
		return lst		# 分段无记录或只有一个记录 -- 递归终止条件
	
	i = l
	j = r
	
	pivot = lst[i]		# lst[i] 为初始空位
	
	while i < j:		# 找pivot的最终位置
		# 用j向左扫描找小于pivot的记录并移动到左边
		while i < j and lst[j].key >= pivot.key:
			j -= 1
		if i < j:
			lst[i] = lst[j]	# 此时lst[i] 为空位
			i += 1		# 小记录移动左边
			
		# 用i向右扫描找大于pivot的记录并移动到右边	
		while i < j and lst[i] .key <= pivot.key:
			i += 1
		if i < j:
			lst[j] = lst[i]		# 此时lst[j] 为空位
			j -= 1		# 大记录移动右边
			
		lst[i] = pivot			# 将pivot 存入为其确定的最终位置
		qsort_rec(lst, l, i-1)		# 递归处理左半区
		qsort_rec(lst, i+1, r)		# 递归处理右半区
		
# 另一种简单实现
"""
	工作过程中分为三段：
		小记录、大记录、未检查记录
		
		两个下标：最后一个小记录小标 i，j第一个未处理记录的下标
		
		每次迭代比较K与记录j的关键码
		1、j较大，将j简单加1
		2、j较小，将记录调到左边，做法是i加1，而后交换i和j的位置，并将j值加一
		
		
"""
def quick_sort_1(lst):
	"""
	"""
	def qsort(lst, begin, end):
		if begin >= end:
			return
		pivot  = lst[begin].key
		i = begin
		for j in range(begin +1, end+1):
			if lst[j].key < pivot:		# 发现一个小元素
				i += 1
				lst[i], lst[j] = lst[j], lst[i] # 小元素换位
		lst[begin], lst[i] = lst[i], lst[begin]		# 枢轴元就位
		qsort(lst, begin, i-1)
		qsort(lst, i+1, end)
		
	qsort(lst, 0, len(lst) - 1)
	
"""
归并排序：
	归并：将两个或更多有序序列合并成为一个有序序列
	
	实现：
		1、把目标序列看成n个有序子序列
		2、将这些子序列两两归并，完成后序列个数减半
		3、对加长的子序列重复以上操作，最终得到一个长度为n的序列
		
		当留单时，就以它为一个有序序列
		
	最下层：
	
		
	二路归并排序
"""

# 最下层
def merge(lfrom, lto, low, mid, high):
	"""
		两分段归并操作
	"""
	i, j, k = low, m, low
	
	while i < mid and j < high:		# 反复复制两分段首记录中较小的
		if lfrom[i].key <= lfrom[j].key:
			lto[k] = lfrom[i]
			i += 1
		else:
			lto[k] = lfrom[j]
			j += 1
		k += 1
		
	while i < mid:		# 复制第一段剩余记录
		lto[k] = lfrom[i]
		i += 1
		k += 1
	while j < high:		# 复制第二段剩余记录
		lto[k] = lfrom[j]
		j += 1
		k += 1
		
def merge_pass(lfrom, lto, llen, slen):
	"""
		两分段持续操作
		llen 子分段长
		slen 分段开头
	"""
	i = 0
	while i + 2*slen < llen:		# 归并长slen的两段
		merge(lfrom, lto, i, i+slen, i + 2*slen)
		i += 2* slen
	# 两种特殊情况处理
	if i + slen < llen:		# 剩下两段，后段长度小于slen
		merge(lfrom, lto, i, i+slen, llen)
	else:			# 只剩下一段，复制到表lto中
		for j in range(i, llen):
			lto[j] = lform[j]
			
def merge_sort(lst):
	"""
		排序算法整体执行操作
	"""
	slen, llen = 1, len(lst)
	templst = [None]*llen
	
	while slen < llen:
		merge_pass(lst, templst, llen, slen)
		slen *= 2
		merge_pass(templst, lst, llen, slen)			# 结果放回原位
		slen *= 2
		

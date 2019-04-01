#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bin_tree_adt import BinTNode
from priority_queue import PrioQueue
"""
	扩充二叉树的权：
		与该结点有关的某种性质
		
	数据集，构成的T的带权外部路径长度WPL最小的扩充二叉树最小
	
	如果集合是huffman树，则交换任意一个或多个结点的左右子树，得到的仍然是huffman树
	
"""

class HTNode(BinTNode):
	"""
		继承二叉树结点类
		构造哈夫曼树的结点类
		增加一个小于操作
	"""
	def __lt__(self, othernode):
		return self.data < othernode.data
	

class HuffmanPrioQ(PrioQueue):
	"""
		哈夫曼算法使用的优先队列类
		增加检查元素个数的方法
	"""
	
	def number(self):
		return len(self._elems)
		
		
def HuffmanTree(weights):
	"""
		weights:
			可以是任意可迭代对象
		哈夫曼树实现：
			1、从优先队列中弹出两个权最小的元素
			2、基于所取的二叉树构造一颗新树，权值等于前两者之和，并将其入队
	"""
	trees = HuffmanPrioQ()	# 设置优先队列用于存储权重集合
	
	for w in weights:
		# 将集合中的元素存入优先队列中（从到小）
		trees.enqueue(HTNode(w))
	while trees.number() > 1:
		t1 = trees.dequeue()		# 取出最小的
		t2 = trees.dequeue()		# 取出次之的
		x = t1.data + t2.data		# 构造新结点的权重值
		trees.enqueue(HTNode(x, t1, t2))
	return trees.dequeue()

"""
	应用：
		哈夫编码：
			得到的哈夫曼树中，从各个分支结点到左子结点的边上标上二进制0，右子结点子树上标上1
			从根结点到叶结点路径上的二进制数字序列就是哈夫编码
			
																			33
																		0	
																	19				14
																0	
															9				10	7			7					
														0
													4				5			4		3				
												0		1
											2				2	
															
			
"""

if __name__ == "__main__":
	weights = [2, 3, 7, 4, 10, 2, 5]
	print(HuffmanTree(weights).data)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class StackUnderflow(ValueError):
	""" 栈下溢 -- 空栈访问"""
	pass
	
	
class LNode(object):
	
	def __init__(self, elem, next_=None):
		self.elem = elem
		self.next = next_

class SStack(object):
	"""
		栈的ADT
		基于顺序表实现栈类
	"""
	
	def __init__(self):
		"""
			创建空栈
			使用list对象 _elems存储栈中元素
			所有的栈操作都映射到list操作
		"""
		self._elems = []
		
	def is_empty(self):
		"""判断栈是否未空，空时返回True，否则返回False"""
		return self._elems == []
		
	def push(self, elem):
		"""将elem加入栈 -- 压栈，入栈"""
		self._elems.append(elem)
		
	def pop(self):
		"""删除栈中最后压入的元素，出栈"""
		if self._elems == []:
			raise StackUnderflow("in SStack.pop() ")
		return self._elems.pop()
		
	def top(self):
		"""取得栈内最后压入的元素，但不删除"""
		if self._elems == []:
			raise StackUnderflow("in SStack.top()")
		return self._elems[-1]
		
		
class LStack(object):
	"""
		栈的ADT
		基于链表实现
		1、以克服顺序表扩大内存时的高代价操作
		2、以克服顺序表需要连续的大块的内存
		
		缺点：
			链接节点的消耗
			节点分散分布的开销
	"""
	
	def __init__(self):
		"""
			创建空栈
			使用list对象 _elems存储栈中元素
			所有的栈操作都映射到list操作
		"""
		self._top = None
		
	def is_empty(self):
		"""判断栈是否未空，空时返回True，否则返回False"""
		return self._top is None
		
	def push(self, elem):
		"""将elem加入栈 -- 压栈，入栈"""
		self._top = LNode(elem, self._top)
		
	def pop(self):
		"""删除栈中最后压入的元素，出栈"""
		if self._top is None:
			raise StackUnderflow("in LStack.pop() ")
		e  = self._top.elem
		self._top = self._top.next
		return e
		
	def top(self):
		"""取得栈内最后压入的元素，但不删除"""
		if self._top is None:
			raise StackUnderflow("in LStack.top()")
		return self._top.elem

		
def test_SStack():
	st1 = LStack()
	st1.push(3)
	st1.push(5)
	while not st1.is_empty():
		print(st1.pop())

		
# 栈的useCase

# 1、翻转list
def rev_list(lst):
	"""翻转list"""
	st1 = SStack()
	
	for i in lst:
		st1.push(x)
	
	lst_rev = []
	
	while not st1.is_empty():
		lst_rev.append(st1.pop())
		
	return lst_rev
	
# 2、括号匹配问题
def check_parents(string):
	"""括号配对检查函数，string是被检查的正文串"""
	parents = "()[]{}"
	open_parents = "([{"
	opposite = {")": "(", "]": "[", "}": "{"}	# 标识符配对关系的字典
	
	def parentheses(string):
		"""括号生成器，每次调用返回string里的下一括号及其位置"""
		i, string_len = 0, len(string)
		while True:
			while i < string_len and string[i] not in parents:
				i += 1
			if i >= string_len:
				return
			yield string[i], i
			i += 1
			
	st = SStack()	# 保存括号的栈
	
	for pr, i in parentheses(string):	# 对string里各个括号和位置迭代
		if pr in open_parents:		# 开括号，压栈并继续
			st.push(pr)
		elif str(st.pop()) != opposite[pr]:		# 不匹配就是失败，退出
			print("Unmatching is found at ", i, "for", pr)
			return False
		# else: 这是一次括号匹配成功，什么都不做，继续
		
	print ("All parentheses are correctly matched.")
	return True
	

# 检测python程序中的括号
def check_parents_python(string):
	"""括号配对检查函数，string是被检查的正文串"""
	parents = "()[]{}"
	open_parents = "([{"
	close_parents = ")]}"
	opposite = {")": "(", "]": "[", "}": "{"}	# 标识符配对关系的字典
	
	def parentheses(string):
		"""括号生成器，每次调用返回string里的下一括号及其位置"""
		i, string_len = 0, len(string)
		while True:		
			while i < string_len and string[i] not in parents:
				# 判断注释类型1
				if string[i:i+3] == '"""':
					i += 2
					while True:
						if string[i:i+3] != '"""':
							i += 1
						else:
							i += 1
							break
				# 判断注释类型2
				if string[i:i+3] == "'''":
					i += 2
					while True:
						if string[i:i+3] != "'''":
							i += 1
						else:
							i += 1
							break
					
				# 判断解释语句 -- #
				if string[i] == '#':
					while True:
						i += 1
						if string[i] == '\n':
							i += 1
							break
				i += 1
				
			if i >= string_len:
				return
			yield string[i], i
			i += 1
			
	st = SStack()	# 保存括号的栈
	
	for pr, i in parentheses(string):	# 对string里各个括号和位置迭代
		if pr in open_parents:		# 开括号，压栈并继续
			st.push(pr)
		elif (pr in close_parents) and st.is_empty():
			print("Unmatching is found at ", i, "for", pr)
		elif st.pop() != opposite[pr]:		# 不匹配就是失败，退出
			print("Unmatching is found at ", i, "for", pr)
			return False
		# else: 这是一次括号匹配成功，什么都不做，继续
		
	print ("All parentheses are correctly matched.")
	return True
	
	
# 3、表达式的计算：
# 后缀表达式
class ESStack(SStack):
	"""拓展栈类，以求得栈的深度"""
	def depth(self):
		return len(self._elems)

def suf_exp_evaluator(exp):
	operators = "+-*/"
	st = ESStack()		# 拓展栈，实现depth方法
	
	for x in exp:
		if x not in operators:
			st.push(float(x))		# 不能转换将自动引发异常
			continue
		if st.depth() < 2:		# x必为运算符，栈元素不够时引发异常
			raise SyntaxError("Short of operand(s) .")
		a = st.pop()		# 取得第二个运算对象
		b = st.pop()		# 取得第一个运算对象
		
		if x == "+":
			c = b + a
		elif x == "-":
			c = b - a
		elif x == "*":
			c = b * a
		elif x == "/":		# 这里可能会引发异常ZeroDivisionError
			c = b / a
		else:
			break
		# else分支不可能出现
		
		st.push(c)
		
	if st.depth() == 1:
		return st.pop()
	raise SyntaxError("Extra operand(s) .")							
									
# 定义一个函数把表示表达式的字符串转化为项的表
def suffix_exp_evaluator(line):
	return suf_exp_evaluator(line.split())
	
	
def suffix_exp_calculator(line):
	while True:
		try:
			line = input("Suffix Expression: ")
			if line == "end": return
			res = suffix_exp_evaluator(line)
			print(res)
		except Exception as ex:
			print("Error:", type(ex), ex.args)
			
	
priority = { "(":1, "+":3, "-":3, "*":5, "/":5}
infix_operators = "+-*/()"		# 把 '(', ')' 也看作运算符，但特殊处理
	
# 中缀表示式  转换  后缀表达式
def trans_infix_suffix(line):
	
	st = SStack()
	exp = []
	
	for x in tokens(line):		# tokens 是一个定义的生成器
		if x not in infix_operators:		# 运算对象，直接送出
			exp.append(x)
		elif st.is_empty() or x == '(':		# 左括号进栈
			st.push(x)
		elif x == ')':		# 处理右括号的分支
			while not st.is_empty() and st.top() != '(':
				exp.append(st.pop())
			if st.is_empty():		# 没找到左括号，就是不配对
				raise SyntaxError("Missing '(' .")
			st.pop()		# 弹出左括号，右括号也不进栈
		else:		# 处理算术运算符，运算符看成左结合
			while (not st.is_empty() and
						priority[st.top()] >= priority[x]):
				exp.append(st.pop())
			st.push(x)		# 算术运算符进栈
			
	while not st.is_empty():		# 送出栈里剩余的运算符
		if st.top() == '(':		# 如果还有左括号，就是不配对
			raise SyntaxError("Extra '(' .")
		exp.append(st.pop())
	return exp

def tokens(line):
	"""生成器函数，逐一生成 line 中一个个项。
	项就是浮点数或运算符
	本函数不能处理一元运算符，也不能处理带符号的浮点数。"""
	i, llen = 0, len(line)
	
	while i < llen:
		while line[i].isspace():
			i += 1
		
		if i >= llen:
			break
		if line[i] in infix_operators:		# 运算符的情况
			yield line[i]
			i += 1
			continue
		j = i + 1		# 下面处理运算对象
		
		while (j < llen and not line[j].isspace() and
					line[j] not in infix_operators):
			if ((line[j] == 'e' or line[j] == 'e')		# 处理负指数
				and j+1 < llen and line[j+1] == '-'):
				j += 1
			j += 1
			
		yield line[i: j]		# 生成运算对象子串
		i = j
	
	
def test_trans_infix_suffix(s):
	print(s)
	print(trans_infix_suffix(s))
	print("Value: ", suf_exp_evaluator(trans_infix_suffix(s)))
	

# 4、栈与递归
"""
	递归定义：
		在一个定义中引用了被定义的对象的本身
		
	递归结构：
	
	递归调用
	
	递归定义的出口：递归的部分必须比原来的整体简单
	
	
"""
# 阶乘
def fact(n):
	"""
		需要一个栈来支持递归函数的运行：
		程序运行栈
		
		函数帧
	"""
	if n == 0:
		return 1
	else:
		return n*fact(n-1)
		
# 非递归的阶乘
def norex_fact(n):		# 自己管理栈，模拟函数的调用过程
	res = 1
	st = SStack()
	
	while n > 0:
		st.push(n)
		n -= 1
	while not st.is_empty():
		res *= st.pop()
		
	return res
	

# 5、简单背包问题：
"""
	问题描述：
		一个包可装weight重的物品， n件物品的集合S，重量分别为’w0,w1, ... , wn-1
		求解：
			能不能存在若干物品将包恰好装满，存在则表示有解，反之则无解
			
		变形：
			n中物品，每种可以任意件
"""
def knap_rec(weight, wlist, n):
	if weight == 0:
		return True
	if weight < 0 or (weight > 0 and n < 1):
		return False
	if knap_rec(weight - wlist[n-1], wlist, n-1):
		print("Item  " + str(n) + ":", wlist[n-1])
		return True
	if knap_rec(weight, wlist, n-1):
		return True
	else:
		return False
	
		
if __name__ == "__main__":
	string = '''
	aaaa()
	#bbbb)
	#ccccd)
	"""ddde}"""
	'''
	if check_parents_python(string):
		print("test success")
		
	if knap_rec(10, [2,3,4,5],4):
		print("The solution is exist!")
	
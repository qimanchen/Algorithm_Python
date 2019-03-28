#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
	离散事件模拟：
		行为特征：
			1、系统运行中可能不断发生一些事件（带有一定的随机性）
			2、一个事件在某个时刻发生，其发生可能导致其他事件在未来发生
	
	通用模拟框架：
		
"""


from random import randint
from priority_queue import PrioQueue


class QueueUnderflow(ValueError):
	"""判断队列为空是，异常类"""
	pass
	
	
class SQueue(object):
	"""队列实现数据结构"""
	
	def __init__(self, init_len=8):		# 默认队列初始长度为8
		"""创建空队列"""
		self._len = init_len		# 存储区长度
		self._elems = [0]*init_len	# 元素存储
		self._head = 0		# 表头元素下标
		self._num = 0		# 元素个数
		
	def is_empty(self):
		"""判断队列是否为空，空时返回True，否则返回False"""
		return self._num == 0
		
	def is_full(self):
		"""判断队列是否已满"""
		pass
		
	def enqueue(self, elem):
		"""将元素elem加入队列 -- 入队"""
		if self._num == self._len:
			self.__extend()
		self._elems[(self._head+self._num)%self._len] = elem
		self._num += 1
		
	def __extend(self):
		"""当队列满时，对列进行扩容"""
		old_len = self._len
		self._len *= 2
		new_elems = [0] * self._len
		for i in range(old_len):
			new_elems[i] = self._elems[(self._head+i) % old_len]
		
		self._elems, self._head = new_elems, 0
		
	def dequeue(self):
		"""删除队列中最早进入的元素并将其删除 -- 出队"""
		if self._num == 0:
			raise QueueUnderflow
		e = self._elems[self._head]
		self._head = (self._head + 1) % self._len
		self._num -= 1
		return e
		
	def peek(self):
		"""查看队列里最早进入的元素，不删除"""
		if self._num == 0:
			raise QueueUnderflow
		return self._elems[self._head]


class Simulation(object):
	"""
	总结：
		Simulation类和下面的Event类实现一个支持离散事件模拟的通用框架
		实际事件类的run方法，通过生成新事件完成模拟过程的实际控制
		Customs类实现检查站模拟系统的基础支撑功能和主控函数
		存在一个队列作为缓冲，保存已经到来但还不能检查的车辆
	"""
	def __init__(self, duration):
		self._eventq = PrioQueue()		# 使用优先队列记录模拟中缓存的事件，事件队列
		self._time = 0		# 记录当前时间
		self._duration = duration		# 记录模拟的总时长
		
	def run(self):
		"""
			实现一次完整的事件模拟
			
			每个事件都是对象：
				有其特定的具体行为，由相应的事件类定义-- 面向对象的离散事件模拟
		"""
		while not self._eventq.is_empty():			# 模拟到事件队列空
			event = self._eventq.dequeue()
			self._time = event.time()		# 事件的时间就是当时的时间
			if self._time > self._duration:		# 时间用完就结束
				break
			event.run()		# 模拟这个事件，其运行可能生成新事件
			
	def add_event(self, event):
		self._eventq.enqueue(event)
		
	def cur_time(self):
		return self._time
		

class Event(object):
	"""事件基类"""
	
	def __init__(self, event_time, host):
		self._ctime = event_time
		self._host = host
	
	def __lt__(self, other_event):
		return self._ctime < other_event._ctime
		
	def __le__(self, other_event):
		return self._ctime <= other_event._ctime
		
	def host(self):
		"""表示有关事件发生所在模拟系统（宿主系统）"""
		return self._host
	
	def time(self):
		return self._ctime
		
	def run(self):		# 具体事件类必须定义这个方法
		"""不同的事件派生类进行实际的定义"""
		pass
		
"""
	海关检查站模拟系统：
		基本设定:
			1、检查过往车辆，只模拟一个通行方向的检查
			2、车辆按一定速率到达，有一定随机性，每a到b分钟有辆车到达
			3、有k条检查通道，检查一辆车耗时c到d分钟
			4、有一个专有等待通道，有空闲检查通道时，立马检查，否则缓存
			5、希望得到的数据包：车辆的平均等待时间，通过检查站的平均时间

"""


# 实际模拟类
class Customs(object):
	
	def __init__(self, gate_num, duration,
						 arrive_interval, check_interval):
		"""模拟参数：
				车辆平均等待时间
				通过检查站的平均时间
				通道数
				总模拟时间
		"""
		self.simulation = Simulation(duration)		# 实际事件驱动类
		self.waitline = SQueue()			# 车辆等待队列
		self.duration = duration		# 模拟时间间隔
		self.gates = [0] * gate_num		# 模拟通道数
		self.total_wait_time = 0		# 总等待时间
		self.total_used_time = 0
		self.car_num = 0
		self.arrive_interval = arrive_interval
		self.check_interval = check_interval
		
	def wait_time_acc(self, n):
		# 计算总等待时间
		self.total_wait_time += n
		
	def total_time_acc(self, n):
		# 计算总检查时间
		self.total_used_time += n
		
	def car_count_1(self):
		# 计算通过的车辆数量
		self.car_num += 1
	
	def add_event(self, event):
		# 将事件加入到模拟器中
		self.simulation.add_event(event)
		
	def cur_time(self):
		# 取得事件的进行的当前时间
		return self.simulation.cur_time()
		
	def enqueue(self, car):
		# 将新等待车辆加入到等待队列中
		self.waitline.enqueue(car)
		
	def has_queued_car(self):
		# 判断是否有车辆在等待排队
		return not self.waitline.is_empty()
		
	def next_car(self):
		# 下一辆车进入检查通道
		return self.waitline.dequeue()
		
	def find_gate(self):
		# 检查那条检查通道可用
		for i in range(len(self.gates)):
			if self.gates[i] == 0:
				self.gates[i] = 1
				return i
		return None
		
	def free_gate(self, i):
		# 车辆检查完，更新通道状态
		if self.gates[i] == 1:
			self.gates[i] = 0		
		else:
			raise ValueError(" Clear gate Error. ")
			
	def simulate(self):
		Arrive(0, self)		# 初始生成一辆车的到来
		self.simulation.run()
		self.statistics()
		
	def statistics(self):
		# 统计数据并输出
		
		print("Simulation " + str(self.duration)
				  + " minutes, for "
				  + str(len(self.gates)) + " gates")
				  
		print(self.car_num, "cars pass the customs")
		
		print("Average waiting time:",
				  self.total_wait_time/self.car_num)
		print("Average passing time: ",
				  self.total_used_time/self.car_num)
		i = 0
		while not self.waitline.is_empty():
			self.waitline.dequeue()
			i += 1
		print(i, "cars are in waiting line.")


# 车辆对象类
class Car(object):
	"""记录车到达时间"""
	
	def __init__(self, arrive_time):
		self.time = arrive_time
		
	def arrive_time(self):
		return self.time
		
def event_log(time, name):
	# 事件日志信息记录类
	print("Event: " + name + ", happends at " + str(time))
	pass
		

# 模拟过程中可能发生的事件类
"""
	可能的事件：
		汽车到达事件：
			生成Car对象
			记录到达时间
			定义一个Arrive类，表示若干时间后下一辆车到达
		
		汽车开始检查事件：
		
		汽车检查完毕离开事件：
			定义Leave
"""
class Arrive(Event):
	"""表示车辆到达的规律"""
	
	def __init__(self, arrive_time, customs):
		Event.__init__(self, arrive_time, customs)
		customs.add_event(self)
		
	def run(self):
		time, customs = self.time(), self.host()
		event_log(time, "car arrive")
		# 生成下一个Arrive事件
		# *customs -- 迭代参数传递
		Arrive(time+randint(*customs.arrive_interval), customs)
		
		# 定义车辆事件的行为
		car = Car(time)
		if customs.has_queued_car():		# 有车辆在等，进入等待队列
			customs.enqueue(car)
			return
		i = customs.find_gate()			# 检查空闲通道
		if i is not None:		# 有通道，进入检查
			event_log(time, "car check")
			# 如果有车离开
			Leave(time + randint(*customs.check_interval), i, car, customs)
		else:
			customs.enqueue(car)
			

class Leave(Event):
	"""车离开事件类"""
	
	def __init__(self, leave_time, gate_num, car, customs):
		Event.__init__(self, leave_time, customs)
		self.car = car
		self.gate_num = gate_num
		customs.add_event(self)
		
	def run(self):
		time, customs = self.time(), self.host()
		event_log(time, "car leave")
		customs.free_gate(self.gate_num)
		customs.car_count_1()
		customs.total_time_acc(time - self.car.arrive_time())
		if customs.has_queued_car():
			# 进行下一辆车的处理
			car = customs.next_car()
			i = customs.find_gate()
			event_log(time,"car check")
			customs.wait_time_acc(time - car.arrive_time())
			Leave(time + randint(*customs.check_interval), self.gate_num, car, customs)
			

def test():
	car_arrive_interval = (1, 2)
	car_check_time = (3, 5)
	cus = Customs(3, 480, car_arrive_interval, car_check_time)
	cus.simulate()
	
	
if __name__ == "__main__":
	test()
		
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Time(object):
	
	def __init__(self, hours, minutes, seconds, days=0):
		if isinstance(hours, int) and hours < 24:
			self._hours = hours
		else:
			raise ValueError
		if isinstance(minutes, int) and minutes < 60:
			self._minutes = minutes
		else:
			raise ValueError
		if isinstance(seconds, int) and minutes < 60:
			self._seconds = seconds
		else:
			raise ValueError
		self._days = days
	
	@staticmethod
	def to_seconds(hours, minutes, seconds):
		hours_seconds = hours * 60 * 60
		minutes_seconds = minutes * 60
		
		all_seconds = hours_seconds + minutes_seconds + seconds
		return all_seconds
	
	@staticmethod
	def seconds_to_time(seconds):
		hours = seconds // (60*60)
		minutes = (seconds%(60*60))//60
		second = ((seconds%(60*60))%60)
		
		return hours, minutes, second
		
	def __str__(self):
		return ":".join((str(self._days), str(self._hours), str(self._minutes), str(self._seconds)))
		
	def hours(self):
		return self._hours
		
	def minutes(self):
		return self._minutes
	
	def seconds(self):
		return self._seconds
		
	def __add__(self, another):
		hour = self._hours + another.hours()
		minutes = self._minutes + another.minutes()
		seconds = self._seconds + another.seconds()
		
		while seconds > 60:
			seconds = seconds - 60
			minutes += 1
		while minutes > 60:
			minutes = minutes - 60
			hour += 1
		while hour > 24:
			hour -= 24
			self._days += 1
			
		return Time(hour, minutes, seconds, self._days)
		
	def __sub__(self, another):
		s_time = self.to_seconds(self._hours, self._minutes, self._seconds)
		
		a_time = self.to_seconds(another.hours(), another.minutes(), another.seconds())
		
		sub_time = s_time - a_time
		if sub_time < 0:
			self._days -= 1
			sub_time = -sub_time
		hour, minutes, seconds = self.seconds_to_time(sub_time)
		return Time(hour, minutes, seconds, self._days)
		
	def __eq__(self, another):
		s_time = self.to_seconds(self._hours, self._minutes, self._seconds)
		
		a_time = self.to_seconds(another.hours(), another.minutes(), another.seconds())
		
		return s_time == a_time
		
	def __lt__(self, another):
		s_time = self.to_seconds(self._hours, self._minutes, self._seconds)
		
		a_time = self.to_seconds(another.hours(), another.minutes(), another.seconds())
		
		return s_time < a_time
		
		
if __name__ == "__main__":
	t1 = Time(20, 34, 40)
	t2 = Time(20, 34, 40)
	t3 = Time(21, 32, 40)
	t4 = Time(2, 34, 40)
	
	t = [t1, t2, t3, t4]
	
	for test in t:
		print(test)
	t_add = t1+t3
	print(t_add)
	t_sub = t3 - t2
	print(t_sub)
	t_sub2 = t4 - t3
	print(t_sub2)
	
	if t1 == t2:
		print("Tesing is true!")
		
	if t2 < t3:
		print ("Testing is true!")
	
		
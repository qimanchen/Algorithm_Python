"""
	ADT Name:
		描述各方面的形式要求、功能要求
"""


class Rational0(object):
	
	def __init__(self, num, den=1):
		self.num = num
		self.den = den
	
	def plus(self, another):
		den = self.den * another.den
		num = (self.num * another.den + self.den * another.num)
		return Rationa10(num, den)
		
	def print(self):
		print(str(self.num) + "/" + str(self.den))
		

class Rational(object):

	@staticmethod
	def _gcd(m, n):
		if n == 0:
			m, n = n, m
		while m != 0:
			m, n = n % m , m
		return n
	
	def __init__(self, num, den=1):
		# type check
		if not isinstance(num, int) or not isinstance(den, int):
			raise TypeError
		if den == 0:
			raise ZeroDivisionError
		sign = 1
		
		if num < 0:
			num, sign = -num, -sign
		if den < 0:
			den, sign = -den, -sign
			
		g = Rational._gcd(num, den)
		
		# call function gcd defined in this class
		self._num = sign * (num//g)
		self._den = den//g
	
	# 定义外部调用内部变量
	def num(self):
		return self._num
	
	def den(self):
		return self._den
		
	def __add__(self, another):
		# mimic + operator
		den = self._den * another.den()
		num = (self._num * another.den() + self._den * another.num())
		return Rational(num, den)
		
	def __mul__(self, another):
		# mimic * operator
		return Rational(self._num * another.num(), self._den * another.den())
		
	def __floordiv__(self, another):
		# mimic // operator
		if another.num() == 0:
			raise ZeroDivisionError
		return Rational(self._num *another.den(), self._den*another.num())
	"""
		__sub__:减法
		__truedive__:整除 -- 除法获得浮点数
		__mod__: 求余
	"""
		
	def __eq__(self, another):
		# equal
		return self._num *another.den() == self._den * another.num()
		
	def __lt__(self, another):
		# less
		return self._num*another.den() < self._den*another.num()
		
	def __str__(self):
		# print string
		return str(self._num) + "/" + str(self._den)
	
	"""
		__ne__: 不等(!=)
		__le__: 小于等于(<=)
		__gt__: 大于(>)
		__ge__: 大于等于(>=)
	"""
		
	def print(self):
		print(str(self._num) + "/" + str(self._den))
		
	
if __name__ == "__main__":
	five = Rational(5)
	x = Rational(3, 5)
	x.print()
	print("Two thirds are ", Rational(2, 3))
	t = type(five)
	if isinstance(five, Rational):
		print("%s type is %s" % (five, t))
		

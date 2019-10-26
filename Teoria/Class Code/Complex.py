from fractions import Fraction

class Complex:
	"Make a complex number x + yi"
	def __init__(self, r, i):
		self.r = r
		self.i = i
	
	def __str__(self):
		if self.i == 0:
			return str(self.r)
		elif self.r == 0:
			return str(self.i)+"i"
		else:
			return str(self.r)+"+"+str(self.i)+"i"

	def __repr__(self):
		return 	"Complex("+str(self.r)+","+str(self.i)+")"

	def __add__(self, other):
		if isinstance(other,Complex):
			return Complex(self.r + other.r, self.i + other.i)
		elif isinstance(other,int):
			return Complex(self.r + other, self.i)
		elif isinstance(other,Fraction):
			return Complex(self.r + other, self.i)
		else:
			return Complex(self.r + float(other), self.i)

	__radd__ = __add__

	def __eq__(self, other):
		return isinstance(other,Complex) and self.r == other.r and self.i == other.i

c1 = Complex(1,2)
c2 = Complex(1,2)
print(c1 == c2)
"""
print("str Complex(0,3)  :",Complex(0,3))
print("repr Complex(0,3) :",repr(Complex(0,3)))
print("str Complex(4,0)  :",Complex(4,0))
print("repr Complex(4,0) :",repr(Complex(4,0)))
print("str Complex(1,2)  :",Complex(1,2))
print("repr Complex(1,2) :",repr(Complex(1,2)))
print("Complex(1,2)+10   :",c1+10)
print("10+Complex(1,2)   :",10+c1)
print("Complex(1,2)+10.0 :",c1+10.0)
print("10.0+Complex(1,2) :",10.0+c1)
print("Complex(1,2)+1/2  :",c1+Fraction(1,2))
print("1/2+Complex(1,2)  :",Fraction(1,2)+c1)
print("C(1,2)+C(100,1000):",c1+c2)
"""
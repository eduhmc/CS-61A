### Sierpinski Triangle (example of Tree Recursion)
### Docs: https://docs.python.org/3.7/library/turtle.html

from turtle import *
from math import sqrt
from time import sleep

def setup(extra):
	"""Set up parameters for the graph, between 0,0 and 1,1 with EXTRA on the edges"""
	setworldcoordinates(-extra,-extra,1+extra,1+extra)
	speed("fastest")
	colormode(1)
	bgcolor("black")

def ccurve(side,n):
	"""Draw a Sierpinski triangle with left edge at X,Y, edge SIDE, and recursion level N
	https://en.wikipedia.org/wiki/Sierpinski_triangle"""
	if n == 0:
		fd(side)
	else:
		lt(45)
		ccurve(side / sqrt(2),n-1)
		rt(90)
		ccurve(side / sqrt(2),n-1)
		lt(45)

setup(0.05)
color(1,1,1)
pu()

for n in range(10):
	clear()
	goto(0.25,0.5)
	pd()
	ccurve(0.5,n)
	pu()
	sleep(1)

done()
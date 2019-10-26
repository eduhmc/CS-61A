### Sierpinski Triangle (example of Tree Recursion)
### Docs: https://docs.python.org/3.7/library/turtle.html

from turtle import *
from math import sin,cos,tan,pi,sqrt

def setup(extra):
	"""Set up parameters for the graph, between 0,0 and 1,1 with EXTRA on the edges"""
	setworldcoordinates(-extra,-extra,1+extra,1+extra)
	speed("fastest")
	colormode(1)
	bgcolor("black")

def triangle(x,y,side):
	"""Draw a filled triangle with left edge at X,Y and edge SIDE"""
	pu()
	goto(x,y)
	n = 3
	color(x,y / (sqrt(3)/2),1)
	begin_fill()
	while n > 0:
		fd(side)
		lt(120)
		n -= 1
	end_fill()

def sierpinski(x,y,side,n):
	"""Draw a Sierpinski triangle with left edge at X,Y, edge SIDE, and recursion level N
	https://en.wikipedia.org/wiki/Sierpinski_triangle"""
	if n == 0:
		triangle(x,y,side)
	else:
		sierpinski(x,        y,                  side/2, n-1)
		sierpinski(x+side/2, y,                  side/2, n-1)
		sierpinski(x+side/4, y+(sqrt(3)/4)*side, side/2, n-1)

setup(0.05)
sierpinski(0,0,1,3)
done()
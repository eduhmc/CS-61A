### Turtle grapher (example of HOFs)
### Docs: https://docs.python.org/3.7/library/turtle.html

from turtle import *
from math import sin,cos,tan,pi

def setup(size):
	"Set up parameters for the graph, between -SIZE and SIZE"
	setworldcoordinates(-size,-size,size,size)
	speed("fastest")

def arrow(text):
	"Draw an arrow with arrowheads 1 unit away, labeled TEXT"
	angle = 20
	arrowhead_length = 0.05

	pd()
	fd(1)
	rt(angle)
	bk(arrowhead_length)
	fd(arrowhead_length)
	rt(180-2*angle)
	fd(arrowhead_length)
	bk(arrowhead_length)
	lt(180-angle)
	bk(0.1)
	write(text, font=("Arial", 18, "normal"))
	bk(0.9)
	pu()

def coords():
	"Draw graph coordinates"
	pen(pencolor="lightgrey", pensize=0.5)
	step = 0.1
	axis = -1
	while axis < 1:
		pu()
		goto(axis,-1)
		pd()
		goto(axis,1)
		pu()
		goto(-1,axis)
		pd()
		goto(1,axis)
		pu()
		axis += step
	seth(0)
	goto(0,0)
	pen(pencolor="black", pensize=1)
	for label in ["X = 1", "Y = -1", "X = -1", "Y = 1"]:
		arrow(label)
		rt(90)

### GRAPHER -- write this in real time 

def grapher(f):
	x = -1
	pu()
	goto(x,f(x))
	pd()
	step = .001
	while x < 1:
		goto(x,f(x))
		x += step
	pu()









"""
def grapher(f):
	"Graph the function y=f(x)"
	goto(-1,f(-1))
	pd()
	x = -1
	step = 0.005
	while x < 1:
		goto(x,f(x))
		x += step
	pu()
"""

setup(1.05)
coords()
#pen(pencolor="red", pensize=10)
#grapher(abs)
pen(pencolor="blue", pensize=10)
grapher(lambda t: tan(t*pi))

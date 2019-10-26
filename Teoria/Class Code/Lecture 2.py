# python DEMO1: "Names, Assignment, and User-Defined Functions"
pi
from math import pi
pi * 71 / 223
from math import sin
sin
sin(pi/2)

# Assignment
radius = 10
radius
2 * radius
area, circ = pi * radius * radius, 2 * pi * radius
area
circ
radius = 20

# Function values
max
max(3, 4)
f = max
f
max
f(3, 4)
max = 7
f(3, 4)
f(3, max)
max = f
f
max
f = 2
# f(3, 4)
# __builtins__.max

### Three ways to bind names to values
### 1. import
from operator import add, mul
### 2. assignment (you saw above) ... abstraction!
### 3. def statement ... abstraction!

# User-defined functions
def square(x):
    return mul(x, x)

square
square(10)
square(add(4, 6))
square(square(3))

def sum_squares(x, y):
    return square(x) + square(y)
sum_squares(3, 4)
sum_squares(5, 12)

def area():
    return pi * radius * radius
area
area()
radius
pi * 20 * 20
radius = 10
area()


### visualize DEMO2: 
from math import pi
tau = 2 * pi


### visualize DEMO3: discussion question
f = min
f = max
g, h = min, max
max = g
max(f(2, g(h(1, 5), 3)), 4)


### visualize DEMO4: 
from operator import mul
def square(x):
    return mul(x, x)
square(-2)


### visualize DEMO5: Name conflicts
from operator import mul
def square(square):
    return mul(square, square)
square(4)


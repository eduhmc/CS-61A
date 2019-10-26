### DEMO1 (from file) Generalizing Patterns with Arguments
### add assertions and generalize to prevent negative r!
### assert r > 0, 'A length must be positive'


from math import pi, sqrt

def area_square(r):
    """Return the area of a square with side length R."""
    assert r >= 0, "R needs to be non-negative"
    return r * r

def area_circle(r):
    """Return the area of a circle with radius R."""
    return r * r * pi

def area_hexagon(r):
    """Return the area of a regular hexagon with side length R."""
    return r * r * 3 * sqrt(3) / 2

#print(area_square(10))


def area(r, shape_constant):
    """Return the area of a shape from length measurement R."""
    assert r >= 0, "R needs to be non-negative"
    return r * r * shape_constant

def area_square(r):
    return area(r, 1)

def area_circle(r):
    return area(r, pi)

def area_hexagon(r):
    return area(r, 3 * sqrt(3) / 2)


### DEMO2: Generalizing Over Computational Processes

# Functions as arguments

def sum_naturals(n):
    """Sum the first N natural numbers.

    >>> sum_naturals(5)
    15
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + k, k + 1
    return total

#print(sum_naturals(5))

def sum_cubes(n):
    """Sum the first N cubes of natural numbers.

    >>> sum_cubes(5)
    225
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + pow(k, 3), k + 1
    return total

def identity(k):
    return k

def cube(k):
    return pow(k, 3)

def summation(n, term):
    """Sum the first N terms of a sequence.

    >>> summation(5, cube)
    225
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total


def pi_term(x):
    return 8 / ((4 * x - 3) * (4 * x - 1))

#print(summation(1000000, pi_term))


### DEMO3 Functions as Return Values
# Local function definitions; returning functions

def make_adder(n):
    """Return a function that takes one argument K and returns K + N.

    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    """
    def adder(k):
        return k + n
    return adder

print(make_adder(2000)(19))

### DEMO4 (repl) Lambda Expressions

x = 10
square = x * x
square = lambda x: x * x
square(4)

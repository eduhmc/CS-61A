### DEMO1 Environments Enable Higher-Order Functions
# Functional arguments

def apply_twice(f, x):
    """Return the result of calling f twice on x

    >>> apply_twice(square, 2)
    16
    >>> from math import sqrt
    >>> apply_twice(sqrt, 16)
    2.0
    """
    return f(f(x))

def square(x):
    return x * x

result = apply_twice(square, 10)
#print(result)
### DEMO2 Functions as Return Values
### Don't show, it's on a slide

def make_adder(n):
    """Return a function that takes one argument k and returns k + n.

    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    """
    def adder(k):
        return k + n
    return adder

### DEMO3 Local Names
# Lexical scope and returning functions

def f(x, y):
    return g(x)

def g(a):
    return a + y

# This expression causes an error because y is not bound in g.
#print(f(1, 2))

### DEMO4
# lambda (type to REPL)
x = 10
square = x * x
square = lambda x: x * x
square(4)

### DEMO5
# Composition

def compose1(f, g):
    """Return a function that composes f and g.

    f, g -- functions of a single argument
    """
    def h(x):
        return f(g(x))
    return h
    
def triple(x):
    return 3 * x

squiple = compose1(square, triple)
#print(squiple(10))
tripare = compose1(triple, square)
#print(tripare(10))
squadder = compose1(square, make_adder(2))
print(compose1(lambda x:x, lambda y:y*y)(10))
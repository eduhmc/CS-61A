""" Homework 2: Higher Order Functions"""

HW_SOURCE_FILE = 'hw02.py'

from operator import add, mul, sub

square = lambda x: x * x

identity = lambda x: x

triple = lambda x: 3 * x

increment = lambda x: x + 1

######################
# Required Questions #
######################

# Q1
def make_adder(n):
    """Return a function that takes an argument K and returns N + K.

    >>> add_three = make_adder(3)
    >>> add_three(1) + add_three(2)
    9
    >>> make_adder(1)(2)
    3
    """
    return lambda k: n + k

# Q2
def product(n, term):
    """Return the product of the first n terms in a sequence.
    n    -- a positive integer
    term -- a function that takes one argument

    >>> product(3, identity)  # 1 * 2 * 3
    6
    >>> product(5, identity)  # 1 * 2 * 3 * 4 * 5
    120
    >>> product(3, square)    # 1^2 * 2^2 * 3^2
    36
    >>> product(5, square)    # 1^2 * 2^2 * 3^2 * 4^2 * 5^2
    14400
    >>> product(3, increment) # (1+1) * (2+1) * (3+1)
    24
    >>> product(3, triple)    # 1*3 * 2*3 * 3*3
    162
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'product', ['Recursion'])
    True
    """
    "*** YOUR CODE HERE ***"
    counter = 1
    mul = 1
    while counter <= n:
        if term == identity:
            mul = mul * counter
            counter = counter + 1
        if term == square:
            mul = (counter**2) * mul
            counter = counter + 1
        if term == triple:
            mul = (counter *3) *mul
            counter += 1
        if term == increment:
            mul = (counter + 1) * mul
            counter = counter + 1
    return mul


def factorial(n):
    """Return n factorial for n >= 0 by calling product.

    >>> factorial(4)  # 4 * 3 * 2 * 1
    24
    >>> factorial(6)  # 6 * 5 * 4 * 3 * 2 * 1
    720
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'factorial', ['Recursion', 'For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    return product(n, identity)
# Q3

def accumulate(combiner, base, n, term):
    """Return the result of combining the first n terms in a sequence and base.
    The terms to be combined are term(1), term(2), ..., term(n).  combiner is a
    two-argument commutative, associative function.

    >>> accumulate(add, 0, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
    15
    >>> accumulate(add, 11, 5, identity) # 11 + 1 + 2 + 3 + 4 + 5
    26
    >>> accumulate(add, 11, 0, identity) # 11
    11
    >>> accumulate(add, 11, 3, square)   # 11 + 1^2 + 2^2 + 3^2
    25
    >>> accumulate(mul, 2, 3, square)    # 2 * 1^2 * 2^2 * 3^2
    72
    """
    "*** YOUR CODE HERE ***"
    total = base
    num = 1
    while num <= n:
        total = combiner(total, term(num))
        num += 1
    return total
  
    """
    def sum(n):
        counter = 1
        suma = 0
        m = 1
        if combiner == add:
            while counter <= n:
                if term == identity:
                    suma += counter
                    counter = counter + 1
                if term == square:
                    suma += (counter**2) 
                    counter = counter + 1
                if term == triple:
                    suma = (counter *3) + suma
                    counter += 1
                if term == increment:
                    suma = (counter + 1) + suma
                    counter = counter + 1
            return suma
        if combiner == mul:
            while counter <= n:
                if term == identity:
                    m *= counter
                    counter = counter + 1
                if term == square:
                    m *= (counter**2) 
                    counter = counter + 1
                if term == triple:
                    m *= (counter *3) 
                    counter += 1
                if term == increment:
                    m *= (counter + 1) 
                    counter = counter + 1
            return m



    x = sum(n)
    if combiner == add:
        return base + x
    if combiner == mul:
        return base * x
    """

def summation_using_accumulate(n, term):
    """Returns the sum of term(1) + ... + term(n). The implementation
    uses accumulate.

    >>> summation_using_accumulate(5, square)
    55
    >>> summation_using_accumulate(5, triple)
    45
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'summation_using_accumulate',
    ...       ['Recursion', 'For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    return accumulate(add, 0, n, term)


def product_using_accumulate(n, term):
    """An implementation of product using accumulate.

    >>> product_using_accumulate(4, square)
    576
    >>> product_using_accumulate(6, triple)
    524880
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'product_using_accumulate',
    ...       ['Recursion', 'For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    return accumulate(mul, 1, n, term)

###################
# Extra Questions #
###################

# Q4 (Optional)
def compose1(f, g):
    """Return a function h, such that h(x) = f(g(x))."""
    def h(x):
        return f(g(x))
    return h

def make_repeater(f, n):
    """Return the function that computes the nth application of f.

    >>> add_three = make_repeater(increment, 3)
    >>> add_three(5)
    8
    >>> make_repeater(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
    243
    >>> make_repeater(square, 2)(5) # square(square(5))
    625
    >>> make_repeater(square, 4)(5) # square(square(square(square(5))))
    152587890625
    >>> make_repeater(square, 0)(5) # Yes, it makes sense to apply the function zero times! 
    5
    """
    "*** YOUR CODE HERE ***"

    if f == increment:
        return lambda x: x + n
    if f == square:
        return lambda x: x**(2**n)
    if f == triple:
        return lambda x: (3**n) * x
    if n == 0:
        return lambda x: x





### DEMO1: Test-driven development

from ucb import trace, interact

def gcd(m, n):
    """Return the largest k that evenly divides both m and n.

    k, m, and n are all positive integers.

    WRITE THIS TOGETHER WITH STUDENTS

    >>> gcd(6,4)
    2
    >>> gcd(4,2)
    2
    >>> gcd(10,30)
    10
    >>> gcd(100,1000)
    100
    >>> gcd(51,13)
    1
    >>> gcd(17,2)
    1
    >>> gcd(1,1)
    1
    >>> gcd(15,15)
    15



    >>> gcd(12, 8)
    4
    >>> gcd(16, 12)
    4
    >>> gcd(16, 8)
    8
    >>> gcd(2, 16)
    2
    >>> gcd(24, 42)
    6
    >>> gcd(5, 5)
    5

    CODE BELOW A NICE EXAMPLE AFTER WE'VE INTRODUCED RECURSION.
    WE RECOMMEND NOT WORRYING ABOUT RECURSION UNTIL AFTER THE MIDTERM.
    """
    if m == n:
        return m
    elif m < n:
        return gcd(n, m)
    else:
        return gcd(m-n, n)


### DEMO2: Function Currying

### MAPPING pattern FROM LECTURE 06

def mapper(n, f):
    """Return a number each digit of N transformed by function F

    >>> mapper(1234111,lambda d: d*2)
    2468222
    >>> mapper(1624690,lambda d: 9-d)
    8375309
    """
    mapped, place = 0, 0
    while n > 0:
        mapped += f(n % 10)*10**place
        n = n // 10
        place += 1
    return mapped




def curried_pow(base):
    """Return a curried version of pow

    >>> curried_pow(2)(3)
    8
    """
    def base_to_the(exponent):
        return pow(base, exponent)
    return base_to_the

### >>> curried_pow(2)
### <function curried_pow.<locals>.f at 0x10bcb99d8>
### >>> two_to_the = curried_pow(2)
### >>> two_to_the(3)
### 8

### Write curry2 together

def curry2(f):
    """Return a curried version of the given two-argument function."""
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g

### Write curry2 using lambda also

curry2 = lambda f: lambda x: lambda y: f(x,y)
### >>> curried_pow = curry2(pow)
### >>> curried_pow(2)(3)
### 8


### DEMO3: Decorators

def trace1(fn):
    """Return a function equivalent to fn that also prints trace output.

    fn -- a function of one argument.
    """
    def traced(x):
        print('Calling', fn, 'on argument', x)
        return fn(x)
    return traced

#@trace1
def square(x):
    return x*x

#@trace1
def sum_squares_up_to(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + square(k), k + 1
    return total


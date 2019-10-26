import timeit
from math import sqrt

def memo(f):
    cache = {}
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized

@memo
def fib(n):  ### Non-memoized->theta(phi^n), memoized->theta(n)
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-2) + fib(n-1)

def fib_fast(n): ### theta(n)
	phi = (1+sqrt(5))/2
	return round((phi ** n) / sqrt(5))

def square(x):
	return x*x

def exp_fast(b, n):
    """Return b to the n.

    >>> exp_fast(2, 10)
    1024
    """
    if n == 0:
        return 1
    elif n % 2 == 0:
        return square(exp_fast(b, n//2))
    else:
        return b * exp_fast(b, n-1)

def fib_veryfast(n): ### theta(log(n))
	phi = (1+sqrt(5))/2
	return round(exp_fast(phi,n) / sqrt(5))

#print(fib(1035))

print("Time:",timeit.timeit("fib_veryfast(35)","from __main__ import fib_veryfast", number=1))
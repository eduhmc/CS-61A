from math import inf

### DEMO1: Assertions and muting them.

### run normally and the restart with python3 -O

__debug__

def assert_false():
    assert False, 'False!'

### DEMO2: Errors

def errors():
    raise TypeError('Bad argument')
    abs('hello') # TypeError
    hello # NameError
    {}['hello'] # KeyError
    def f(): f()
    f() # RuntimeError

### DEMO3: try/except

def invert(x):
    """Return 1/x

    >>> invert(2)
    Never printed if x is 0
    0.5
    """
    result = 1/x  # Raises a ZeroDivisionError if x is 0
    print('Never printed if x is 0')
    return result

def invert_test():
    invert(0.5)
    invert(2)
    invert(0)

def invert_safe(x):
    """Return 1/x, or the string 'divison by zero' if x is 0.

    >>> invert_safe(2)
    Never printed if x is 0
    0.5
    >>> invert_safe(0)
    handled division by zero
    inf
    """
    try:
        return invert(x)
    except ZeroDivisionError as e:
        print("handled", e)
        return inf

### DEMO4: reduce

from operator import add, mul, truediv
def reduce1(f, s, initial):
    """Combine elements of s pairwise using f, starting with initial.

    >>> reduce1(mul, [2, 4, 8], 1)
    64
    >>> reduce1(pow, [1, 2, 3, 4], 2)
    16777216
    """
    if not s:
        return initial
    else:
        first, rest = s[0], s[1:]
        return reduce1(f, rest, f(initial, first))


def reduce2(f, s, initial):
    """Combine elements of s pairwise using f, starting with initial.

    >>> reduce2(mul, [2, 4, 8], 1)
    64
    >>> reduce2(pow, [1, 2, 3, 4], 2)
    16777216
    """
    if len(s) == 1:
        return f(initial,s[0])
    else:
        return f(reduce2(f,s[:-1],initial), s[-1])


def reduce3(f, s, initial):
    """Combine elements of s pairwise using f, starting with initial.

    >>> reduce3(mul, [2, 4, 8], 1)
    64
    >>> reduce3(pow, [1, 2, 3, 4], 2)
    16777216
    """
    for x in s:
        initial = f(initial, x)
    return initial


def divide_all(n, ds):
    """Divide n by every d in ds.

    >>> divide_all(1024, [2, 4, 8])
    16.0
    >>> divide_all(1024, [2, 4, 0, 8])
    inf
    """
    try:
        return reduce(truediv, ds, n)
    except ZeroDivisionError:
        return float('inf')

### DEMO1: Print and None
-2
print(-2)
'Cal'
print('Cal')
None
print(None)
print(1, 2, 3)
print(None, None)
print(print(1), print(2))

### DEMO2: Miscellaneous Python Features
# Division
123 / 10
123 // 10
123 % 10
from operator import truediv, floordiv, mod
floordiv(123, 10)
truediv(123, 10)
mod(123, 10)

# Approximation
5 / 3
5 // 3
5 % 3

# Multiple return values
def divide_exact(n, d):
    return n // d, n % d
q, r = divide_exact(123, 10)

# Dostrings, doctests, & default arguments

### (put this in ex.py, show what happens with mistake)
### BEGIN
from operator import floordiv, mod
def divide_exact(n, d=10):
    """Return the quotient and remainder of dividing N by D.

    >>> quotient, remainder = divide_exact(123, 10)
    >>> quotient
    12
    >>> remainder
    3
    """
    return floordiv(n, d), mod(n, d)
### END

### put a print statement in there
### python3 ex.py 
### take print statement out, show interactive mode
### python3 -i ex.py
### python3 -m doctest ex.py
### pythone -m doctest -v ex.py

### DEMO3: Conditional Statements
### Add this to ex.py, show in interactive mode, say we had 'abs'
### BEGIN
# Conditional expressions
def my_abs(x):
    """Return the absolute value of X.

    >>> my_abs(-3)
    3
    >>> my_abs(0)
    0
    >>> my_abs(3)
    3
    """
    if x < 0:
        return -x
    elif x == 0:
        return 0
    else:
        return x
### END

### DEMO4: Iteration: While Statements (just type into interpreter)
# Summation via while
i, total = 0, 0
while i < 3:
    i = i + 1
    total = total + i
i
total


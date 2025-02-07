""" Lab 04 Optional Questions """

from lab04 import *


this_file = __file__

def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> check(this_file, 'hailstone',
    ...       ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    print(n)
    
    if n == 1:
        return 1

    if n % 2 == 0:
        return 1 + hailstone(n//2)

    else:
        return 1 + hailstone(int((n*3) + 1))

     
   
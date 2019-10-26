def iterator_demos():
    """Using iterators

    "DEMO1"

    >>> s = [[1, 2], 3, 4, 5]
    >>> next(s)
    Traceback (most recent call last):
        ...
    TypeError: 'list' object is not an iterator
    >>> t = iter(s)
    >>> next(t)
    [1, 2]
    >>> next(t)
    3
    >>> u = iter(s)
    >>> next(u)
    [1, 2]
    >>> list(t)
    [4, 5]
    >>> next(t)
    Traceback (most recent call last):
        ...
    StopIteration

    "DEMO2"

    >>> d = {'one': 1, 'two': 2} # Keys and values
    >>> k = iter(d)
    >>> next(k)
    'one'
    >>> d['zero'] = 0
    >>> next(k)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    RuntimeError: dictionary changed size during iteration
    >>> d
    {'one': 1, 'two': 2, 'zero': 0}
    >>> k = iter(d)
    >>> next(k)
    'one'
    >>> next(k)
    'two'
    >>> d['zero'] = 0.001
    >>> next(k)
    0.001

    "DEMO3"

    >>> r = range(3,6)
    >>> list(r)
    [3, 4, 5]
    >>> for i in r:
    ...     print(i)
    ... 
    3
    4
    5
    >>> for i in r:
    ...     print(i)
    ... 
    3
    4
    5
    >>> ri = iter(r)
    >>> ri
    <range_iterator object at 0x10c5e9e10>
    >>> next(ri)
    3
    >>> for i in ri:
    ...     print(i)
    ... 
    4
    5
    >>> r
    range(3, 6)
    >>> ri = iter(r)
    >>> for i in ri:
    ...     print(i)
    ... 
    3
    4
    5
    >>> for i in ri:
    ...     print(i)
    ... 
    """

def double(x):
    print('***', x, '=>', 2*x, '***')
    return 2*x

def built_in_demo():
    """Using built-in sequence functions.

    "DEMO4"

    >>> bcd = ['b', 'c', 'd']
    >>> [x.upper() for x in bcd]
    ['B', 'C', 'D']
    >>> map(lambda x: x.upper(), bcd)
    <map object at 0x10237aef0>
    >>> m = map(lambda x: x.upper(), bcd)
    >>> next(m)
    'B'
    >>> next(m)
    'C'
    >>> next(m)
    'D'
    >>> next(m)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration

    >>> map(double, [3, 5, 7])
    >>> m = map(double, [3, 5, 7])
    >>> next(m)
    *** 3 => 6 ***
    6
    >>> next(m)
    *** 5 => 10 ***
    8
    >>> list(m)
    *** 7 => 14 ***
    [14]

    >>> m = map(double, range(3, 7))
    >>> f = lambda y: y >= 10
    >>> t = filter(f, m)
    >>> next(t)
    *** 3 ==> 6 ***
    *** 4 ==> 8 ***
    *** 5 ==> 10 ***
    10
    >>> next(t)
    *** 6 ==> 12 ***
    12
    >>> list(t)
    []
    >>> list(filter(f, map(double, range(3, 7))))
    *** 3 ==> 6 ***
    *** 4 ==> 8 ***
    *** 5 ==> 10 ***
    *** 6 ==> 12 ***
    [10, 12]

    >>> t = [1, 2, 3, 2, 1]
    >>> reversed(t) == t
    False
    >>> list(reversed(t)) == t
    True

    >>> d = {'a': 1, 'b': 2}
    >>> d
    {'b': 2, 'a': 1}
    >>> items = iter(d.items())
    >>> next(items)
    ('b', 2)
    >>> next(items)
    ('a', 1)
    >>> items = zip(d.keys(), d.values()) # Call next(items)
    >>> next(items)
    ('b', 2)
    >>> next(items)
    ('a', 1)
    """

def plus_minus(x):
    """Yield x and -x.

    >>> t = plus_minus(3)
    >>> next(t)
    3
    >>> next(t)
    -3
    >>> list(plus_minus(5))
    [5, -5]
    >>> list(map(abs, plus_minus(7)))
    [7, 7]
    """
    yield x
    yield -x

def evens(start, end):
    """A generator function that returns even numbers.

    "DEMO5"

    >>> list(evens(2, 10))
    [2, 4, 6, 8]
    >>> list(evens(1, 10))
    [2, 4, 6, 8]
    """
    even = start + (start % 2)
    while even < end:
        yield even
        even += 2

def a_then_b_for(a, b):
    """The elements of a followed by those of b.

    >>> list(a_then_b_for([3, 4], [5, 6]))
    [3, 4, 5, 6]
    """
    for x in a:
        yield x
    for x in b:
        yield x

def a_then_b(a, b):
    """The elements of a followed by those of b.

    >>> list(a_then_b([3, 4], [5, 6]))
    [3, 4, 5, 6]
    """
    yield from a
    yield from b

def countdown(k):
    """Count down to zero.

    >>> list(countdown(5))
    [5, 4, 3, 2, 1]
    """
    if k > 0:
        yield k
        yield from countdown(k-1)

def prefixes(s):
    """Yield all prefixes of s.

    >>> list(prefixes('both'))
    ['b', 'bo', 'bot', 'both']
    """
    if s:
        yield from prefixes(s[:-1])
        yield s

def substrings(s):
    """Yield all substrings of s.

    >>> list(substrings('tops'))
    ['t', 'to', 'top', 'tops', 'o', 'op', 'ops', 'p', 'ps', 's']
    """
    if s:
        yield from prefixes(s)
        yield from substrings(s[1:])
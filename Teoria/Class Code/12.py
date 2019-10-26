### DEMO1: Lists

odds = [41, 43, 47, 49]
len(odds)
odds[1]
odds[0] - odds[3] + len(odds)
odds[odds[3]-odds[2]]

### DEMO2: Containers

digits = [1, 8, 2, 8]
1 in digits
3 in digits
1 == '1'
'1' in digits
[1, 8] in digits
[1, 2] in [[1, 2], 3]
[1, 2] in [[[1, 2]], 3]
len([[1, 2], 3])

### DEMO3: For statements
### Start with count_while, evolve to count_for

def count_while(s, value):
    """Count the number of occurrences of VALUE in sequence S.

    >>> count_while(digits, 8)
    2
    """
    total, index = 0, 0
    while index < len(s):
        if s[index] == value:
            total = total + 1
        index = index + 1
    return total

def count_for(s, value):
    """Count the number of occurrences of value in sequence s.

    >>> count_for(digits, 8)
    2
    """
    total = 0
    for elem in s:
        if elem == value:
            total = total + 1
    return total

### Don't show, just for reference

def count_same(pairs):
    """Return how many pairs have the same element repeated.

    >>> pairs = [[1, 2], [2, 2], [2, 3], [4, 4]]
    >>> count_same(pairs)
    2
    """
    same_count = 0
    for x, y in pairs:
        if x == y:
            same_count = same_count + 1
    return same_count

### DEMO4: Ranges

list(range(5, 8))
range(4)
list(range(4))
len(range(4))

def sum_below(n):
    total = 0
    for i in range(n):
        total += i
    return total

def cheer():
    for _ in range(3):
        print('Go Bears!')


### DEMO5: List comprehensions

odds = [1, 3, 5, 7, 9]
[x+1 for x in odds]
[x for x in odds if 25 % x == 0]
[x for x in odds if 25 % x == 0]

def divisors(n):
    """Return the integers that evenly divide n.

    >>> divisors(1)
    [1]
    >>> divisors(4)
    [1, 2, 4]
    >>> divisors(12)
    [1, 2, 3, 4, 6, 12]
    """
    return [x for x in range(1, n+1) if n % x == 0]

#print(divisors(12))

### DEMO6: Strings

f = 'curry = lambda f: lambda x: lambda y: f(x, y)'
exec(f)

### DEMO7: Dictionaries

def dict_demos():
    numerals = {'I': 1, 'V': 5, 'X': 10}
    numerals['X']
    numerals[10]
    numerals.keys()
    numerals.values()
    numerals.items()
    pairs = numerals.items()
    dict(pairs)
    'X' in numerals
    10 in numerals
    list(numerals.values())
    sum(numerals.values())
    numerals.get('X', 0)
    numerals.get('X-ray', 0)
    {x: x*x for x in range(3,6)}

    {1: 2, 1: 3}
    {[1]: 2}
    {1: [2]}

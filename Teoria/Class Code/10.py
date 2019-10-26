from ucb import trace

### DEMO1 Ordering

def cascade(n):
    """Print a cascade of prefixes of n.

    >>> cascade(1234)
    1234
    123
    12
    1
    12
    123
    1234
    """
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n//10)
        print(n)

#cascade(123)

### DEMO2: Rewrite cascade

def cascade2(n):
    """Print a cascade of prefixes of n."""
    print(n)
    if n >= 10:
        cascade(n//10)
        print(n)

#cascade2(1234)

def inverse_cascade(n):
    """Print an inverse cascade of prefixes of n.
    
    >>> inverse_cascade(1234)
    1
    12
    123
    1234
    123
    12
    1
    """
    grow(n)
    print(n)
    shrink(n)

def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)

grow   = lambda n: f_then_g(grow,  print,  n//10)
shrink = lambda n: f_then_g(print, shrink, n//10)

#inverse_cascade(1234)

### DEMO3 Tree recursion

def fib(n):
    """Compute the nth Fibonacci number.

    >>> fib(8)
    21
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)


def fib_dot(n):
    """Compute the Nth Fibonacci number, and print every call in DOT format

    >>> fib_dot(4)
    4->2
    4->3
    2->0
    2->1
    3->1
    3->2
    2->0
    2->1
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        print(str(n) + "->" + str(n-2))
        print(str(n) + "->" + str(n-1))
        return fib_dot(n-2) + fib_dot(n-1)

#fib_dot(4)

def fib_tree(n):
    print("digraph G {")
    fib_dot(n)
    print("}")

fib_tree(5)

## DEMO4: count_partitions

def count_partitions(n, m):
    """Count the partitions of n using parts up to size m.

    >>> count_partitions(6, 4)
    9
    >>> count_partitions(10, 10)
    42
    """
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        with_m = count_partitions(n-m, m)
        without_m = count_partitions(n, m-1)
        return with_m + without_m

#print(count_partitions(6,4))

def count_partitions_dot(n, m):
    """Count the partitions of n using parts up to size m and print edges in DOT format
    """
    if n == 0:
        print('"'+str(n)+","+str(m)+'"' + " [ style = filled, color=red ];")
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        print('"'+str(n)+","+str(m)+'"' + " -> " + '"'+str(n-m)+","+str(m)+'"')
        print('"'+str(n)+","+str(m)+'"' + " -> " + '"'+str(n)+","+str(m-1)+'"')
        with_m    = count_partitions_dot(n-m, m)
        without_m = count_partitions_dot(n  , m-1)
        return with_m + without_m

def count_positions_tree(n,m):
    print("digraph G {")
    count_partitions_dot(n,m)
    print("}")

#count_positions_tree(6,4)
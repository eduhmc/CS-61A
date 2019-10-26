### DEMO1: sum_primes python O(1) vs scheme O(n)

def is_prime(x):
    """Return whether x is prime.

    >>> [is_prime(x) for x in range(1, 10)]
    [False, True, True, False, True, False, True, False, False]
    """
    if x <= 1:
        return False
    else:
        return all(map(lambda y: x % y, range(2, x)))

def sum_primes(a, b):
    """Sum all primes in the interval range(a, b).
    
    >>> sum_primes(1, 10)
    17
    """
    total = 0
    x = a
    while x < b:
        if is_prime(x):
            total = total + x
        x = x + 1
    return total

def sum_primes_filter(a, b):
    """Sum all primes in the interval range(a, b).
    
    >>> sum_primes(1, 10)
    17
    """
    return sum(filter(is_prime, range(a, b)))


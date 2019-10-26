
def make_adder_inc(n):
    """
    >>> adder1 = make_adder_inc(5)
    >>> adder2 = make_adder_inc(6)
    >>> adder1(2) 
    7
    >>> adder1(2) # 5 + 2 + 1
    8
    >>> adder1(10) # 5 + 10 + 2
    17
    >>> [adder1(x) for x in [1, 2, 3]]
    [9, 11, 13]
    >>> adder2(5)
    11
    """
    "*** YOUR CODE HERE ***"
    my_dict = {}
    c = 0
    def add(x):
        nonlocal my_dict
        nonlocal c
        if n not in my_dict:
            my_dict[n] = x + n

        else:
            my_dict[n] = x + n + c

        c = c + 1
        return my_dict[n]
    return add
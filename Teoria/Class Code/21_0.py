class Link:
    """A linked list."""
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(self.first, rest_str)

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ', '
            self = self.rest
        return string + str(self.first) + '>'

def empty(s):
    return s is Link.empty

def contains(s, v):
    """Return true if set s contains value v as an element.

    >>> s = Link(1, Link(2, Link(3))) 
    >>> contains(s, 2)
    True
    >>> contains(s, 5)
    False
    """

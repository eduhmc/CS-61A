### DEMO1: (repl) Slicing

odds = [3, 5, 7, 9, 11]
list(range(1, 3))
[odds[i] for i in range(1, 3)]
odds[1:3]
odds[1:]
odds[:3]
odds[:]

### DEMO2: (repl) Aggregation

sum(odds)
sum(odds, 1000)
[] + [2, 3] + [4]
sum([[2, 3], [4]], [])
sum({3:9, 5:25})

max(range(10))
words = ['apple', 'banana', 'cherry']
max(words)
max(words, key=len)
max(words, key=lambda word: word[1])
max(range(10), key=lambda x: 7 - (x-2)*(x-4))
# min complement

bool(5)
bool(True)
bool(False)
bool(0)
bool('hello')
bool('')

[x < 5 for x in range(5)]
all([x < 5 for x in range(5)])
perfect_square = lambda x: x == round(x ** 0.5) ** 2
any([perfect_square(x) for x in range(50, 60)]) # Try ,65)

### DEMO3: Trees (skip this go to REPL fun below)

def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

### Repl fun

t = tree(1, [tree(5, [tree(7)]), tree(6)]     )
#print(label(branches(t)[0]))
tree(1)
[1] # looks the same but we didn't use a constructor!
is_leaf(tree(1))
#tree(1, [5])
t = tree(1, [tree(5, [tree(7)]), tree(6)])
"""
1-5-7
 \
  6
"""
t
label(t)
branches(t)
branches(t)[0]
is_tree(branches(t)[0])
label(branches(t)[0])

### +++ === ABSTRACTION BARRIER === +++ ###

### DEMO4A: Print Tree (write this)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each label is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> print_tree(fib_tree(4))
    3
      1
        0
        1
      2
        1
        1
          0
          1
    """
    print('  ' * indent, label(t))
    for b in branches(t):
        print_tree(b, indent + 1)

#print_tree(t)

### DEMO4: TREE PROCESSING (Write this live, then play

def fib_tree(n):
    """Construct a Fibonacci tree.

    >>> fib_tree(1)
    [1]
    >>> fib_tree(3)
    [2, [1], [1, [0], [1]]]
    >>> fib_tree(5)
    [5, [2, [1], [1, [0], [1]]], [3, [1, [0], [1]], [2, [1], [1, [0], [1]]]]]
    """
    if n == 0 or n == 1:
        return tree(n)
    else:
        left = fib_tree(n-2)
        right = fib_tree(n-1)
        fib_n = label(left) + label(right)
        return tree(fib_n, [left, right])

print_tree(fib_tree(5)) ### 0 through 5
#print(label(fib_tree(5)))

### DEMO5: Tree Processing (written already, show use)

def count_leaves(t):
    """The number of leaves in tree.

    >>> count_leaves(fib_tree(5))
    8
    """
    if is_leaf(t):
        return 1
    else:
        return sum([count_leaves(b) for b in branches(t)])

#print(count_leaves(fib_tree(5)))

def leaves(tree):
    """Return a list containing the leaf labels of tree.

    >>> leaves(fib_tree(5))
    [1, 0, 1, 0, 1, 1, 0, 1]
    """
    if is_leaf(tree):
        return [label(tree)]
    else:
        return sum([leaves(b) for b in branches(tree)], [])

def increment_leaves(t):
    """Return a tree like t but with leaf labels incremented.
    
    
    >>> print_tree(increment_leaves(fib_tree(4)))
    3
      1
        1
        2
      2
        2
        1
          1
          2
    """
    if is_leaf(t):
        return tree(label(t) + 1)
    else:
        bs = [increment_leaves(b) for b in branches(t)]
        return tree(label(t), bs)
"""
print("fib(3)")
print_tree(fib_tree(3))
print("fib(3) leaves incremeneted")
print_tree(increment_leaves(fib_tree(3)))
"""

def increment(t):
    """Return a tree like t but with all labels incremented.
    
    >>> print_tree(increment(fib_tree(4)))
    4
      2
        1
        2
      3
        2
        2
          1
          2
    """
    return tree(label(t) + 1, [increment(b) for b in branches(t)])
"""
print("fib(3)")
print_tree(fib_tree(3))
print("fib(3) all incremented")
print_tree(increment(fib_tree(3)))
"""


def tree_map(t,f):
    """Return a tree like t but with all labels having f applied to them."""
    return tree(f(label(t)), [tree_map(b,f) for b in branches(t)])

#print_tree(tree_map(fib_tree(3), lambda l:l*10))
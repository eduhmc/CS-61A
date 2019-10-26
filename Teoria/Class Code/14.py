### DEMO1: objects

from datetime import date
today = date.today()
final = date(2019, 5, 14)
str(final - today)
### Dot expressions for attributes and methods
today.year
today.strftime('%A, %B %d')
type(today)

### DEMO2: strings

s = 'Hello'
s.upper()
s.lower()
s.swapcase()

ord('A')
hex(ord('A'))

print('\a')
print('1\n2\n3')

### DEMO3: unicode

from unicodedata import lookup, name
name('A')
lookup('LATIN CAPITAL LETTER A')
len('A')
'A'.encode()

b = lookup('BASKETBALL AND HOOP')
len(b)
b.encode()

### DEMO4: lists

suits = ['coin', 'string', 'myriad']  # A list literal (denominations of money)
original_suits = suits
suits.pop()             # Removes and returns the final element ... europe
suits.remove('string')  # Removes the first element that equals the argument ... europe
suits.append('cup')              # Add an element to the end ... spanish added
suits.extend(['sword', 'club'])  # Add all elements of a list to the end ... spanish added
suits[2] = 'spade'  # Replace an element ... italians "spade is italian for sword"
suits
suits[0:2] = ['heart', 'diamond']  # Replace a slice ... french

### DEMO5: dictionary

nums = {'I': 1.0, 'V': 5, 'X': 10}
nums['X']
nums['I'] = 1
nums['L'] = 50
nums
nums.pop('X')

### DEMO6: tuples

(3, 4, 5, 6)
3, 4, 5, 6
()
tuple()
tuple([1, 2, 3])
# tuple(2)
(2,)
(3, 4) + (5, 6)
(3, 4, 5) * 2
5 in (3, 4, 5)

# {[1]: 2}
{1: [2]}
{(1, 2): 3}
# {([1], 2): 3}
{tuple([1, 2]): 3} 

### DEMO7: identity

def identity_demos():
    a = [10]
    b = a
    a == b
    a is b
    a.extend([20, 30])
    a == b
    a is b
    
    a = [10]
    b = [10]
    a == b
    a is not b
    a.append(20)
    a != b
    

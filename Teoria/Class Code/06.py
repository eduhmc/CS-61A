### DEMO: Return statements

def end(n, d):
    """Print the final digits of N in reverse order until D is found.    

    >>> end(34567, 5)
    7
    6
    5
    """
    while n > 0:
        last, n = n % 10, n // 10
        print(last)
        if d == last:
            return None

### FINDING pattern

def find_digit(n, d):
	"""Return True if digit D is found in number N, otherwise False

	>>> find_digit(12345689,7)
	False
	>>> find_digit(12345689,5)
	True
	"""
	while n > 0:
		if n % 10 == d:
			return True
		n = n // 10
	return False

### FINDING pattern with HOFs, more general than just finding a digit

def finder(n, pred):
	"""Return True if digit D is found in number N, otherwise False

	>>> finder(31415926535,lambda d: d==8 or d==7)
	False
	>>> finder(3141592653589,lambda d: d==8 or d==7)
	True
	"""
	while n > 0:
		if pred(n % 10):
			return True
		n = n // 10
	return False

### REVERSE pattern

def reverse(n):
	"""Return a number with the digits of the input number N reversed

	>>> reverse(31415926535897932)
	23979853562951413
	"""
	rev = 0
	while n > 0:
		rev = rev*10 + n % 10
		n = n // 10
	return rev

### MAPPING pattern

def mapper(n,f):
	"""Return a number each digit of N transformed by function F

	>>> mapper(1234111,lambda d: d*2)
	2468222
	>>> mapper(1624690,lambda d: 9-d)
	8375309
	"""
	mapped, place = 0, 0
	while n > 0:
		mapped += f(n % 10)*10**place
		n = n // 10
		place += 1
	return mapped

### ABSTRACTION...GENERALIZING THESE PATTERNS INTO ONE

def process_digit(n,digit_mapper,digit_check,digit_retval):
	"""Process every digit of number N through DIGIT_CHECK, 
	which if True calls DIGIT_RETVAL. Otherwise, each digit
	passes through DIGIT_MAPPER which keeps track of the output
	fragment so far and updates the the mapped return value

	>>> new_finder = lambda n,pred: process_digit(n, lambda mapped,place,d:False, lambda d:pred(d), lambda mapped,place,d:True)
	>>> new_finder(31415926535,lambda d: d==8 or d==7)
	False
	>>> new_finder(3141592653589,lambda d: d==8 or d==7)
	True

	>>> new_reverse = lambda n: process_digit(n, lambda mapped,place,d:mapped*10+d, lambda d:False, lambda mapped,place,d:None)
	>>> new_reverse(31415926535897932)
	23979853562951413

	>>> new_mapper = lambda n,f: process_digit(n, lambda mapped,place,d:mapped+f(d)*10**place, lambda d:False, lambda mapped,place,d:None)
	>>> new_mapper(1234111,lambda d: d*2)
	2468222
	>>> new_mapper(1624690,lambda d: 9-d)
	8375309
	"""	
	mapped, place = 0, 0
	while n > 0:
		d = n%10
		if digit_check(d):
			return(digit_retval(mapped,place,d))
		mapped = digit_mapper(mapped,place,d)
		n = n // 10
		place += 1
	return mapped

### HAPPY tree and "Melancoil"
### https://youtu.be/_DpzAvb3Vk4
### https://en.wikipedia.org/wiki/Happy_number

def happy_child(n):
	"""Return the next number in the happy sequence, 
	derived by summing the squares of the digits of N

	>>> happy_child(13)
	10
	>>> happy_child(145)
	42
	"""
	sum = 0
	while n > 0:
		sum, n = sum + (n % 10) ** 2, n // 10
	return sum

def new_happy_child(n):
	"""Return the next number in the happy sequence, 
	derived by summing the squares of the digits of N

	>>> new_happy_child(13)
	10
	>>> new_happy_child(145)
	42
	"""
	return process_digit(n, lambda mapped,place,d:mapped+d*d, lambda d:False, lambda mapped,place,d:None)

def happy_v1(n):
	"""Return True if the number is happy, otherwise False.
	A happy number is one which, after going through successive
	new_happy_children (summing the squares of the digits) becomes 1.
	While this is normally coded recursively, we're lucky that all numbers
	less than 1000 don't take more than 20 numbers until they converge, and
	if they don't, they're not in the happy tree (thus they're not happy)

	>>> happy_v1(7)
	True
	>>> happy_v1(6)
	False
	"""
	count = 0
	while count < 25 and n != 1:
		count, n = count + 1, happy_child(n)
	return n == 1

def happy_dot(n):
	"""Print a dot file based on the happy sequence staring at N
	https://www.graphviz.org/

	>>> happy_dot(7)
	digraph G {
	7->49
	49->97
	97->130
	130->10
	10->1
	}
	>>> happy_dot(4)
	digraph G {
	4->16
	16->37
	37->58
	58->89
	89->145
	145->42
	42->20
	20->4
	}
	"""
	count = 0
	seen = set()
	print("digraph G {")
	while count < 25 and n != 1:
		if n not in seen:
			print(str(n) + "->" + str(happy_child(n)))
			seen.add(n)
		count, n = count + 1, happy_child(n)
	print("}")

#happy_dot(4)
#happy_dot(7)

def happy_fancydot(orig_n,seen):
	"""Print the links of a graphviz dot file based on the happy sequence starting at N"""
	n = orig_n
	count = 0
	while count < 25 and n != 1:
		if n not in seen:
			print(str(n) + "->" + str(happy_child(n)))
			seen.add(n)
		count, n = count + 1, happy_child(n)
	if n == 1:
		print(str(orig_n) + " [ style = filled, color=yellow ];")
	elif orig_n in [89, 145, 42, 20, 4, 16, 37, 58]:
		print(str(orig_n) + " [ style = filled, color=red ];")
	else:
		print(str(orig_n) + " [ style = filled, color=green ];")

def happy_tree(n):
	"""Print a pretty dot file of the happy and unhappy tree structure for numbers from 1 to N"""

	seen = set()
	print("digraph G {")
	while(n > 0):
		happy_fancydot(n, seen)
		n -= 1
	print("}")

#happy_tree(200)
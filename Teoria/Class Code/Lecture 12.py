def divisors(n):
	return [x for x in range(1,n+1) if n % x == 0]

print(divisors(12))





def cheer():
	for _ in range(3):
		print("Go Bears!")

#cheer()

def sum_below(n):
	total = 0
	for i in range(n):
		total += i
	return total

#print(sum_below(5))








def count_for(s, value):
	total = 0
	for element in s:
		if element == value:
			total += 1
	return total

#print(count_for([1,2,4,2,5,2],2))


import sys
import math

numbers = []

for arg in sys.argv[1:]:
	numbers.append(float(arg))

count = len(numbers)

def minmax(numbers):
	mini = numbers[0]
	maxi = numbers[0]
	for i in numbers:
		if i < mini: mini = i
		if i > maxi: maxi = i
	return mini, maxi
	
def mean(numbers):
	total = 0
	for i in numbers:
		total += i
	return total/len(numbers)

def std(numbers):
	m = mean(numbers)
	sum = 0
	for i in numbers:
		p = i-m
		sum += p**2
	return math.sqrt(sum / len(numbers))

print(count)
print(minmax(numbers))
print(mean(numbers))
print(std(numbers))
		

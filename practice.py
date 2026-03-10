import math


def minimum(vals):
	mini = vals[0]
	for val in vals[1:]:
		if val < mini: mini = val
	return mini

list= [0, 20, 20, 11, 100, 0, -1, 253, 29]
print(minimum(list))

def minmax(vals):
	mini = vals[0]
	maxi = vals[0]
	for val in vals[1:]:
		if val < mini: mini = val
		elif val > maxi: maxi = val
	return mini, maxi
print(minmax(list))

def mean(vals):
	sum = 0
	for val in vals: sum += val
	return sum/len(vals)
print(mean(list))

def ent(prob):
	h = 0
	for p in prob:
		if minimum(prob) <= 0: h -= p+1 * math.log2(p+1)
		else:      h -= p * math.log2(p)
	return h
print(f'entropy: {ent([0.4, 0.6, 0.2, 1, 0, 0, 0])}')
print()

def dkl(P, Q):
	d = 0
	
	if len(P) != len(Q):
		print("error1")
		return None
		
	for p, q in zip(P, Q):
		if p < 0 or q < 0:
			print("error2")
			return None
		if p == 0:
			continue
		if q == 0:
			return float("inf")
	
		d += p * math.log2(p/q)
	return d
p1 = [0.4, 0.3, 0.2, 0.5]
p2 = (0.34, 0.13, 0.2)
print(dkl(p1,p2))
print()
print("="*20)
print()

#input()
#line = input('type something and hit return: ')
#print('that line was', len(line), 'characters long')


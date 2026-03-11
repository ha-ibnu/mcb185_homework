import sys

alphabet = sys.argv[1]
match = sys.argv[2]
mismatch = sys.argv[3]

print(' ', end= ' ')
for i in range(len(alphabet)):
	print(alphabet[i], end= ' ')
print()
for i in range(len(alphabet)):
	print(alphabet[i], end= ' ')
	for j in range(len(alphabet)):
		if i == j: print(match, end= ' ')
		else: print(mismatch, end= ' ')
	print()	

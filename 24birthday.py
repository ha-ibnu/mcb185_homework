import sys
import random

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

matches = 0

for i in range(trials):
	calendar = [0] * days
	shared = False
	
	for j in range(people):
		birthday = random.randint(0, days-1)
		calendar[birthday] += 1
		
		if calendar[birthday] > 1:
			shared = True
			break
	
	if shared:
		matches += 1

prob =  matches/trials

print(f'{prob*100:.2f}%')

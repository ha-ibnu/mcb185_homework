import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

matches = 0

for i in range(trials):
	birthday = []
	
	for j in range(people):
		bday = random.randint(0, days-1)
		birthday.append(bday)
		
		total_match = False
	for k in range(len(birthday)):
		for l in range(k +1, len(birthday)):
			
			if birthday[k] == birthday[l]:
				total_match = True
	
	if total_match:
		matches += 1

probability = matches / trials
print(f'owh they match with {probability} probalility')



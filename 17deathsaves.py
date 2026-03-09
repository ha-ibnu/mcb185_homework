import random

fail = 0
succ = 0

while fail < 3 and succ < 3:
	roll = random.randint(1, 20)
	
	if roll == 1:
		fail += 2
	elif roll == 20:
		print("revived")
		break
	elif roll < 10:
		fail += 1
	else:
		succ += 1
		
	print(f"Roll: {roll}, Failures: {fail}, Successes: {succ}")
	
died = 0
stabilized = 0
revived = 0
simulation = 100

for i in range(100):
	fail = 0
	succ = 0
	while fail < 3 and succ < 3:
		roll = random.randint(1, 20)
		if roll == 1:
			fail += 2
		elif roll == 20:
			revived += 1
			break
		elif roll < 10:
			fail += 1
		else:
			succ += 1
	else:
		if fail >= 3:
			died += 1
		elif succ >= 3:
			stabilized += 1
			
print(f'prob die: {died / simulation}')
print(f'prob stabilized: {stabilized / simulation}')
print(f'prob revived: {revived / simulation}')
print(f'prpb alive: {1 - (died / simulation)}')

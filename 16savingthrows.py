import random

#pi = 0
#inside = 0
#total = 0

#while True:
#	x = random.random()
#	y = random.random()
#	c = x**2 + y**2
#	total += 1
#	if c <= 1:
#		inside += 1
#	pi = 4 * inside/total
	
#	print(pi)

# Normal rolls
print("Normal rolls:")
for dc in [5, 10, 15]:
    roll = random.randint(1, 20)
    if roll >= dc:
        print(f"DC {dc}: rolled {roll} = success")
    else:
        print(f"DC {dc}: rolled {roll} = fail")

# Advantage rolls
print("\nAdvantage rolls:")
for dc in [5, 10, 15]:
    roll1 = random.randint(1, 20)
    roll2 = random.randint(1, 20)
    result = max(roll1, roll2)
    if result >= dc:
        print(f"DC {dc}: rolled {roll1}, {roll2} = success (advantage)")
    else:
        print(f"DC {dc}: rolled {roll1}, {roll2} = fail (advantage)")

# Disadvantage rolls
print("\nDisadvantage rolls:")
for dc in [5, 10, 15]:
    roll1 = random.randint(1, 20)
    roll2 = random.randint(1, 20)
    result = min(roll1, roll2)
    if result >= dc:
        print(f"DC {dc}: rolled {roll1}, {roll2} = success (disadvantage)")
    else:
        print(f"DC {dc}: rolled {roll1}, {roll2} = fail (disadvantage)")


	

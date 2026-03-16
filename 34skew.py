import sequence
import sys
import mcb185

path = sys.argv[1]
w = int(sys.argv[2])

for defline, seq in mcb185.read_fasta(path):
	g = 0
	c = 0
	
	for nt in seq[:w]:
		if nt == 'G': g += 1
		elif nt == 'C': c += 1
	
	if g + c == 0: skew = 0
	else: skew = (g -c) / (g + c)
	print(0, (g + c)/w, skew)
	
	for i in range(1, len(seq) -w +1):
		left = seq[i-1]
		right = seq[i+w-1]
		
		if left == 'G': g -= 1
		elif left == 'C': c -= 1
		
		if right == 'G': g += 1
		elif right == 'C': c +=1
		
		if g + c == 0: skew = 0
		else: skew = (g -c) / (g + c)
		
		print(i, (g+c)/w, skew)
			


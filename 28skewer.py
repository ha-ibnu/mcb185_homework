import sequence
import sys
import mcb185

path = sys.argv[1]
w = int(sys.argv[2])

for defline, seq in mcb185.read_fasta(path):
	for i in range(len(seq) -w + 1):
		s = seq[i:i+w]
		print(i, sequence.gc_comp(s), sequence.gc_skew(s))

#s = 'ACGTACGTGGGGGACGTACGTCCCCC'
#w = 10
#for i in range(len(s) -w +1):
#	p = s[i: i+w]
#	print(i, seq.gc_comp(p), seq.gc_skew(p)) 


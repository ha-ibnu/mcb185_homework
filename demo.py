# import sys

# def read_catalog(filepath):
# 	catalog = []
# 	with open(filepath) as fp:
# 		for line in fp:
			
# 			if line.startswith('#'): continue
# 			name, length, seq, desc = line.rstrip().split(',')
# 			record = {
# 			'Name': name,
# 			'Length': length,
# 			'Sequence': seq,
# 			'Description': desc
# 			}
# 			catalog.append(record)
# 	return catalog

# path = sys.argv[1]

# catalog = read_catalog(path)
# for primer in catalog:
# 	print(primer['Description'], primer['Sequence'])
	
seq =  'ACACACATTCAGATCGATCGACGCGACACACATGCGATGTGCATCGCGCTAGCATGCATAAAAAAATTAGCTGGGT'
k = 4
kloc = {}
for i in range(len(seq) -k +1):
	kmer = seq[i:i+k]
	if kmer not in kloc: kloc[kmer] = []
	kloc[kmer].append(i)
print(kloc)
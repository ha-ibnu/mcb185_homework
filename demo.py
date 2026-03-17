import sys


def read_catalog(filepath):
	catalog = []
	with open(filepath) as fp:
		for line in fp:
			
			if line.startswith('#'): continue
			name, length, seq, desc = line.rstrip().split(',')
			record = {
			'Name': name,
			'Length': length,
			'Sequence': seq,
			'Description': desc
			}
			catalog.append(record)
	return catalog

path = sys.argv[1]

catalog = read_catalog(path)
for primer in catalog:
	print(primer['Name'], primer['Description'])
	

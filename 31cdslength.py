import gzip
import sys

path =  sys.argv[1]

with gzip.open(path, 'rt') as fp:
	for line in fp:
		if line[0] != '#':
			words = line.split()
			if words[2] =='CDS':
				beg = int(words[3])
				end = int(words[4])
				print(beg-end+1)

with gzip.open(path, 'rt') as fp:
	for line in fp:
		if line[0] == '#': continue
		words = line.split()
		if words[2] != "CDS": continue
		beg = int(words[3])
		end = int(words[4])
		print(end - beg + 1)

#my library mcb185

def transcribe(dna):
	return dna.replace('T', 'U')

def revcomp(dna):
	rc = []
	for nt in dna [::-1]:
		if nt == 'A': rc.append('T')
		elif nt == 'C': rc.append('G')
		elif nt == 'G': rc.append('C')
		elif nt == 'T': rc.append('A')
		else: rc.append('N')
	return ''.join(rc)
	
def translate(dna):
	aas = []
	for i in range(0, len(dna), 3):
		codon = dna[i: i+3]
		if codon == 'ATG': aas.append('M')
		elif codon == 'TAA': aas.append('*')
		elif codon == 'TAG': aas.append('*')
		elif codon == 'TGA': aas.append('*')
		elif codon == 'TAG': aas.append('*')
		else: 				 aas.append('X')
	return ''.join(aas)
	
def translate1(dna):
	codons = ('ATG', 'TAA', 'TAG', 'TGA')
	aminos = 'M***'
	aas = []
	for i in range(0, len(dna), 3):
		codon = dna[i: i+3]
		if codon in codons:
			idx = codons.index(codon)
			aa = aminos[idx]
			aas.append(aa)
		else:
			aas.append('X')
	return ''.join(aas)

def gc_comp(seq):
	return (seq.count('C') + seq.count('G')) / len(seq)

def gc_skew(seq):
	c = seq.count('C')
	g = seq.count('G')
	if c +g == 0: return 0
	return (g - c) / (g + c)
	
aas = 'ACDEFGHIKLMNPQRSTVWY'
kd  = [1.8,2.5,-3.5,-3.5,2.8,-0.4,-3.2,4.5,-3.9,3.8,
       1.9,-3.5,-1.6,-3.5,-4.5,-0.8,-0.7,4.2,-0.9,-1.3]

def kd_avg(seq):
	total = 0
	for aa in seq:
		i = aas.index(aa)
		total += kd[i]
	return total / len(seq)
	
def hydrophob(seq, start, end, w, cutoff):
	for i in range(start, end -w +1):
		win = seq[i:i+w]
		if 'P' in win: continue
		
		if kd_avg(win) >= cutoff:
			return True
	return False

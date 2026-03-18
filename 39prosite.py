import sys
import re
import mcb185

path = sys.argv[1]

# for defline, seq in mcb185.read_fasta(path):
#     if 'DKTGT' in seq: print(defline)


# for defline, seq in mcb185.read_fasta(path):
#     if re.search('DKTGT', seq): print(defline)

# for defline, seq in mcb185.read_fasta(path):
#     if re.search('C.{2,4}C.{3}[LIVMFYWC].{8}H.{3,5}H', seq): print(defline)

pat = 'C.{2,4}C.{3}[LIVMFYWC].{8}H.{3,5}H'
for defline, seq in mcb185.read_fasta(path):
    m = re.search(pat, seq)
    if m: print(m.group(1))
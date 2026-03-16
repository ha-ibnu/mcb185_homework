import sequence as seq

print(seq.transcribe('ATCG'*40))
print(seq.revcomp('ATTTTTTACGCC'))


print(seq.translate('ATGACTCATCACAGATCAT'))
print()

s = 'ACGTGGGGGGCATATG'
print(seq.gc_comp(s))
print(seq.gc_skew(s), seq.gc_skew(seq.revcomp(s)))

import sys
import mcb185
import sequence

path = sys.argv[1]

#for defline, seq in mcb185.read_fasta(path):
#	signal = False
#	tm = False
#	end = min(30, len(seq))
	
#	for i in range(end -8 + 1):
#		w = seq[i:i+8]
		
#		if 'P' in w: continue
		
#		if sequence.kd_avg(w) >= 2.5:
#			signal = True
#			break
	
#	if signal:
#		for i in range(30, len(seq) -11 +1):
#			w = seq[i:i+11]
			
#			if 'P' in w: continue
#			if sequence.kd_avg(w) >= 2.0:
#				tm = True
#				break
	
#	if signal and tm:
#		print(defline)
			
for defline, seq in mcb185.read_fasta(path):
	n_term = min(30, len(seq))
	signal = sequence.hydrophob(seq, 0, n_term, 8, 2.5)
	tm = False
	
	if signal and len(seq)> 30:
		tm = sequence.hydrophob(seq, 30, len(seq), 11, 2.0)
	
	if signal and tm:
		print(defline)
	
	
	

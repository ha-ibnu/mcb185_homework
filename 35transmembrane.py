import sys
import mcb185
import sequence

path = sys.argv[1]

for defline, seq in mcb185.read_fasta(path):
	signal = False
	tm = False
	end = min(30, len(seq))
	
	for i in range(end -8 + 1):
		w = seq[i:i+8]
		
		if 'P' in w: continue
		
		if sequence.kd_avg(w) >= 2.5:
			signal = True
			break
	
	if signal:
		for i in range(30, len(seq) -11 +1):
			w = seq[i:i+11]
			
			if 'P' in w: continue
			if sequence.kd_avg(w) >= 2.0:
				tm = True
				break
	
	if signal and tm:
		print(defline)
			
			

def stop_cod(codons,i, stop_codons = ('TAA', 'TGA', 'TAG')):
	d=dict()	
	for x in stop_codons:
		if x in codons: 
			d[x] = [codons.index(x)]
	lt=list()
	for key, val in d.items():
   		lt.append([val,key])
	lt.sort()
	a=lt[0]
	y=a[1]
	return y 


from itertools import takewhile
from Bio import SeqIO
def translate_dna(sequence, record_id, stop_codons = ('TAA', 'TGA', 'TAG')):       
    answer = []
    for frame in range (2,3): 
    	trimmed_sequence = sequence[frame:]
    	codons = [trimmed_sequence[i:i+3] for i in range(0, len(trimmed_sequence), 3)]
    	for i in range (len(codons)):
    		if codons[i]=='ATG':
				start= i
				try: 
					y= stop_cod(codons[i:],i, stop_codons = ('TAA', 'TGA', 'TAG'))
					stop = codons[i:].index(y)+i
					codon= codons[start:stop+1]
					answer.append ((len(codon)*3, frame+1, ((start)*3)+frame+1, stop*3, record_id[-3:]))
				except: continue
	answer.sort()
	return answer 
for record in SeqIO.parse("dna1.fasta.fasta", "fasta"):
	orf_list = translate_dna(record.seq, record.id) 
	for length, frame, start, end, record_id  in orf_list:
   		print(length, frame, start, end, record_id)
fname = raw_input("Enter file name: ")

map= {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',}

def translate_RNA_codon(seq): 
	prot=''
	start=seq.find('ATG')
	seq_start=seq[int(start):]
	stop=seq_start.find('TAA')
	cds=str(seq_start[:int(stop)+3])
	for i in range (0, len(cds), 3):
#		if map[codon]=='_':break #to avoid printing STop instes-ad of using stop=seq_start.find('TAA')
		if cds[i:i+3] in map: 
			codon=cds[i:i+3]
			prot+= map[codon]
	return prot

Outfile='Output.'+fname 
with open(fname) as fh, open(Outfile,"w") as trans_prot:
	for line in fh:# otherwise you got error unhashable type: 'list'
		if line.startswith('>') : 
			header=line
		else:
			line=line.replace('\n','')
			my_seq=translate_RNA_codon(line)
			final =header+my_seq +'\n'
			trans_prot.write(final)
	fh.close()
	trans_prot.close()
print "Done !"
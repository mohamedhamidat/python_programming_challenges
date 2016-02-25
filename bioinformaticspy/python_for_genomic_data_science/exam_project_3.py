from Bio import SeqIO
count=0
for record in SeqIO.parse("dna1.fasta.fasta", "fasta"):
	print '>',record.id,'\n',record.seq 
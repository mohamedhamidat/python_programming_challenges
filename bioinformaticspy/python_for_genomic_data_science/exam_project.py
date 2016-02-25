from Bio import SeqIO

l1= [len(seq_record) for seq_record in SeqIO.parse("dna1.fasta.fasta", "fasta")]
#	l1.append(len(seq_record))
#	d.get(len(seq_record))
print 'max',max(l1)
print 'min',min(l1)
#    print(seq_record.id)
#    print(repr(seq_record.seq))
#	print len(seq_record)
count=0
table=22
frame=1
min_pro_len=300
maxi = []
for record in SeqIO.parse("dna1.fasta.fasta", "fasta"):
	count=count+1
	for strand, nuc in [(+1, record.seq)]:
		length = 3 * ((len(record)-frame) // 3) #Multiple of three
		for pro in nuc[frame:frame+length].translate(table).split("*"):
				if len(pro)*3 >= min_pro_len*3:
					#print len(pro)*3
					maxi.append(len(pro)*3)
print "longest orf in reading frame",frame, max(maxi), count 



					
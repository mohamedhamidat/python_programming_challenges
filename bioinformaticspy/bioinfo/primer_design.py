#blatsn
from Bio.Blast import NCBIWWW
from Bio import SeqIO
from Bio import Seq

def primer_design("NC_000913.3","gi"):
   
    result_handle = NCBIWWW.qblast("blastn", "NC_000913.3", first_seq)
    
    save_file = open("my_blast.xml", "w")
    save_file.write(result_handle.read())
    save_file.close()
    result_handle.close()
    print "****Alignment****"
    print "sequence:", alignment.title
    print "length:", alignment.length
    print "E-value:", hsp.expect
    print hsp.query[:50] + "..."
    print hsp.match[:50] + "..."
    print hsp.sbjct[:50] + "..."
#function de compute GC content
def gc_content(bas_seq):
#Return the percentage of G and C characters in base_seq
    seq = bas_seq.upper()
    f= float((seq.count('G')+ seq.count('C'))/len(seq))
    return f
    
def gc_content(base_seq):

    seq = base_seq.upper()
    return (seq.count('G') + seq.count('C')) / len(seq)
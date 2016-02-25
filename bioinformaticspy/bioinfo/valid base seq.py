#validate_base_sequence True or False
def validate_base_sequence(base_sequence):
    seq= base_sequence.upper()
# entirely of upper- or lowercase T, C, A, and G characters
    return len(seq)== (seq.count('T')+ seq.count('A')+\
                        seq.count('G')+ seq.count('C'))


                                 
def number_base_sequence(base_sequence):
    seq= base_sequence.upper()
# entirely of upper- or lowercase T, C, A, and G characters
    len(seq)== (seq.count('T')+ seq.count('A')+\
                        seq.count('G')+ seq.count('C'))
    print len(seq)
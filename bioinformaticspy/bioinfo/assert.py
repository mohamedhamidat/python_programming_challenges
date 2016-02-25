#assert

def validate_base_sequence(base_seq):
    seq= base_seq.upper()
# entirely of upper- or lowercase T, C, A, and G characters
    return len(seq)== (seq.count('T')+ seq.count('A')+\
                        seq.count('G')+ seq.count('C'))


def gc_content(base_seq):
#"""Return the percentage of G and C characters in base_seq"""
    seq = base_seq.upper()
    assert validate_base_sequence(base_seq), \
            'argument has invalid characters'
    return ((base_seq.count('G') + base_seq.count('C')) /
            len(base_seq))

Python 2.7.5 (default, May 15 2013, 22:43:36) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> dna

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    dna
NameError: name 'dna' is not defined
>>> mydna

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    mydna
NameError: name 'mydna' is not defined
>>> dna = ’gcatgacgttattacgactctgtcacgccgcggtgcgactgaggcgtggcgtctgctggg’
SyntaxError: invalid syntax
>>> dna = "gcatgacgttattacgactctgtcacgccgcggtgcgactgaggcgtggcgtctgctggg"
>>> dnasuite="cctttacttcgcctccgcgccctgcattccgttcctggcctcg"
>>> dna=dna+dnasuite
>>> dna
'gcatgacgttattacgactctgtcacgccgcggtgcgactgaggcgtggcgtctgctgggcctttacttcgcctccgcgccctgcattccgttcctggcctcg'
>>> len(dna)
103
>>> "n" in dna
False
>>> count(dna, 'a')

Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    count(dna, 'a')
NameError: name 'count' is not defined
>>> count(dna,"a")

Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    count(dna,"a")
NameError: name 'count' is not defined
>>> a= count(dna, "a")

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a= count(dna, "a")
NameError: name 'count' is not defined
>>> from string import *
>>> count(dna, 'a')
10
>>> 'n'in dna
False
>>> 'n' in dna
False
>>> replace(dna, 'a', 'A')
'gcAtgAcgttAttAcgActctgtcAcgccgcggtgcgActgAggcgtggcgtctgctgggcctttActtcgcctccgcgccctgcAttccgttcctggcctcg'
>>> dna
'gcatgacgttattacgactctgtcacgccgcggtgcgactgaggcgtggcgtctgctgggcctttacttcgcctccgcgccctgcattccgttcctggcctcg'
>>> count(dna,'g','c')

Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    count(dna,'g','c')
  File "C:\Python27\lib\string.py", line 348, in count
    return s.count(*args)
TypeError: slice indices must be integers or None or have an __index__ method
>>> a=(count(dna,'g')+count(dna,'c'))
>>> gc=a/len(dna)
>>> gc
0
>>> a
66
>>> len(dna)
103
>>> b=len(dna)
>>> gc=a/b
>>> gc
0
>>> int(gc)
0
>>> count(dna,'a,g')
0
>>> gc=a/float(len(dna))
>>> gc
0.6407766990291263
>>> t=maketrans("AGCTagct", "TCGAtcga")
>>> t
'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f !"#$%&\'()*+,-./0123456789:;<=>?@TBGDEFCHIJKLMNOPQRSAUVWXYZ[\\]^_`tbgdefchijklmnopqrsauvwxyz{|}~\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff'
>>> translate(dna, t)
'cgtactgcaataatgctgagacagtgcggcgccacgctgactccgcaccgcagacgacccggaaatgaagcggaggcgcgggacgtaaggcaaggaccggagc'
>>> translate(CCAGATC, t)

Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    translate(CCAGATC, t)
NameError: name 'CCAGATC' is not defined
>>>  Count(TACGCATTACAAAGCACA, AA)
 
  File "<pyshell#36>", line 1
    Count(TACGCATTACAAAGCACA, AA)
   ^
IndentationError: unexpected indent
>>> count(TACGCATTACAAAGCACA, AA)

Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    count(TACGCATTACAAAGCACA, AA)
NameError: name 'TACGCATTACAAAGCACA' is not defined
>>> count('TACGCATTACAAAGCACA', 'AA')
1
>>> import numpy as np

Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    import numpy as np
ImportError: No module named numpy
>>> dna ="ttcacctatgaatggactgtccccaaagaagtaggacccactaatgcagatcctgtg
tgtctagctaagatgtattattctgctgtggatcccactaaagatatattcactgggcttattgggccaa
tgaaaatatgcaagaaaggaagtttacatgcaaatgggagacagaaagatgtagacaaggaattctattt
gtttcctacagtatttgatgagaatgagagtttactcctggaagataatattagaatgtttacaactgca
cctgatcaggtggataaggaagatgaagactttcaggaatctaataaaatgcactccatgaatggattca
tgtatgggaatcagccgggtctcactatgtgcaaaggagattcggtcgtgtggtacttattcagcgccgg
aaatgaggccgatgtacatggaatatacttttcaggaaacacatatctgtggagaggagaacggagagac
acagcaaacctcttccctcaaacaagtcttacgctccacatgtggcctgacacagaggggacttttaatg
ttgaatgccttacaactgatcattacacaggcggcatgaagcaaaaatatactgtgaaccaatgcaggcg
gcagtctgaggattccaccttctacctgggagagaggacatactatatcgcagcagtggaggtggaatgg
gattattccccacaaagggagtgggaaaaggagctgcatcatttacaagagcagaatgtttcaaatgcat
ttttagataagggagagttttacataggctcaaagtacaagaaagttgtgtatcggcagtatactgatag
cacattccgtgttccagtggagagaaaagctgaagaagaacatctgggaattctaggtccacaacttcat
gcagatgttggagacaaagtcaaaattatctttaaaaacatggccacaaggccctactcaatacatgccc
atggggtacaaacagagagttctacagttactccaacattaccaggtgaaactctcacttacgtatggaa
aatcccagaaagatctggagctggaacagaggattctgcttgtattccatgggcttattattcaactgtg
gatcaagttaaggacctctacagtggattaattggccccctgattgtttgtcgaagaccttacttgaaag
tattcaatcccagaaggaagctggaatttgcccttctgtttctagtttttgatgagaatgaatcttggta
cttagatgacaacatcaaaacatactctgatcaccccgagaaagtaaacaaagatgatgaggaattcata
gaaagcaataaaatgcatgctattaatggaagaatgtttggaaacct"
SyntaxError: EOL while scanning string literal
>>> dan="ttcacctatgaatggactgtccccaaagaagtaggacccactaatgcagatcctgtgtgtctagctaagatgtattattctgctgtggatcccactaaagatatattcactgggcttattgggccaatgaaaatatgcaagaaaggaagtttacatgcaaatgggagacagaaagatgtagacaaggaattctatttgtttcctacagtatttgatgagaatgagagtttactcctggaagataatattagaatgtttacaactgcacctgatcaggtggataaggaagatgaagactttcaggaatctaataaaatgcactccatgaatggattcatgtatgggaatcagccgggtctcactatgtgcaaaggagattcggtcgtgtggtacttattcagcgccggaaatgaggccgatgtacatggaatatacttttcaggaaacacatatctgtggagaggagaacggagagacacagcaaacctcttccctcaaacaagtcttacgctccacatgtggcctgacacagaggggacttttaatgttgaatgccttacaactgatcattacacaggcggcatgaagcaaaaatatactgtgaaccaatgcaggcggcagtctgaggattccaccttctacctgggagagaggacatactatatcgcagcagtggaggtggaatgggattattccccacaaagggagtgggaaaaggagctgcatcatttacaagagcagaatgtttcaaatgcatttttagataagggagagttttacataggctcaaagtacaagaaagttgtgtatcggcagtatactgatagcacattccgtgttccagtggagagaaaagctgaagaagaacatctgggaattctaggtccacaacttcatgcagatgttggagacaaagtcaaaattatctttaaaaacatggccacaaggccctactcaatacatgcccatggggtacaaacagagagttctacagttactccaacattaccaggtgaaactctcacttacgtatggaaaatcccagaaagatctggagctggaacagaggattctgcttgtattccatgggcttattattcaactgtggatcaagttaaggacctctacagtggattaattggccccctgattgtttgtcgaagaccttacttgaaagtattcaatcccagaaggaagctggaatttgcccttctgtttctagtttttgatgagaatgaatcttggtacttagatgacaacatcaaaacatactctgatcaccccgagaaagtaaacaaagatgatgaggaattcatagaaagcaataaaatgcatgctattaatggaagaatgtttggaaacct"
>>> EcoRI = 'gaattc'
>>> find(dna, EcoRI)
-1
>>> find (dan, EcoRI)
186
>>> index(dan, EcoRI)
186
>>> find (dan, EcoRI, 187)
874
>>> def restrict(dna, enz):
"print all start positions of a restriction site"
site = find (dan, enz)
while site != -1:
print "restriction site %s at position %d" % (enz, site)
site = find (dan, enz, site + 1)
  File "<pyshell#47>", line 2
    "print all start positions of a restriction site"
                                                    ^
IndentationError: expected an indented block
>>> def restrict(dna, enz):
site = find (dan, enz)
while site != -1:
print "restriction site %s at position %d" % (enz, site)
site = find (dan, enz, site + 1)
  File "<pyshell#48>", line 2
    site = find (dan, enz)
       ^
IndentationError: expected an indented block
>>> a= def restrict(dna, enz):
"print all start positions of a restriction site"
site = find (dan, enz)
while site != -1:
print "restriction site %s at position %d" % (enz, site)
site = find (dan, enz, site + 1)
SyntaxError: invalid syntax
>>> def restrict(dna, enz):
"print all start positions of a restriction site"
site = find (dan, enz)
while site != -1:
print "restriction site %s at position %d" % (enz, site)
site = find (dan, enz, site + 1)
  File "<pyshell#50>", line 2
    "print all start positions of a restriction site"
                                                    ^
IndentationError: expected an indented block
>>> def restrict(dna, enz):
site = find (dan, enz)
while site != -1:
    print "restriction site %s at position %d" % (enz, site)
    site = find (dan, enz, site + 1)
    
  File "<pyshell#51>", line 2
    site = find (dan, enz)
       ^
IndentationError: expected an indented block
>>> from string import *
def restrict(dna, enz):
site = find (dan, enz)
while site != -1:
    print "restriction site %s at position %d" % (enz, site)
    site = find (dan, enz, site + 1)
    
>>> from string import *
def restrict(dan, enz):
site = find (dan, enz)
while site != -1:
    print "restriction site %s at position %d" % (enz, site)
    site = find (dan, enz, site + 1)
    
>>> restrict(dan, EcoRI)

Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    restrict(dan, EcoRI)
NameError: name 'restrict' is not defined
>>> dan
'ttcacctatgaatggactgtccccaaagaagtaggacccactaatgcagatcctgtgtgtctagctaagatgtattattctgctgtggatcccactaaagatatattcactgggcttattgggccaatgaaaatatgcaagaaaggaagtttacatgcaaatgggagacagaaagatgtagacaaggaattctatttgtttcctacagtatttgatgagaatgagagtttactcctggaagataatattagaatgtttacaactgcacctgatcaggtggataaggaagatgaagactttcaggaatctaataaaatgcactccatgaatggattcatgtatgggaatcagccgggtctcactatgtgcaaaggagattcggtcgtgtggtacttattcagcgccggaaatgaggccgatgtacatggaatatacttttcaggaaacacatatctgtggagaggagaacggagagacacagcaaacctcttccctcaaacaagtcttacgctccacatgtggcctgacacagaggggacttttaatgttgaatgccttacaactgatcattacacaggcggcatgaagcaaaaatatactgtgaaccaatgcaggcggcagtctgaggattccaccttctacctgggagagaggacatactatatcgcagcagtggaggtggaatgggattattccccacaaagggagtgggaaaaggagctgcatcatttacaagagcagaatgtttcaaatgcatttttagataagggagagttttacataggctcaaagtacaagaaagttgtgtatcggcagtatactgatagcacattccgtgttccagtggagagaaaagctgaagaagaacatctgggaattctaggtccacaacttcatgcagatgttggagacaaagtcaaaattatctttaaaaacatggccacaaggccctactcaatacatgcccatggggtacaaacagagagttctacagttactccaacattaccaggtgaaactctcacttacgtatggaaaatcccagaaagatctggagctggaacagaggattctgcttgtattccatgggcttattattcaactgtggatcaagttaaggacctctacagtggattaattggccccctgattgtttgtcgaagaccttacttgaaagtattcaatcccagaaggaagctggaatttgcccttctgtttctagtttttgatgagaatgaatcttggtacttagatgacaacatcaaaacatactctgatcaccccgagaaagtaaacaaagatgatgaggaattcatagaaagcaataaaatgcatgctattaatggaagaatgtttggaaacct'
>>> from string import *
def restrict(dan, enz):
site = find (dan, enz)
while site != -1:
    print "restriction site %s at position %d" % (enz, site)
    site = find (dan, enz, site + 1)
    
>>> restrict(dan, EcoRI)

Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    restrict(dan, EcoRI)
NameError: name 'restrict' is not defined
>>> EcoRI
'gaattc'
>>> EcoRI
'gaattc'
*
>>> (dan, EcoRI)
('ttcacctatgaatggactgtccccaaagaagtaggacccactaatgcagatcctgtgtgtctagctaagatgtattattctgctgtggatcccactaaagatatattcactgggcttattgggccaatgaaaatatgcaagaaaggaagtttacatgcaaatgggagacagaaagatgtagacaaggaattctatttgtttcctacagtatttgatgagaatgagagtttactcctggaagataatattagaatgtttacaactgcacctgatcaggtggataaggaagatgaagactttcaggaatctaataaaatgcactccatgaatggattcatgtatgggaatcagccgggtctcactatgtgcaaaggagattcggtcgtgtggtacttattcagcgccggaaatgaggccgatgtacatggaatatacttttcaggaaacacatatctgtggagaggagaacggagagacacagcaaacctcttccctcaaacaagtcttacgctccacatgtggcctgacacagaggggacttttaatgttgaatgccttacaactgatcattacacaggcggcatgaagcaaaaatatactgtgaaccaatgcaggcggcagtctgaggattccaccttctacctgggagagaggacatactatatcgcagcagtggaggtggaatgggattattccccacaaagggagtgggaaaaggagctgcatcatttacaagagcagaatgtttcaaatgcatttttagataagggagagttttacataggctcaaagtacaagaaagttgtgtatcggcagtatactgatagcacattccgtgttccagtggagagaaaagctgaagaagaacatctgggaattctaggtccacaacttcatgcagatgttggagacaaagtcaaaattatctttaaaaacatggccacaaggccctactcaatacatgcccatggggtacaaacagagagttctacagttactccaacattaccaggtgaaactctcacttacgtatggaaaatcccagaaagatctggagctggaacagaggattctgcttgtattccatgggcttattattcaactgtggatcaagttaaggacctctacagtggattaattggccccctgattgtttgtcgaagaccttacttgaaagtattcaatcccagaaggaagctggaatttgcccttctgtttctagtttttgatgagaatgaatcttggtacttagatgacaacatcaaaacatactctgatcaccccgagaaagtaaacaaagatgatgaggaattcatagaaagcaataaaatgcatgctattaatggaagaatgtttggaaacct', 'gaattc')
>>> restrict(dan, EcoRI):
	
SyntaxError: invalid syntax
>>> restrict(dan, EcoRI)

Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    restrict(dan, EcoRI)
NameError: name 'restrict' is not defined
>>> from string import *
def restrict(dan, 'enz'):
site = find (dan, 'enz')
while site != -1:
    print "restriction site %s at position %d" % ('enz', site)
    site = find (dan, 'enz', site + 1)
    
>>> restrict(dan, EcoRI)

Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    restrict(dan, EcoRI)
NameError: name 'restrict' is not defined
>>> from string import *
>>> def restrict(dan, enz):
site = find (dan, enz)
while site != -1:
    print "restriction site %s at position %d" % (enz, site)
    site = find (dan, enz, site + 1)
    
  File "<pyshell#66>", line 2
    site = find (dan, enz)
       ^
IndentationError: expected an indented block
>>> def restrict(dan, enz):
	site = find (dan, enz)
	while site != -1:
	    print "restriction site %s at position %d" % (enz, site)
	    site = find (dan, enz, site + 1)

>>> restrict(dan, EcoRI)
restriction site gaattc at position 186
restriction site gaattc at position 874
restriction site gaattc at position 1308
>>>  def restrict(dan, enz):
	site = find (dan, enz)
	while site != -1:
	    print "restriction site %s at position %d" % ('enz', site)
	    site = find (dan, enz, site + 1)
	    
  File "<pyshell#71>", line 1
    def restrict(dan, enz):
   ^
IndentationError: unexpected indent
>>>  def restrict(dan, enz):
	site = find (dan, enz)
	while site != -1:
	    print "restriction site %s at position %d" % (enz, site)
	    site = find (dan, enz, site + 1)
	    
  File "<pyshell#72>", line 1
    def restrict(dan, enz):
   ^
IndentationError: unexpected indent
>>> from string import *
>>> def restrict(dan, enz):
	site = find (dan, enz)
	while site != -1:
	    print "restriction site %s at position %d" % (enz, site)
	    site = find (dan, enz, site + 1)

>>> restrict(dan, EcoRI)
restriction site gaattc at position 186
restriction site gaattc at position 874
restriction site gaattc at position 1308
>>>  from string import *
>>> def restrict(dan, enz):
	site = find (dan, enz)
	while site != -1:
	    print "restriction site %s at position %d" % ('enz', site)
	    site = find (dan, enz, site + 1)
	    
  File "<pyshell#77>", line 1
    from string import *
   ^
IndentationError: unexpected indent
>>> from string import *
>>> def restrict(dan, enz):
	site = find (dan, enz)
	while site != -1:
	    print "restriction site %s at position %d" % ('enz', site)
	    site = find (dan, enz, site + 1)

>>> restrict(dan, EcoRI)
restriction site enz at position 186
restriction site enz at position 874
restriction site enz at position 1308
>>> 

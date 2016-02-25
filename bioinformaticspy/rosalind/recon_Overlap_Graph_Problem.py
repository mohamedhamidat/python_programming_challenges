with open('dataset_198_3.txt') as input_data:
    dna = [line.strip() for line in input_data.readlines()]
# Lambda functions to check for overlap and print overlaps in the desired way.
head=dna[0]
#print head[len(head)-1:]
#def seq(dna, head): 
list=[]
for ele in dna[1:]:
#	print ele[len(ele)-1:]
#	if ele[:-1] in head:
	list.append(ele[len(ele)-1:]) 
	seq=''.join(list)
head=head+seq
print head
# Print and save the answer.
#seq(dna, head)
with open('Assignment_04B.txt', 'w') as output_data:
    output_data.write(head)
with open('dataset_198_9.txt') as input_data:
    dna = [line.strip() for line in input_data.readlines()]

# Lambda functions to check for overlap and print overlaps in the desired way.
check_overlap = lambda pair: pair[0][1:] == pair[1][:-1]
print_overlap = lambda pair: ' -> '.join(pair)

# Get all pairs, filter out non-overlapping pairs, print overlapping pairs appropriately.
pairs = ([dna1, dna2] for i, dna1 in enumerate(dna) for j, dna2 in enumerate(dna) if i != j)
overlaps = map(print_overlap, filter(check_overlap, pairs))

# Print and save the answer.
print '\n'.join(overlaps)
with open('Assignment_dataset_198_9.txt', 'w') as output_data:
    output_data.write('\n'.join(overlaps))
    
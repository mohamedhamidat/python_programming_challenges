with open('dataset_197_3.txt') as input_data:
	k = int(input_data.readline().strip())
	text = input_data.readline().strip()

# Generate the list of all k-mers in text and sort them lexiographically.
composition = sorted([text[i:i+k] for i in xrange(len(text)-k+1)])

# Print and save the answer.
print '\n'. join(composition)
with open('Assignment_04A.txt', 'w') as output_data:
	output_data.write('\n'. join(composition))
	
	
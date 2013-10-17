import sys

file = sys.argv[1]

with open(file) as data:
	# first line of input defines number of items to return
	num_lines = int(data.readline().strip())
	
	# get list of all the words
	words = []
	for line in data.readlines():
		word = line.strip()

		if len(word):
			words.append( (len(word), word) )

	# sort time! ascending to descending
	words.sort()

	# get top X
	words = words[:num_lines:-1]

	# output  (cleaner ways, but more memory)
	print("\n".join(item[1] for item in words))

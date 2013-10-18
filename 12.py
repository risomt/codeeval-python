"""
Challenge Description:

	Write a program to find the first non repeated character in a string.

Input sample:

	The first argument will be a text file containing strings. e.g.

	yellow
	tooth

Output sample:

	Print to stdout, the first non repeating character, one per line.
	e.g.

	y
	h
 
Notes::
* I overshot the implementation!  I made it tally each instance of a character in a string and then make it 
output the character that was the earliest in the list with lowest count.  The problem doesn't require that
but it works out.
* this is not very pythonic! 
* note that the input file tied to this has an extra item (tttbbbee) to check a final case
"""

from sys import argv

with open(argv[1]) as data:
	for line in data.readlines():
		string = list(line.strip())

		# the characters in the string and their occurances [char, # of occurances]
		chars = []

		# loop through all items, keep them in order, and count occurences of char
		# we can't do this in a dictionary outright because it does not maintain order so use lists
		for char in string:
			found = False

			# check for it in chars, if it's there increment the count
			for item in range(0, len(chars)):
				if len(chars[item]) and char == chars[item][0]:
					chars[item][1] += 1
					found = True

			# if it's not in chars add it as a new item (in order)
			if not found:
				chars.append([char, 1])

		# variable to track lowest count and a pointer to it's index in chars
		lowest = chars[0][1]
		lowest_index = 0

		# find the index of the earliest character in the list with the lowest count
		for item in range(0, len(chars)):
			if chars[item][1] < lowest:
				lowest = chars[item][1]
				lowest_index = item

		print chars[lowest_index][0]
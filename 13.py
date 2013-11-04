"""
Challenge Description:

	Write a program to remove specific characters from a string.

Input sample:

	The first argument will be a text file containing an input string followed by a comma and then the characters that need to be scrubbed. e.g.

	how are you, abc
	hello world, def

Output sample:

	Print to stdout, the scrubbed strings, one per line. Trim out any leading/trailing whitespaces if they occur.
	e.g.

	how re you
	hllo worl
"""

# solution 1 - seemed like cheating
"""
from sys import argv

with open(argv[1]) as data:
	for line in data.readlines():
		string, scrub = line.strip().split(', ')
		
		for scrub_char in scrub:
			string = string.replace(scrub_char, '')

		print string
"""

from sys import argv

with open(argv[1]) as data:
	for line in data.readlines():
		string, scrub = line.strip().split(', ')
		string = list(string)

		for scrub_char in scrub:
			for x_char in range(0, len(string)):
				if scrub_char == string[x_char]:
					string.pop(x_char)

		print string

# loop through each character to remove
# loop through each character in list
# if character to remove = character in list
# remove character from list
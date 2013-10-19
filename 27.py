"""
Challenge Description:

	Given a decimal (base 10) number, print out its binary representation.

Input sample:

	File containing positive whole decimal numbers, one per line. e.g.

	2
	10
	67

Output sample:

	Print the decimal representation, one per line.
	e.g.

	10
	1010
	1000011
"""

# if we're allowed to use functions: print(bin(int(line.strip()))[2:])

from sys import argv		

with open(argv[1]) as data:
	for line in data.readlines():
	
		# parse out the number to generate in binary
		original= int(line.strip())
		number = original
		binary = []

		while True:
			if number == 0:
				# hack
				binary[-1] = original % 2
				break
			else:
				remainder = number / 2
				number = number / 2

				binary.append(remainder % 2)

		print "".join(map(str, binary))
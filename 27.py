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
# algorithm derived from http://www.wikihow.com/Convert-from-Decimal-to-Binary #2

from sys import argv		

with open(argv[1]) as data:
	for line in data.readlines():
	
		# parse out the number to generate in binary
		original = int(line.strip())
		number = original
		binary = []

		while True:
			# if we hit 0 we're done!
			if number == 0:
				# hack - the (last) 2^0 is not coming out correctly
				# this makes the 2^0 position 1 if the original is odd
				binary[-1] = original % 2
				break
			else:
				# divide by base (2) to get new number and continue on
				number = number / 2

				# determine whether to add a 1 or 0
				binary.append(number % 2)

		print "".join(map(str, binary))
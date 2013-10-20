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
		number = int(line.strip())
		binary = []

		# explanation: http://www.wikihow.com/Convert-from-Decimal-to-Binary #2
		# the remainder (mod) of the current number and the base (2) represents the
		# opposite value in binary (hence the reverse at the end)
		while True:
			if number == 0:
				break
			else:
				# determine binary representation of current number
				binary.append(number % 2)

				# divide number by half and continue until we reach 0
				number = number / 2

		# reverse to complete and turn it into a string
		binary.reverse()
		print("".join(map(str, binary)))
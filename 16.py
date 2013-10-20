"""
Challenge Description:

	Write a program to determine the number of 1 bits in the internal representation of a given integer.

Input sample:

	The first argument will be a text file containing an integer, one per line. e.g.

	10
	22
	56

Output sample:

	Print to stdout, the number of ones in the binary form of each number.
	e.g.

	2
	3
	3
"""

from sys import argv

with open(argv[1]) as data:
	for line in data.readlines():
		# it seems like cheating to use bin() function so this is the hard way
	
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

		# reverse to complete algorithm
		#binary.reverse()
		# we can skip this because order of bits doesn't change result

		# count number of 1s
		# we could use list.count(1) here

		count = 0

		for bit in binary:
			if bit == 1:
				count += 1

		print count
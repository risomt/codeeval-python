"""
Challenge Description:

	Write a program to determine the largest sum of contiguous integers in a list.

Input sample:

	The first argument will be a text file containing a comma separated list of integers, one per line. e.g.

	-10, 2, 3, -2, 0, 5, -15
	2,3,-2,-1,10

Output sample:

	Print to stdout, the largest sum. In other words, of all the possible contiguous subarrays for a given array, find the one with the largest sum, and print that sum.
	e.g.

	8
	12
"""

from sys import argv

with open(argv[1]) as data:
	for line in data.readlines():
		# turn into list of integers
		list = map(int, line.strip().split(','))

		# create variable to track largest sum
		largest = 0

		# loop through each element of the list and sum every combination of integers to find the highest
		for index in range(0, len(list)):
			# create temp list of everything from the current index onwards (move list pointer forwards)
			reverse = list[index:]

			# look through temp list backwards, summing each version as we go
			for reverse_index in range(len(reverse)-index, 0, -1):
				new_value = sum(reverse[:reverse_index])

				if new_value > largest:
					largest = new_value

		print(largest)

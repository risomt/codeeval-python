"""
Challenge Description:

	You are given two strings 'A' and 'B'. Print out a 1 if string 'B' occurs at the end of string 'A'. Else a zero.

Input sample:

	The first argument is a file, containing two strings, comma delimited, one per line. Ignore all empty lines in the input file.e.g.

	Hello World,World
	Hello CodeEval,CodeEval
	San Francisco,San Jose

Output sample:

	Print out 1 if the second string occurs at the end of the first string. Else zero. Do NOT print out empty lines between your output.
	e.g.

	1
	1
	0
"""

from sys import argv

with open(argv[1]) as data:
	for line in data.readlines():
		# get both strings
		string1, string2 = line.strip().split(',')
		
		# get # of chars from string 2, slice string 1 from right to <index> and compare to string 2
		if string1[-len(string2):] == string2:
			print(1)
		else:
			print(0)
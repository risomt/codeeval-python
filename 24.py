"""
Challenge Description:

        Print out the sum of integers read from a file.

Input sample:

        The first argument to the program will be a text file containing a positive integer, one per line. E.g.

        5
        12

Output sample:

        Print out the sum of all the integers read from the file. E.g.

        17
"""

from sys import argv

with open(argv[1]) as data:
        print sum(map(int, list(line.strip() for line in data.readlines())))

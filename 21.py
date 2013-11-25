"""
Challenge Description:

        Given a positive integer, find the sum of its constituent digits.

Input sample:

        The first argument will be a text file containing positive integers, one per line. E.g.

        23
        496

Output sample:

        Print to stdout, the sum of the numbers that make up the integer, one per line. E.g.

        5
        19
"""

from sys import argv

with open(argv[1]) as data:
        for line in data.readlines():
                print sum(int(digit) for digit in line.strip())

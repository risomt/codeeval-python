"""
Challenge Description:

        Given numbers x and n, where n is a power of 2, print out the smallest
        multiple of n which is greater than or equal to x. Do not use division or modulo operator.

Input sample:

        The first argument will be a text file containing a comma separated
        list of two integers, one list per line. E.g.

        13,8
        17,16

Output sample:

        Print to stdout, the smallest multiple of n which is greater than or equal to x, one per line. E.g.

        16
        32
"""

from sys import argv

with open(argv[1]) as data:
        for line in data.readlines():
                x, n = map(int, line.split(','))

                while n < x:
                        n = n * 2

                print n

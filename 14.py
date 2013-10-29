"""
Challenge Description:

        Write a program to print out all the permutations of a string in alphabetical order.

Input sample:

        The first argument will be a text file containing an input string, one per line. e.g.

        hat

Output sample:

        Print to stdout, permutations of the string, comma separated, in alphabetical order.
        e.g.

        aht,ath,hat,hta,tah,tha
"""

# because python is awesome, but it's cheating:
# from itertools import permutations
# permutations(a) # generator

from sys import argv

def permutations(elements):
        if len(elements) <=1:
                yield elements
        else:
                for permute in permutations(elements[1:]):
                        for i in range(len(elements)):
                                yield permute[:i] + elements[0:1] + permute[i:]


with open(argv[1]) as data:
        for line in data.readlines():

               characters = [x for x in line.strip()]
               print ",".join(str("".join(x)) for x in permutations(characters))
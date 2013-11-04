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

# suggestion from http://stackoverflow.com/questions/104420/how-to-generate-all-permutations-of-a-list-in-python/104436#104436
# much nicer than my versions!
def permutations(elements):
        if len(elements) <=1:
                yield elements
        else:
                # for each set of characters in [hat] - [at] - [t] (recursive call)
                for permutation in permutations(elements[1:]):
                        # create all possible combinations with given set and return
                        for i in range(len(elements)):
                                # yield (return generator) each possible permutation to parent
                                yield permutation[:i] + elements[0:1] + permutation[i:]


with open(argv[1]) as data:
        for line in data.readlines():

                # print out a list of all unique permutations for each string in the file 
                # permutations() returns a list of lists of the permutations, hence the
                # double join to convert each item in the list, then the list itself into CSV
                # test expects answer to be alphabetically sorted.. and one linered it
                print ",".join(sorted([str("".join(x)) for x in permutations([x for x in line.strip()])]))
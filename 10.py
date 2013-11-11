"""
Challenge Description:

        Write a program to determine the Mth to last element of a list. 

Input sample:

        The first argument will be a text file containing a series of space delimited characters followed by an integer representing a index into the list (1 based), one per line. E.g. 

        a b c d 4
        e f g h 2

Output sample:

        Print to stdout, the Mth element from the end of the list, one per line. If the index is larger than the list size, ignore that input. E.g.

        a
        g

Notes:
        The example output is a lie and misleading! There should be no output for the first example :(
"""

from sys import argv

# note - first example is a trick.  python indices start at 0, so 4 is technically element #5 which DNE
with open(argv[1]) as data:
        for line in data:
                characters = line.strip().split()

                # get the position of our special Mth character and remove that from list
                mth_element = int(characters[-1])
                characters = characters[:-1]

                # if our mth is bigger than list skip the input (line)
                # else print mth element from the end!
                if mth_element <= len(characters):
                        print characters[-mth_element]

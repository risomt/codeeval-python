"""
Challenge Description:

        Given a sequence, write a program to detect cycles within it.

Input sample:

        A file containing a sequence of numbers (space delimited). The file
        can have multiple such lines. e.g

        2 0 6 3 1 6 3 1 6 3 1

        Ensure to account for numbers that have more than one digit eg. 12.
        If there is no sequence, ignore that line.

Output sample:

        Print to stdout the first sequence you find in each line. Ensure
        that there are no trailing empty spaces on each line you print. e.g.

        6 3 1
"""

from sys import argv

with open(argv[1]) as data:
        for line in data.readlines():
                sequence = line.strip().split(' ')
                sequences = []

                # loop through each number in the sequence
                for index, key in enumerate(sequence):

                        # loop through all forward values
                        for indexb in range(index+1, len(sequence)):
                                keyb = sequence[indexb]

                                # if the number we're checking exists anywhere else in the
                                # sequence, check to see if it's a sequence
                                if key == keyb:

                                        # check to see if the sequence matches by comparing the subset
                                        # of the value to it's duplcate value - if the two sublists are exactly
                                        # equal we have a sequence!
                                        for x in range(indexb, index, -1):
                                                if len(sequence) - indexb >= x:
                                                        if sequence[index:x] == sequence[indexb:indexb + (x - index)]:
                                                                sequences.append(sequence[indexb:indexb + (indexb - index)])

                print sequences

                # if there are any sequences print the first one
                if len(sequences):
                        print " ".join(sequences[0])

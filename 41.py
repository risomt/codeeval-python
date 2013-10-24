"""
Challenge Description:

        Imagine we have an immutable array of size N which we know to be filled with integers ranging from 0 to N-2, 
        inclusive. Suppose we know that the array contains exactly one duplicated entry and that duplicate appears 
        exactly twice. Find the duplicated entry. (For bonus points, ensure your solution has constant space and time
        proportional to N)

Input sample:

        Your program should accept as its first argument a path to a filename. Each line in this file is one test case.
        Ignore all empty lines. Each line begins with a positive integer(N) i.e. the size of the array, then a semicolon
        followed by a comma separated list of positive numbers ranging from 0 to N-2, inclusive. i.e eg.

        5;0,1,2,3,0
        20;0,1,10,3,2,4,5,7,6,8,11,9,15,12,13,4,16,18,17,14

Output sample:

        Print out the duplicated entry, each one on a new line eg

        0
        4
"""

# this is http://www.geeksforgeeks.org/find-the-two-repeating-elements-in-a-given-array/
# used a neat little break nested hack below - http://stackoverflow.com/questions/653509/breaking-out-of-nested-loops

from sys import argv

with open(argv[1]) as data:
        for line in data.readlines():
                # skip blank lines
                line = line.strip()

                if len(line):
                        # clean up input
                        size, values = line.split(';')
                        size = int(size)
                        values = map(int, values.split(','))

                        # pythonic approach - use collections to pull most common value and get the key of that
                        # from collections import Counter
                        # print Counter(values).most_common(1)[0][0]

                        # loop through each value of the list and check for dupes
                        for x in range(0, size):
                                # grab value to see if there's a duplicate of it
                                target = values[x]

                                # loop through all items in the list except the one we just grabbed
                                # if we find the value break out of the loops
                                for value in list(values[:x] + values[x+1:]):
                                        if value == target:
                                                print target
                                                break
                                else:
                                        continue
                                break
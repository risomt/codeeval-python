"""
Challenge Description:

        Write a program which finds the next-to-last word in a string.

Input sample:

        Your program should accept as its first argument a path to a
        filename. Input example is the following

        some line with text
        another line

        Each line has more than one word.

Output sample:

        Print the next-to-last word in the following way.

        with
        another
"""

from sys import argv

with open(argv[1]) as data:
        for line in data.readlines():
                #split words apart by space and then output second to last
                words = line.strip().split()
                print words[-2]

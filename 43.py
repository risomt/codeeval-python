"""
Challenge Description:

        Credits: Programming Challenges by Steven S. Skiena and Miguel A. Revilla

        A sequence of n > 0 integers is called a jolly jumper if the absolute values of the differences between successive elements take on all possible values 1
        through n - 1. eg.

        1 4 2 3 

        is a jolly jumper, because the absolute differences are 3, 2, and 1, respectively. The definition implies that any sequence of a single integer is a jolly
         jumper. Write a program to determine whether each of a number of sequences is a jolly jumper.

Input sample:

        Your program should accept as its first argument a path to a filename. Each line in this file is one test case. Each test case will contain an integer n <
         3000 followed by n integers representing the sequence. The integers are space delimited.

Output sample:

        For each line of input generate a line of output saying 'Jolly' or 'Not jolly'. 
"""

from sys import argv

with open(argv[1]) as data:
        for line in data.readlines():
                # clean up and get values
                values = map(int, line.strip().split())

                # get all jumpers - subtract each value from the previous and get absolute value of that, then sort it for comparison later
                jumpers = sorted(abs(values[x] - values[x-1]) for x in xrange(1, len(values)))

                # determine whether or not the jumper values are equivalent to n - 1 - sort them to sync up
                if jumpers[:-1] ==  range(1, len(values)-1):
                        print 'Jolly'
                else:
                        print 'Not jolly'
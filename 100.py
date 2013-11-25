"""
Challenge Description:

        Write a program which checks input numbers and
        determines whether a number is even or not.

Input sample:

        Your program should accept as its first argument a
         path to a filename. Input example is the following

        701
        4123
        2936

Output sample:

        Print 1 if the number is even or 0 if the number is odd.

        0
        0
        1
"""

from sys import argv

with open(argv[1]) as data:
        for line in data.readlines():
                number = int(line.strip())

                if number % 2 == 1:
                        print 0
                else:
                        print 1

# not workng properly
# with open(argv[1]) as data:
#         print "\n".join(str(int(line.strip()) % 2) for line in data.readlines())

#!/usr/bin/python
"""
Challenge Description:

        Credits: Programming Challenges by Steven S. Skiena and Miguel A. Revilla

        The problem is as follows: choose a number, reverse its digits and add it to the original. If the sum is not a palindrome (which means, it is not the same number from left to right and right to left), repeat this procedure. E.g.

        195 (initial number) + 591 (reverse of initial number) = 786

        786 + 687 = 1473

        1473 + 3741 = 5214

        5214 + 4125 = 9339 (palindrome)

        In this particular case the palindrome 9339 appeared after the 4th addition. This method leads to palindromes in a few step for almost all of the integers. But there are interesting exceptions. 196 is the first number for which no palindrome has been found. It is not proven though, that there is no such a palindrome.
        
Input sample:

        Your program should accept as its first argument a path to a filename. Each line in this file is one test case. Each test case will contain an integer n < 10,000. Assume each test case will always have an answer and that it is computable with less than 100 iterations (additions).

Output sample:

        For each line of input, generate a line of output which is the number of iterations (additions) to compute the palindrome and the resulting palindrome. (they should be on one line and separated by a single space character). E.g.

        4 9339
"""

# function to identify if an integer is a palindrome
# this was my version - but there's an easier way
# def is_palindrome(integer):
#         string = str(integer)
#         length = len(string)

#         if length % 2 == 1:
#                 # if it's an odd length - skip the mid point
#                 return string[0:length / 2] == string[(length / 2)+1:length][::-1]
#         else:
#                 return string[0:length / 2] == string[length / 2:length][::-1]

# function to identify if an integer is a palindrome
# much simpler version, more pythonic version: http://stackoverflow.com/a/17331328
def is_palindrome(integer):
        return str(integer) == str(integer)[::-1]

# little function to return the reverse of an integer - probably pretty inefficient
# apparently i'm not the first to come up with this exact function! http://pythonadventures.wordpress.com/2010/09/29/reverse-integer/
def reverse_int(integer):
        return int(str(integer)[::-1])

from sys import argv

with open(argv[1]) as data:
        for line in data.readlines():
                number = int(line.strip())

                # keep running the algorithm until it produces a palindrome
                # warning - very big potential for infinite loop, I think
                counter = 0
                while is_palindrome(number) == False:
                        number = number + reverse_int(number)
                        counter += 1

                print counter, number
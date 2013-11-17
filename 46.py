"""
Challenge Description:

        Print out the prime numbers less than a given number N. For bonus points your solution should run in N*(log(N)) time or better. You may assume that N is always a positive integer.

Input sample:

        Your program should accept as its first argument a path to a filename. Each line in this file is one test case. Each test case will contain an integer n < 4,294,967,295. E.g.

        10
        20
        100

Output sample:

        For each line of input, print out the prime numbers less than N, in ascending order, comma delimited. (There should not be any spaces between the comma and numbers) E.g.

        2,3,5,7
        2,3,5,7,11,13,17,19
        2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97
"""

# taken from one of the earlier tests
def isprime(number):
        "Return true if given integer is a prime number"
        if all(number % i != 0 for i in range(number - 1, 1, -1)):
                return True

from sys import argv

with open(argv[1]) as data:
        for line in data.readlines():
                number = int(line.strip())

                # loop through all values from 2 to number 
                # why 2? 0 and 1 are not prime numbers (also - see output examples)
                primes = []
                for x in range(2, number):
                        if isprime(x):
                                primes.append(x)

                # print out comma delimited list of values
                print ",".join(map(str, primes))

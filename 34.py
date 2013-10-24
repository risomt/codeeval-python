"""
Challenge Description:

    You are given a sorted array of positive integers and a number 'X'. Print out all pairs of numbers whose sum is
     equal to X. Print out only unique pairs and the pairs should be in ascending order

Input sample:

    Your program should accept as its first argument a filename. This file will contain a comma separated list of 
    sorted numbers and then the sum 'X', separated by semicolon. Ignore all empty lines. If no pair exists, print
     the string NULL eg.

    1,2,3,4,6;5
    2,4,5,6,9,11,15;20
    1,2,3,4;50

Output sample:

    Print out the pairs of numbers that equal to the sum X. The pairs should themselves be printed in sorted order
     i.e the first number of each pair should be in ascending order .e.g.

    1,4;2,3
    5,15;9,11
    NULL
"""

from sys import argv

with open(argv[1]) as data:
        for line in data.readlines():

                # get list of numbers and sum to target
                numbers, target_sum = line.strip().split(';')
                numbers = map(int, numbers.split(','))
                target_sum = int(target_sum)

                pairs = []

                # this would be a lot prettier with a permutation
                for x_num in range(0, len(numbers)):
                        num = numbers[x_num]

                        for num2 in numbers[:x_num] + numbers[x_num+1:]:
                                if num + num2 == target_sum and [num, num2] not in pairs and [num2, num] not in pairs:
                                        pairs.append([num, num2])
                                        #pairs.append("%s,%s" % (num, num2))

                # if none of the pairs meet the target print NULL, else print pairs
                if not len(pairs):
                        print 'NULL'
                else:
                        print ";".join("%s,%s" % (x[0], x[1]) for x in pairs)


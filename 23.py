"""
Challenge Description:

        Print out the grade school multiplication table upto 12*12.

Input sample:

        There is no input for this program.

Output sample:

        Print out the table in a matrix like fashion, each number formatted
        to a width of 4 (The numbers are right-aligned and strip out
        leading/trailing spaces on each line). The first 3 line will look like:

        1   2   3   4   5   6   7   8   9  10  11  12
        2   4   6   8  10  12  14  16  18  20  22  24
        3   6   9  12  15  18  21  24  27  30  33  36
"""

matrix = []

# multiply row number (x) by column number (y) and add to matrix
for row in xrange(1, 13):
        temp = []

        for column in xrange(1, 13):
                temp.append(row * column)

        matrix.append(temp)

for row in matrix:
        print "".join("{:>4}".format(number) for number in row)

# TO DO - fix formatting

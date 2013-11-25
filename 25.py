"""
Challenge Description:

        Print the odd numbers from 1 to 99.

Input sample:

        There is no input for this program.

Output sample:

        Print the odd numbers from 1 to 99, one number per line.
"""

print "\n".join(str(number) for number in range(1, 100) if number % 2 == 1)

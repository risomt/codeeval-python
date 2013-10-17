"""
Challenge Description:

	Write a program to determine the biggest prime palindrome under 1000.

Input sample:

	There is no input for this program.

Output sample:

	Your program should print the largest palindrome on stdout, i.e.

	929
"""

def isprime(number):
	"Return true if given integer is a prime number"
	if all(number % i != 0 for i in range(number - 1, 1, -1)):
		return True

# print out the largest integer palindrome between 1000 and 0
# start backwards to reduce total lookup cost
for number in range(999,0, -1):

	# make sure it's a palindrome first to reduce total lookup cost
	if str(number) == str(number)[::-1]:
		if isprime(number) == True:
			print(number)
			break
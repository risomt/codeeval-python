"""
Challenge Description:

	Write a program to determine the sum of the first 1000 prime numbers.

Input sample:

	There is no input for this program.

Output sample:

	Your program should print the sum on stdout, i.e.

	3682913
"""

def isprime(number):
	"Return true if given integer is a prime number"
	if all(number % i != 0 for i in range(number - 1, 1, -1)):
		return True

"""
sum_primes = 0
num_primes = 0
last_number = 0# does this need to be 2?

# sum all prime numbers to 1000
while num_primes <= 1000:
	last_number += 1

	if isprime(last_number) == True:
		sum_primes += last_number
		num_primes += 1

print(sum_primes)
"""

primes = []
last_number = 1

while len(primes) <= 1000:
	last_number += 1

	if isprime(last_number) == True:
		primes.append(last_number)

print(primes)
print(sum(primes))

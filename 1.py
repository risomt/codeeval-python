import sys

file = sys.argv[1]

with open(file) as data:
	for line in data.readlines():
		# get fizz and buzz quotients, max value for range
		fizz, buzz, end = [int(x) for x in line.strip().split(' ')]

		# create a list of values
		output = []
		for num in range(1, end + 1):
			temp = ""

			if num % fizz == 0:
				temp = "F"
			if num % buzz == 0:
				temp += "B"
			if not len(temp):
				temp = str(num)
			
			output.append(temp)

		# output list
		print(" ".join(x for x in output))

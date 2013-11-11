"""
Challenge Description:

        Write a program to remove specific characters from a string.

Input sample:

        The first argument will be a text file containing an input string followed by a comma and then the characters that need to be scrubbed. e.g.

        how are you, abc
        hello world, def

Output sample:

        Print to stdout, the scrubbed strings, one per line. Trim out any leading/trailing whitespaces if they occur.
        e.g.

        how re you
        hllo worl
"""

# solution 1 - seemed like cheating
# from sys import argv

# with open(argv[1]) as data:
#         for line in data.readlines():
#                 string, scrub = line.strip().split(', ')
                
#                 for scrub_char in scrub:
#                         string = string.replace(scrub_char, '')

#                 print string

from sys import argv

# solution #2 - the "less python" way
with open(argv[1]) as data:
        for line in data.readlines():
                # grab string to strip and characters to strip out
                string, scrub = line.strip().split(', ')
                # string = list(string) # if we want to do it the list way

                # loop through each character to remove 
                for scrub_char in scrub:
                        index = 0

                        # loop through each element of the string (as a list) and pop the value
                        # if it's one of the character we're trying to replace
                        # this is a while loop to make it easy to remove chars from the string
                        while index <= len(string) - 1:
                                if scrub_char == string[index]:
                                        # if characters are equal pop it - which automatically moves to next character in string
                                        #string.pop(index) # slightly easier but avoiding builtins
                                        string = string[:index] + string[index+1:]
                                else:
                                        # else go to next character
                                        index += 1

                # print string
                print "".join(string)
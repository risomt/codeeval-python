"""
https://www.codeeval.com/open_challenges/9/

Challenge Description:

        Write a program implementing a stack inteface for integers.The interface should have 'push' and 'pop' functions. You will 
        be asked to 'push' a series of integers and then 'pop' and print out every alternate integer.

Input sample:

        The first argument will be a text file containing a series of space delimited integers, one per line. e.g.

        1 2 3 4
        10 -2 3 4

Output sample:

        Print to stdout, every alternate integer(space delimited), one per line.
        e.g.

        4 2
        4 -2
"""

# note - avoided builtins in the actual stack implementation

class Stack:
        """Class to operate a stack"""

        # the stack
        __data = []

        # store the length - more efficient than always running len(<list>)
        __len = 0

        def __init__(self):
                self.__data, self.__len = [], 0

        # push a new integer onto the stack
        def push(self, element):
                if type(element) == int:
                        self.__data.insert(self.__len, element)
                        self.__len += 1

        # pop an item off the stack, return special None if there are no more
        def pop(self):
                if self.__len > 0:
                        # grab top element
                        out = self.__data[self.__len-1]

                        # remove top element from stack
                        self.__data = self.__data[:-1]

                        # decrement the length and return top value
                        self.__len -= 1
                        return out
                else:
                        return None

from sys import argv

with open(argv[1]) as data:
        for line in data.readlines():
                stack = Stack()

                # fill it with the given input, e.g.: "1 2 3 4\n"
                for element in map(int, line.strip().split()):
                        stack.push(element)

                # pop everything off and shove into temporary list
                # note - because it's a stack the order will be reversed from what we put in
                output = []
                while True:
                        temp = stack.pop()
                        if temp:
                                output.append(temp)
                        else:
                                break

                # print out every other value 
                print " ".join(str(output[x]) for x in range(0, len(output), 2))
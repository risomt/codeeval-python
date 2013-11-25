"""
Challenge Description:

        Write a program which swaps letters' case in a sentence. All non-letter characters should remain the same.

Input sample:

        Your program should accept as its first argument a path to a filename. Input example is the following

        Hello world!
        JavaScript language 1.8
        A letter

Output sample:

        Print results in the following way.

        hELLO WORLD!
        jAVAsCRIPT LANGUAGE 1.8
        a LETTER
"""

from sys import argv
from string import uppercase

with open(argv[1]) as data:
        for line in data.readlines():

                sentence = []
                for char in line.strip():
                        if char in uppercase:
                                sentence.append(char.lower())
                        else:
                                sentence.append(char.upper())

                print "".join(sentence)

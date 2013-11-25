"""
Challenge Description:

        Write a program which capitalizes words in a sentence.

Input sample:

        Your program should accept as its first argument a path
        to a filename. Input example is the following

        Hello world
        javaScript language
        a letter

Output sample:

        Print capitalized words in the following way.

        Hello World
        JavaScript Language
        A Letter
"""

from sys import argv

with open(argv[1]) as data:
        for line in data.readlines():
                print " ".join(word[0].upper() + word[1:] for word in line.strip().split())

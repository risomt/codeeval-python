#!/usr/bin/env python
"""
Challenge Description:

        The sentence 'A quick brown fox jumps over the lazy dog' contains every single letter in the alphabet. Such sentences are called pangrams. You are to 
        write a program, which takes a sentence, and returns all the letters it is missing (which prevent it from being a pangram). You should ignore the case of 
        the letters in sentence, and your return should be all lower case letters, in alphabetical order. You should also ignore all non US-ASCII characters.In case 
        the input sentence is already a pangram, print out the string NULL

Input sample:

        Your program should accept as its first argument a filename. This file will contain several text strings, one per line. Ignore all empty lines. eg.

        A quick brown fox jumps over the lazy dog
        A slow yellow fox crawls under the proactive dog

Output sample:

        Print out all the letters each string is missing in lowercase, alphabetical order .e.g.

        NULL
        bjkmqz
"""

from sys import argv
from string import lowercase

with open(argv[1]) as data:

        all_characters = list(lowercase)

        for line in data.readlines():
                # process input and get list of unique characters
                input_characters = set(line.strip().lower().replace(' ', ''))

                missing = []

                # go through each valid character and check to see if it does not exist in list of input characters
                for character in all_characters:
                        if character not in input_characters:
                                missing.append(character)

                # process output
                if len(missing):
                        print ''.join(missing)
                else:
                        print 'NULL'

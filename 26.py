"""
Challenge Description:

        Print the size of a file in bytes.

Input:

        The first argument to your program has the path to the file you need
         to check the size of.

Output sample:

        Print the size of the file in bytes. e.g.

        55
"""

from sys import argv
from os import stat

print stat(argv[1]).st_size

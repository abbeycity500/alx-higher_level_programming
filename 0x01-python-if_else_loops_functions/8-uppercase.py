#!/usr/bin/python3
#8-uppercase.py

def uppercase(str):
    """Print a string in uppercase."""
    for s in str:
        if ord(s) in range(97, 123):
            i = ord(s) - 32
        else:
            i = ord(s)
        print("{:c}".format(i), end='')
        print("")

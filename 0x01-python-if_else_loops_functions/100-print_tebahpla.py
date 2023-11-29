#!/usr/bin/python3
#100-print_tebahpla.py

"""Print the alphabet in reverse order alternating upper- and lower-case."""
for i in range(122, 97, -2):
    print("{:c}{:c}".format(i, i-33), end="")

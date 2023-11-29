#!/usr/bin/python3
#6-print_comb3.py

"""Print all possible different combination of two digits in ascending order.

    The two digits must be different - 01 and 10 are considered identical.
    """
for i in range(0, 90):
    for j in range(i + 1, 10):
        if i != 8:
            print("{:d}{:d}".format(i, j), end=', ')
        else:
            print("{:d}{:d}".format(i, j))

#!/usr/bin/python3
#9-print_last_digit.py

def print_last_digit(number):
    """A function that prints the last digit of a number and return it."""
    lastdigit = abs(number) % 10
    print(lastdigit, end="")
    return lastdigit

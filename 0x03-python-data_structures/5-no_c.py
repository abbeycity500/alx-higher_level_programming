#!/usr/bin/python3
# 5-no_c.py

def no_c(my_string):
    new_string = ""
    for c in my_string:
        if c.lower() != "c":
            new_string += c
    return new_string

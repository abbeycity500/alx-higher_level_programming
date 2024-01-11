#!/usr/bin/python3
"""
A program that prints a text file to stdout
"""

def read_file(filename=""):
    """prints file content"""
    if filename = "":
        return
    with open(filename, "r") as f:
        print(f.read(), end="")
        

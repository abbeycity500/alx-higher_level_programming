#!/usr/bin/python3
#12-fizzbuzz.py

def fizzbuzz():
    """Print the numbers from 1 to 100 separated by a space.
    
    For multples of three, print Fizz instead of the number.
    For multipes of five, print Buzz instead of the number.
    For multiples of both three and five, print FizzBuzz instead of the number
    """
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")

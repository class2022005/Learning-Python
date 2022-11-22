#!/usr/bin/env python3

# Modify code below and implement guess_number so that it repeatedly asks the user for a number between 0 and 100, inclusive.
# If the user correctly guesses the value of the given argument n, print 'WIN' and return. 
# Otherwise, indicate whether the guess was too high or too low.

def guess_number(n):
    while True:
        guess = int(input("Give me a numbah!!! (0-100)"))
        if guess == n:
            print("WIN")
            break
        elif guess > n:
            print("too high")
        elif guess < n:
            print("too low")
guess_number(23)
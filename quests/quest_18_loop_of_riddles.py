#!/usr/bin/env python3

secret_number = 7

guess = int(input("Guess the secret number: "))

while guess != secret_number:
    print("Wrong guess, try again!")
    guess = int(input("Guess again: "))

print("Correct! You guessed it!")

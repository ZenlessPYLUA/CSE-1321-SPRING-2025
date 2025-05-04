# Class: CSE 1321L
# Section: W04
# Term: Spring 2025
# Instructor: Nalamati
# Name: Zenzele Broomfield
# Lab: 06

import random

def guess_the_number():
    random_number = random.randint(1, 100)
    print("Guess the number I am thinking!")

    while True:
        guess = int(input("Enter any number between 1 and 100: "))

        if guess < random_number:
            print("Too low!")
        elif guess > random_number:
            print("Too high!")
        else:
            print(f"Correct! I was thinking of {random_number}")
            break


if __name__ == "__main__":
    guess_the_number()

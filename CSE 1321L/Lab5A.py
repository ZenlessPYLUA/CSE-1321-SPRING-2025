# Class: CSE 1321L
# Section: W04
# Term: Spring 2025
# Instructor: Nalamati
# Name: Zenzele Broomfield
# Lab: 05

print("Please enter 10 numbers and this program will display the largest.")

largest = 0

for i in range(1, 11):
    number = int(input(f"Please enter number {i}: "))

    if number > largest:
        largest = number

print(f"The largest number was {largest}")

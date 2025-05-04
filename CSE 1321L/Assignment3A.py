# Class: CSE 1321L
# Section: W04
# Term: Spring 2025
# Instructor: Nalamati
# Name: Zenzele Broomfield
# Assignment: 03

size = int(input("Enter an odd number for the size of the diamond: "))

if size % 2 == 0:
    size += 1
    print(f"Size must be an odd number; we will increase it to {size}")

mid = size // 2
num = 0

for i in range(mid + 1):
    spaces = mid - i
    print(" " * spaces, end="")

    for j in range(2 * i + 1):
        print(num % 10, end="")
        num += 1

    print()

for i in range(mid - 1, -1, -1):
    spaces = mid - i
    print(" " * spaces, end="")

    for j in range(2 * i + 1):
        print(num % 10, end="")
        num += 1

    print()

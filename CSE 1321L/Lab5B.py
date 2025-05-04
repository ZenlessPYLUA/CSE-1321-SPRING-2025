# Class: CSE 1321L
# Section: W04
# Term: Spring 2025
# Instructor: Nalamati
# Name: Zenzele Broomfield
# Lab: 05

size = int(input("Please enter a value for the size: "))

# Print the box
print(f"This is the requested {size}x{size} box:")
for i in range(size):
    for j in range(size):
        print("*", end="")
    print()

print(f"This is the requested right-facing {size}x{size} right-triangle:")
for i in range(1, size + 1):
    for j in range(i):
        print("*", end="")
    print()

print(f"This is the requested left-facing {size}x{size} right-triangle:")
for i in range(1, size + 1):
    for j in range(size - i):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()

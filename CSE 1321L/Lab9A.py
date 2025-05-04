# Class: CSE 1321L
# Section: W04
# Term: Spring 2025
# Instructor: Nalamati
# Name: Zenzele Broomfield
# Lab: 09


def allMath(num1, num2):
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = num1 / num2 if num2 != 0 else None
    floor_division = num1 // num2 if num2 != 0 else None
    modulus = num1 % num2 if num2 != 0 else None
    power = num1 ** num2

    def format_number(n):
        if n is None:
            return None
        return int(n) if n == int(n) else n

    return tuple(map(format_number, (addition, subtraction, multiplication, division, floor_division, modulus, power)))

num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))

result = allMath(num1, num2)
print(f"Your resulting tuple is {result}")

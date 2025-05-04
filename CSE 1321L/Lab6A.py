# Class: CSE 1321L
# Section: W04
# Term: Spring 2025
# Instructor: Nalamati
# Name: Zenzele Broomfield
# Lab: 06

def multiply(a, b):
    result = 0
    for _ in range(b):
        result += a
    return result


def exponentiate(base, exponent):
    result = 1
    for _ in range(exponent):
        temp = 0
        for _ in range(result):
            temp += base
        result = temp
    return result


def main():
    while True:
        print("Multiplication and Exponent Calculator")
        print("Choose option 1 for Multiplication")
        print("Choose option 2 for Exponentiation")
        print("Choose option 3 to Exit")

        choice = int(input())

        if choice == 1:
            a = int(input("Enter an operand: "))
            b = int(input("Enter the other operand: "))
            print(f"{a} x {b} = {multiply(a, b)}")
        elif choice == 2:
            base = int(input("Enter the base: "))
            exponent = int(input("Enter the exponent: "))
            print(f"{base}^({exponent}) = {exponentiate(base, exponent)}")
        elif choice == 3:
            print("Closing the Calculator...")
            break
        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()


# Class: CSE 1321L
# Section: W04
# Term: Spring 2025
# Instructor: Nalamati
# Name: Zenzele Broomfield
# Lab: 04

def main():
    print("Welcome!")
    number = float(input("Please input a number: "))

    print("What would you like to do with this number:")
    print("0) Get the additive inverse of the number")
    print("1) Get the reciprocal of the number")
    print("2) Square the number")
    print("3) Cube the number")
    print("4) Exit the program")

    option = int(input())

    match option:
        case 0:
            print(f"The additive inverse of {number:.1f} is {-number:.1f}")
        case 1:
            if number == 0:
                print("Cannot divide by 0!")
            else:
                print(f"The reciprocal of {number:.1f} is {1 / number:.1f}")
        case 2:
            print(f"The square of {number:.1f} is {number ** 2:.1f}")
        case 3:
            print(f"The cube of {number:.1f} is {number ** 3:.1f}")
        case 4:
            print("Thank you, goodbye!")
        case _:
            print("Invalid option!")


if __name__ == "__main__":
    main()

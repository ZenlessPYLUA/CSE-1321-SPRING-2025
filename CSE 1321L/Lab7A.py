# Class: CSE 1321L
# Section: W04
# Term: Spring 2025
# Instructor: Nalamati
# Name: Zenzele Broomfield
# Lab: 07

def isValid(width, height):
    return (width + height) > 30


def area(width, height):
    return width * height


def perimeter(width, height):
    return 2 * (width + height)


def main():
    while True:
        try:
            width = float(input("Enter width: "))
            height = float(input("Enter height: "))

            if isValid(width, height):
                print("This is a valid rectangle.")
                print(f"The area is: {area(width, height)}")
                print(f"The perimeter is: {perimeter(width, height)}")
            else:
                print("This is an invalid rectangle.")

        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        repeat = input("Do you want to enter another width and height (Y/N)?: ").strip().lower()
        if repeat != 'y':
            break

    print("Program Ends")


if __name__ == "__main__":
    main()
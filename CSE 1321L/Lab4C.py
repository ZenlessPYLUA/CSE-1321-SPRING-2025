# Class: CSE 1321L
# Section: W04
# Term: Spring 2025
# Instructor: Nalamati
# Name: Zenzele Broomfield
# Lab: 04

def main():
    try:
        a = int(input("Enter the first side of the triangle: "))
        b = int(input("Enter the second side of the triangle: "))
        c = int(input("Enter the third side of the triangle: "))

        if a > 0 and b > 0 and c > 0:
            if a + b > c and a + c > b and b + c > a:
                if a == b == c:
                    print("The triangle is an equilateral triangle.")
                else:
                    if a == b or a == c or b == c:
                        print("The triangle is an isosceles triangle.")
                    else:
                        print("The triangle is a scalene triangle.")
            else:
                print("The sides do not form a valid triangle.")
        else:
            print("Invalid input. All sides must be greater than 0.")
    except ValueError:
        print("Invalid input. Please enter integer values only.")


if __name__ == "__main__":
    main()

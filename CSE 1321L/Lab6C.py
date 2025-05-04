# Class: CSE 1321L
# Section: W04
# Term: Spring 2025
# Instructor: Nalamati
# Name: Zenzele Broomfield
# Lab: 06

def print_pyramid(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i), end="")

        for j in range(i, 0, -1):
            print(j, end="")

        for j in range(2, i + 1):
            print(j, end="")

        print()


def main():
    while True:
        rows = int(input("Enter Number for Rows or 0 to quit: "))
        if rows == 0:
            break
        print_pyramid(rows)


if __name__ == "__main__":
    main()

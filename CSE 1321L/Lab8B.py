# Class: CSE 1321L
# Section: W04
# Term: Spring 2025
# Instructor: Nalamati
# Name: Zenzele Broomfield
# Lab: 08

def main():
    friend_list = []

    while True:
        print("\n[Friend List]")
        print("1 - Add friend")
        print("2 - List friends")
        print("3 - Quit")

        choice = input("Make your selection: ")

        if choice == "1":
            name = input("Enter your friend's name: ")
            age = input("Enter your friend's age: ")
            friend_list.append((name, age))
            print("Friend added.")

        elif choice == "2":
            if friend_list:
                for friend in friend_list:
                    print(f"Name: {friend[0]}, Age: {friend[1]}")
            else:
                print("Friend list is empty.")

        elif choice == "3":
            print("Shutting down...")
            break

        else:
            print("Invalid selection. Please choose a number between 1 and 3.")


if __name__ == "__main__":
    main()

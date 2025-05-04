# Class: CSE 1321L
# Section: W04
# Term: Spring 2025
# Instructor: Nalamati
# Name: Zenzele Broomfield
# Lab: 09

users = {}


def register():
    print("[Register]")
    username = input("Username: ")
    password = input("Password: ")

    if username in users:
        print("Username already exists!")
    else:
        users[username] = password
        print("User successfully added!")


def login():
    print("[Login]")
    username = input("Username: ")
    password = input("Password: ")

    if username in users and users[username] == password:
        print("Success!")
        user_menu(username)
    else:
        print("Incorrect username/password!")


def user_menu(username):
    while True:
        print("\nChoose an option")
        print("3 - Change Password")
        print("4 - Logout")
        print("E - Exit")
        option = input().strip().upper()

        if option == "3":
            print("[Changing password]")
            new_password = input("Password: ")
            users[username] = new_password
        elif option == "4":
            print("Logging Out...")
            break
        elif option == "E":
            print("Terminating...")
            exit()
        else:
            print("Invalid option!")


def main():
    while True:
        print("\nChoose an option")
        print("1 - Login")
        print("2 - Register")
        print("E - Exit")

        option = input().strip().upper()

        if option == "1":
            login()
        elif option == "2":
            register()
        elif option == "E":
            print("Terminating...")
            break
        else:
            print("Invalid option!")


main()

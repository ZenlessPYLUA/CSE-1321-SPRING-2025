# Class: CSE 1321L
# Section: W04
# Term: Spring 2025
# Instructor: Nalamati
# Name: Zenzele Broomfield
# Assignment: 04


import A4C_Functions

def main():
    print("Welcome to the ATM!")
    name = input("Please enter your name: ")
    balance = float(input("Enter your initial balance: $"))

    while True:
        choice = A4C_Functions.display_main_menu()

        if choice == "1":
            balance = A4C_Functions.deposit(balance)
        elif choice == "2":
            balance = A4C_Functions.withdraw(balance)
        elif choice == "3":
            A4C_Functions.check_balance(balance)
        elif choice == "4":
            print(f"Goodbye, {name}! Thank you for using the ATM.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

# Class: CSE 1321L
# Section: W04
# Term: Spring 2025
# Instructor: Nalamati
# Name: Zenzele Broomfield
# Assignment: 04

def display_main_menu():
    print("ATM Main Menu:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Please choose an option (1-4): ")
    return choice


def deposit(balance):
    amount = float(input("Enter the amount to deposit: $"))
    balance += amount
    print(f"Deposited ${amount:.2f}. New balance: ${balance:.1f}")
    return balance


def withdraw(balance):
    amount = float(input("Enter the amount to withdraw: $"))
    if amount > balance:
        print("Insufficient balance.")
    else:
        balance -= amount
        print(f"Withdrew ${amount:.2f}. New balance: ${balance:.1f}")
    return balance


def check_balance(balance):
    print(f"Your current balance is: ${balance:.1f}")

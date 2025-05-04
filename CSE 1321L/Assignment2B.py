# Class: CSE 1321L
# Section: W04
# Term: Spring 2025
# Instructor: Nalamati
# Name: Zenzele Broomfield
# Assignment: 02

print("[Loan Approval System]")

age = int(input("Enter your age: ").strip())
income = int(input("Enter your income: $").strip())
credit_score = int(input("Enter your credit score: ").strip())

if age < 18:
    print("You do not qualify for a loan due to age.")
else:
    match credit_score:
        case score if 700 <= score <= 850:
            credit_category = "Good"
        case score if 600 <= score <= 699:
            credit_category = "Fair"
        case score if 300 <= score <= 599:
            credit_category = "Poor"
        case _:
            print("Invalid credit score. Must be between 300 and 850.")
            exit()

    if credit_category == "Poor":
        print("You do not qualify for a loan due to poor credit.")
    else:
        if income >= 100000 and credit_category == "Good":
            print("You qualify for a Premium Loan.")
        elif income >= 50000:
            print("You qualify for a Standard Loan.")
        elif credit_category == "Fair":
            print("You qualify for a Basic Loan.")
        else:
            print("Your income is too low for a loan.")

# Class: CSE 1321L
# Section: W04
# Term: Spring 2025
# Instructor: Nalamati
# Name: Zenzele Broomfield
# Assignment: 02

print("[Discount Calculator]")

total_purchase = float(input("Enter your total purchase amount: $").strip())

membership_status = input("Are you a member of the shopping club (Yes or No)? ").strip().lower()

discount = 0

if total_purchase < 50:
    discount = 0
elif 50 <= total_purchase <= 200:
    if membership_status == "yes":
        discount = total_purchase * 0.10
    else:
        discount = total_purchase * 0.05
else:
    if membership_status == "yes":
        discount = total_purchase * 0.15
    else:
        discount = total_purchase * 0.10

total_after_discount = total_purchase - discount

print(f"Your discount is: ${discount:.1f}")
print(f"Your total price after discount is: ${total_after_discount:.1f}")

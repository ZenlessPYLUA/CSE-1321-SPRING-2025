# Class: CSE 1321L
# Section: W04
# Term: Spring 2025
# Instructor: Nalamati
# Name: Zenzele Broomfield
# Assignment: 01

print("[Centimeters to Feet and Inches Converter]")

length_cm = float(input("Enter the length in centimeters: "))

CM_PER_FOOT = 30.48
CM_PER_INCH = 2.54

total_feet = length_cm // CM_PER_FOOT
remaining_cm = length_cm % CM_PER_FOOT
total_inches = remaining_cm / CM_PER_INCH


print(f"The length is {int(total_feet)} feet and {round(total_inches, 2)} inches")

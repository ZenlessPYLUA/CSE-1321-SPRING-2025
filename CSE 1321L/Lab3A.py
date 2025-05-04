# Class: CSE 1321L
# Section: W04
# Term: Spring 2025
# Instructor: Nalamati
# Name: Zenzele Broomfield
# Lab: 03

amount_owned = float(input("Amount owed: "))
apr = float(input("$APR: "))

monthly_percentage_rate = apr / 12
minimum_payment = amount_owned * (monthly_percentage_rate / 100)

print(f"Monthly percentage rate: {round(monthly_percentage_rate, 3)}")
print(f"Minimum payment: ${round(minimum_payment, 2)}")
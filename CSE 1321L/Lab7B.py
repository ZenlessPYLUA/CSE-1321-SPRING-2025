# Class: CSE 1321L
# Section: W04
# Term: Spring 2025
# Instructor: Nalamati
# Name: Zenzele Broomfield
# Lab: 07

import MyMath

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

min_value = MyMath.my_min(num1, num2)
max_value = MyMath.my_max(num1, num2)
avg_value = MyMath.my_avg(num1, num2)

print(f"Min is {min_value}")
print(f"Max is {max_value}")
print(f"Average is {avg_value}")

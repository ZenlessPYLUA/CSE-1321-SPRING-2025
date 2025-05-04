# Class: CSE 1321L
# Section: W04
# Term: Spring 2025
# Instructor: Nalamati
# Name: Zenzele Broomfield
# Lab: 03

num_small = int(input("Enter the number of small sandwiches: "))
num_medium = int(input("Enter the number of medium sandwiches: "))
num_large = int(input("Enter the number of large sandwiches: "))
num_extra_large = int(input("Enter the number of extra-large sandwiches: "))


print(f"You've entered {num_small} small sandwiches.")
print(f"You've entered {num_medium} medium sandwiches.")
print(f"You've entered {num_large} large sandwiches.")
print(f"You've entered {num_extra_large} extra-large sandwiches.")


time_small = 30
time_medium = 60
time_large = 75
time_extra_large = 135


total_seconds = (num_small * time_small +
                 num_medium * time_medium +
                 num_large * time_large +
                 num_extra_large * time_extra_large)


minutes = total_seconds // 60
seconds = total_seconds % 60


print(f"Total cooking time is {minutes} minutes and {seconds} seconds.")

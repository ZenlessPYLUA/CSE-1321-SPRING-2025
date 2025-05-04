# Class: CSE 1321L
# Section: W04
# Term: Spring 2025
# Instructor: Nalamati
# Name: Zenzele Broomfield
# Lab: 10


class Chair:
    def __init__(self, numOfLegs = 4, rolling=False, material="plastic"):
        self.numOfLegs = numOfLegs
        self.rolling = rolling
        self.material = material

    def display(self):
        roll_status = "rolling" if self.rolling else "not rolling"
        print(f"Your chair has {self.numOfLegs} legs, is {roll_status}, and is made of {self.material}.")

print("You are about to create a chair.")
numOfLegs = int(input("How many legs does your chair have: "))
rolling = input("Is your chair rolling (true/false): ").strip().lower() == "true"
material = input("What is your chair made of: ")

chair = Chair(numOfLegs, rolling, material)
chair.display()

print("This program is going to change that.")
chair.numOfLegs = 4
chair.rolling = False
chair.material = "wood"
chair.display()

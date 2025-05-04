# Class: CSE 1321L
# Section: W04
# Term: Spring 2025
# Instructor: Nalamati
# Name: Zenzele Broomfield
# Lab: 10

class Dog:
    def __init__(self, agev1, weightv1, namev1, furcolorv1, breedv1):
        self.age = agev1
        self.weight = weightv1
        self.name = namev1
        self.furcolor = furcolorv1
        self.breed = breedv1

    def bark(self):
        print("Woof! Woof!")

    def rename(self, new_namev1):
        self.name = new_namev1

    def eat(self, amount):
        self.weight += amount

    def display(self):
        print(f"{self.name} is a {self.age} year old {self.furcolor} {self.breed} that weighs {self.weight:.1f} lbs.")

print("You are about to create a dog.")
age = int(input("How old is the dog: "))
weight = float(input("How much does the dog weigh: "))
name = input("What is the dog’s name: ")
furColor = input("What color is the dog: ")
breed = input("What breed is the dog: ")

dog = Dog(age, weight, name, furColor, breed)
dog.display()
dog.bark()

food = float(input(f"{dog.name} is hungry, how much should he eat: "))
dog.eat(food)
dog.display()

new_name = input(f"{dog.name} isn’t a very good name. What should they be renamed to: ")
dog.rename(new_name)
dog.display()

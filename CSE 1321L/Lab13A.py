# Class: CSE 1321L
# Section: W04
# Term: Spring 2025
# Instructor: Nalamati
# Name: Zenzele Broomfield
# Lab: 13

temps = input("Enter temperatures for each day separated by space: ")
temps = list(map(int, temps.split()))

print()

streak = 0
num_of_heatwaves = 0
in_heatwave = False

for temp in temps:
    if temp > 38:
        streak += 1
    else:
        if streak >= 3:
            num_of_heatwaves += 1
        streak = 0

if streak >= 3:
    num_of_heatwaves += 1

print(f"Number of heat waves: {num_of_heatwaves}")

streak = 0
max_streak = 0

for temp in temps:
    if temp < 15:
        streak += 1
        max_streak = max(max_streak, streak)
    else:
        streak = 0

print(f"Longest cold streak: {max_streak} days")

average_temp = sum(temps) / len(temps)
print(f"Average temperature: {average_temp:.2f}°C")

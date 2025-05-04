# Class: CSE 1321L
# Section: W04
# Term: Spring 2025
# Instructor: Nalamati
# Name: Zenzele Broomfield
# Assignment: 01

print("[Ideal Gas Law Calculator]")

IDEAL_GAS_CONSTANT = 0.0821

n = float(input("Enter the number of moles of the gas: "))
temperature_celsius = float(input("Enter the temperature of the gas in Celsius: "))
volume_liters = float(input("Enter the volume of the gas in Liters: "))

temperature_kelvin = temperature_celsius + 273.15

pressure = (n * IDEAL_GAS_CONSTANT * temperature_kelvin) / volume_liters

print(f"The pressure of the gas is {pressure:.2f} atm")

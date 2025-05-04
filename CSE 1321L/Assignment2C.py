# Class: CSE 1321L
# Section: W04
# Term: Spring 2025
# Instructor: Nalamati
# Name: Zenzele Broomfield
# Assignment: 02

print("Welcome to the RPG Game!")
print("Choose your class: 1. Warrior 2. Mage 3. Healer")

# Get user input for class selection
class_choice = input("Enter the number of your class (1/2/3): ").strip()

# Initialize class name and action choices
class_name = ""
actions = []

match class_choice:
    case "1":
        class_name = "Warrior"
        actions = ["Attack with your sword", "Defend with your shield"]
        print("You have chosen Warrior! You are strong and brave.")
    case "2":
        class_name = "Mage"
        actions = ["Cast a fireball", "Cast a healing spell"]
        print("You have chosen Mage! You wield powerful magic.")
    case "3":
        class_name = "Healer"
        actions = ["Heal your ally", "Attack with your staff"]
        print("You have chosen Healer! You are kind and supportive.")
    case _:
        print("Invalid class choice. The game ends.")
        print("Thank you for playing!")
        exit()

# Prompt for action choice
print("What would you like to do? 1.", actions[0], "2.", actions[1])
action_choice = input("Choose your action (1/2): ").strip()

match action_choice:
    case "1":
        match class_name:
            case "Warrior":
                print("You swing your sword and defeat the enemy!")
            case "Mage":
                print("You cast a fireball and scorch the enemy!")
            case "Healer":
                print("You heal your ally and boost their morale!")
    case "2":
        match class_name:
            case "Warrior":
                print("You raise your shield and block the enemy's attack!")
            case "Mage":
                print("You cast a healing spell and restore your energy.")
            case "Healer":
                print("You swing your staff and knock out the enemy!")
    case _:
        print("Invalid action choice. The game ends.")

print("Thank you for playing!")

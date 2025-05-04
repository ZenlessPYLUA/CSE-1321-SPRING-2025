# Class: CSE 1321L
# Section: W04
# Term: Spring 2025
# Instructor: Nalamati
# Name: Zenzele Broomfield
# Assignment: 03

print("[Character Frequencies]")
user_input = input("Enter a string: ")

# Convert to lowercase to treat uppercase and lowercase as the same
user_input = user_input.lower()

# Remove spaces
user_input = user_input.replace(" ", "")

# Iterate over the string to count character frequencies
while user_input:
    char = user_input[0]  # Take the first character
    count = 0  # Initialize counter

    # Count occurrences of the character
    for c in user_input:
        if c == char:
            count += 1

    # Print result
    if count == 1:
        print(f"{char} appears {count} time")
    else:
        print(f"{char} appears {count} times")

    # Replace all occurrences of the counted character with a number to avoid recounting
    user_input = user_input.replace(char, "1")

    # Remove counted characters (all 1s)
    user_input = user_input.replace("1", "")

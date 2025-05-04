# Class: CSE 1321L
# Section: W04
# Term: Spring 2025
# Instructor: Nalamati
# Name: Zenzele Broomfield
# Assignment: 04

def format_word(word):

    return word.capitalize()

def convert_to_pascal_case(text):
    words = text.split()
    pascal_case = "".join(format_word(word) for word in words)
    return pascal_case

def main():
    user_input = input("Enter a string: ").strip()
    pascal_case_result = convert_to_pascal_case(user_input)
    print(f"Pascal Case: {pascal_case_result}")

if __name__ == "__main__":
    main()



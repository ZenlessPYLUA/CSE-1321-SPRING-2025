# Class: CSE 1321L
# Section: W04
# Term: Spring 2025
# Instructor: Nalamati
# Name: Zenzele Broomfield
# Lab: 04

def determine_letter_grade():
    grade = float(input("Enter your grade: "))

    if 97 < grade <= 100:
        letter_grade = "A+"
    elif 94 < grade <= 97:
        letter_grade = "A"
    elif 91 < grade <= 94:
        letter_grade = "A-"
    elif 88 < grade <= 91:
        letter_grade = "B+"
    elif 85 < grade <= 88:
        letter_grade = "B"
    elif 82 < grade <= 85:
        letter_grade = "B-"
    elif 79 < grade <= 82:
        letter_grade = "C+"
    elif 76 < grade <= 79:
        letter_grade = "C"
    elif 73 < grade <= 76:
        letter_grade = "C-"
    elif 70 < grade <= 73:
        letter_grade = "D+"
    elif 67 < grade <= 70:
        letter_grade = "D"
    elif 64 < grade <= 67:
        letter_grade = "D-"
    elif 0 <= grade <= 64:
        letter_grade = "F"
    else:
        letter_grade = "Invalid grade"

    print(f"Letter grade is: {letter_grade}")



determine_letter_grade()

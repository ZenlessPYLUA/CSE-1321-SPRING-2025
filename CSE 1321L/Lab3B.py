# Class: CSE 1321L
# Section: W04
# Term: Spring 2025
# Instructor: Nalamati
# Name: Zenzele Broomfield
# Lab: 03

# Input for Course 1
course1_hours = int(input("Course 1 hours: "))
course1_grade = int(input("Grade for course 1: "))

# Input for Course 2
course2_hours = int(input("Course 2 hours: "))
course2_grade = int(input("Grade for course 2: "))

# Input for Course 3
course3_hours = int(input("Course 3 hours: "))
course3_grade = int(input("Grade for course 3: "))

# Input for Course 4
course4_hours = int(input("Course 4 hours: "))
course4_grade = int(input("Grade for course 4: "))


total_hours = course1_hours + course2_hours + course3_hours + course4_hours
total_quality_points = (course1_hours * course1_grade +
                        course2_hours * course2_grade +
                        course3_hours * course3_grade +
                        course4_hours * course4_grade)


gpa = total_quality_points / total_hours

if gpa == int(gpa):
    gpa_output = f"{gpa:.1f}"
else:
    gpa_output = f"{gpa:.2f}"

print(f"Total hours: {total_hours}")
print(f"Total quality points: {total_quality_points}")
print(f"Your GPA for this semester is {gpa:.2f}")


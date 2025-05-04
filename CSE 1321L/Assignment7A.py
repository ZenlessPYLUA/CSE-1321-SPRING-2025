# Class: CSE 1321L
# Section: W04
# Term: Spring 2025
# Instructor: Nalamati
# Name: Zenzele Broomfield
# Assignment: 07

def calculate_average(scores):
    return sum(scores) / len(scores)

def get_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'

def main():
    students = []
    num = int(input("Enter number of students: "))

    for i in range(num):
        print(f"\nEnter details for student {i+1}:")
        name = input("Enter student name: ")
        scores = []

        for subject in ["Math", "English", "Science"]:
            while True:
                try:
                    score = float(input(f"Enter score for {subject}: "))
                    if 0 <= score <= 100:
                        scores.append(score)
                        break
                    else:
                        print("Score must be between 0 and 100.")
                except ValueError:
                    print("Invalid input. Enter a numeric value.")

        total = sum(scores)
        average = calculate_average(scores)
        grade = get_grade(average)
        status = "Pass" if grade != 'F' else "Fail"

        student = {
            "name": name,
            "scores": scores,
            "total": total,
            "average": round(average, 2),
            "grade": grade,
            "status": status
        }
        print(f"Total score: {total}")
        print(f"Average score: {student['average']}")
        print(f"Grade: {grade}")
        print(f"Status: {status}")
        students.append(student)

    # Summary Report
    print("\n" + "="*30)
    print(" Summary Report")
    print("="*30)

    total_avg = 0
    pass_count = 0
    fail_count = 0
    top_student = max(students, key=lambda x: x['average'])

    for s in students:
        print(f"Name: {s['name']}")
        print(f"Scores: {s['scores']}")
        print(f"Total: {s['total']}")
        print(f"Average: {s['average']}")
        print(f"Grade: {s['grade']}")
        print(f"Status: {s['status']}")
        total_avg += s['average']
        if s['status'] == "Pass":
            pass_count += 1
        else:
            fail_count += 1

    class_avg = round(total_avg / len(students), 2)
    print(f"Class Average: {class_avg}")
    print(f"Students Passed: {pass_count}")
    print(f"Students Failed: {fail_count}")
    print(f"Top Student: {top_student['name']}")

if __name__ == "__main__":
    main()

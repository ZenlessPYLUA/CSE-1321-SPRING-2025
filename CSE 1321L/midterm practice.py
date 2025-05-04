def quiz_game():
    score= 0

    print("What programming language is taught in CSE 1321L?")
    print("A) Python")
    print("B) C#")
    print("C) Java")
    print("D) C++")

    answer1 = input("Your Answer: ")

    if answer1 == "A":
        print("correct!")
        score += 1
    else:
        print("Wrong..")

    print("What is your lab instructors name?")
    print("A) Gesick")
    print("B) Aydin")
    print("C) Nalamati")
    print("D) Markowsky")

    answer2 = input("Your Answer: ")

    if answer2 == "C":
        print("correct!")
        score += 1
    else:
        print("Wrong..")

    print(f"Final score: {score}/2")

if __name__ == '__main__':
    quiz_game()
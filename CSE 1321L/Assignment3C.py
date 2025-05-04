# Class: CSE 1321L
# Section: W04
# Term: Spring 2025
# Instructor: Nalamati
# Name: Zenzele Broomfield
# Assignment: 03

print("Welcome to the Guess the Word game!")

secret_word = input("Enter a word to guess (lowercase letters only): ")

hidden_word = "_" * len(secret_word)

while hidden_word != secret_word:
    print("\nThe word to guess is:", " ".join(hidden_word))

    guess = input("Guess a letter: ")

    if guess in secret_word:
        print("Good guess!")

        updated_word = ""
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                updated_word += guess
            else:
                updated_word += hidden_word[i]

        hidden_word = updated_word
    else:
        print("Oops! That letter is not in the word.")

print(f"Congratulations! You've guessed the word: {secret_word}")

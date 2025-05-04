import random
def overunder():

    wins = 0
    losses = 0
    while True:
        player_number = random.randint(10, 25)
        random_num = random.randint(1,6)

        print("\n[Over/Under]")
        print("Options: n\1")
        print("1) Add: {random_num}\n2) 2) Subtract: {random_num}")
        choice = input("Choice: ").strip()

        if input == f"{player_number}":
            print("You win!")
            wins += 1
        else:
            print("you lose!")
            losses += 1

        input("Do you want to play again? (Y/N)")
        if input == "Y":
            whileloop = True
        else:
            whileloop = False

    print(" Your wins: {wins} --- CPU Wins: {losses}")

if __name__ == "__main__":
    overunder()
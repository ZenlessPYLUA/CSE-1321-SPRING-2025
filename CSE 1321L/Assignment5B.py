import random

def create_board(width, height):
    board = []
    treasure_count = 0

    for _ in range(height):
        row = []
        for _ in range(width):
            if random.random() >= 0.7:
                row.append('T')
                treasure_count += 1
            else:
                row.append('O')
        board.append(row)

    return board, treasure_count


def display_board(board, reveal=False):
    for row in board:
        display_row = [
            'X' if cell == 'X' else ('O' if not reveal and cell == 'T' else cell)
            for cell in row
        ]
        print(" ".join(display_row))


def play_game():
    width = int(input("Enter the width of the grid: "))
    height = int(input("Enter the height of the grid: "))

    board, treasures = create_board(width, height)

    if treasures == 0:
        print("No treasures hidden! Try again with a larger grid.")
        return

    print(f"Number of treasures hidden: {treasures}")

    undiscovered = treasures

    while undiscovered > 0:
        row = int(input(f"Enter the row number (0 to {height - 1}): "))
        col = int(input(f"Enter the column number (0 to {width - 1}): "))

        if board[row][col] == 'T':
            print("Congratulations! You found a treasure!")
            board[row][col] = 'X'
            undiscovered -= 1
        else:
            print("No treasure here, try again!")

        display_board(board)

    print("\nCongratulations! You've found all the treasures!")
    display_board(board, reveal=True)


play_game()

import random

# Game setup
GAME_AREA = 5
user_board = [[' ' for _ in range(GAME_AREA)] for _ in range(GAME_AREA)]
pc_board = [[' ' for _ in range(GAME_AREA)] for _ in range(GAME_AREA)]
user_name = input("Please enter your name: ")

# Welcome message and user asked to place ships on the board
# Invalid enteries checked and user is asked to re-enter input if location
# outside of the board is selected or if anything other than
# an int between 0 - 4 is inputted. User is also informed if they have already 
# selected this location on the board.
print((f"{user_name}, Welcome to Battleship!"))
print("The board is 5 x 5. please enter 0 - 4 for your selections.\n")
for i in range(3):
    permitted_location = False
    while not permitted_location:
        try:
            row = int(input(f"Please select row for ship {i + 1}: "))
            col = int(input(f"Please select column for ship {i + 1} "))
            print("\n")
            if row < GAME_AREA and col < GAME_AREA:
                if user_board[row][col] == ' ':
                    user_board[row][col] = 'S'
                    permitted_location = True
                else:
                    print("A ship is already in this location.")
            else:
                print(f"Location is not on the board. Choose between 0 and 4.")
        except ValueError:
            print("Input is not valid. Please enter a whole number.")


# PC's ships are created and placed in random locations on the board. 
print("The computer is randomly selecting locations for their ships.\n")
for i in range(3):
    permitted_location = False
    while not permitted_location:
        row = random.randint(0, GAME_AREA-1)
        col = random.randint(0, GAME_AREA-1)
        if pc_board[row][col] == ' ':
            pc_board[row][col] = 'S'
            permitted_location = True


def display_board(area):
    """
    function iterates over all of the squares in the game area
    and prints them out with spaces between them.
    """
    print("    " + " ".join(str(i) for i in range(GAME_AREA)))
    print("  +" + "--" * GAME_AREA + "+")
    for i in range(GAME_AREA):
        print(f"{i} | {' '.join(area[i])} |")
    print("  +" + "--" * GAME_AREA + "+")


def eliminate_target(area, row, col):
    """
    This function tries to find the target in the game area.
    If it finds 'S' it changes that square to an 'O' indicating a hit.
    Also an 'X' is printed to the squares to indicate the computer missed.
    """
    if area[row][col] == 'S':
        area[row][col] = 'O'
        print(f"Direct Hit!\n")
        return True
    else:
        area[row][col] = 'X'
        print(f"Missed!\n")
        return False


# Game loop
while True:
    # Player's turn
    print(f"{user_name}, take your shot.\n")
    display_board(user_board)
    guess_is_good = False
    while not guess_is_good:
        try:
            pick_row = int(input("Choose row: "))
            pick_col = int(input("Choose column: "))
            if pick_row < GAME_AREA and pick_col < GAME_AREA:
                if user_board[pick_row][pick_col] == 'X' or user_board[pick_row][pick_col] == 'O':
                    print("You've picked that location already. Try another!")
                else:
                    guess_is_good = True
                    eliminate_target(pc_board, pick_row, pick_col)
            else:
                print("Location is invalid. Please choose values between 0 - 4.")
        except ValueError:
            print("Invalid input. Please pick one of 0,1,2,3,4.")

    # If the user wins
        if all('S' not in row for row in pc_board):
            print(f"{user_name}, you have sunk all of your opponents battleships! You are the winner!")
            break

    # the PC's turn to shoot
    print("The computer is taking it's shot...")
    pc_pick_row = random.randint(0, GAME_AREA-1)
    pc_pick_col = random.randint(0, GAME_AREA-1)
    while user_board[pc_pick_row][pc_pick_col] == 'X' or user_board[pc_pick_row][pc_pick_col] == 'O':
        pc_pick_row = random.randint(0, GAME_AREA-1)
        pc_pick_col = random.randint(0, GAME_AREA-1)
    eliminate_target(user_board, pc_pick_row, pc_pick_col)

    # If the PC wins
    if all('S' not in row for row in user_board):
        print("The computer has sunk all of your Battleships! You lose!")
        break

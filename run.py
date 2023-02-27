import random

# Game setup
GAME_AREA = 5
user_board = [[' ' for _ in range(GAME_AREA)] for _ in range(GAME_AREA)]
pc_board = [[' ' for _ in range(GAME_AREA)] for _ in range(GAME_AREA)]
user_name = input("Please enter your name: ")

# Welcome message and user asked to place ships on the board
# Invalid enteries checked and user is asked to re-enter input if location
# outside of the board is selected or if anything other than
# an int between 0 - 4 is inputted. User is also informed if they have already selected
# this location on the board.
print((f"{user_name}, Welcome to Battleship!"))
print("The board is 5 x 5. please enter 0 - 4 for your selections.\n")
for i in range(3):
    permitted_location = False
    while not permitted_location:
        try:
            row = int(input(f"Please select row for ship {i+1}: "))
            col = int(input(f"Please select column for ship {i+1} "))
            print("\n")
            if row < GAME_AREA and col < GAME_AREA:
                if user_board[row][col] == ' ':
                    user_board[row][col] == 'S'
                    permitted_location = True
                else:
                    print("A ship is already in this location, please choose another.")
            else:
                print(f"Location is not part of the game area. Choose between 0 and 4.")
        except ValueError:
            print("Input is not valid. Please enter a whole number.")


# PC's ships are created and placed in random locations on the board. 
print("The computer is randomly selecting locations for their ships.")
for i in range(3):
    permitted_location = False
    while not permitted_location:
        row = random.randint(0, GAME_AREA-1)
        col = random.randint(0, GAME_AREA-1)
        if pc_board[row][col] == ' ':
            pc_board[row][col] == 'S'
            permitted_location = True


# Function to print the board to the terminal
def display_board(area):
    print("   " + " ".join(str(i) for i in range(GAME_AREA)))
    print("  +" + "--" * GAME_AREA + "+")
    for i in range(board_size):
        print(f"{i} | {' '.join(area[i])} |")
    print("  +" + "--" * GAME_AREA + "+")


# Function to display the game area
def display(board):
    print("   " + " ".join(str(i) for i in range(GAME_AREA)))
    print("  +" + "--" * GAME_AREA + "+")
    for i in range(GAME_AREA):
        print(f"{i} | {' '.join(board[i])} |")
    print("  +" + "--" * GAME_AREA + "+")

# Function that checks whether or not guesses are hit or miss.
def target_eliminated(area, row, col):
    if area[row][col] == 'S':
        area[ro][col] == 'O'
        print("Direct Hit!\n")
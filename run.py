import random
from termcolor import colored

# Game setup
game_area = 5
user_board = [[' ' for _ in range(game_area)] for _ in range(game_area)]
pc_board = [[' ' for _ in range(game_area)] for _ in range(game_area)]
user_name = input("Please enter your name: ")

TITLE = """
888             888   888   888                888     d8b         
888             888   888   888                888     Y8P         
888             888   888   888                888                 
88888b.  8888b. 888888888888888 .d88b. .d8888b 88888b. 88888888b.  
888 "88b    "88b888   888   888d8P  Y8b88K     888 "88b888888 "88b 
888  888.d888888888   888   88888888888"Y8888b.888  888888888  888 
888 d88P888  888Y88b. Y88b. 888Y8b.         X88888  888888888 d88P 
88888P" "Y888888 "Y888 "Y888888 "Y8888  88888P'888  88888888888P"  
                                                          888      
                                                          888      
                                                          888  
"""

print(TITLE)

LEGEND = """
----------------------------------------+
LEGEND:                                 |
                                        |
S = Your Ship                           |
X = Miss by the computer                |
O = The computer sunk your battleship   |
                                        |
BOARD:                                  |
                                        |
row = row                               |
col = column                            |
----------------------------------------+
"""

print(LEGEND)

def game_setup(game_area, user_board, pc_board, user_name):
    """
    function asks user to place 3 ships on the board.
    The function also randomly places 3 ships on the board for the computer.
    The function checks if the user has entered a valid location for
    their ships. If the user has entered an invalid location they are
    asked to re-enter the location. The function also checks if the
    computer has randomly placed a ship in a location
    that already has a ship. If the computer has placed a ship in a
    location that already has a ship,
    the function will randomly select a new location for the ship.
    """
    print(colored(f'{user_name}, Welcome to Battleship!', 'green'))
    print(colored('Begin by placing 3 battleships on the board.', 'green'))
    print(colored('The board is 5 x 5. please enter 0 - 4 for your selections.\n', 'green'))
    for i in range(3):
        permitted_location = False
        while not permitted_location:
            try:
                row = int(input(f"Please select row for ship {i + 1}: "))
                col = int(input(f"Please select col for ship {i + 1}: "))
                print("\n")
                if row <= game_area and col <= game_area:
                    if user_board[row][col] == ' ':
                        user_board[row][col] = 'S'
                        permitted_location = True
                    else:
                        print("A ship is already in this location.")
                else:
                    print("Location not on the board. Choose between 0 and 4")
            except ValueError:
                print("Input is not valid. Please enter a whole number.")

    # PC's ships are created and placed in random locations on the board.
    print("The computer is randomly selecting locations for ship placement.\n")
    for i in range(3):
        permitted_location = False
        while not permitted_location:
            row = random.randint(0, game_area-1)
            col = random.randint(0, game_area-1)
            if pc_board[row][col] == ' ':
                pc_board[row][col] = 'S'
                permitted_location = True


game_setup(game_area, user_board, pc_board, user_name)


def display_board(area):
    """
    function iterates over all of the squares in the game area
    and prints them out with spaces between them.
    """
    print("    " + " ".join(str(i) for i in range(game_area)))
    print("  +" + "--" * game_area + "+")
    for i in range(game_area):
        print(f"{i} | {' '.join(area[i])} |")
    print("  +" + "--" * game_area + "+")


def eliminate_target(area, row, col):
    """
    This function tries to find the target in the game area.
    If it finds 'S' it changes that square to an 'O' indicating a hit.
    Also an 'X' is printed to the squares to indicate the computer missed.
    """
    if area[row][col] == 'S':
        area[row][col] = 'O'
        print(colored(f'Direct Hit!\n', 'blue'))
        return True
    else:
        area[row][col] = 'X'
        print(colored(f'Missed!\n', 'blue'))
        return False


# Game loop
def game_loop(GAME_AREA, user_board, pc_board, user_name, display_board, eliminate_target):
    """
    This function is the game loop. It asks the user to pick a location on the board
    and then the computer randomly picks a location on the board.
    The function checks if the user has entered a valid location for their ships.
    If the user has entered an invalid location they are asked to re-enter the location.
    The function also checks if the computer has randomly placed a ship in a location
    that already has a ship. If the computer has placed a ship in a location that already
    has a ship, the function will randomly select a new location for the ship.
    """
    while True:
        # Player's turn
        print(colored(f"{user_name}, take your shot.\n", "blue"))
        display_board(user_board)
        guess_is_good = False
        while not guess_is_good:
            try:
                pick_row = int(input(colored("Choose row: ", 'yellow')))
                pick_col = int(input(colored("Choose col: ", 'yellow')))
                print("\n")
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
            print(colored(f'{user_name}, you have sunk all of your opponents battleships! You are the winner!', 'green'))
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
            print(colored('The computer has sunk all of your Battleships! You lose!', 'red'))
            break


game_loop(game_area, user_board, pc_board, user_name, display_board, eliminate_target)

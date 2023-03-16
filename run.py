"""
Importing random, time & colored from termcolor
"""
import random
import time
from termcolor import colored

# Game setup
GAME_AREA = 5

TITLE = r"""
 _           _   _   _           _     _
| |         | | | | | |         | |   (_)
| |__   __ _| |_| |_| | ___  ___| |__  _  __
| '_ \ / _` | __| __| |/ _ \/ __| '_ \| | '_ \
| |_) | (_| | |_| |_| |  __/\__ \ | | | | |_) |
|_.__/ \__,_|\__|\__|_|\___||___/_| |_|_| .__/
                                        | |
                                        |_|
"""

LEGEND = """
----------------------------------------+
LEGEND:                                 |
                                        |
S = Your Ship                           |
X = Miss by the computer                |
O = The computer sunk your battleship   |
@ = You sunk the computers ship         |
                                        |
----------------------------------------+
"""


def clear_screen():
    """
    Clear the console screen.
    This function uses the ANSI escape code '\033c' to clear the console.
    """
    print('\033c')


def display_header():
    """
    Clears the screen and displays the title and legend of the program.
    """
    clear_screen()
    print(TITLE)
    print(LEGEND)


def game_setup(user_board, pc_board, user_name):
    """
     Set up the game by placing user's and computer's ships on the boards.

    This function prompts the user to place 3 ships on their board and
    validates the entered locations. It also randomly places 3 ships for
    the computer on its board. The user's and computer's ships are placed
    in non-overlapping locations.

    Parameters:
    user_board (list): A 2D list representing the user's game board.
    pc_board (list): A 2D list representing the computer's game board.
    user_name (str): The user's name.

    Returns:
    list: A list of tuples containing the row and column coordinates of
    each ship on the computer's board.
    """
    # Importing color from termcolor enables text to be printed
    # in color to the terminal
    print("\n")
    print(colored(f'      {user_name}, Welcome to Battleship!', 'green'))
    print(colored('Begin by placing 3 battleships on the board.', 'green'))
    print(colored('          The board is 5 x 5.', 'green'))
    print(colored('Please enter 0 - 4 for your selections.', 'green'))
    print("\n")

    for i in range(3):
        display_board(user_board)
        permitted_location = False
        while not permitted_location:
            try:
                row = int(input(f"Please select row for ship {i + 1}: "))
                col = int(input(f"Please select col for ship {i + 1}: "))
                print("\n")
                if row < GAME_AREA and col < GAME_AREA:
                    if user_board[row][col] == ' ':
                        user_board[row][col] = 'S'
                        permitted_location = True
                    else:
                        print("A ship is already in this location.")
                else:
                    print("Location not on the board. Choose between 0 and 4")
            except ValueError:
                print("Input is not valid. Please enter a whole number.")

    # Wait 1 second before clearing the screen
    # made possible by importing the time library
    time.sleep(1)

    # Clear the screen, display the header, and show the current game board
    clear_screen()
    display_header()
    display_board(user_board)

    # PC's ships are created and placed in random locations on the board.
    print("The computer is randomly selecting locations.\n")

    # Get the locations of the user's ships
    user_ship_locations = [(r, c) for r in range(GAME_AREA)
                           for c in range(GAME_AREA)
                           if user_board[r][c] == 'S']

    # Place computer's ships randomly
    pc_ship_locations = []
    for i in range(3):
        permitted_location = False
        while not permitted_location:
            row = random.randint(0, GAME_AREA-1)
            col = random.randint(0, GAME_AREA-1)
            if pc_board[row][col] == ' ' and (row, col)\
                    not in user_ship_locations:
                pc_board[row][col] = 'S'
                pc_ship_locations.append((row, col))
                permitted_location = True

    return pc_ship_locations


def display_board(area):
    """
    Display the game board with row and column indices.

    This function iterates over all the squares in the game area and prints
    them with spaces between the elements, along with row and column indices.
    The board is enclosed in a border for better visualization.

    Parameters:
    area (list): A 2D list representing the game area to be displayed.

    Returns:
    None
    """
    print("    " + " ".join(str(i) for i in range(GAME_AREA)))
    print("  +" + "--" * GAME_AREA + "-+")
    for i in range(GAME_AREA):
        print(f"{i} | {' '.join(area[i])} |")
    print("  +" + "--" * GAME_AREA + "-+")


def eliminate_target(area, row, col):
    """
    This function tries to find the target in the game area.
    If it finds 'S' it changes that square to an 'O' indicating a hit.
    Also an 'X' is printed to the squares to indicate the computer missed.

    Parameters:
    area (list): A 2D list representing the game area.
    row (int): The row index of the target square.
    col (int): The column index of the target square.

    Returns:
    bool: True if the target is found and hit, False otherwise.
    """

    # Check if the target is at the specified row and column
    if area[row][col] == 'S':
        area[row][col] = 'O'
        print(colored('Direct Hit!\n', 'blue'))
        # Return True as the target has been hit
        return True
    else:
        # Change the square to 'X' to indicate a miss
        area[row][col] = 'X'
        print(colored('Missed!\n', 'blue'))
        # Return False as the target has not been hit
        return False


def game_loop(user_board, pc_board, user_name, pc_ship_locations):
    """
    Execute the main game loop for a player and computer opponent.

    This function handles the game loop, alternating turns between the user and
    the computer. It validates user input and checks for valid ship placement,
    prompting the user to re-enter their choice if necessary. The function also
    ensures that the computer doesn't place a ship on an occupied location.

    Parameters:
    user_board (list): A 2D list representing the user's game board.
    pc_board (list): A 2D list representing the computer's game board.
    user_name (str): The user's name.
    pc_ship_locations (list): A list of tuples representing the computer's
    ship locations.

    Returns:
    None
    """
    while True:
        # Clear the screen before displaying the updated boards
        clear_screen()
        display_header()
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
                    if user_board[pick_row][pick_col] == 'X' or\
                         user_board[pick_row][pick_col] == 'O':
                        print("There are no enemy ships in squares marked X, "
                              "try again!")
                    else:
                        guess_is_good = True
                        hit = eliminate_target(pc_board, pick_row, pick_col)
                        if hit:
                            user_board[pick_row][pick_col] = '@'
                else:
                    print("Location is invalid. Please choose values"
                          "between 0 - 4.")
            except ValueError:
                print("Invalid input. Please pick one of 0,1,2,3,4.")

        # If the user wins
        if all('S' not in row for row in pc_board):
            clear_screen()
            display_board(user_board)
            print(colored(f'{user_name}, YOU WIN!', 'green'))
            break

        # the PC's turn to shoot
        print("\n")
        print("The computer is taking its shot...")
        print("\n")
        pc_pick_row = random.randint(0, GAME_AREA-1)
        pc_pick_col = random.randint(0, GAME_AREA-1)

        while (pc_pick_row, pc_pick_col) in pc_ship_locations or\
                user_board[pc_pick_row][pc_pick_col] == 'X' or\
                user_board[pc_pick_row][pc_pick_col] == 'O':
            pc_pick_row = random.randint(0, GAME_AREA-1)
            pc_pick_col = random.randint(0, GAME_AREA-1)

        eliminate_target(user_board, pc_pick_row, pc_pick_col)

        # If the PC wins
        if all('S' not in row for row in user_board):
            clear_screen()
            display_board(user_board)
            print(colored('COMPUTER WINS!, ALL YOUR SHIPS ARE SUNK', 'red'))
            break

        # Add a small delay before updating the board display
        # made possible by importing the time library
        time.sleep(2)


def play_game():
    """
    Execute the main function to play the game.

    This function manages the game flow, starting with displaying the header,
    setting up the game, and initiating the game loop. It also prompts the user
    to play again after a game has ended.

    Returns:
    None
    """
    display_header()
    while True:
        # Initialize game variables
        user_board = [[' ' for _ in range(GAME_AREA)] for _ in
                      range(GAME_AREA)]
        pc_board = [[' ' for _ in range(GAME_AREA)] for _ in range(GAME_AREA)]
        while True:
            user_name = input("Please enter your name: ").strip()
            if len(user_name) >= 3:
                break
            else:
                print("Name must be at least 3 characters long.")

        # Start game
        pc_ship_locations = game_setup(user_board, pc_board, user_name)
        game_loop(user_board, pc_board, user_name, pc_ship_locations)

        # Prompt user to play again
        play_again = input("Would you like to play again? (y/n) ").lower()
        while play_again not in ['y', 'n']:
            play_again = input("Invalid input."
                               "Please enter 'y' or 'n': ").lower()

        # Exit loop if user doesn't want to play again
        if play_again == 'n':
            clear_screen()
            print(TITLE)
            print("Thanks for playing!")
            print("\n")
            break

        # Clear screen and display header if the user wants to play again
        if play_again == 'y':
            display_header()


play_game()

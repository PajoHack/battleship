import random

# Game setup
game_area = 5
user_board = [[' ' for _ in range(game_area)] for _ in range(game_area)]
pc_board = [[' ' for _ in range(game_area)] for _ in range(game_area)]
user_name = input("Please enter your name: ")

# User places ships on the board
print((f"{user_name}, Welcome to Battleship. Place your ships on the board to start!"))
for i in range(3):
    permitted_location = False
    while not permitted_location:
        try:
            row = int(input(f"Please select row for ship {i+1}: "))
            col = int(input(f"Please select column for ship {i+1} "))
            print("\n")
            if row < game_area and col < game_area:
                if user_board[row][col] == ' ':
                    user_board[row][col] == 'S'
                    permitted_location = True
                else:
                    print("A ship is already in this location, please choose another.")
            else:
                print(f"Location is not part of the game area. Choose between 0 and 4.")
        except ValueError:
            print("Input is not valid. Please enter a whole number.")

# PC's ships are created


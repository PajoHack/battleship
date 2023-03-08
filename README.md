
# Battleship

This is a Battleships game written in python, the game runs in the terminal. You can see it in action in the Code Institute mock terminal Heroku.

The user attempts to defeat the computer by sinking it's battleships and in turn, the computer attempts to sink the users's ships.

[The live version of the project can be seen here](https://ci-battleship-pp3.herokuapp.com/)


## Features

- The title "battleship" is displayed when the game is run. 
- A legend is also displayed to show the user what each charachter represents. 
- An input asking the user for their name is also displayed.

![On game start](documentation/on_game_start.png)

- A welcome message containing the users name is displayed.
- The user is asked to begin by placing 3 ships on the board.
- The user is also told that the game area / board is 5 rows x 5 columns.
- It is also explained how to place their ships on the board by selecting digits from 0 to 4.

![Welcome user](documentation/welcome_user.png)

- The user makes their selections 

![User places ships on the board](documentation/placing_ships.png)

- Next the computer randomly selects 3 locations on the board for it's ships.
- The game can now begin and the user is encouraged to take the first shot.

![PC places it's ships](documentation/pc_selects_locations.png)

- The user is told if their shot was a hit or a miss.
- The computer then takes a shot and the user is informed if it hit or missed.
- Then the game loop continues.

![Missed shot](documentation/missed_shot.png)

- With this shot both the player and computer sink a battleship!

![Direct Hit](documentation/direct_hit.png)

- If the user chooses a location that they previous selected, they are promted to choose again.

![Already selected](documentation/already_selected.png)

- Here, the computer sunk all the users ships so the game is lost.

![Game over](documentation/game_over.png)


## Testing
## Bugs
## Deployment

To deploy this project run

```bash
  npm run deploy
```

## Acknowledgements

 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)
## Credits
## Technologies & Tools Used
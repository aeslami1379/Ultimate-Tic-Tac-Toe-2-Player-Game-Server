# User Manual

To outline the current functionality of our ultimate tic-tac-toe game, we have created a [video](user_manual.mp4) that outlines the basic user interactions of the game.
The video outlines the following:
* Two users register, using a username and password. Both are saved to the database.
* Both users then login, assigning the first user, in this case "frank", as player1 and is assigned to "X". The second user "harold", is assigned as Player 2 which is assigned to "O" in game.
* The game starts and on the first run, both players fill out the board completely, and tie. 
* During this game you can see in the top right corner information on which users turn it is, where they have to play on the subgrid, and the validity of each move.
* The game is then restarted, clearing the board.
* In the second game, both play until finally player 2 - "harold" wins.
* The server is then restarted, where the login functionality for both "harold" and "frank" is shown, as they have been previously saved to the database on the first run.
* They each make a couple of moves and then decide to save the current state of their game, demonstrating the save game functionality, this clears the board.
* The server is then started again, and the two players login as usual.
* This time around they decide to load the game from their second run. The load game page shows a dropdown menu of all gameIDs associated with player 1, in this case for "frank".
* The game is loaded to the board and then the server is terminated using the stop button.

*Disclaimer*: This video shows the implementation of a few features not implemented in our master branch. Both save and load game functionality were implemented after our code pull request deadline. To run the game with the shown functionality, in the terminal run: 'python3 start_game.py' from branch 103 - Ashfaq. This was documented in our [README](../../README.md).
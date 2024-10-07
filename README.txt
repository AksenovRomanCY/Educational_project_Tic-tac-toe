A learning project for practicing Python programming, developed as part of the
Yandex practicum course.

##Documentation
This project is designed to implement a simple Tic-Tac-Toe game.
The main functions of the program allow players to take turns making moves,
draw the game board and figures on the screen, and determine the winner.
The project uses the Board class to manage the game state and Pygame library for visualization.
Results of the game are saved in a text file using the save_result function.

-------------------------------------

##Data Structure
The game board is represented by a class Board.
The board is a 3x3 grid initialized with empty strings (' '), which represents free cells.

Example of data structure:
board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]

-------------------------------------

##Description of Functions
#Main File
1.draw_lines():
-Draws the lines that divide the game board into cells.

2.draw_figures(board):
-Draws the 'X' and 'O' figures on the game board based on the current state.
Parameters:
    -"board": current state of the game board.

3.main():
-The main function to start and run the game.


#Board Class
1.make_move(row, col, player):
-Makes a move by placing the symbol of the current player ('X' or 'O') in the specified cell.
Parameters:
    -"row": row number where the figure will be placed.
    -"col": column number where the figure will be placed.
    -"player": current player symbol ('X' or 'O').

2.is_board_full():
-Checks if the game board is completely filled.
Result:
    -Returns True if all cells are filled, otherwise False.

3.check_win(player):
-Checks if there is a winning combination for the current player.
Parameters:
    -"player": current player symbol ('X' or 'O').
Result:
    -Returns True if the player wins, otherwise False.


#Additional Functions
1.save_result(winner=None):
-Saves the result of the game to the text file results.txt.
Parameters:
    -winner: symbol of the winner ('X' or 'O'). If None, saves "It's a draw."

-------------------------------------

##Game Flow
1.Initialization:
    -The game starts by creating an instance of the Board class and setting the
     current player to 'X'.
2.Drawing the Board:
    -The function draw_lines() is used to create a visual grid of the game board.
3.Game Loop:
  A while running loop:
    -Handles events like mouse clicks.
    -Determines which cell the player clicked.
    -Makes a move if the cell is free using make_move().
    -Checks for a winner with check_win().
    -Checks if the board is full with is_board_full().
    -Saves the result using save_result().
    -Switches the current player and redraws the figures with draw_figures().
4.Ending the Game:
    -The game ends when there is a winner or all cells are filled.

-------------------------------------

##File Structure
1.Main File: Contains the game logic, board rendering, and game loop (main(),
  draw_lines(), draw_figures()).
2.gameparts/parts.py: Defines the Board class, including methods for making
  moves, displaying the board, checking for a winner, and checking if the board is full.
3.gameparts/file_actions.py: Defines the function save_result() to write the
  game result to a text file.
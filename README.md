# AI Tic Tac Toe Game

This project is a simple Tic Tac Toe game implemented in Python using the Tkinter library. In this game, you play against an AI that employs the minimax algorithm to choose its moves, ensuring optimal play.

## Features

- **Interactive GUI:**  
  Built using Tkinter, featuring a start menu and a 3x3 game board.
- **Intelligent AI:**  
  The AI opponent uses the minimax algorithm to decide its moves.
- **Game Outcome Indications:**  
  - Winning line is highlighted in green.
  - Tie game highlights the board in yellow.
- **Multiple Start Options:**  
  Choose whether the player or the AI starts the game.

## How to Run

1. **Prerequisites:**  
   Ensure you have Python 3.6 or higher installed on your system.
2. **Download the Code:**  
   Clone the repository or download the source code files.
3. **Run the Game:**  
   Open a terminal or command prompt in the project directory and run:
   ```bash
   python your_file_name.py
   ```
   Replace `your_file_name.py` with the name of your Python file containing the code.
4. **Gameplay:**  
   - A window will appear with a start menu.
   - Click **Player** or **AI** to choose who should start.
   - Play the game by clicking on the grid.

## Code Overview

- **evaluateTerminal(board):**  
  Checks the board for a win or tie state.

- **minimax(board, isMaximizing):**  
  Implements the minimax algorithm to evaluate and choose the best move.

- **getBoard():**  
  Retrieves the current state of the board from the UI buttons.

- **bestMove():**  
  Determines the best move for the AI and updates the board accordingly.

- **checkWinner():**  
  Checks if there is a winning combination or if the game is a tie. It also updates the button colors to indicate the result.

- **updateAfterMove():**  
  Updates the game status after each move, checks for a win/tie, and toggles the turn.

- **nextTurn(row, column):**  
  Handles the player's move when a cell is clicked.

- **disableButtons():**  
  Disables the board buttons when the game ends.

- **resetGame():**  
  Resets the game to its initial state, allowing for a new game.

- **startGame(starter):**  
  Initializes the game based on whether the player or the AI starts first.

## Global Variables

- **Turn:**  
  A global variable that tracks whose turn it is (0 for Player, 1 for AI).

## Customization

- **Messages:**  
  You can modify the messages displayed in the label to change the tone or feedback to the player.
- **Styling:**  
  Adjust button sizes, colors, and fonts in the code to suit your preferences.

## License

This project is open for educational and personal use. Feel free to modify the code as needed.

---

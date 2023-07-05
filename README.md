# IBM-Ponder-This-July-2023


This repo contains a puzzle game implemented in Python using the Pygame library. This game is based on the board game featured in [IBM's Ponder This July 2023 Challenge](https://research.ibm.com/haifa/ponderthis/challenges/July2023.html).
## Controls
- Use the arrow keys to move the selected block: Up, Down, Left, and Right.
- Press 'r' to reset the game, which will set the blocks to their initial configuration.
- Press 'u' to undo the last move.
- Press 'p' to print the move history.
- Press 'q' to quit the game window and end the script

## Features

  - The game features a 5x5 grid where blocks of different colors are placed.
  - Blocks can be moved in any direction as long as there is enough free space.
  - When a square within a block is selected, the entire block will be selected and move together.
  - The number of steps taken to solve the puzzle and the cost to move the blocks are displayed on the screen.
  - The game supports resetting the puzzle, undoing moves, and printing the move history.

## Execution Steps

- Ensure you have Python installed on your system.
- Install the Pygame library by running the command:  
    ``` 
    pip install pygame
    ```
- Download the 'script.py' file and place it in your desired directory.
- Open a terminal or command prompt and navigate to the directory where the 'script.py' file is located.
- Run the game by executing the following command: 
    ``` 
    python script.py
    ```
- The game window will appear, and you can start playing by following the on-screen instructions and using the controls described above.

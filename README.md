
# Connect4 Game (User vs. PC)
-This Python script implements a classic Connect Four game where the player competes against the computer. The objective of the game is to connect four of your colored discs in a row, column, or diagonal before the opponent does.
- It is developed fully in **Python** and uses **Guizero** for the Graphical User Interface
# How to Play
- Setup: Run the Python script to start the game.

- Gameplay: The player starts by inputting their move, selecting the column where they want to drop their colored disc. The computer then makes its move.

- Win Condition: The game continues until one player (either the user or the computer) connects four of their colored discs in a row, column, or diagonal, or until the grid is full (resulting in a draw).

- Restart: After the game ends, players have the option to restart and play again.

# Features
- User vs. PC Gameplay: Players can compete against the computer, making strategic moves to outsmart the AI.
- Win Detection: The script automatically detects when either the user or the computer has won the game.
- Grid Display: The current state of the game grid is displayed after each move, allowing players to visualize the game progress.

# How it looks

- This is the beggining of the game, where all unused cells are purple.

  ![Connect4 2024-03-21 at 10 59 15](https://github.com/alexiulian/StarCatalogue/assets/115142081/aa81af5a-e083-4eff-b1f3-af6fb55c66af)

- **User** move is **orange** and has write on cell **YYY**, and for the **PC** move the cell is **white** and has **XXX**.
- Below are some cases where the PC knows how to block the opponent moves.

  ![Connect4 2024-03-21 at 11 01 55](https://github.com/alexiulian/StarCatalogue/assets/115142081/427f052f-d779-49d0-a3c8-557194cf36c1)
  ![Connect4 2024-03-21 at 11 02 37](https://github.com/alexiulian/StarCatalogue/assets/115142081/ff46ec72-744b-43f2-b7d4-3547053553c7)
  
- And here we can see that he recognise the situation to **win** and if the next move don't block it, then the PC will know what to do.

  ![Connect4 2024-03-21 at 11 04 36](https://github.com/alexiulian/StarCatalogue/assets/115142081/f98e5882-6c51-4d85-9462-d91089748265)
  
  - And here we are, PC wins and makes the expected move.
    
  ![Connect4 2024-03-21 at 11 04 47](https://github.com/alexiulian/StarCatalogue/assets/115142081/58235875-2546-4348-8bb6-68021a9ae6cd)




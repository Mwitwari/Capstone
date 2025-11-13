🧩 Sudoku Solver (Pygame)

A simple interactive Sudoku Solver built with Python and Pygame.
You can manually enter Sudoku numbers, visualize the board, and solve the puzzle automatically using a backtracking algorithm.

📸 Features

✅ Clean 9x9 Sudoku grid
✅ Interactive number input via keyboard and mouse
✅ Automatic solving using recursion and backtracking
✅ Visual representation of the Sudoku board
✅ Simple and fast execution

🧠 How It Works

This project combines two main components:

1. Pygame Interface

The Sudoku grid is displayed using pygame.draw.line().

You can click on a cell and press a number key (1–9) to fill it.

Press Enter (RETURN) to trigger the solver.

2. Backtracking Algorithm

The function solve(board) uses recursion to try numbers (1–9) in each empty cell.

It checks whether a number is valid in that position using the valid() function:

Checks the row

Checks the column

Checks the 3x3 subgrid

If a number violates Sudoku rules, it backtracks (undoes that number) and tries the next possible one.

When all cells are filled correctly, the puzzle is solved.

🧩 Controls
Action	Key / Mouse
Enter a number	Click a cell, then press 1–9
Solve the puzzle	Press Enter (Return)
Quit	Close the window


# Sudoku Solver, submission from TISVV


<p>
  This sudoku solver can accept sudokus in 2 ways, either from a .csv (comma separated values) file or get it directly from the user via the terminal. <br>
  To input sudoku as a list, enter 1, but to use a csv input 2
</p>

## How to use normal input:

<p>
  Input a 2-D list, of the format: <br>[2,0,0,0,0,0,0,0,8], [7,0,0,0,9,0,0,0,0], [6,0,5,0,3,0,0,0,0], [3,0,0,0,0,0,6,0,0], [0,0,8,4,0,7,9,0,0], [1,0,0,6,8,0,0,0,0], [0,0,3,2,0,0,0,0,1], [0,5,0,0,0,0,0,0,6], [0,0,0,8,0,0,0,4,0]]
  </p>

## How to use the csv:

<p>
  A file named "Sudoku.csv" should already exist in the folder with "Sudoku_Solver.py", and it should have 9 rows & columns, with the sudoku puzzle, where "0" represents empty space.
  <br>
  If user chooses to use the csv file as input, a new file called "Sudoku_Solution.csv" will be created and will be the completely solved sudoku, if any solution is possible for the given puzzle.
</p>

## Modules used

<p> Only the csv module is being used for file handling, the main algorithm for solving sudoku is in pure python </p>

## Introduction:
-	Sudoku is one of the most popular logic-based number-placement puzzle game. The literal meaning of "Su-doku" in Japanese is "the number that is single".

-	The objective is to fill a nine-by-nine (9x9) grid with digits so that each row, column and 3x3 section contain number between 1 and 9, with each number used once and only once in each section. The Sudoku game players are provided with partially filled grid meant to be solved.

-	To solve sudoku one doesn't require the knowledge of mathematics but require the logic and reasoning. Solving Sudoku Puzzles daily helps with your brain. It improves the concentration and logical thinking. One can look for sudoku puzzles given in Newspapers or can play them online provided by many websites. 

## About:

This Script is a Sudoku Solver that solves almost any Sudoku Puzzle by visualizing through the Backtracking Algorithm which is made using the PyGame Library in Python. Ever tried but stucked on Sudoku Puzzles given in newspapers, magazines and online. You can use this script to get its solution instantly and move further.

## Working:

-	Every time this Script is executed, a Random Solvable board is created which is imported from API by [bertoort](https://github.com/bertoort) named as [Sugoku](https://github.com/bertoort/sugoku).
-	Pressing ENTER key will generate new random solvable board.
- Now, the user can first try to attempt solving it by clicking on the cells and entering values manually. If the value is valid it will be added to the board.
-	If the value is valid it will be added to the board else error msg will be displayed.  
-	Values can be removed by left clicking the value and pressing 0 or pressing RESET button.

<p align="center">
	<img src="https://github.com/wajahati/Extras/blob/main/screen%201%2C2.gif">
</p>

-	If at any point the player decides to solve the board SOLVE button can be pressed.
-	This will commence a visual which will demonstrate how the backtracking algorithm works and how it is being applied in order to solve the board.

<p align="center">
	<img src="https://github.com/wajahati/Extras/blob/main/gif%20Video_3.gif">
</p>

## **Algorithm**

**What is backtracking algorithm?**

Backtracking is a general algorithm for finding all (or some) solutions to some computational problems, that incrementally builds candidates to the solutions, and abandons each partial candidate (“backtracks”) as soon as it determines that the candidate cannot possibly be completed to a valid solution.

Starting with an incomplete board:

* Find the first empty space if it exist
* Attempt to place the digits 1-9 in that space
* Check if that digit is valid in the current spot based on the current board
* attempt the board with backtrack
  + If the digit is valid, recursively attempt to fill the board using steps 1-3.
  + If it is not valid, reset the square you just filled and go back to the previous step.
* Once the board is full by the definition of this algorithm we have found a solution.

## Requirements:
In order to run the Script, the require **Python, PyGame & Requests** which are already included in the repository and you can just clone the repository and you are good to go:

## Execution:
-	Clone this repository using
```
git clone https://github.com/wajahati/AiDoku-Ai-Sudoku-Solver.git
```
**OR**
Zip Download the Repository and Extract it's contents.
-	Now run the [Start_Screen.py](https://github.com/wajahati/AiDoku-Ai-Sudoku-Solver/blob/main/Start_Screen.py) file directly in your Terminal using
```
python Start_Screen.py
```
**OR**
- Simply Run the [Start_Screen.py](https://github.com/wajahati/AiDoku-Ai-Sudoku-Solver/blob/main/Start_Screen.py) using any compiler.

## Contributor:
- This project was a group project with [Muhammad Sameer](#).
<p align='center'><b>Made with ❤ by Wajahati</b></p>

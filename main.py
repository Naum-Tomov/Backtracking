import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


DIM = 9;
sudokuGrid = np.zeros((DIM, DIM), dtype=np.int32);

primer1 = [ [3, 0, 6, 5, 0, 8, 4, 0, 0],
         [5, 2, 0, 0, 0, 0, 0, 0, 0],
         [0, 8, 7, 0, 0, 0, 0, 3, 1],
         [0, 0, 3, 0, 1, 0, 0, 8, 0],
         [9, 0, 0, 8, 6, 3, 0, 0, 5],
         [0, 5, 0, 0, 9, 0, 6, 0, 0],
         [1, 3, 0, 0, 0, 0, 2, 5, 0],
         [0, 0, 0, 0, 0, 0, 0, 7, 4],
         [0, 0, 5, 2, 0, 6, 3, 0, 0] ]


for row in range(len(primer1)):
    for col in range(len(primer1)):
        if primer1[row][col] != 0:
            sudokuGrid[row][col] = primer1[row][col];

print("Our sudoku grid: ")
print(sudokuGrid)



df = pd.DataFrame(sudokuGrid)
#display(df)

w = 5
h = 5
plt.figure(1, figsize=(w, h))
tb = plt.table(cellText=sudokuGrid, loc=(0,0), cellLoc='center')


ax = plt.gca()
ax.set_xticks([])
ax.set_yticks([])
plt.show()


def isValidMove(number, Xcoord, Ycoord):
    global sudokuGrid;
    for col in range(DIM):  # Check row
        if sudokuGrid[Xcoord][col] == number:
            return False;
    for row in range(DIM):  # Check column
        if sudokuGrid[row][Ycoord] == number:
            return False;
    return isNumberInSquare(number, (Xcoord//3)*3, (Ycoord//3)*3)


def isNumberInSquare(number, squareIndex1, squareIndex2):
    global sudokuGrid;
    for X in range(squareIndex1, squareIndex1+2):
        for Y in range(squareIndex2, squareIndex2+2):
            if sudokuGrid[X][Y] == number:
                return False;
    return True;


def solve():
    global sudokuGrid;
    for row in range(DIM):
        for col in range(DIM):
            if sudokuGrid[row][col] == 0:
                for number in range(1,10):
                    if isValidMove(number, row, col):
                        sudokuGrid[row][col] = number;  # try this number
                        solve();  # continue solving with the previous number
                        sudokuGrid[row][col] = 0;  # set the number back to 0 if the solution failed
                return;  # return after you check all numbers
    print(sudokuGrid);


solve();
import numpy as np
import pygame

DIM = 9;
x = 0
y = 0
dif = 500 / 9

screen = pygame.display.set_mode((500, 600))

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

# Load test fonts for future use
font1 = pygame.font.SysFont()


def get_cord(pos):
    global x
    x = pos[0] // dif
    global y
    y = pos[1] // dif


# Highlight the cell selected
def draw_box():
    for i in range(2):
        pygame.draw.line(screen, (255, 0, 0), (x * dif - 3, (y + i) * dif), (x * dif + dif + 3, (y + i) * dif), 7)
        pygame.draw.line(screen, (255, 0, 0), ((x + i) * dif, y * dif), ((x + i) * dif, y * dif + dif), 7)

    # Function to draw required lines for making Sudoku grid


def draw():
    # Draw the lines

    for i in range(9):
        for j in range(9):
            if sudokuGrid[i][j] != 0:
                # Fill blue color in already numbered grid
                pygame.draw.rect(screen, (0, 153, 153), (i * dif, j * dif, dif + 1, dif + 1))

                # Fill gird with default numbers specified
                text1 = font1.render(str(sudokuGrid[i][j]), 1, (0, 0, 0))
                screen.blit(text1, (i * dif + 15, j * dif + 15))
                # Draw lines horizontally and verticallyto form grid
    for i in range(10):
        if i % 3 == 0:
            thick = 7
        else:
            thick = 1
        pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (500, i * dif), thick)
        pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), thick)

    # Fill value entered in cell


def draw_val(val):
    text1 = font1.render(str(val), 1, (0, 0, 0))
    screen.blit(text1, (x * dif + 15, y * dif + 15))


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


def solve(X, Y):
    while sudokuGrid[X][Y] != 0:  # not empty
        if X < 8:  # going throw row
            X += 1
        elif X == 8 and Y < 8:  # finished row
            X = 0
            Y += 1
        elif X == 8 and Y == 8:  # solved sudoku
            return True
    pygame.event.pump()
    for number in range(1, 10):
        if isValidMove(number, X, Y):
            sudokuGrid[X][Y] = number  # set that number
            global x, y
            x = X
            y = Y
            # white color background\
            screen.fill((255, 255, 255))
            draw()
            draw_box()
            pygame.display.update()
            pygame.time.delay(20)
            if solve(sudokuGrid, X, Y) == 1:
                return True
            else:
                sudokuGrid[X][Y] = 0
            # white color background\
            screen.fill((255, 255, 255))
            draw()
            draw_box()
            pygame.display.update()
            pygame.time.delay(50)
    return False

run = True
while run:
    screen.fill((255, 255, 255)) ;
    solve(0, 0);
    pygame.display.update();
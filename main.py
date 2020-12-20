# import pygame library 
import pygame
import numpy as np

# initialise the pygame font 
pygame.font.init()

# Total window 
screen = pygame.display.set_mode((500, 600))

# Title and Icon  
pygame.display.set_caption("SUDOKU SOLVER USING BACKTRACKING")
DIM = 9
x = 0
y = 0
dif = 500 / 9
val = 0
# Default Sudoku Board.
sudokuGrid = np.zeros((9, 9))


def reset():
    global sudokuGrid
    sudokuGrid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
                  [5, 2, 0, 0, 0, 0, 0, 0, 0],
                  [0, 8, 7, 0, 0, 0, 0, 3, 1],
                  [0, 0, 3, 0, 1, 0, 0, 8, 0],
                  [9, 0, 0, 8, 6, 3, 0, 0, 5],
                  [0, 5, 0, 0, 9, 0, 6, 0, 0],
                  [1, 3, 0, 0, 0, 0, 2, 5, 0],
                  [0, 0, 0, 0, 0, 0, 0, 7, 4],
                  [0, 0, 5, 2, 0, 6, 3, 0, 0]]


# Load test fonts for future use
font1 = pygame.font.SysFont("times new roman", 35)
font2 = pygame.font.SysFont("times new roman", 15)


# Highlight the cell selected
def draw_box(x, y):
    for i in range(2):
        pygame.draw.line(screen, (239, 92, 157), (x * dif - 3, (y + i) * dif), (x * dif + dif + 3, (y + i) * dif), 7)
        pygame.draw.line(screen, (239, 92, 157), ((x + i) * dif, y * dif), ((x + i) * dif, y * dif + dif), 7)


# Function to draw the sudoku grid
def draw():
    global sudokuGrid
    # Draw the lines 

    for i in range(9):
        for j in range(9):
            if sudokuGrid[j][i] != 0:
                # Fill blue color in already numbered grid
                pygame.draw.rect(screen, (124, 193, 239), (i * dif, j * dif, dif + 1, dif + 1))

                # Fill gird with default numbers specified 
                text1 = font1.render(str(sudokuGrid[j][i]), 1, (0, 0, 0))
                screen.blit(text1, (i * dif + 20, j * dif + 9))
                # Draw lines horizontally and vertically to form grid
    for i in range(10):
        if i % 3 == 0:
            thick = 5
        else:
            thick = 2
        pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (500, i * dif), thick)
        pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), thick)




# Check if the value entered in board is valid
def isValidMove(number, Xcoord, Ycoord):
    global sudokuGrid;
    for col in range(DIM):  # Check row
        if sudokuGrid[Xcoord][col] == number:
            return False;
    for row in range(DIM):  # Check column
        if sudokuGrid[row][Ycoord] == number:
            return False;
    return isNumberInSquare(number, (Xcoord // 3) * 3, (Ycoord // 3) * 3)


def isNumberInSquare(number, squareIndex1, squareIndex2):
    global sudokuGrid;
    for X in range(squareIndex1, squareIndex1 + 3):
        for Y in range(squareIndex2, squareIndex2 + 3):
            if sudokuGrid[X][Y] == number:
                return False;
    return True;


# Solves the sudoku board using Backtracking Algorithm
def solve(X, Y, Slow=False):
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
            # white color background
            screen.fill((255, 255, 255))
            draw()
            draw_box(Y, X)
            pygame.display.update()
            if Slow:
                pygame.time.delay(65)
            else:
                pygame.time.delay(10)
            if solve(X, Y, Slow) == 1:
                return True
            else:
                sudokuGrid[X][Y] = 0  # if we failed to solve it
            # white color background
            screen.fill((255, 255, 255))
            draw()
            draw_box(Y, X)
            pygame.display.update()
            if Slow:
                pygame.time.delay(100)
            else:
                pygame.time.delay(30)
    return False


# Display instruction for the game
def instruction():
    text = font2.render("Press enter to visualize, S for slow visualization or D to reset", 1, (0, 0, 0))
    screen.blit(text, (20, 540))


run = True
reset();
# The loop thats keep the window running 
while run:

    # White color background 
    screen.fill((255, 255, 255))
    # Loop through the events stored in event.get() 
    for event in pygame.event.get():
        # Quit the game window 
        if event.type == pygame.QUIT:
            run = False
            # Get the mouse postion to insert number
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                solve(0, 0);
            if event.key == pygame.K_d:
                reset();
            if event.key == pygame.K_s:
                solve(0, 0, Slow=True);

    draw()
    instruction()

    # Update window 
    pygame.display.update()

# Quit pygame window     
pygame.quit()

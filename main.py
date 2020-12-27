# Sudoku project
# written by Kambham Satwik
# Github: https://github.com/code-explorer

from copy import deepcopy
from random import randint
from time import time

board = [[[0, 7, 0, 0, 0, 0, 0, 0, 9],
          [5, 1, 0, 4, 2, 0, 6, 0, 0],
          [0, 8, 0, 3, 0, 0, 7, 0, 0],
          [0, 0, 8, 0, 0, 1, 3, 7, 0],
          [0, 2, 3, 0, 8, 0, 0, 4, 0],
          [4, 0, 0, 9, 0, 0, 1, 0, 0],
          [9, 6, 2, 8, 0, 0, 0, 3, 0],
          [0, 0, 0, 0, 1, 0, 4, 0, 0],
          [7, 0, 0, 2, 0, 3, 0, 9, 6]],

         [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]],

         [[0, 0, 0, 0, 0, 0, 2, 0, 0],
          [0, 8, 0, 0, 0, 7, 0, 9, 0],
          [6, 0, 2, 0, 0, 0, 5, 0, 0],
          [0, 7, 0, 0, 6, 0, 0, 0, 0],
          [0, 0, 0, 9, 0, 1, 0, 0, 0],
          [0, 0, 0, 0, 2, 0, 0, 4, 0],
          [0, 0, 5, 0, 0, 0, 6, 0, 3],
          [0, 9, 0, 4, 0, 0, 0, 7, 0],
          [0, 0, 6, 0, 0, 0, 0, 0, 0]]]


# fancy printing
def fancy(matrix):
    print("┌───────────┬───────────┬───────────┐")
    for i in range(3):
        print("│  %d  %d  %d  │  %d  %d  %d  │  %d  %d  %d  │" % (
            matrix[i][0], matrix[i][1], matrix[i][2], matrix[i][3], matrix[i][4], matrix[i][5], matrix[i][6],
            matrix[i][7],
            matrix[i][8]))
    print("├───────────┼───────────┼───────────┤")
    for i in range(3, 6):
        print("│  %d  %d  %d  │  %d  %d  %d  │  %d  %d  %d  │" % (
            matrix[i][0], matrix[i][1], matrix[i][2], matrix[i][3], matrix[i][4], matrix[i][5], matrix[i][6],
            matrix[i][7],
            matrix[i][8]))
    print("├───────────┼───────────┼───────────┤")
    for i in range(6, 9):
        print("│  %d  %d  %d  │  %d  %d  %d  │  %d  %d  %d  │" % (
            matrix[i][0], matrix[i][1], matrix[i][2], matrix[i][3], matrix[i][4], matrix[i][5], matrix[i][6],
            matrix[i][7],
            matrix[i][8]))
    print("└───────────┴───────────┴───────────┘")


# checking if the number is valid in the given position
def valid(p, m, k, l):
    # checking if there are any duplicates in row/column/grid
    p[k][l] = m
    validity = True
    # row
    for b in range(9):
        for x in range(1, 10):
            count = 0
            for a in range(9):
                if p[b][a] == x:
                    count += 1
            if count > 1:
                validity = False
    # column
    for b in range(9):
        for x in range(1, 10):
            count = 0
            for a in range(9):
                if p[a][b] == x:
                    count += 1
            if count > 1:
                validity = False
    # grid
    for n in range(1, 10):
        for a in range(3):
            for b in range(3):
                count = 0
                for x in range(3):
                    for y in range(3):
                        if p[x + (3 * a)][y + (3 * b)] == n:
                            count += 1
                        if count > 1:
                            validity = False

    return validity


# is coordinate empty or not
def is_empty(x, y, p):
    if p[x][y] == 0:
        return True
    else:
        return False


# finding if game has ended
def game_end(p):
    for x in range(9):
        for y in range(9):
            if p[x][y] == 0:
                return False  # row, column

    return True


# input checker
def input_checker(p):
    coordinates = input("For example '3 4'.\n")
    if len(coordinates) == 3 and coordinates[1] == ' ':
        x = int(coordinates[0]) - 1
        y = int(coordinates[2]) - 1
        if is_empty(x, y, board[nx]):
            print("Enter the number you want to place there (between 1 and 9):")
            number_checker(p, x, y)
        else:
            print("The coordinate is occupied by", p[x][y], "try again.")
            input_checker(p)
    else:
        print(
            "The coordinates you entered are in the wrong format. Please ensure that it is of the format 'x y'.")
        # retake input
        input_checker(p)


# number checker
def number_checker(p, x, y):
    n = int(input())
    if n in range(1, 10):
        if valid(p, n, x, y):
            print("Placed", n, "at", x + 1, ",", y + 1)
            player[x][y] = n
        else:
            print("The number is not possible there please try a different number.")
            number_checker(p, x, y)
    else:
        print("Please enter a number between 1 to 9.")
        number_checker(p, x, y)


# Main menu
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("│       Welcome to Sudoku      │")
print("│   Written by Kambham Satwik  │")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
seconds_i = time()
print("Press q to quit")
a = input("Press enter to start\n")
if a == 'q':
    print("Thanks for playing")
    exit()
# Game start
nx = randint(0, 2)
player = deepcopy(board[nx])
print("The game has started")
fancy(player)

# looping until game ends
while not game_end(player):
    # checking input
    print("Enter the coordinates in the format 'x y'.")
    input_checker(player)
    fancy(player)

# game end
print("Congratulations you have completed the sudoku.")

# calculating time taken
seconds_f = time()
print("Time:", seconds_f - seconds_i, "seconds")

import numpy as np
import pandas as pd

#sick arrays
boardLen = 8
board = np.array([[[0]*2]*boardLen]*boardLen)

## Colors ##
black = 'B'     #66
white = 'W'     #87

## Figures ##
pawn = 'p'      #112
rook = 'r'      #114    
knight = 'k'    #107
bishop = 'b'    #98
queen = 'q'     #113
king = 'K'      #75

## fill Board ##
for i in range(8):
    board[1,i] = np.array([ord(black), ord(pawn)])                          #black pawns
    board[6,i] = np.array([ord(white), ord(pawn)])                          #white pawns

for i in range(2):
    color = black if i == 0 else white
    line = 0 if i == 0 else 7
    board[line,0] = board[line,7] = np.array([ord(color), ord(rook)])       #rook
    board[line,1] = board[line,6] = np.array([ord(color), ord(knight)])     #knight
    board[line,2] = board[line,5] = np.array([ord(color), ord(bishop)])     #bishop
    board[line,3] = np.array([ord(color), ord(queen)])                      #queen
    board[line,4] = np.array([ord(color), ord(king)])                       #king


## helper functions ##
def printBoard(board):
    row = ""
    for a in range(boardLen):
        for b in range(boardLen):
            row += (chr(board[a,b][0]) if board[a,b][0] != 0 else '🬀') + (chr(board[a,b][1]) if board[a,b][1] != 0 else '🬀') + ' '
        row += '\n'
    print(row)
    
printBoard(board)
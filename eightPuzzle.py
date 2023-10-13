# eightPuzzle.py

import copy

class eightPuzzle:

    def __init__(self, grid: list):
        self.grid = grid
        self.emptySpace = self.findEmptySpace()
        
    def findEmptySpace(self) -> tuple:
        for i in range(3):
            for j in range(3):
                if self.grid[i][j] == 0:
                    return (i,j)
        return (0,0)
    
    def solved(self) -> bool:
        return self.grid == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    def up(self) -> None:
        if(self.validMove('up')): # If the empty space is not in the first row
            self.grid[self.emptySpace[0]][self.emptySpace[1]] = self.grid[self.emptySpace[0] - 1][self.emptySpace[1]]
            self.grid[self.emptySpace[0] - 1][self.emptySpace[1]] = 0
            self.emptySpace = (self.emptySpace[0] - 1, self.emptySpace[1])
        else:
            print("Can't move up")
            
    def down(self) -> None:
        if(self.validMove('down')): # If the empty space is not in the last row
            self.grid[self.emptySpace[0]][self.emptySpace[1]] = self.grid[self.emptySpace[0] + 1][self.emptySpace[1]]
            self.grid[self.emptySpace[0] + 1][self.emptySpace[1]] = 0
            self.emptySpace = (self.emptySpace[0] + 1, self.emptySpace[1])
        else:
            print("Can't move down")
            
    def left(self) -> None:
        if(self.validMove('left')): # If the empty space is not in the first column
            self.grid[self.emptySpace[0]][self.emptySpace[1]] = self.grid[self.emptySpace[0]][self.emptySpace[1] - 1]
            self.grid[self.emptySpace[0]][self.emptySpace[1] - 1] = 0
            self.emptySpace = (self.emptySpace[0], self.emptySpace[1] - 1)
        else:
            print("Can't move left")
            
    def right(self) -> None:
        if(self.validMove('right')): # If the empty space is not in the last column
            self.grid[self.emptySpace[0]][self.emptySpace[1]] = self.grid[self.emptySpace[0]][self.emptySpace[1] + 1]
            self.grid[self.emptySpace[0]][self.emptySpace[1] + 1] = 0
            self.emptySpace = (self.emptySpace[0], self.emptySpace[1] + 1)
        else:
            print("Can't move right")
            
    def move(self, direction) -> None:
        if direction == 'up':
            self.up()
        elif direction == 'down':
            self.down()
        elif direction == 'left':
            self.left()
        elif direction == 'right':
            self.right()
            
    def validMove(self, move) -> bool:
        if move == 'up':
            return self.emptySpace[0] > 0
        elif move == 'down':
            return self.emptySpace[0] < 2
        elif move == 'left':
            return self.emptySpace[1] > 0
        elif move == 'right':
            return self.emptySpace[1] < 2
        
    def validMoves(self) -> list:
        possibleActions = ['up', 'down', 'left', 'right']
        valid = []
        for action in possibleActions:
            if self.validMove(action):
                valid.append(action)
        return valid
        
    def printGrid(self) -> None:
        for i in range(3):
            for j in range(3):
                if self.grid[i][j] == 0:
                    print('  ', end='')
                else:
                    print(self.grid[i][j], end=' ')
            print('\b')
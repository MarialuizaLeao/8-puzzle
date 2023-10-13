import numpy as np
import copy

from eightPuzzle import eightPuzzle
from bfs import breadthFirstSearch
from ids import iterativeDeepeningSearch
from ucs import uniformCostSearch
from aStar import aStar
from gready import gready
from hillClimbing import hillClimbing

solution = []

def parseAlgorithm(algorithm: str) -> list:
    if algorithm == 'B':
        return breadthFirstSearch(puzzle)
    elif algorithm == 'I':
        return iterativeDeepeningSearch(puzzle)
    elif algorithm == 'U':
        return uniformCostSearch(puzzle)
    elif algorithm == 'A':
        return aStar(puzzle)
    elif algorithm == 'G':
        return gready(puzzle)
    elif algorithm == 'H':
        return hillClimbing(puzzle)

def printSolution(solution: list) -> None:
    if printSteps:
        print(len(solution)) 
        print()
        puzzle.printGrid()
        for i in range(len(solution)):
            print()
            puzzle.move(solution[i])
            puzzle.printGrid()
    else:
        for i in range(len(solution)):
            puzzle.move(solution[i])
        puzzle.printGrid()

input = input().split()
algorithm = ""
board = []
printSteps = False

if (len(input) != 11 and len(input) != 12) or input[0] != "TP1" or input[1] not in ["B", "I", "U", "A", "G", "H"] or (len(input) == 12 and input[-1] != "PRINT") or (len(input) == 11 and input[-1] == "PRINT"):
    print("Invalid input")
    exit()
numbers = {"0", "1", "2", "3", "4", "5", "6", "7", "8"}
for i in range(2, 11): 
    if input[i] not in numbers: 
        print("Invalid puzzle"); 
        exit()
    else:
        numbers.remove(input[i])
        
algorithm = input[1]
if input[-1] == "PRINT":
    board = input[2:-1]
    printSteps = True
else: board = input[2:]


puzzleGrid = np.zeros((3, 3), dtype=int)

for i in range(3):
    for j in range(3):
        puzzleGrid[i][j] = int(board[i * 3 + j])
        
puzzle = eightPuzzle(puzzleGrid)
solution = parseAlgorithm(algorithm)
if solution == ["failure"]:
    print("No solution found")
else: printSolution(solution)
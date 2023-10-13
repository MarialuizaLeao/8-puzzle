# heuristics.py

import heapq
import copy

from eightPuzzle import eightPuzzle

def manhattanDistance(grid: list) -> int:
    right = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    sum = 0
    for i in range(3):
        for j in range(3):
            sum += abs(grid[i][j] % right[i][j] - grid[i][j] // right[i][j])
    return  sum

def misplacedTiles(grid: list) -> int:
    right = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    sum = 0
    for i in range(3):
        for j in range(3):
            if grid[i][j] != right[i][j] and grid[i][j] != 0: sum += 1
    return sum
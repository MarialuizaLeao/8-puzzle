# heuristics.py

import heapq
import copy

from eightPuzzle import eightPuzzle

def manhattanDistance(grid: list) -> int:
    sum = 0
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 0: continue
            x = (grid[i][j] - 1) // 3
            y = (grid[i][j] - 1) % 3
            sum += abs(x - i) + abs(y - j)
    return sum

def misplacedTiles(grid: list) -> int:
    right = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    sum = 0
    for i in range(3):
        for j in range(3):
            if grid[i][j] != right[i][j] and grid[i][j] != 0: sum += 1
    return sum
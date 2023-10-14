# heuristics.py

import heapq
import copy

from eightPuzzle import eightPuzzle

def manhatan_distance(tile, state1, state2):
    
    iT = 0
    jT = 0
    for i in range(3):
        for j in range(3):
            if state1[i][j] == tile:
                iT = i * 3 + j
            if state2[i][j] == tile:
                jT = i * 3 + j
    gs = 3
    
    row_i, col_i = iT // gs, iT % gs
    row_j, col_j = jT // gs, jT % gs
    
    return abs(row_i - row_j) + abs(col_i - col_j)

def manhattanDistance(grid: list) -> int:
    right = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    return sum([manhatan_distance(tile, grid, right)
                for tile in range(1, 9)])

def misplacedTiles(grid: list) -> int:
    right = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    sum = 0
    for i in range(3):
        for j in range(3):
            if grid[i][j] != right[i][j] and grid[i][j] != 0: sum += 1
    return sum
# heuristics.py

import numpy as np
import heapq
import copy

from eightPuzzle import eightPuzzle

def manhattanDistance(grid: np.array) -> int:
    right = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])       
    return  np.sum(abs(grid % right - grid // right))

def misplacedTiles(grid: np.array) -> int:
    right = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    return 0 if (np.sum(np.sum((y == False for y in (grid == right)))) - 1) < 0 else np.sum(np.sum((y == False for y in (grid == right)))) - 1
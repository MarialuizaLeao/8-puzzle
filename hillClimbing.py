# hillClimbing.py

import numpy as np
import heapq
import copy

from eightPuzzle import eightPuzzle
from heuristics import manhattanDistance, misplacedTiles
from node import Node

def func(x,y): return manhattanDistance(x)

def hillClimbing(puzzle: eightPuzzle) -> list:
    root = Node(puzzle.grid, func)
    k = 100
    current = root
    while True:
        neighbor = []
        heapq.heapify(neighbor)
        for child in current.nodeChildren():
            heapq.heappush(neighbor, child)
        bestNeighbor = heapq.heappop(neighbor)
        if bestNeighbor > current: 
            if current.puzzle.solved(): return current.solution
            else: return ["failure"]
        elif bestNeighbor == current: k -= 1
        elif bestNeighbor < current: k = 5
        if k == 0:
            if current.puzzle.solved(): return current.solution
            else: return ["failure"]
        current = bestNeighbor
# gready.py

import heapq
import copy

from eightPuzzle import eightPuzzle
from heuristics import manhattanDistance, misplacedTiles
from node import Node

def func1(grid: list, realCost: int) -> int:
    return manhattanDistance(grid)

def func2(grid: list, realCost: int) -> int:
    return misplacedTiles(grid)
        
def gready(puzzle: eightPuzzle) -> list:
    frontier = []
    heapq.heapify(frontier)
    root = Node(puzzle.grid, func1)
    heapq.heappush(frontier, root)
    parent = dict()
    while len(frontier) != 0:
        current = heapq.heappop(frontier)
        if current.puzzle.solved(): return current.solution
        for child in current.nodeChildren():
            if child not in parent:
                parent[child] = current
                heapq.heappush(frontier, child)
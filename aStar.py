# aStar.py

import heapq
import copy

from eightPuzzle import eightPuzzle
from heuristics import manhattanDistance, misplacedTiles
from node import Node

def func1(grid: list, realCost: int) -> int:
    return realCost + manhattanDistance(grid)

def func2(grid: list, realCost: int) -> int:
    return realCost + misplacedTiles(grid)

        
def aStar(puzzle: eightPuzzle) -> (list, list):
    root = Node(puzzle.grid, func1)
    open = []
    heapq.heapify(open)
    heapq.heappush(open, root)
    closed = set()
    parent = dict()
    while open:
        current = heapq.heappop(open)
        if current.puzzle.solved(): return current.solution
        closed.add(current)
        for child in current.nodeChildren():
            if child not in parent:
                parent[child] = current
                heapq.heappush(open, child)
            elif len(current.solution) < len(parent[child].solution):
                parent[child] = current
                heapq.heappush(open, child)
    return ["failure"]
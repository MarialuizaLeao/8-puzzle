# aStar.py

import heapq
import copy

from eightPuzzle import eightPuzzle
from heuristics import manhattanDistance, misplacedTiles
from node import Node

def costCalcManhattanDistance(grid: list, realCost: int) -> int:
    return realCost + manhattanDistance(grid)

def costCalcMisplacedTiles(grid: list, realCost: int) -> int:
    return realCost + misplacedTiles(grid)

        
def aStar(puzzle: eightPuzzle) -> list:
    root = Node(puzzle.grid)
    open = []
    heapq.heapify(open)
    heapq.heappush(open, root)
    closed = set()
    parent = dict()
    
    while len(open) != 0:
        current = heapq.heappop(open)
        if current.puzzle.solved(): return current.solution
        closed.append(current)
        for child in current.nodeChildren():
            if parent.get(str(child.puzzle.grid)) == None:
                parent[child] = current
                heapq.heappush(open, child)
            elif len(child.solution) < len(parent[str(child.puzzle.grid)]):
                parent[str(child.puzzle.grid)] = current
                open.remove(child)
                heapq.heappush(open, child)
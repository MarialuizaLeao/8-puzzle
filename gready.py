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
        
def gready(puzzle: eightPuzzle) -> (list, list):
    frontier = []
    heapq.heapify(frontier)
    root = Node(puzzle.grid, func1)
    heapq.heappush(frontier, root)
    parent = dict()
    history = []
    i = 0
    while frontier:
        current = heapq.heappop(frontier)
        history.append((misplacedTiles(current.puzzle.grid), i))
        i+=1
        if current.puzzle.solved(): return current.solution, history
        for child in current.nodeChildren():
            if child not in parent:
                parent[child] = current
                heapq.heappush(frontier, child)
    return ["failure"], history
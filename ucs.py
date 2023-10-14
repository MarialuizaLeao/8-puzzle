# ucs.py

import heapq
import copy

from eightPuzzle import eightPuzzle
from node import Node
from heuristics import manhattanDistance, misplacedTiles

def costCalc(grid: list, realCost: int) -> int:
    return realCost
    

def uniformCostSearch(puzzle: eightPuzzle) -> (list, list):
    root = Node(puzzle.grid, costCalc)
    frontier = []
    heapq.heapify(frontier)
    heapq.heappush(frontier, root)
    parent = dict()
    history = []
    i = 0
    while frontier:
        node = heapq.heappop(frontier)
        history.append((misplacedTiles(node.puzzle.grid), i))
        i+=1
        if node.puzzle.solved(): return node.solution, history
        for child in node.nodeChildren():
            if child not in parent or (child in parent and parent[child] > node):
                parent[child] = node
                heapq.heappush(frontier, child)
    return ["failure"], history
            
    
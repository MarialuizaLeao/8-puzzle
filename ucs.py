# ucs.py

import heapq
import copy

from eightPuzzle import eightPuzzle
from node import Node

def costCalc(grid: list, realCost: int) -> int:
    return realCost
    

def uniformCostSearch(puzzle: eightPuzzle) -> list:
    root = Node(puzzle.grid, costCalc)
    frontier = []
    heapq.heapify(frontier)
    heapq.heappush(frontier, root)
    parent = dict()
    while frontier:
        node = heapq.heappop(frontier)
        if node.puzzle.solved(): return node.solution
        for child in node.nodeChildren():
            if child not in parent or (child in parent and parent[child] > node):
                parent[child] = node
                heapq.heappush(frontier, child)
    return ["failure"]
            
    
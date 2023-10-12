# ucs.py

import numpy as np
import heapq
import copy

from eightPuzzle import eightPuzzle
from dataclasses import dataclass, field
from typing import Any

class Node:
        
        def __init__(self, grid: np.array, cost = 0):
            self.puzzle = eightPuzzle(grid)
            self.solution = list()
            self.cost = cost
            
            
        def __hash__(self): return hash(id(self))
        
        def __lt__(self, other): return self.cost < other.cost
        
        def __le__(self, other): return self.cost <= other.cost
        
        def __gt__(self, other): return self.cost > other.cost
        
        def __ge__(self, other): return self.cost >= other.cost
        
        def __ne__(self, other): return not (np.array_equal(self.puzzle.grid, other.puzzle.grid))
            
        def __eq__(self, other): return (np.array_equal(self.puzzle.grid, other.puzzle.grid))
        
        def __str__(self): return str(self.puzzle.grid)
        
        def __repr__(self): return str(self.puzzle.grid)

def uniformCostSearch(puzzle: eightPuzzle) -> list:
    root = Node(puzzle.grid, 0)
    frontier = []
    heapq.heapify(frontier)
    heapq.heappush(frontier, root)
    explored = []
    while(True):
        if(len(frontier) == 0): return ["failure"]
        node = heapq.heappop(frontier)
        if node.puzzle.solved(): return node.solution
        explored.append(node)
        actions = node.puzzle.validMoves()
        for action in actions:
            child = copy.deepcopy(node)
            child.puzzle.move(action)
            child.cost += 1
            child.solution.append(action)
            if(child not in explored and child not in frontier):
                heapq.heappush(frontier, child)
            elif(child in frontier):
                for i in range(len(frontier)):
                    if(frontier[i] == child and frontier[i] > child):
                        frontier[i] = child
                        heapq.heapify(frontier)
                        break
            
    
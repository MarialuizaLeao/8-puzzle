# aStar.py

import numpy as np
import heapq
import copy

from eightPuzzle import eightPuzzle
from heuristics import manhattanDistance, misplacedTiles

class Node:
        
        def __init__(self, grid: np.array, parent = None):
            self.puzzle = eightPuzzle(grid)
            self.solution = list()
            self.hNode = manhattanDistance(self.puzzle.grid)
            self.gNode = len(self.solution)
            self.fNode = self.gNode + self.hNode
            self.parent = parent
            
        def __hash__(self): return hash(id(self))
        
        def __lt__(self, other): return self.fNode < other.fNode
        
        def __le__(self, other): return self.fNode <= other.fNode
        
        def __gt__(self, other): return self.fNode > other.fNode
        
        def __ge__(self, other): return self.fNode >= other.fNode
        
        def __ne__(self, other): return not (np.array_equal(self.puzzle.grid, other.puzzle.grid))
            
        def __eq__(self, other): return (np.array_equal(self.puzzle.grid, other.puzzle.grid))
        
        def __str__(self): return str(self.puzzle.grid)
        
        def __repr__(self): return str(self.puzzle.grid)
        
def aStar(puzzle: eightPuzzle) -> list:
    root = Node(puzzle.grid)
    open = []
    heapq.heapify(open)
    heapq.heappush(open, root)
    closed = []
    parent = dict()
    
    while len(open) != 0:
        current = heapq.heappop(open)
        
        if current.puzzle.solved(): return current.solution
        closed.append(current)
        actions = current.puzzle.validMoves()
        for action in actions:
            child = copy.deepcopy(current)
            child.puzzle.move(action)
            child.solution.append(action)
            if child not in open:
                child.gNode = current.gNode + 1 # g(n)
                child.hNode = manhattanDistance(child.puzzle.grid) # h(n)
                child.fNode = child.gNode + child.hNode # f(n)
                parent[str(child.puzzle.grid)] = current
                heapq.heappush(open, child)
            elif current.gNode + 1 < parent[str(child.puzzle.grid)].gNode:
                parent[str(child.puzzle.grid)] = current
                heapq.heappush(open, child)
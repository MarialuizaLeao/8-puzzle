# hillClimbing.py

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

def hillClimbing(puzzle: eightPuzzle) -> list:
    root = Node(puzzle.grid)
    open = []
    heapq.heapify(open)
    parent = dict()
    closed = []
    current = root
    
    actions = root.puzzle.validMoves()
    for action in actions:
            child = copy.deepcopy(root)
            child.puzzle.move(action)
            child.solution.append(action)
            child.gNode = root.gNode + 1 # g(n)
            child.hNode = manhattanDistance(child.puzzle.grid) # h(n)
            child.fNode = child.gNode + child.hNode # f(n)
            heapq.heappush(open, child)
            parent[str(child.puzzle.grid)] = root
            
    while len(open) != 0:
        if open[0] < current:
            closed.append(current)
            current = heapq.heappop(open)
        elif current == open[0]:
            #escolher aleatoriamente um nó de open MOVIMENTO LATERAL???
        elif
        if current.puzzle.solved(): return current.solution
        else:
            actions = current.puzzle.validMoves()
            for action in actions:
                child = copy.deepcopy(current)
                child.puzzle.move(action)
                child.solution.append(action)
                child.gNode = current.gNode + 1
                child.hNode = manhattanDistance(child.puzzle.grid)
                child.fNode = child.gNode + child.hNode
                if child not in open and child not in closed:
                    parent[str(child.puzzle.grid)] = current
                    heapq.heappush(open, child)
                else:
                    if child in open and child.fNode < parent[str(child.puzzle.grid)].fNode:
                        parent[str(child.puzzle.grid)] = current
                        heapq.heappush(open, child)
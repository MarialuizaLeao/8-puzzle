# node.py

import heapq
import copy

from eightPuzzle import eightPuzzle
from heuristics import manhattanDistance, misplacedTiles

class Node:
        
        def __init__(self, grid: list, costFunction):
            self.puzzle = eightPuzzle(grid)
            self.solution = list()
            self.costFunction = costFunction
            self.cost = self.costFunction(self.puzzle.grid, len(self.solution))
            
        def nodeChildren(self):
            actions = self.puzzle.validMoves()
            children = []
            for action in actions:
                child = copy.deepcopy(self)
                child.puzzle.move(action)
                child.solution.append(action)
                child.reCalcCost()
                children.append(child)
            return children
        
        def reCalcCost(self):
            self.cost = self.costFunction(self.puzzle.grid, len(self.solution))
            
        def __hash__(self): return hash(str(self.puzzle.grid))
        
        def __lt__(self, other): return self.cost < other.cost
        
        def __le__(self, other): return self.cost <= other.cost
        
        def __gt__(self, other): return self.cost > other.cost
        
        def __ge__(self, other): return self.cost >= other.cost
        
        def __ne__(self, other): return not self.puzzle.grid == other.puzzle.grid
            
        def __eq__(self, other): return self.puzzle.grid == other.puzzle.grid
        
        def __str__(self): return str(self.puzzle.grid)
        
        def __repr__(self): return str(self.puzzle.grid)
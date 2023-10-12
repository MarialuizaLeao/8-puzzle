# ids.py

import numpy as np
import copy

from eightPuzzle import eightPuzzle

class Node:
        
        def __init__(self, grid: np.array, depth = 0, parent = None):
            self.puzzle = eightPuzzle(grid)
            self.solution = list()
            self.depth = depth
            self.parent = parent
            
        def __hash__(self): return hash(id(self))
        
        def __ne__(self, other): return not np.array_equal(self.puzzle.grid, other.puzzle.grid)
            
        def __eq__(self, other): return np.array_equal(self.puzzle.grid, other.puzzle.grid)
        
        def __str__(self): return str(self.puzzle.grid)
        
        def __repr__(self): return str(self.puzzle.grid)
                
def isCycle(node: Node) -> bool:
        while node.parent is not None:
            if node == node.parent:
                return True
            node = node.parent
        return False
                
def depthLimitedSearch(puzzle: eightPuzzle, limit: int) -> list:
    root = Node(puzzle.grid, parent = None, depth = 0) # Create the root node    
    frontier = []
    frontier.append(root)
    while(len(frontier) != 0):
        node = frontier.pop(0)
        if(node.puzzle.solved()): return node.solution
        if(node.depth > limit): return ["cutoff"]
        elif not isCycle(node):
            actions = node.puzzle.validMoves()
            for action in actions:
                child = copy.deepcopy(node)
                child.parent = copy.deepcopy(node)
                child.puzzle.move(action)
                child.solution.append(action)
                child.depth += 1
                frontier.append(child)
                
    return ["failure"]
            
def iterativeDeepeningSearch(puzzle: eightPuzzle) -> list:
    i = 0
    while(True):
        i += 1
        solution = depthLimitedSearch(puzzle, i)
        if(solution != ['cutoff']):
            return solution
# bfs.py

import numpy as np
import copy

from eightPuzzle import eightPuzzle

class Node:
        
        def __init__(self, grid: np.array):
            self.puzzle = eightPuzzle(grid)
            self.solution = list()
            
        def __hash__(self): return hash(id(self))
        
        def __ne__(self, other): return not np.array_equal(self.puzzle.grid, other.puzzle.grid)
            
        def __eq__(self, other): return np.array_equal(self.puzzle.grid, other.puzzle.grid)
        
        def __str__(self): return str(self.puzzle.grid)
        
        def __repr__(self): return str(self.puzzle.grid)

def breadthFirstSearch(puzzle: eightPuzzle) -> list:
    root = Node(puzzle.grid) # Create the root node
    if root.puzzle.solved(): return root.solution
    frontier = []
    explored = []
    frontier.append(root)
    while(True):
        if(len(frontier) == 0):
            return []
        node = frontier.pop(0)
        explored.append(node)
        actions = node.puzzle.validMoves()
        for action in actions:
            child = copy.deepcopy(node)
            child.puzzle.move(action)
            child.solution.append(action)
            if(child not in explored and child not in frontier):
                if(child.puzzle.solved()):
                    return child.solution
                frontier.append(child)
# ids.py

import numpy as np
import copy

from eightPuzzle import eightPuzzle
from node import Node

def func(x,y): return 0
                
def depthLimitedSearch(puzzle: eightPuzzle, limit: int) -> list:
    root = Node(puzzle.grid, func) # Create the root node    
    frontier = []
    explored = set()
    frontier.append(root)
    gotToLimit = False
    while frontier:
        node = frontier.pop(-1)
        explored.add(node)
        if node.puzzle.solved(): return node.solution
        if len(node.solution) > limit: 
            gotToLimit = True
            continue
        for child in node.nodeChildren():
            if child not in explored and not child in frontier:
                frontier.append(child)
    if not gotToLimit: return ["failure"]
    else: return ["cutoff"]
            
def iterativeDeepeningSearch(puzzle: eightPuzzle) -> list:
    i = 0
    limit = 30
    while(True):
        print(f"Limite = {i}")
        if i > limit: return ["failure"]
        i += 1
        solution = depthLimitedSearch(puzzle, i)
        if(solution != ['cutoff']):
            return solution
# ids.py

import numpy as np
import copy

from eightPuzzle import eightPuzzle
from node import Node
from heuristics import manhattanDistance, misplacedTiles

def func(x,y): return 0
                
def depthLimitedSearch(puzzle: eightPuzzle, limit: int) -> (list, list):
    root = Node(puzzle.grid, func) # Create the root node    
    frontier = []
    explored = dict()
    frontier.append(root)
    gotToLimit = False
    while frontier:
        node = frontier.pop(-1)
        explored[node] = node
        if node.puzzle.solved(): return node.solution
        if len(node.solution) > limit:
            gotToLimit = True
            continue
        for child in node.nodeChildren():
            if child not in explored and not child in frontier:
                frontier.append(child)
            elif child in explored and len(explored[child].solution) > len(child.solution):
                explored[child] = child
                frontier.append(child)
    if not gotToLimit: return ["failure"]
    else: return ["cutoff"]
            
def iterativeDeepeningSearch(puzzle: eightPuzzle) -> (list,list):
    i = 0
    limit = 30
    while(True):
        if i > limit: return ["failure"]
        solution = depthLimitedSearch(puzzle, i)
        if(solution != ['cutoff']):
            return solution
        i += 1
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
    explored = set()
    frontier.append(root)
    gotToLimit = False
    history = []
    i = 0
    while frontier:
        node = frontier.pop(-1)
        history.append((misplacedTiles(node.puzzle.grid), i))
        i+=1
        explored.add(node)
        if node.puzzle.solved(): return node.solution, history
        if len(node.solution) > limit: 
            gotToLimit = True
            continue
        for child in node.nodeChildren():
            if child not in explored and not child in frontier:
                frontier.append(child)
    if not gotToLimit: return ["failure"], history
    else: return ["cutoff"], history
            
def iterativeDeepeningSearch(puzzle: eightPuzzle) -> (list,list):
    i = 0
    limit = 30
    while(True):
        print(f"Limite = {i}")
        if i > limit: return ["failure"]
        i += 1
        solution,history = depthLimitedSearch(puzzle, i)
        if(solution != ['cutoff']):
            return solution,history
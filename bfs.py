# bfs.py

import networkx as nx
import matplotlib.pyplot as plt

import copy

from eightPuzzle import eightPuzzle
from node import Node
        
def func(x,y): return 0

def breadthFirstSearch(puzzle: eightPuzzle) -> list:
    i = 0
    root = Node(puzzle.grid, func) # Create the root node
    if root.puzzle.solved(): return root.solution
    frontier = []
    explored = set()
    frontier.append(root)
    while frontier:
        i+=1
        node = frontier.pop(0)
        explored.add(node)
        for child in node.nodeChildren():
            if child not in explored and child not in frontier:
                if child.puzzle.solved():
                    return child.solution
                frontier.append(child)
    return ["failure"]
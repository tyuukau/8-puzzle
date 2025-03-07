# Documentation for src/algorithms Folder

This folder is responsible for the implementation of various search algorithms. Each file in this folder represents a different search algorithm or a related functionality. 

## Table of Contents

1. [__init__.py](#__init__.py)
2. [abstract_search.py](#abstract_search.py)
3. [astar.py](#astar.py)
4. [gbfs.py](#gbfs.py)
5. [rbfs.py](#rbfs.py)

## __init__.py

The `__init__.py` file is a special Python file that allows a directory to become a Python package which can be imported as a module. In the context of this folder, it might be used to initialize certain variables, functions or classes when the package is imported.

[Link to __init__.py documentation](#__init__.py)

## abstract_search.py

The `abstract_search.py` file contains classes and methods that define the structure and functionality of search algorithms. It includes both uninformed and informed search algorithms, as well as a class to represent the result of a search algorithm. The file uses Python's built-in `enum`, `dataclasses`, and `abc` modules, as well as custom modules `heuristics`, `node`, and `state`.

[Link to abstract_search.py documentation](#abstract_search.py)

## astar.py

The `astar.py` file implements the A* search algorithm. The A* algorithm is a popular choice in pathfinding and graph traversal, which is the process of finding a path between multiple points, called "nodes". It's widely used in applications such as maps, robotics, and AI.

[Link to astar.py documentation](#astar.py)

## gbfs.py

The `gbfs.py` file contains the implementation of the Greedy Best-First Search (GBFS) algorithm. GBFS is an informed search algorithm that uses a heuristic function to estimate the cost of reaching the goal from a given state.

[Link to gbfs.py documentation](#gbfs.py)

## rbfs.py

The `rbfs.py` file implements the Recursive Best First Search (RBFS) algorithm. The RBFS algorithm is a type of informed search algorithm that uses a heuristic function to guide its search. This implementation of the RBFS algorithm is designed to be used with a callable heuristic class and allows for a limit to be set on the f_cost of nodes.

[Link to rbfs.py documentation](#rbfs.py)

[Link to repository](/src/algorithms)
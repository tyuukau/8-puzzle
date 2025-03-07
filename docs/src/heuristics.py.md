# heuristics.py

This Python file, `heuristics.py`, contains several classes and methods for calculating different types of distances between two states of a puzzle. These distances are used as heuristics in solving the puzzle. The file also includes a `main` function that demonstrates how to use these classes and methods.

## Classes

### CallableHeuristicClass

This is a base class for all the heuristic classes. It doesn't contain any methods or properties.

### MistileDistance

This class calculates the Misplaced-tile distance between the current state and the goal state of the puzzle. It inherits from `CallableHeuristicClass`.

#### Method: `__call__(self, current_state: State, goal_state: State) -> int`

This method calculates the Misplaced-tile distance. It takes two parameters:

- `current_state` (`State`): The current state of the puzzle.
- `goal_state` (`State`): The goal state of the puzzle.

It returns an integer representing the Misplaced-tile distance.

### ManhattanDistance

This class calculates the Manhattan distance between the current state and the goal state of the puzzle. It inherits from `CallableHeuristicClass`.

#### Method: `__call__(self, current_state: State, goal_state: State) -> int`

This method calculates the Manhattan distance. It takes two parameters:

- `current_state` (`State`): The current state of the puzzle.
- `goal_state` (`State`): The goal state of the puzzle.

It returns an integer representing the Manhattan distance.

### GaschnigDistance

This class calculates the Gaschnig distance between the current state and the goal state of the puzzle. It inherits from `CallableHeuristicClass`.

#### Method: `__call__(self, current_state: State, goal_state: State) -> int`

This method calculates the Gaschnig distance. It takes two parameters:

- `current_state` (`State`): The current state of the puzzle.
- `goal_state` (`State`): The goal state of the puzzle.

It returns an integer representing the Gaschnig distance.

### AnnDistance

This class calculates the ANN distance between the current state and the goal state of the puzzle. It inherits from `CallableHeuristicClass`.

#### Method: `__init__(self, model_path: str = "data/models/puzzle_model.pth") -> None`

This method initializes the `AnnDistance` class. It takes one optional parameter:

- `model_path` (`str`): The path to the model file. The default value is "data/models/puzzle_model.pth".

#### Method: `__call__(self, current_state: State, goal_state: State) -> int`

This method calculates the ANN distance. It takes two parameters:

- `current_state` (`State`): The current state of the puzzle.
- `goal_state` (`State`): The goal state of the puzzle.

It returns an integer representing the ANN distance.

## Functions

### main

This function demonstrates how to use the classes and methods in this file. It creates two `State` objects, `a` and `b`, and then calculates and prints the four types of distances between `a` and `b`.

## Usage

To use this file, you can import the classes and use them to calculate distances. Here is an example:

```python
from heuristics import MistileDistance, ManhattanDistance, GaschnigDistance, AnnDistance, State

a = State(15, 14, 8, 12, 10, 11, 9, 13, 2, 6, 5, 1, 3, 7, 4, 0)
b = State(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0)

mistile_distance = MistileDistance()
print(mistile_distance(a, b))

manhattan_distance = ManhattanDistance()
print(manhattan_distance(a, b))

gaschnig_distance = GaschnigDistance()
print(gaschnig_distance(a, b))

ann_distance = AnnDistance()
print(ann_distance(a, b))
```

This will print the four types of distances between `a` and `b`.
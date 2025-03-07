# gbfs.py

This is a Python code file named `gbfs.py` which contains the implementation of the Greedy Best-First Search (GBFS) algorithm. GBFS is an informed search algorithm that uses a heuristic function to estimate the cost of reaching the goal from a given state.

## Class: GBFS

The `GBFS` class is a subclass of the `InformedSearchAlgorithm` abstract base class. It overrides the `_search` method to implement the GBFS algorithm.

### Initialization

The `GBFS` class is initialized with a `heuristic` argument of type `CallableHeuristicClass`. This heuristic function is used to estimate the cost of reaching the goal from a given state.

```python
gbfs = GBFS(heuristic)
```

### Method: _search

The `_search` method is the main method of the `GBFS` class. It takes a `start_state` of type `State` as an argument and returns a `SearchResult` object.

```python
result = gbfs._search(start_state)
```

The method initializes a priority queue `frontier` with the `start_state` and a `closed` set to keep track of visited states. It then enters a loop where it continuously dequeues a node from the `frontier`, adds it to the `closed` set, and checks if it is a goal node. If it is, it reconstructs the path from the start state to the goal node and returns a `SearchResult` object with a `SUCCESS` result. If it is not, it expands the node, adds the resulting child nodes to the `frontier` if they have not been visited before, and continues with the next iteration of the loop. If the `frontier` is empty, it returns a `SearchResult` object with a `FAILURE` result.

The `_search` method also keeps track of the time complexity `time_cp` and space complexity `space_cp` of the search.

### Method: _reconstruct_path

The `_reconstruct_path` method is a helper method used to reconstruct the path from the start state to a given goal node. It is not directly called by the user but is used internally by the `_search` method.

### Method: _is_goal

The `_is_goal` method is a helper method used to check if a given node is a goal node. It is not directly called by the user but is used internally by the `_search` method.

## Examples

Here is an example of how to use the `GBFS` class:

```python
# Define a heuristic function
def heuristic(state):
    # ... implementation of the heuristic ...

# Initialize the GBFS class
gbfs = GBFS(heuristic)

# Define a start state
start_state = State()

# Perform the search
result = gbfs._search(start_state)

# Print the result
print(result)
```

## Technical Concepts

The `GBFS` class uses a priority queue to keep track of the frontier, i.e., the set of nodes that are to be explored. The priority of a node in the queue is determined by the heuristic cost of the node. This is why GBFS is called a "greedy" algorithm: it always chooses to explore the node with the lowest heuristic cost, i.e., the node that it estimates to be closest to the goal.

The `GBFS` class also uses a set to keep track of the closed list, i.e., the set of nodes that have already been explored. This is to prevent the algorithm from exploring the same node more than once.

The `GBFS` class uses the `CallableHeuristicClass` type for the heuristic function. This is a callable class, i.e., a class that implements the `__call__` method, which allows instances of the class to be called as if they were functions. This is a common pattern in Python for creating function-like objects that have state.
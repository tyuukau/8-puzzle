# rbfs.py

This is a Python code file that implements the Recursive Best First Search (RBFS) algorithm. The RBFS algorithm is a type of informed search algorithm that uses a heuristic function to guide its search. This implementation of the RBFS algorithm is designed to be used with a callable heuristic class and allows for a limit to be set on the f_cost of nodes.

## Class: RBFS

The `RBFS` class is the main class in this file. It inherits from the `InformedSearchAlgorithm` class.

### Initialization

The `RBFS` class is initialized with two parameters:

- `heuristic` (`CallableHeuristicClass`): This is the heuristic function that the RBFS algorithm will use to guide its search. It must be an instance of the `CallableHeuristicClass`.

- `limit` (`int`): This is the limit for the f_cost of nodes. The default value is 1e15.

### Method: _rbfs

The `_rbfs` method is a private method that implements the main logic of the RBFS algorithm. It takes four parameters:

- `node` (`PNode`): This is the node that the algorithm is currently examining.

- `limit` (`int`): This is the limit for the f_cost of nodes.

- `time_cp` (`int`): This is a counter for the time complexity of the algorithm. The default value is 1.

- `space_cp` (`int`): This is a counter for the space complexity of the algorithm. The default value is 1.

The `_rbfs` method returns a tuple containing a `SearchResult` object and an integer representing the f_cost of the node.

### Method: _search

The `_search` method is a private method that starts the RBFS algorithm. It takes one parameter:

- `start_state` (`State`): This is the state from which the algorithm will start its search.

The `_search` method returns a `SearchResult` object.

## Examples

Here is an example of how to use the `RBFS` class:

```python
from heuristics import MyHeuristic
from rbfs import RBFS
from state import MyState

# Initialize the heuristic
heuristic = MyHeuristic()

# Initialize the RBFS algorithm
rbfs = RBFS(heuristic, limit=1000)

# Initialize the start state
start_state = MyState()

# Start the search
result = rbfs._search(start_state)
```

In this example, `MyHeuristic` and `MyState` are placeholder names for your own heuristic and state classes. You would replace these with the actual classes that you are using in your code.
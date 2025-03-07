# abstract_search.py

This Python file, `abstract_search.py`, contains classes and methods that define the structure and functionality of search algorithms. It includes both uninformed and informed search algorithms, as well as a class to represent the result of a search algorithm. The file uses Python's built-in `enum`, `dataclasses`, and `abc` modules, as well as custom modules `heuristics`, `node`, and `state`.

## SearchResult Class

The `SearchResult` class represents the result of a search algorithm. It has four attributes:

- `result`: The result of the search, which is an instance of the `Result` enum class.
- `path`: The path from the start node to the goal node, if found. It is a list of `Node` objects or `None`.
- `time_cp`: The time complexity of the search algorithm.
- `space_cp`: The space complexity of the search algorithm.

The `SearchResult` class also has a method `print_result()`, which prints the result. If a path is found, it also prints the path.

## SearchAlgorithm Class

The `SearchAlgorithm` class is an abstract base class representing a search algorithm. It has several methods:

- `_is_goal(node: Node)`: Checks if the given node is the goal state.
- `_reconstruct_path(node: Node)`: Reconstructs the path from the start node to the given node.
- `_set_goal(goal_state: State)`: Sets the goal state of the search algorithm.
- `_search(start_state: State)`: An abstract method that searches for a path from the start node to the goal node. It returns a `SearchResult` object. This method must be implemented by any class that inherits from `SearchAlgorithm`.
- `solve(start_state: State, goal_state: State, do_print: bool = False)`: Sets the goal state of the search algorithm, then searches using `_search()`. If `do_print` is `True`, it also prints the result.

## UninformedSearchAlgorithm Class

The `UninformedSearchAlgorithm` class is an abstract class representing an uninformed search algorithm. It inherits from the `SearchAlgorithm` class. Any specific uninformed search algorithm should be implemented as a subclass of this class.

## InformedSearchAlgorithm Class

The `InformedSearchAlgorithm` class is an abstract class representing an informed search algorithm. It inherits from the `SearchAlgorithm` class and has an additional attribute:

- `heuristic`: The heuristic function, which is an instance of the `CallableHeuristicClass`.

The `InformedSearchAlgorithm` class also has a method `h_cost(node: Node)`, which calculates the heuristic cost of the given node. Any specific informed search algorithm should be implemented as a subclass of this class.
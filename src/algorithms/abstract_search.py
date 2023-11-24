from typing import List, Tuple, Callable, Union
from enum import Enum
from dataclasses import dataclass

from node import Node


class Result(Enum):
    SUCCESS = "success"
    FAILURE = "failure"
    CUTOFF = "cutoff"


@dataclass
class SearchResult(object):
    """
    Represents the result of a search algorithm.

    Attributes:
    - `result (Result)`: The result of the search.
    - `path (Union[List[Node], None])`: The path from the start node to the goal node, if found.
    - `time_cp (int)`: The time complexity of the search algorithm.
    - `space_cp (int)`: The space complexity of the search algorithm.

    Methods:
    - `print_result()`: Print the result. If a path is found, print the path.
    """

    result: Result
    path: Union[List[Node], None]
    time_cp: int
    space_cp: int

    def print_result(self) -> None:
        print(self.result)
        if self.path is not None:
            print("Path:")
            print(f"\tLength: {len(self.path)-1}")
            for p in self.path:
                print(f"\t{p}")
        else:
            print("No Path is found")
        print(f"Space: {self.space_cp}")
        print(f"Time: {self.time_cp}")


class SearchAlgorithm(object):
    """
    An abstract class representing a search algorithm. Subclasses should implement the `search`
    method to define the specific search algorithm.

    Methods:
    - `search(start: Node, goal: Node) -> SearchResult`:
        Searches for a path from the start node to the goal node. Returns a `SearchResult` object.
    """

    def _is_goal(self, node: Node, goal: Node) -> bool:
        return node.state == goal.state

    def _reconstruct_path(self, node: Node) -> List[Node]:
        path = []
        while node is not None:
            path.append(node)
            node = node.parent
        return path[::-1]

    def search(self, start: Node, goal: Node) -> SearchResult:
        raise NotImplementedError()


class UninformedSearchAlgorithm(SearchAlgorithm):
    """
    An abstract class representing an uninformed search algorithm.

    This class inherits from the `SearchAlgorithm` class and provides a template for implementing
    uninformed search algorithms. Subclasses should implement the `search` method to define the
    specific search algorithm.
    """

    def __init__(self) -> None:
        super().__init__()


class InformedSearchAlgorithm(SearchAlgorithm):
    """
    An abstract class representing an informed search algorithm.

    This class inherits from the `SearchAlgorithm` class and provides a template for implementing
    informed search algorithms. Subclasses should implement the `search` method to define the
    specific search algorithm.

    Attributes:
    - `heuristic (Callable)`: A function that estimates the cost of reaching the goal state from a
      given state.
    """

    def __init__(self, heuristic: Callable) -> None:
        super().__init__()
        self.heuristic = heuristic

from __future__ import annotations
from typing import List, Tuple, Set, Optional, Callable
from node import Node

from typing import List, Tuple

class SearchAlgorithm(object):
  """
  An abstract class representing a search algorithm. Subclasses should implement the `search` 
  method to define the specific search algorithm.

  Attributes:
    None

  Methods:
    search(start: Node, goal: Node) -> Tuple[str, List[Node], int, int]:
      Searches for a path from the start node to the goal node.

      Returns a tuple containing:
        - A string representing the name of the search algorithm used.
        - A list of nodes representing the path from the start node to the goal node.
        - An integer representing the time complexity.
        - An integer representing the space complexity.
  """

  def _is_empty(self, frontier: List) -> bool:
    return len(frontier) == 0

  def _is_goal(self, node: Node, goal: Node) -> bool:
    return node == goal
  
  def _reconstruct_path(self, node: Node) -> List[Node]:
    path = []
    while node is not None:
      path.append(node)
      node = node.parent
    return path[::-1]

  def search(self, start: Node, goal: Node) -> Tuple[str, List[Node], int, int]:
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
    heuristic (Callable): A function that estimates the cost of reaching the goal state from a given state.
  """
  def __init__(self, heuristic: Callable) -> None:
    super().__init__()
    self.heuristic = heuristic
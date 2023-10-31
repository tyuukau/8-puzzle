from __future__ import annotations
from typing import List, Tuple, Set, Optional, Callable
from algorithms.abstract_search import UninformedSearchAlgorithm
from node import Node

from typing import List, Optional, Tuple
from src.algorithms.UninformedSearchAlgorithm import UninformedSearchAlgorithm
from src.Node import Node

class IDS(UninformedSearchAlgorithm):
  """
  Iterative Deepening Search (IDS) algorithm implementation.

  Args:
    max_depth : int, optional
      Maximum depth to search for a solution. Default is 10000.
  """
  def __init__(self, max_depth: int=10000) -> None:
    super().__init__()
    self.max_depth = max_depth
    
  def _dls(self, start: Node, goal: Node, limit: int) -> Tuple[str, Optional[List[Node]], int, int]:
    frontier = [(start, 0)]

    time_cp = 0
    space_cp = len(frontier)

    result = "failure"

    while not self._is_empty(frontier):
      node, depth = frontier.pop()

      time_cp += 1

      if self._is_goal(node, goal):
        result = "success"
        path = self._reconstruct_path(node)
        return result, path, time_cp, space_cp
      if depth > limit:
        result = "cutoff"
      else:
        for child in node.expand():
          frontier.append((child, depth + 1))

          time_cp += 1
          space_cp = max(len(frontier), space_cp)

    return result, None, time_cp, space_cp

  def search(self, start: Node, goal: Node) -> Tuple[str, List[Node], int, int]:
    for depth in range(self.max_depth):
      result, path, time_cp, space_cp = self._dls(start, goal, limit=depth)
      if result != "cutoff":
        return result, path, time_cp, space_cp
    return result, path, time_cp, space_cp

class IDSWithCyclePruning(UninformedSearchAlgorithm):
  """
  Iterative Deepening Search (IDS) algorithm implementation.
  Includes cycle pruning.

  Args:
    max_depth : int, optional
      Maximum depth to search for a solution. Default is 10000.
  """
  def __init__(self, max_depth: int=10000) -> None:
    super().__init__()
    self.max_depth = max_depth

  def _dls(self, start: Node, goal: Node, limit: int) -> Tuple[str, Optional[List[Node]], int, int]:
    frontier = [start]

    expanded = []

    time_cp = 0
    space_cp = len(frontier)

    result = "failure"

    while not self._is_empty(frontier):
      node = frontier.pop()

      if node in expanded: # Skip nodes that we have already visited
        continue

      expanded.append(node)

      time_cp += 1

      if self._is_goal(node, goal):
        result = "success"
        path = self._reconstruct_path(node)
        return result, path, time_cp, space_cp
      if node.cost > limit:
        result = "cutoff"
      else:
        for child in node.expand():
          if child not in expanded:
            frontier.append(child)

            time_cp += 1
            space_cp = max(len(frontier), space_cp)

    return result, None, time_cp, space_cp

  def search(self, start: Node, goal: Node) -> Tuple[str, List[Node], int, int]:
    for depth in range(self.max_depth):
      result, path, time_cp, space_cp = self._dls(start, goal, limit=depth)
      if result != "cutoff":
        return result, path, time_cp, space_cp
    return result, path, time_cp, space_cp
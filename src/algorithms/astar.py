from __future__ import annotations
from typing import List, Tuple, Set, Optional, Callable
from algorithms.abstract_search import InformedSearchAlgorithm
from node import Node
from queue import PriorityQueue

class AStar(InformedSearchAlgorithm):
  """
  A* search algorithm implementation.

  Args:
    heuristic (Callable): A function that takes two arguments: the current state and the goal state,
      and returns the estimated cost to reach the goal state from the current state.
  """
  def __init__(self, heuristic: Callable) -> None:
    super().__init__(heuristic)

  def search(self, start: Node, goal: Node) -> Tuple[str, Optional[List[Node]], int, int]:
    open_list = PriorityQueue()
    open_list.put((0, start))
    
    time_cp = 0
    space_cp = open_list.qsize()

    cost_so_far = {}
    cost_so_far[start.state] = 0

    while not open_list.empty():
      _, node = open_list.get()
      
      time_cp += 1

      if self._is_goal(node, goal):
        path = self._reconstruct_path(node)
        return "success", path, time_cp, space_cp

      for next_node in node.expand():
        new_cost = cost_so_far[node.state] + next_node.cost
        if next_node.state not in cost_so_far or new_cost < cost_so_far[next_node.state]:
          cost_so_far[next_node.state] = new_cost
          priority = new_cost + self.heuristic(next_node.state, goal.state)
          open_list.put((priority, next_node))
          
          time_cp += 1
          space_cp = max(space_cp, len(cost_so_far) + open_list.qsize())

    return "failure", None, time_cp, space_cp

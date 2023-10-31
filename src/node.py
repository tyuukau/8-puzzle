from __future__ import annotations
from typing import List, Tuple, Set, Optional, Callable

class Node(object):
  """
  Represents a node in a search tree.

  Attributes:
    state (State): The state of the node.
    parent (Node): The parent node of the node.
    action (str): The action taken to reach the node.
    cost (int): The cost of the path from the initial state to the node.
    
  Methods:
    expand() -> List[Node]: 
      Returns a list of neighbors expanded from the node.
  """
  __slots__ = ['state', 'parent', 'action', 'cost']

  def __init__(self, state, parent: Optional[Node]=None, action: Optional[str]=None, cost: int=0) -> None:
    self.state = state
    self.parent = parent
    self.action = action
    self.cost = cost

  def __repr__(self) -> str:
    return f'Node(state={self.state}, parent={self.parent}, action={self.action}, cost={self.cost})'

  def __str__(self) -> str:
    return f'Node(state={self.state}, parent={self.parent}, action={self.action}, cost={self.cost})'

  def __eq__(self, other) -> bool:
    return self.state == other.state

  def __lt__(self, other) -> bool:
    return self.cost < other.cost

  def expand(self) -> List[Node]:
    children = []
    x_old, y_old = self.state.find_blank()
    action_dict = [(x_old - 1, y_old, 'Up'), (x_old + 1, y_old, 'Down'),
                   (x_old, y_old - 1, 'Left'), (x_old, y_old + 1, 'Right')]
    for (x_new, y_new, action) in action_dict:
      try:
        new_state = self.state.swap(x_old, y_old, x_new, y_new)
        children.append(Node(state=new_state, parent=self, action=action, cost=self.cost+1))
      except AssertionError:
        continue
    return children
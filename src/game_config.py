from __future__ import annotations
from typing import List, Tuple, Set, Optional, Callable
from state import State

class GameConfig(object):
  """
  Stores game configuration.

  Attributes:
    width (int): Width of the square puzzle grid.
    start_state (State): Initial state of the puzzle represented as a list of integers.
    goal_state (State): Goal state of the puzzle represented as a list of integers.
    blank (int): The value represented as blank in the grid, default is 0.
    solvable (bool): A boolean indicating if the puzzle is solvable. Calculated using self._is_solvable().
  """
  __slots__ = ['width', 'start_state', 'goal_state', 'solvable']

  def __init__(self, start_state: State, goal_state: State) -> None:
    self.width = start_state.width
    self.start_state = start_state
    self.goal_state = goal_state
    self._validate_data()
    self.solvable = self._is_solvable()

  def __str__(self) -> str:
    return f"GameConfig(width={self.width}, start_state={self.start_state.array}, goal_state={self.goal_state.array}, solvable={self.solvable})"

  def _validate_data(self) -> None:
    if not ((self.width == self.start_state.width) and (self.width == self.goal_state.width)):
      raise ValueError('The dimension of the start and goal states must be consistent')

  def _count_inversions(self, numbers: Tuple[int]) -> int:
    inversions = 0
    for i in range(0,len(numbers)):
      n = numbers[i]
      if n <= 1:
        continue
      for j in range(i + 1, len(numbers)):
        m = numbers[j]
        if m > 0 and n > m:
          inversions += 1
    return inversions

  def _is_solvable(self) -> bool:
    start_inversions = self._count_inversions(self.start_state.array)
    goal_inversions = self._count_inversions(self.goal_state.array)
    if self.width % 2 == 0:
      goal_zero_row_index = self.goal_state.index(0) // self.width
      start_zero_row_index = self.start_state.index(0) // self.width
      return (goal_inversions % 2) == ((start_inversions + goal_zero_row_index + start_zero_row_index) % 2)
    else:
      return (start_inversions % 2) == (goal_inversions % 2)
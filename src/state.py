from __future__ import annotations
from typing import List, Tuple, Set, Optional, Callable
import math

class State(object):
  __slots__ = ['width', 'array', 'blank']

  def __init__(self, array: Tuple[int], blank: int=0) -> None:
    self.array = array
    self.blank = blank
    self.width = int(math.sqrt(len(array)))
    self._validate_data()

  def __eq__(self, other) -> bool:
    return self.array == other.array
  
  def __hash__(self) -> int:
    return hash(self.array)

  def __str__(self) -> str:
    return f"State({self.array})"

  def _validate_data(self) -> None:
    if len(self.array) != self.width ** 2:
      raise ValueError('The length of the array must be width squared')

    if any(x < 0 or x > self.width ** 2-1 for x in self.array):
      raise ValueError('All numbers in a state must be >= 0 and <= width*width-1')

  def idx_to_val(self, idx: int) -> Tuple[int, int]:
    return idx // self.width, idx % self.width

  def val_to_idx(self, x: int, y: int) -> int:
    return x * self.width + y

  def swap(self, x_old: int, y_old: int, x_new: int, y_new: int) -> State:
    assert 0 <= x_new < self.width and 0 <= y_new < self.width
    array_new = list(self.array)

    old_idx = self.val_to_idx(x_old, y_old)
    new_idx = self.val_to_idx(x_new, y_new)

    array_new[old_idx], array_new[new_idx] = array_new[new_idx], array_new[old_idx]
    return State(array=tuple(array_new))

  def find_blank(self) -> Tuple[int, int]:
    for idx, cell in enumerate(self.array):
      if cell == 0:
        return self.idx_to_val(idx)
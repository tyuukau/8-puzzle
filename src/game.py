from __future__ import annotations
from typing import List, Tuple, Set, Optional, Callable
from game_config import GameConfig
from algorithms.abstract_search import SearchAlgorithm
from node import Node
from state import State

from algorithms.ids import *
from algorithms.astar import *

from heuristics import *

class Game(object):
  '''
  Represents an instance of the n-puzzle game.

  Attributes:
    game_config (GameConfig): The configuration of the game, including the start and goal states.
    algorithm (SearchAlgorithm): The search algorithm to use to solve the game.
  '''
  __slots__ = ['game_config', 'algorithm', 'heuristic']

  def __init__(self, game_config: GameConfig, algorithm: SearchAlgorithm) -> None:
    self.game_config = game_config
    self.algorithm = algorithm

  def solve(self) -> None:
    start_state = self.game_config.start_state
    goal_state = self.game_config.goal_state
    result, path, time_cp, space_cp = self.algorithm.search(Node(start_state), Node(goal_state))
    print(result)
    print("Path:")
    if path is not None:
      print(f'\tLength: {len(path)-1}')
      for p in path:
        print(f'\t{p}')
    print(f'Space: {space_cp}')
    print(f'Time: {time_cp}')
    
def game_generator(n: int = 3) -> GameConfig:
  """
  Generates a new game configuration for the 8-puzzle game.

  Args:
    n (int): The size of the puzzle. Default is 3.

  Returns:
    GameConfig: A new game configuration object containing the start and goal states.
  """
  try:
    start = [i for i in range (n**2)]
    goal = [i for i in range (n**2)]

    random.shuffle(start)
    random.shuffle(goal)

    start_state_array, goal_state_array = tuple(start), tuple(goal)

    start_state = State(array=start_state_array)
    goal_state = State(array=goal_state_array)

    game_config = GameConfig(start_state=start_state, goal_state=goal_state)

  except ValueError as e:
    print(f"An error occurred: {e}")
    return None

  return game_config

def main():
  game_config = GameConfig(State((1, 2, 3, 4, 5, 6, 7, 8, 0)),
                           State((1, 2, 3, 4, 5, 6, 8, 7, 0)))
  algorithm = IDS(max_depth=80)
  g = Game(game_config=game_config, algorithm=algorithm)
  g.solve()
  
if __name__ == "__main__":
    main()
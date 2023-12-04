import random

from game_config import GameConfig
from algorithms.abstract_search import SearchAlgorithm
from algorithms import IDS, IDSWithCyclePruning, AStar, GBFS, RBFS, PRBFS
from node import Node
from state import State
from heuristics import *


class Game(object):
    """
    Represents an instance of the n-puzzle game.

    Attributes:
    - `game_config` (`GameConfig`): The configuration of the game, including the start and goal states.
    - `algorithm` (`SearchAlgorithm`): The search algorithm to use to solve the game.

    Methods:
    - `solve()`: Solves the given game configuration using the given algorithm.
    """

    __slots__ = ["game_config", "algorithm", "heuristic"]

    def __init__(self, game_config: GameConfig, algorithm: SearchAlgorithm) -> None:
        self.game_config = game_config
        self.algorithm = algorithm

    def solve(self) -> None:
        print(f"Algorithm: {self.algorithm.__class__.__name__}")
        start_state = self.game_config.start_state
        goal_state = self.game_config.goal_state
        search_result = self.algorithm.search(Node(start_state), Node(goal_state))
        search_result.print_result()


def game_generator(n: int = 3) -> GameConfig:
    """
    Generates a new game configuration for the 8-puzzle game.

    Args:
    - `n` (`int`): The size of the puzzle. Default is 3.

    Returns:
    - `GameConfig`: A new game configuration object containing the start and goal states.

    Example:
    ```
    game_config = game_generator(n = 4)
    ```
    """
    try:
        start = [i for i in range(n**2)]
        goal = [i for i in range(n**2)]

        random.shuffle(start)
        random.shuffle(goal)

        start_state = State(*start)
        goal_state = State(*goal)

        game_config = GameConfig(start_state=start_state, goal_state=goal_state)

    except ValueError as e:
        print(f"An error occurred: {e}")
        return None

    return game_config


def main():
    game_config = GameConfig(
        start_state=State(3, 7, 4, 8, 5, 6, 2, 0, 1),
        goal_state=State(0, 1, 2, 3, 4, 5, 6, 7, 8),
    )
    algorithm = AStar(heuristic=manhattan_distance)
    g = Game(game_config=game_config, algorithm=algorithm)
    if game_config.is_solvable():
        g.solve()


if __name__ == "__main__":
    main()

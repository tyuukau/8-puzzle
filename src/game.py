import random
from sys import exit
import time

from .game_config import GameConfig
from .algorithms.abstract_search import SearchAlgorithm
from .state import State


class Game(object):
    """
    Represents an instance of the n-puzzle game.

    Attributes:
    - `game_config` (`GameConfig`): The configuration of the game, including the start and goal states.
    - `algorithm` (`SearchAlgorithm`): The search algorithm to use to solve the game.

    Methods:
    - `solve()`: Solves the given game configuration using the given algorithm.
    """

    __slots__ = ["game_config", "algorithm", "ignore_solvability"]

    def __init__(
        self,
        game_config: GameConfig,
        algorithm: SearchAlgorithm,
        ignore_solvability: bool = True,
    ) -> None:
        self.game_config = game_config
        self.algorithm = algorithm
        self.ignore_solvability = ignore_solvability

    def play(self) -> None:
        print(f"Algorithm: {self.algorithm.__class__.__name__}")
        start_state = self.game_config.start_state
        goal_state = self.game_config.goal_state

        if not self.ignore_solvability:
            if not self.game_config.is_solvable():
                exit("Solvability is False. Game terminated.")
        else:
            print("Ignoring solvability...")

        start_time = time.time()
        end_time = time.time()
        self.algorithm.solve(start_state, goal_state)
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time:.4f} seconds")


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

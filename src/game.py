import random
from sys import exit
import time
from dataclasses import dataclass
import signal

from .algorithms.abstract_search import SearchResult
from .game_config import GameConfig
from .algorithms.abstract_search import SearchAlgorithm
from .state import State
from .node import Node


@dataclass
class ResultRecord(object):
    """
    Represents the result of a search algorithm.

    Attributes:
    - `path (list[Node])`: The path from the start node to the goal node, if found.
    - `path_length (int)`: The length of the path from the start node to the goal node, if found.
    - `time_cp (int)`: The time complexity of the search algorithm.
    - `space_cp (int)`: The space complexity of the search algorithm.
    - `time (float)`: The runtime of the search algorithm.
    """

    path: list[Node] | None
    path_length: int
    time_cp: int
    space_cp: int
    time: float


class TimeoutError(Exception):
    pass


def timeout_handler(signum, frame):
    raise TimeoutError("Function timed out")


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

    def _play(self, do_print: bool = False) -> SearchResult:
        start_state = self.game_config.start_state
        goal_state = self.game_config.goal_state

        if not self.ignore_solvability:
            if not self.game_config.is_solvable():
                exit("Solvability is False. Game terminated.")

        search_result = self.algorithm.solve(start_state, goal_state)
        return search_result

    def play(self, do_print: bool = False) -> ResultRecord:
        start_time = time.time()

        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(60)

        try:
            search_result = self._play()
        except TimeoutError:
            search_result = None
        finally:
            signal.alarm(0)

        end_time = time.time()
        execution_time = end_time - start_time

        path = search_result.path if search_result else None
        path_length = len(search_result.path) - 1 if search_result else -1
        time_cp = search_result.time_cp if search_result else -1
        space_cp = search_result.space_cp if search_result else -1

        if do_print:
            if search_result:
                search_result.print_result()
            else:
                print("Failed to solve on time.")

        return ResultRecord(path, path_length, time_cp, space_cp, execution_time)


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

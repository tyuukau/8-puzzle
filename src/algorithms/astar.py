from typing import Callable, List, Tuple
import heapq

from algorithms.abstract_search import Result, SearchResult, InformedSearchAlgorithm
from node import Node
from state import State


class AStar(InformedSearchAlgorithm):
    """
    A* search algorithm implementation.

    Args:
    - `heuristic` (`Callable[[State, State], int]`): The heuristic function.
    """

    def __init__(self, heuristic: Callable[[State, State], int]) -> None:
        super().__init__(heuristic)

    def _search(self, start_state: State) -> SearchResult:
        start = Node(start_state)

        frontier: List[Tuple[int, int, Node]] = []
        frontier.append((start.cost + self.h_cost(start), -start.cost, start))

        closed = set()

        time_cp = 0
        space_cp = len(closed) + len(frontier)

        while frontier:
            node = heapq.heappop(frontier)[2]
            closed.add(node.state)

            time_cp += 1
            space_cp = max(space_cp, len(closed) + len(frontier))

            if self._is_goal(node):
                path = self._reconstruct_path(node)
                return SearchResult(
                    result=Result.SUCCESS, path=path, time_cp=time_cp, space_cp=space_cp
                )

            for child in node.expand():
                if child.state not in closed:
                    heapq.heappush(
                        frontier,
                        (
                            child.cost + self.h_cost(child),
                            -child.cost,
                            child,
                        ),
                    )
                    time_cp += 1
            space_cp = max(space_cp, len(closed) + len(frontier))

        return SearchResult(
            result=Result.FAILURE, path=None, time_cp=time_cp, space_cp=space_cp
        )


__all__ = ["AStar"]

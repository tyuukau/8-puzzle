from typing import Callable
from algorithms.abstract_search import Result, SearchResult, InformedSearchAlgorithm
from node import Node
import heapq


class GBFS(InformedSearchAlgorithm):
    """
    GBFS search algorithm implementation.

    Args:
    - `heuristic (Callable)`: A function that takes two arguments: the current state and the goal state,
        and returns the estimated cost to reach the goal state from the current state.
    """

    def __init__(self, heuristic: Callable) -> None:
        super().__init__(heuristic)

    def search(self, start: Node, goal: Node) -> SearchResult:
        frontier = []
        frontier.append((self.heuristic(start.state, goal.state), -start.cost, start))

        closed = set()

        time_cp = 0
        space_cp = len(closed) + len(frontier)

        while frontier:
            node = heapq.heappop(frontier)[2]
            closed.add(node.state)

            time_cp += 1
            space_cp = max(space_cp, len(closed) + len(frontier))

            if self._is_goal(node, goal):
                path = self._reconstruct_path(node)
                return SearchResult(
                    result=Result.SUCCESS, path=path, time_cp=time_cp, space_cp=space_cp
                )

            for child in node.expand():
                if child.state not in closed:
                    heapq.heappush(
                        frontier,
                        (
                            self.heuristic(child.state, goal.state),
                            -child.cost,
                            child,
                        ),
                    )
                    time_cp += 1
            space_cp = max(space_cp, len(closed) + len(frontier))

        return SearchResult(
            result=Result.FAILURE, path=None, time_cp=time_cp, space_cp=space_cp
        )


__all__ = ["GBFS"]

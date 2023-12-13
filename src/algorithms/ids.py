from typing import List

from algorithms.abstract_search import Result, SearchResult, UninformedSearchAlgorithm
from node import Node
from state import State


class IDS(UninformedSearchAlgorithm):
    """
    Iterative Deepening Search (IDS) algorithm implementation.

    Args:
    - `heuristic` (`Callable[[State, State], int]`): The heuristic function.
    - `max_depth` (`int`): Maximum depth to search for a solution. Default is 10000.
    """

    def __init__(self, max_depth: int = 10000) -> None:
        super().__init__()
        self.max_depth = max_depth

    def _dls(self, start: Node, limit: int) -> SearchResult:
        frontier = []
        frontier.append((start, None, 0))

        time_cp = 0
        space_cp = len(frontier)

        result = Result.FAILURE

        while frontier:
            data = frontier.pop()
            node, _, depth = data

            time_cp += 1

            if self._is_goal(node):
                result = Result.SUCCESS

                def _path(data):
                    while data:
                        yield data[0]
                        data = data[1]

                path = list(_path(data))[::-1]
                return SearchResult(
                    result=result, path=path, time_cp=time_cp, space_cp=space_cp
                )

            if depth > limit:
                result = Result.CUTOFF
            else:
                for child in node.expand():
                    frontier.append((child, data, depth + 1))

                    time_cp += 1
                    space_cp = max(len(frontier), space_cp)

        return SearchResult(result=result, path=None, time_cp=time_cp, space_cp=space_cp)

    def _search(self, start_state: State) -> SearchResult:
        start = Node(start_state)

        for depth in range(self.max_depth):
            search_result = self._dls(start, limit=depth)
            if search_result.result != Result.CUTOFF:
                return search_result
        return search_result


class IDSWithCyclePruning(UninformedSearchAlgorithm):
    """
    Iterative Deepening Search (IDS) algorithm implementation.
    Includes cycle pruning.

    Args:
    - `max_depth` (`int`): Maximum depth to search for a solution. Default is 10000.
    """

    def __init__(self, max_depth: int = 10000) -> None:
        super().__init__()
        self.max_depth = max_depth

    def _dls(self, start: Node, limit: int) -> SearchResult:
        frontier = []
        frontier.append((start, None, 0))

        expanded = set()

        time_cp = 0
        space_cp = len(frontier) + len(expanded)

        result = Result.FAILURE

        while frontier:
            data = frontier.pop()
            node, _, depth = data

            if node.state in expanded:
                continue

            expanded.add(node.state)

            time_cp += 1

            if self._is_goal(node):
                result = Result.SUCCESS

                def _path(data):
                    while data:
                        yield data[0]
                        data = data[1]

                path = list(_path(data))[::-1]
                return SearchResult(
                    result=result, path=path, time_cp=time_cp, space_cp=space_cp
                )

            if depth > limit:
                result = Result.CUTOFF
            else:
                for child in node.expand():
                    if child.state not in expanded:
                        frontier.append((child, data, depth + 1))

                        time_cp += 1
                        space_cp = max(len(frontier) + len(expanded), space_cp)

        return SearchResult(result=result, path=None, time_cp=time_cp, space_cp=space_cp)

    def _search(self, start_state: State) -> SearchResult:
        start = Node(start_state)

        for depth in range(self.max_depth):
            search_result = self._dls(start, limit=depth)
            if search_result.result != Result.CUTOFF:
                return search_result
        return search_result


__all__ = ["IDS", "IDSWithCyclePruning"]

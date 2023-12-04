from typing import List, Tuple, Set, Optional, Callable
from algorithms.abstract_search import Result, SearchResult, InformedSearchAlgorithm
from node import Node, PNode
from state import State


class RBFS(InformedSearchAlgorithm):
    def __init__(self, heuristic: Callable, limit: int = 1e15) -> None:
        super().__init__(heuristic)
        self.limit = limit
        self.f_cost = {}

    def _rbfs(
        self, node: Node, goal_state: State, limit: int, time_cp: int = 1, space_cp: int = 1
    ) -> Tuple[SearchResult, int]:
        if self._is_goal(node, goal_state):
            path = self._reconstruct_path(node)
            return SearchResult(Result.SUCCESS, path, time_cp, space_cp), limit

        children = node.expand()

        if not children:
            return SearchResult(Result.FAILURE, None, time_cp, space_cp), 1e15

        for child in children:
            h_cost = self.heuristic(child.state, goal_state)
            self.f_cost[child] = max(child.cost + h_cost, self.f_cost[node])
            if node.parent is not None:
                if child.state == node.parent.state:
                    self.f_cost[child] = 1e20

        while True:
            children.sort(key=lambda node: self.f_cost[node])
            best = children[0]
            alternative = children[1]

            if self.f_cost[best] > limit:
                return SearchResult(Result.FAILURE, None, time_cp, space_cp), self.f_cost[best]

            search_result, best_path = self._rbfs(
                best, goal_state, min(limit, self.f_cost[alternative]), time_cp, space_cp
            )
            self.f_cost[best] = best_path
            if search_result.result != Result.FAILURE:
                return search_result, self.f_cost[best]

    def search(self, start_state: State, goal_state: State) -> SearchResult:
        start = Node(start_state)

        self.f_cost[start] = 0
        search_result, _ = self._rbfs(start, goal_state, self.limit)
        return search_result


class PRBFS(InformedSearchAlgorithm):
    def __init__(self, heuristic: Callable, limit: int = 1e15) -> None:
        super().__init__(heuristic)
        self.limit = limit

    def _rbfs(
        self, node: PNode, goal_state: State, limit: int, time_cp: int = 1, space_cp: int = 1
    ) -> Tuple[SearchResult, int]:
        if self._is_goal(node, goal_state):
            path = self._reconstruct_path(node)
            return SearchResult(Result.SUCCESS, path, time_cp, space_cp), limit

        children = node.expand()

        if not children:
            return SearchResult(Result.FAILURE, None, time_cp, space_cp), 1e15

        for child in children:
            heuristic_cost = self.heuristic(child.state, goal_state)
            child.f_cost = max(child.cost + heuristic_cost, node.f_cost)
            if node.parent is not None:
                if child.state == node.parent.state:
                    child.f_cost = 1e20

        while True:
            children.sort(key=lambda node: node.f_cost)
            best = children[0]
            alternative = children[1]

            if best.f_cost > limit:
                return SearchResult(Result.FAILURE, None, time_cp, space_cp), best.f_cost

            search_result, best.f_cost = self._rbfs(
                best, goal_state, min(limit, alternative.f_cost), time_cp, space_cp
            )
            if search_result.result != Result.FAILURE:
                return search_result, best.f_cost

    def search(self, start_state: State, goal_state: State) -> SearchResult:
        start = Node(start_state)

        search_result, _ = self._rbfs(start, goal_state, self.limit)
        return search_result


__all__ = ["RBFS", "PRBFS"]

from typing import Callable
import heapq

from algorithms.abstract_search import Result, SearchResult, InformedSearchAlgorithm
from node import Node
from state import State


class IDA(InformedSearchAlgorithm):
    def __init__(self, heuristic: Callable[[State, State], int]) -> None:
        super().__init__(heuristic)

    def _search(self, start_state: State) -> SearchResult:
        pass


__all__ = ["IDA"]

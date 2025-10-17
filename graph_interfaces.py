
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Iterable, Hashable, List, Dict


Vertex = Hashable


class GraphInterface(ABC):

    @abstractmethod
    def add_vertex(self, v: Vertex) -> None:
        raise NotImplementedError

    @abstractmethod
    def add_edge(self, src: Vertex, dst: Vertex) -> None:
        raise NotImplementedError

    @abstractmethod
    def vertices(self) -> List[Vertex]:
        raise NotImplementedError

    @abstractmethod
    def neighbors(self, v: Vertex) -> List[Vertex]:
        raise NotImplementedError

    @abstractmethod
    def has_vertex(self, v: Vertex) -> bool:
        raise NotImplementedError

    @abstractmethod
    def has_edge(self, src: Vertex, dst: Vertex) -> bool:
        raise NotImplementedError


class TraversalInterface(ABC):
    @abstractmethod
    def bfs(self, start: Vertex) -> List[Vertex]:
        raise NotImplementedError

    @abstractmethod
    def dfs(self, start: Vertex) -> List[Vertex]:
        """Depth-First Search (iterative) pre-order visit order starting at *start*."""
        raise NotImplementedError

"""Graph Interfaces for a directed graph implementation.

These abstract base classes define the required surface for the assignment.
If you're using a different language, create analogous interfaces.
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Iterable, Hashable, List, Dict


Vertex = Hashable


class GraphInterface(ABC):
    """Minimal interface for a directed graph."""

    @abstractmethod
    def add_vertex(self, v: Vertex) -> None:
        """Add a vertex to the graph (no-op if it exists)."""
        raise NotImplementedError

    @abstractmethod
    def add_edge(self, src: Vertex, dst: Vertex) -> None:
        """Add a directed edge from *src* to *dst*. Vertices are created if needed."""
        raise NotImplementedError

    @abstractmethod
    def vertices(self) -> List[Vertex]:
        """Return all vertices (order not guaranteed)."""
        raise NotImplementedError

    @abstractmethod
    def neighbors(self, v: Vertex) -> List[Vertex]:
        """Return the outbound neighbors of *v* (raise KeyError if *v* not present)."""
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
        """Breadth-First Search visit order starting at *start*."""
        raise NotImplementedError

    @abstractmethod
    def dfs(self, start: Vertex) -> List[Vertex]:
        """Depth-First Search (iterative) pre-order visit order starting at *start*."""
        raise NotImplementedError

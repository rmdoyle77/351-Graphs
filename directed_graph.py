"""Directed graph implementation that satisfies the provided interfaces."""
from __future__ import annotations
from typing import Dict, List, Set, Hashable
from collections import deque

from graph_interfaces import GraphInterface, TraversalInterface, Vertex


class DirectedGraph(GraphInterface, TraversalInterface):
    def __init__(self) -> None:
        # adjacency list: vertex -> sorted list of neighbors (kept stable insertion order)
        self._adj: Dict[Vertex, List[Vertex]] = {}

    # --- GraphInterface ---
    def add_vertex(self, v: Vertex) -> None:
        if v not in self._adj:
            self._adj[v] = []

    def add_edge(self, src: Vertex, dst: Vertex) -> None:
        if src not in self._adj:
            self._adj[src] = []
        if dst not in self._adj:
            self._adj[dst] = []
        # prevent duplicates while preserving order
        if dst not in self._adj[src]:
            self._adj[src].append(dst)

    def vertices(self) -> List[Vertex]:
        return list(self._adj.keys())

    def neighbors(self, v: Vertex) -> List[Vertex]:
        if v not in self._adj:
            raise KeyError(f"Vertex {v!r} not in graph")
        return list(self._adj[v])

    def has_vertex(self, v: Vertex) -> bool:
        return v in self._adj

    def has_edge(self, src: Vertex, dst: Vertex) -> bool:
        return src in self._adj and dst in self._adj[src]

    # --- TraversalInterface ---
    def bfs(self, start: Vertex) -> List[Vertex]:
        if start not in self._adj:
            raise KeyError(f"Start vertex {start!r} not in graph")
        order: List[Vertex] = []
        seen: Set[Vertex] = set([start])
        q = deque([start])
        while q:
            v = q.popleft()
            order.append(v)
            for w in self._adj[v]:
                if w not in seen:
                    seen.add(w)
                    q.append(w)
        return order

    def dfs(self, start: Vertex) -> List[Vertex]:
        if start not in self._adj:
            raise KeyError(f"Start vertex {start!r} not in graph")
        order: List[Vertex] = []
        seen: Set[Vertex] = set()
        stack: List[Vertex] = [start]
        while stack:
            v = stack.pop()
            if v in seen:
                continue
            seen.add(v)
            order.append(v)
            # push neighbors in reverse to visit in original insertion order
            nbrs = self._adj[v]
            for w in reversed(nbrs):
                if w not in seen:
                    stack.append(w)
        return order

# Graph

**Author:** Ryan Doyle


## Features

- Directed graph with adjacency-list internals
- Interfaces defined via `abc.ABC` (see `graph_interfaces.py`)
- Robust parser that accepts:
  - Edge lines as `A B` or `A->B`
  - `#` comments and blank lines are ignored
- BFS (queue-based) and DFS (iterative, stack-based) traversals



## Assumptions & Design Decisions

- Graph is directed. `add_edge(u, v)` does not imply `add_edge(v, u)`.
- Duplicate edges are ignored
- DFS is iterative to avoid recursion depth issues; it is pre-order and uses reverse push to
  produce a natural, readable order that respects insertion..
- File I/O errors (missing, unreadable) are surfaced with clear messages.
- Had AI Help in places I was stuck (mostly with edge's)


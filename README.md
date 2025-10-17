# Directed Graph (Python)

**Author:** Your Name Here

This repository implements a directed graph with a clear interface, a parser that loads
graph data from `sample_graph_data.txt`, and traversal algorithms **BFS** and **DFS**.
It includes a small CLI to run traversals and print visit order.

## Features

- Directed graph with adjacency-list internals
- Interfaces defined via `abc.ABC` (see `graph_interfaces.py`)
- Robust parser that accepts:
  - `V: A,B,C` vertex declaration (optional)
  - Edge lines as `A B` or `A->B`
  - `#` comments and blank lines are ignored
- BFS (queue-based) and DFS (iterative, stack-based) traversals
- Simple CLI (`main.py`) for running traversals and printing orders

## File Layout

```
graph_interfaces.py   # Interfaces (GraphInterface, TraversalInterface)
directed_graph.py     # Concrete DirectedGraph implementation
parser.py             # Parser for sample_graph_data.txt / graph.txt
sample_graph_data.txt # Sample graph
graph.txt             # Alias sample also included to match assignment text
main.py               # CLI entrypoint
```

## How to Run

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
python main.py --file sample_graph_data.txt --start A --algo both
```

Options:
- `--file` path to data file (default: `sample_graph_data.txt`)
- `--start` starting vertex label (default: `A`)
- `--algo` one of `bfs`, `dfs`, `both`

## Sample Data Format

```
# Sample directed graph
V: A, B, C, D, E, F
# Edges (you can mix 'A B' and 'A->B' styles)
A B
A C
B D
C D
D E
E F
C F
```

## Output: DFS

Command:
```bash
python main.py --algo dfs
```

Output:
```
DFS order: A B D E F C
```

## Output: BFS

Command:
```bash
python main.py --algo bfs
```

Output:
```
BFS order: A B C D F E
```

## Assumptions & Design Decisions

- Graph is **directed**. `add_edge(u, v)` does *not* imply `add_edge(v, u)`.
- Duplicate edges are ignored; vertex insertion order is preserved for neighbor visitation.
- DFS is iterative to avoid recursion depth issues; it is pre-order and uses reverse push to
  produce a natural, readable order that respects insertion.
- Parser is permissive and whitespace-tolerant. It raises on malformed edge lines.
- File I/O errors (missing, unreadable) are surfaced with clear messages.

## Tests (informal)

You can try different start nodes and files:
```bash
python main.py --file graph.txt --start C --algo both
```

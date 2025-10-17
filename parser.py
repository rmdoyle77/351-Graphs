
from __future__ import annotations
from typing import Iterable, Tuple
from directed_graph import DirectedGraph


def parse_graph_file(path: str) -> DirectedGraph:
    g = DirectedGraph()
    try:
        with open(path, 'r', encoding='utf-8') as f:
            for raw in f:
                line = raw.strip()
                if not line or line.startswith('#'):
                    continue
                if line.startswith('V:') or line.startswith('v:'):
                    verts_part = line.split(':', 1)[1]
                    tokens = [t.strip() for t in verts_part.replace(',', ' ').split() if t.strip()]
                    for t in tokens:
                        g.add_vertex(t)
                    continue
                if '->' in line:
                    src, dst = [t.strip() for t in line.split('->', 1)]
                else:
                    parts = line.split()
                    if len(parts) != 2:
                        raise ValueError(f"Invalid edge line: {line!r}")
                    src, dst = parts
                g.add_edge(src, dst)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Graph data file not found: {path}") from e
    except OSError as e:
        raise OSError(f"Error reading file {path}: {e}") from e
    return g

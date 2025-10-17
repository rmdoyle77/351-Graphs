from __future__ import annotations
import argparse
from parser import parse_graph_file

def main():
    ap = argparse.ArgumentParser(description='Directed Graph: BFS & DFS')
    ap.add_argument('--file', default='sample_graph_data.txt', help='Path to graph data file')
    ap.add_argument('--start', default='A', help='Start vertex for traversals')
    ap.add_argument('--algo', choices=['bfs','dfs','both'], default='both', help='Which traversal to run')
    args = ap.parse_args()

    g = parse_graph_file(args.file)

    if args.algo in ('bfs','both'):
        bfs_order = g.bfs(args.start)
        print('BFS order:', ' '.join(map(str, bfs_order)))
    if args.algo in ('dfs','both'):
        dfs_order = g.dfs(args.start)
        print('DFS order:', ' '.join(map(str, dfs_order)))

if __name__ == '__main__':
    main()

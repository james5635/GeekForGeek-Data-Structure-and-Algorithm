"""
Karger's Algorithm for Minimum Cut.

Randomized algorithm to find minimum cut in undirected graphs. Contracts random edges until 2 vertices remain. Run multiple times for reliable results.

Based on: https://www.geeksforgeeks.org/kargers-algorithm-for-minimum-cut-set-1-introduction-and-implementation/
"""

import random
from typing import List


class Edge:
    def __init__(self, src: int, dest: int):
        self.src = src
        self.dest = dest


class Graph:
    def __init__(self, num_vertices: int, edges: List[Edge]):
        self.V = num_vertices
        self.edges = edges.copy()


def find(subsets: List[List[int]], i: int) -> int:
    if subsets[i][0] != i:
        subsets[i][0] = find(subsets, subsets[i][0])
    return subsets[i][0]


def union(subsets: List[List[int]], x: int, y: int) -> None:
    x_root = find(subsets, x)
    y_root = find(subsets, y)
    if subsets[x_root][1] < subsets[y_root][1]:
        subsets[x_root][0] = y_root
    elif subsets[x_root][1] > subsets[y_root][1]:
        subsets[y_root][0] = x_root
    else:
        subsets[y_root][0] = x_root
        subsets[x_root][1] += 1


def karger_min_cut(graph: Graph, iterations: int = 1000) -> int:
    """Run Karger's algorithm multiple times to find minimum cut."""
    min_cut = float("inf")
    for _ in range(iterations):
        current_edges = graph.edges.copy()
        subsets = [[i, 0] for i in range(graph.V)]
        vertices = graph.V

        while vertices > 2:
            idx = random.randint(0, len(current_edges) - 1)
            edge = current_edges[idx]
            src_root = find(subsets, edge.src)
            dest_root = find(subsets, edge.dest)
            if src_root == dest_root:
                continue
            union(subsets, src_root, dest_root)
            vertices -= 1

        cut_edges = 0
        for edge in current_edges:
            if find(subsets, edge.src) != find(subsets, edge.dest):
                cut_edges += 1
        min_cut = min(min_cut, cut_edges)
    return min_cut


if __name__ == "__main__":
    edges = [Edge(0, 1), Edge(0, 2), Edge(0, 3), Edge(1, 3), Edge(2, 3)]
    graph = Graph(4, edges)
    print(f"Minimum cut (Karger's): {karger_min_cut(graph)}")  # Output: ~2

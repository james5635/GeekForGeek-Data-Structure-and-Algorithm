"""
Prim's Minimum Spanning Tree (MST) Algorithm

Prim's algorithm is a greedy algorithm that finds the Minimum Spanning Tree (MST)
of a connected, undirected, weighted graph. The MST is a subset of edges that
connects all vertices with the minimum possible total edge weight.

Algorithm:
1. Start with an arbitrary vertex and add it to the MST set.
2. Maintain a priority queue of edges connecting MST vertices to non-MST vertices.
3. Repeatedly extract the minimum weight edge from the priority queue.
4. If the edge connects to a vertex not yet in the MST, add it to the MST.
5. Continue until all vertices are included in the MST.

Time Complexity: O((V + E) log V) using a binary heap
Space Complexity: O(V + E)
"""

import heapq
from typing import List, Tuple


class Graph:
    """Represents an undirected weighted graph using adjacency list."""

    def __init__(self, vertices: int) -> None:
        """
        Initialize the graph.

        Args:
            vertices: Number of vertices in the graph.
        """
        self.V = vertices
        self.adj: List[List[Tuple[int, int]]] = [[] for _ in range(vertices)]

    def add_edge(self, u: int, v: int, w: int) -> None:
        """
        Add an undirected edge to the graph.

        Args:
            u: First vertex.
            v: Second vertex.
            w: Weight of the edge.
        """
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))

    def prim_mst(self) -> List[Tuple[int, int, int]]:
        """
        Find the Minimum Spanning Tree using Prim's algorithm.

        Returns:
            List of tuples (u, v, weight) representing edges in the MST.
        """
        mst_edges: List[Tuple[int, int, int]] = []
        in_mst: List[bool] = [False] * self.V
        parent: List[int] = [-1] * self.V

        # Min-heap storing (weight, vertex)
        pq: List[Tuple[int, int]] = [(0, 0)]  # Start from vertex 0

        while pq:
            weight, u = heapq.heappop(pq)

            if in_mst[u]:
                continue

            in_mst[u] = True

            if parent[u] != -1:
                mst_edges.append((parent[u], u, weight))

            for v, w in self.adj[u]:
                if not in_mst[v]:
                    heapq.heappush(pq, (w, v))
                    parent[v] = u

        return mst_edges

    def mst_weight(self) -> int:
        """
        Calculate the total weight of the MST.

        Returns:
            Total weight of the Minimum Spanning Tree.
        """
        edges = self.prim_mst()
        return sum(w for _, _, w in edges)


def prims_mst(
    num_vertices: int, edges: List[Tuple[int, int, int]]
) -> List[Tuple[int, int, int]]:
    """
    Find MST using Prim's algorithm (convenience function).

    Args:
        num_vertices: Number of vertices in the graph.
        edges: List of tuples (u, v, weight) representing graph edges.

    Returns:
        List of tuples (u, v, weight) representing edges in the MST.
    """
    g = Graph(num_vertices)
    for u, v, w in edges:
        g.add_edge(u, v, w)
    return g.prim_mst()


if __name__ == "__main__":
    # Example 1: Graph from GeeksforGeeks
    V = 5
    g = Graph(V)
    g.add_edge(0, 1, 2)
    g.add_edge(0, 3, 6)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 8)
    g.add_edge(1, 4, 5)
    g.add_edge(2, 4, 7)
    g.add_edge(3, 4, 9)

    print("=" * 50)
    print("Prim's MST Algorithm - Example 1")
    print("=" * 50)
    mst_edges = g.prim_mst()
    print("Edges in MST:")
    total_weight = 0
    for u, v, w in mst_edges:
        print(f"  {u} -- {v} == {w}")
        total_weight += w
    print(f"Total MST Weight: {total_weight}")

    # Example 2: Using convenience function
    print("\n" + "=" * 50)
    print("Prim's MST Algorithm - Example 2")
    print("=" * 50)
    edges_list = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
    mst = prims_mst(4, edges_list)
    print("Edges in MST:")
    for u, v, w in mst:
        print(f"  {u} -- {v} == {w}")
    print(f"Total MST Weight: {sum(w for _, _, w in mst)}")

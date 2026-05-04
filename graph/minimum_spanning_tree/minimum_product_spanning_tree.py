"""
Minimum Product Spanning Tree

The Minimum Product Spanning Tree is a spanning tree where the product of all
edge weights is minimized (instead of the sum as in standard MST).

Key Insight:
Using the logarithm property: log(w1 * w2 * ... * wN) = log(w1) + log(w2) + ... + log(wN)

We can convert each edge weight to its logarithm, then apply any standard MST
algorithm (Prim's or Kruskal's) on the transformed graph. Minimizing the sum of
logarithms is equivalent to minimizing the product of original weights.

Note: This algorithm assumes all edge weights are positive (as log is undefined
for zero or negative values).

Algorithm:
1. Transform each edge weight w to log(w).
2. Apply Prim's MST algorithm on the transformed graph.
3. The resulting MST minimizes the product of original edge weights.

Time Complexity: O(V^2) for adjacency matrix implementation
Space Complexity: O(V^2)
"""

import math
from typing import List, Tuple


class MinimumProductSpanningTree:
    """Find the Minimum Product Spanning Tree of a weighted graph."""

    def __init__(self, graph: List[List[int]]) -> None:
        """
        Initialize with an adjacency matrix representation.

        Args:
            graph: Adjacency matrix where graph[i][j] is the weight of edge (i, j).
                   Use 0 to indicate no edge.
        """
        self.V = len(graph)
        self.graph = graph

    def _min_key(self, key: List[float], mst_set: List[bool]) -> int:
        """
        Find the vertex with minimum key value not yet included in MST.

        Args:
            key: Key values for each vertex.
            mst_set: Boolean array indicating if vertex is in MST.

        Returns:
            Index of vertex with minimum key.
        """
        min_val = float("inf")
        min_index = 0

        for v in range(self.V):
            if not mst_set[v] and key[v] < min_val:
                min_val = key[v]
                min_index = v

        return min_index

    def find_minimum_product_mst(self) -> Tuple[List[Tuple[int, int, int]], int]:
        """
        Find the Minimum Product Spanning Tree using Prim's algorithm on log-transformed weights.

        Returns:
            Tuple of (mst_edges, min_product) where mst_edges is a list of
            (u, v, weight) tuples and min_product is the product of all edge weights.
        """
        # Transform graph using logarithms
        log_graph: List[List[float]] = [[0.0] * self.V for _ in range(self.V)]
        for i in range(self.V):
            for j in range(self.V):
                if self.graph[i][j] > 0:
                    log_graph[i][j] = math.log(self.graph[i][j])

        # Prim's MST on the log-transformed graph
        parent: List[int] = [-1] * self.V
        key: List[float] = [float("inf")] * self.V
        mst_set: List[bool] = [False] * self.V

        key[0] = 0  # Start from vertex 0

        for _ in range(self.V - 1):
            u = self._min_key(key, mst_set)
            mst_set[u] = True

            for v in range(self.V):
                if log_graph[u][v] > 0 and not mst_set[v] and log_graph[u][v] < key[v]:
                    parent[v] = u
                    key[v] = log_graph[u][v]

        # Build MST edges and calculate product
        mst_edges: List[Tuple[int, int, int]] = []
        min_product = 1

        for i in range(1, self.V):
            u, v = parent[i], i
            w = self.graph[u][v]
            mst_edges.append((u, v, w))
            min_product *= w

        return mst_edges, min_product

    def display_mst(self) -> None:
        """Print the Minimum Product Spanning Tree."""
        mst_edges, min_product = self.find_minimum_product_mst()
        print("Edge    Weight")
        for u, v, w in mst_edges:
            print(f"{u}  -  {v}    {w}")
        print(f"Minimum Obtainable Product: {min_product}")


def minimum_product_mst(
    adjacency_matrix: List[List[int]],
) -> Tuple[List[Tuple[int, int, int]], int]:
    """
    Find the Minimum Product Spanning Tree (convenience function).

    Args:
        adjacency_matrix: Adjacency matrix with edge weights (0 = no edge).

    Returns:
        Tuple of (mst_edges, min_product).
    """
    mpst = MinimumProductSpanningTree(adjacency_matrix)
    return mpst.find_minimum_product_mst()


if __name__ == "__main__":
    # Example 1: Standard example from GeeksforGeeks
    print("=" * 50)
    print("Minimum Product Spanning Tree - Example 1")
    print("=" * 50)
    graph = [
        [0, 2, 0, 6, 0],
        [2, 0, 3, 8, 5],
        [0, 3, 0, 0, 7],
        [6, 8, 0, 0, 9],
        [0, 5, 7, 9, 0],
    ]

    mpst = MinimumProductSpanningTree(graph)
    mpst.display_mst()

    # Example 2: Smaller graph
    print("\n" + "=" * 50)
    print("Minimum Product Spanning Tree - Example 2")
    print("=" * 50)
    graph2 = [
        [0, 3, 0, 1],
        [3, 0, 2, 5],
        [0, 2, 0, 4],
        [1, 5, 4, 0],
    ]

    mst_edges, product = minimum_product_mst(graph2)
    print("Edge    Weight")
    for u, v, w in mst_edges:
        print(f"{u}  -  {v}    {w}")
    print(f"Minimum Obtainable Product: {product}")

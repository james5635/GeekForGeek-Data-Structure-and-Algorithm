"""
Vertex Cover Problem - Approximate Solution

A vertex cover of an undirected graph is a subset of its vertices such that
for every edge (u, v) of the graph, either 'u' or 'v' is in the vertex cover.

The Vertex Cover problem is to find the minimum size vertex cover.
This is an NP-Complete problem, so we implement an approximate greedy algorithm
that finds a vertex cover at most twice the size of the optimal solution.

Algorithm (2-Approximate):
1. Initialize result as empty set
2. Consider all edges one by one
3. Pick an edge (u, v) where both endpoints are not yet in cover
4. Add both u and v to cover
5. Remove all edges incident on u or v
6. Repeat until all edges are covered

Reference: https://www.geeksforgeeks.org/vertex-cover-problem-set-1-introduction-approximate-algorithm/
"""

from typing import List, Set, Tuple, Dict
from collections import defaultdict


def vertex_cover_approx(edges: List[Tuple[int, int]], n: int) -> List[int]:
    """
    Find an approximate vertex cover using greedy approach.

    Args:
        edges: List of edges as (u, v) tuples.
        n: Number of vertices (0 to n-1).

    Returns:
        List of vertices forming the approximate vertex cover.

    Time Complexity: O(V + E)
    Space Complexity: O(V)
    """
    # Build adjacency list
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # Track visited vertices (in vertex cover)
    visited = [False] * n

    # Consider all edges
    for u in range(n):
        if not visited[u]:
            for v in adj[u]:
                if not visited[v]:
                    # Found an edge where neither endpoint is in cover
                    # Add both to cover
                    visited[u] = True
                    visited[v] = True
                    break

    # Return vertices in the cover
    return [i for i in range(n) if visited[i]]


def vertex_cover_approx_edges(edges: List[Tuple[int, int]], n: int) -> List[int]:
    """
    Alternative implementation working directly with edge set.

    Args:
        edges: List of edges as (u, v) tuples.
        n: Number of vertices (0 to n-1).

    Returns:
        List of vertices forming the approximate vertex cover.
    """
    visited = [False] * n
    remaining_edges = set(edges)

    while remaining_edges:
        # Pick an arbitrary edge
        u, v = remaining_edges.pop()

        if not visited[u] and not visited[v]:
            visited[u] = True
            visited[v] = True

            # Remove all edges incident on u or v
            remaining_edges = {
                (a, b)
                for a, b in remaining_edges
                if a != u and a != v and b != u and b != v
            }

    return [i for i in range(n) if visited[i]]


class VertexCover:
    """
    A class-based implementation for Vertex Cover problem.

    Attributes:
        n: Number of vertices.
        edges: List of edges.
        adj: Adjacency list representation.
    """

    def __init__(self, vertices: int, edges: List[Tuple[int, int]]) -> None:
        """
        Initialize Vertex Cover solver.

        Args:
            vertices: Number of vertices.
            edges: List of edges as (u, v) tuples.
        """
        self.n = vertices
        self.edges = edges
        self.adj = defaultdict(list)
        for u, v in edges:
            self.adj[u].append(v)
            self.adj[v].append(u)

    def approximate_cover(self) -> List[int]:
        """Find approximate vertex cover using greedy algorithm."""
        visited = [False] * self.n

        for u in range(self.n):
            if not visited[u]:
                for v in self.adj[u]:
                    if not visited[v]:
                        visited[u] = True
                        visited[v] = True
                        break

        return [i for i in range(self.n) if visited[i]]

    def is_valid_cover(self, cover: List[int]) -> bool:
        """
        Verify if a given set of vertices forms a valid vertex cover.

        Args:
            cover: List of vertices to check.

        Returns:
            True if cover is valid, False otherwise.
        """
        cover_set = set(cover)
        for u, v in self.edges:
            if u not in cover_set and v not in cover_set:
                return False
        return True


if __name__ == "__main__":
    # Example from GeeksforGeeks
    print("Vertex Cover Problem - Approximate Solution")
    print("=" * 50)

    # Create graph with 7 vertices
    # Edges: 0-1, 0-2, 1-3, 3-4, 4-5, 5-6
    n = 7
    edges = [(0, 1), (0, 2), (1, 3), (3, 4), (4, 5), (5, 6)]

    print(f"Number of vertices: {n}")
    print(f"Edges: {edges}")
    print()

    # Find approximate vertex cover
    cover = vertex_cover_approx(edges, n)
    print(f"Approximate Vertex Cover: {cover}")
    print(f"Size of cover: {len(cover)}")
    print()

    # Verify using class-based implementation
    vc = VertexCover(n, edges)
    cover2 = vc.approximate_cover()
    print(f"Class-based Vertex Cover: {cover2}")
    print(f"Is valid cover: {vc.is_valid_cover(cover2)}")
    print()

    # Another example
    print("Another Example:")
    print("-" * 30)
    n2 = 5
    edges2 = [(0, 1), (0, 2), (1, 3), (2, 3), (2, 4), (3, 4)]
    print(f"Edges: {edges2}")

    vc2 = VertexCover(n2, edges2)
    cover3 = vc2.approximate_cover()
    print(f"Vertex Cover: {cover3}")
    print(f"Size: {len(cover3)}")
    print(f"Is valid cover: {vc2.is_valid_cover(cover3)}")

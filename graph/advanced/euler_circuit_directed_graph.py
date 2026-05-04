"""
Euler Circuit in a Directed Graph

A directed graph has an Eulerian circuit if and only if:
1. All vertices with nonzero degree belong to a single strongly connected component
2. In-degree equals out-degree for every vertex

This implementation uses Kosaraju's algorithm to check strong connectivity
and degree comparison for the Eulerian circuit condition.

Time Complexity: O(V + E)
Space Complexity: O(V)
"""

from typing import List
from collections import defaultdict


class DirectedEulerGraph:
    """Directed graph with Eulerian circuit detection."""

    def __init__(self, num_vertices: int):
        self.num_vertices = num_vertices
        self.adj: List[List[int]] = [[] for _ in range(num_vertices)]
        self.in_degree = [0] * num_vertices

    def add_edge(self, u: int, v: int) -> None:
        """Add directed edge u -> v."""
        self.adj[u].append(v)
        self.in_degree[v] += 1

    def _dfs(self, v: int, visited: List[bool]) -> None:
        """DFS traversal."""
        visited[v] = True
        for neighbor in self.adj[v]:
            if not visited[neighbor]:
                self._dfs(neighbor, visited)

    def _get_transpose(self) -> "DirectedEulerGraph":
        """Get the transpose (reversed) graph."""
        gt = DirectedEulerGraph(self.num_vertices)
        for u in range(self.num_vertices):
            for v in self.adj[u]:
                gt.add_edge(v, u)
        return gt

    def _is_strongly_connected(self) -> bool:
        """
        Check if all non-zero degree vertices are strongly connected.

        Uses Kosaraju's simplified approach:
        1. DFS from a non-zero degree vertex on original graph
        2. DFS from same vertex on transposed graph
        Both must visit all non-zero degree vertices.
        """
        visited = [False] * self.num_vertices

        # Find first vertex with non-zero out-degree
        start = 0
        for i in range(self.num_vertices):
            if len(self.adj[i]) > 0:
                start = i
                break
        else:
            return True  # No edges, trivially connected

        # DFS on original graph
        self._dfs(start, visited)

        # Check all non-zero degree vertices are visited
        for i in range(self.num_vertices):
            if len(self.adj[i]) > 0 and not visited[i]:
                return False

        # DFS on transposed graph
        gt = self._get_transpose()
        visited = [False] * self.num_vertices
        gt._dfs(start, visited)

        for i in range(self.num_vertices):
            if len(self.adj[i]) > 0 and not visited[i]:
                return False

        return True

    def is_eulerian_cycle(self) -> bool:
        """
        Check if the directed graph has an Eulerian circuit.

        Returns:
            True if Eulerian circuit exists, False otherwise
        """
        # Check strong connectivity of non-zero degree vertices
        if not self._is_strongly_connected():
            return False

        # Check in-degree equals out-degree for all vertices
        for v in range(self.num_vertices):
            out_degree = len(self.adj[v])
            if out_degree != self.in_degree[v]:
                return False

        return True

    def is_eulerian_path(self) -> bool:
        """
        Check if the directed graph has an Eulerian path (not necessarily a circuit).

        Conditions:
        - At most one vertex has out_degree - in_degree = 1 (start)
        - At most one vertex has in_degree - out_degree = 1 (end)
        - All other vertices have equal in/out degree
        - Underlying undirected graph is connected

        Returns:
            True if Eulerian path exists
        """
        plus_one = 0  # vertices with out - in = 1
        minus_one = 0  # vertices with in - out = 1

        for v in range(self.num_vertices):
            diff = len(self.adj[v]) - self.in_degree[v]
            if diff == 1:
                plus_one += 1
            elif diff == -1:
                minus_one += 1
            elif diff != 0:
                return False

        return plus_one <= 1 and minus_one <= 1


def check_eulerian_directed(num_vertices: int, edges: List[List[int]]) -> str:
    """
    Check Eulerian property of a directed graph.

    Args:
        num_vertices: Number of vertices
        edges: List of [u, v] directed edges

    Returns:
        'Eulerian Circuit', 'Eulerian Path', or 'Not Eulerian'
    """
    g = DirectedEulerGraph(num_vertices)
    for u, v in edges:
        g.add_edge(u, v)

    if g.is_eulerian_cycle():
        return "Eulerian Circuit"
    elif g.is_eulerian_path():
        return "Eulerian Path"
    return "Not Eulerian"


if __name__ == "__main__":
    # Example 1: Eulerian Circuit
    print("=== Example 1: Eulerian Circuit ===")
    g1 = DirectedEulerGraph(5)
    g1.add_edge(1, 0)
    g1.add_edge(0, 2)
    g1.add_edge(2, 1)
    g1.add_edge(0, 3)
    g1.add_edge(3, 4)
    g1.add_edge(4, 0)

    print(f"Has Eulerian Cycle: {g1.is_eulerian_cycle()}")

    # Example 2: Not Eulerian
    print("\n=== Example 2: Not Eulerian ===")
    g2 = DirectedEulerGraph(5)
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)
    g2.add_edge(2, 3)
    # Vertex 0: out=1, in=0 -> diff=1
    # Vertex 3: out=0, in=1 -> diff=-1
    # Not strongly connected (no path back)

    print(f"Has Eulerian Cycle: {g2.is_eulerian_cycle()}")
    print(f"Has Eulerian Path: {g2.is_eulerian_path()}")

    # Example 3: Functional check
    print("\n=== Example 3: Functional check ===")
    edges3 = [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4], [4, 1]]
    result = check_eulerian_directed(5, edges3)
    print(f"Result: {result}")

    # Example 4: Simple cycle
    print("\n=== Example 4: Simple cycle ===")
    edges4 = [[0, 1], [1, 2], [2, 0]]
    result4 = check_eulerian_directed(3, edges4)
    print(f"Result: {result4}")

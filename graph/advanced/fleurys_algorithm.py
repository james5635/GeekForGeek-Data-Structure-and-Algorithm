"""
Fleury's Algorithm for Printing Eulerian Path or Circuit

Fleury's algorithm prints an Eulerian trail or circuit by carefully
selecting edges during traversal, preferring non-bridge edges.

Algorithm:
1. Verify the graph has 0 or 2 vertices of odd degree
2. If 2 odd-degree vertices exist, start from one; otherwise start from any
3. At each step, choose an edge that is NOT a bridge (unless it's the only option)
4. Remove the chosen edge and continue until all edges are traversed

A bridge is an edge whose removal increases the number of connected components.

Time Complexity: O((V + E)^2) due to bridge detection at each step
Space Complexity: O(V + E)
"""

from typing import List, Tuple
from collections import defaultdict
import copy


class FleuryEulerian:
    """Find Eulerian path/circuit using Fleury's Algorithm."""

    def __init__(self, num_vertices: int):
        self.num_vertices = num_vertices
        self.adj: List[List[int]] = [[] for _ in range(num_vertices)]

    def add_edge(self, u: int, v: int) -> None:
        """Add undirected edge."""
        self.adj[u].append(v)
        self.adj[v].append(u)

    def _remove_edge(self, u: int, v: int) -> None:
        """Remove edge u-v from adjacency list."""
        self.adj[u].remove(v)
        self.adj[v].remove(u)

    def _count_reachable(self, start: int) -> int:
        """Count vertices reachable from start using DFS."""
        visited = [False] * self.num_vertices
        stack = [start]
        visited[start] = True
        count = 0

        while stack:
            node = stack.pop()
            count += 1
            for neighbor in self.adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append(neighbor)

        return count

    def _is_valid_next_edge(self, u: int, v: int) -> bool:
        """
        Check if edge (u, v) is a valid next edge (not a bridge).

        An edge is a bridge if removing it reduces the number of
        reachable vertices from u.
        """
        # If only one edge, it's always valid
        if len(self.adj[u]) == 1:
            return True

        # Count reachable vertices before removing edge
        count_before = self._count_reachable(u)

        # Remove edge temporarily
        self._remove_edge(u, v)

        # Count reachable vertices after removing edge
        count_after = self._count_reachable(u)

        # Restore edge
        self.adj[u].append(v)
        self.adj[v].append(u)

        # If counts are same, edge is not a bridge
        return count_before == count_after

    def _get_odd_degree_vertex(self) -> int:
        """Find a vertex with odd degree, or return 0."""
        for i in range(self.num_vertices):
            if len(self.adj[i]) % 2 != 0:
                return i
        return 0

    def find_euler_tour(self) -> List[Tuple[int, int]]:
        """
        Find Eulerian tour/path using Fleury's algorithm.

        Returns:
            List of edges (u, v) in the Eulerian tour
        """
        start = self._get_odd_degree_vertex()
        edges = []
        self._get_euler_util(start, edges)
        return edges

    def _get_euler_util(self, u: int, edges: List[Tuple[int, int]]) -> None:
        """Recursive helper to find Eulerian path."""
        for i in range(len(self.adj[u])):
            next_v = self.adj[u][i]
            if self._is_valid_next_edge(u, next_v):
                edges.append((u, next_v))
                self._remove_edge(u, next_v)
                self._get_euler_util(next_v, edges)
                break


def fleury_eulerian_path(
    num_vertices: int, edges: List[Tuple[int, int]]
) -> List[Tuple[int, int]]:
    """
    Functional version: find Eulerian path using Fleury's algorithm.

    Args:
        num_vertices: Number of vertices
        edges: List of undirected edge tuples

    Returns:
        List of edges in Eulerian path order
    """
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    def remove_edge(u, v):
        adj[u].remove(v)
        adj[v].remove(u)

    def count_reachable(start):
        visited = set()
        stack = [start]
        visited.add(start)
        while stack:
            node = stack.pop()
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
        return len(visited)

    def is_bridge(u, v):
        if len(adj[u]) == 1:
            return True
        count_before = count_reachable(u)
        remove_edge(u, v)
        count_after = count_reachable(u)
        adj[u].append(v)
        adj[v].append(u)
        return count_before != count_after

    # Find start vertex
    start = 0
    all_vertices = set()
    for u, v in edges:
        all_vertices.add(u)
        all_vertices.add(v)
    for v in all_vertices:
        if len(adj[v]) % 2 != 0:
            start = v
            break

    euler_path = []
    current = start

    while adj[current]:
        next_v = None
        for neighbor in adj[current]:
            if not is_bridge(current, neighbor):
                next_v = neighbor
                break
        if next_v is None:
            next_v = adj[current][0]

        euler_path.append((current, next_v))
        remove_edge(current, next_v)
        current = next_v

    return euler_path


if __name__ == "__main__":
    # Example 1: Eulerian Circuit
    print("=== Example 1: Eulerian Circuit ===")
    g = FleuryEulerian(4)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(0, 3)
    g.add_edge(3, 2)

    tour = g.find_euler_tour()
    print("Eulerian tour edges:")
    for u, v in tour:
        print(f"  {u} - {v}")
    print(f"Total edges: {len(tour)}")

    # Example 2: Functional version
    print("\n=== Example 2: Functional version ===")
    edges2 = [(0, 1), (1, 2), (2, 0), (0, 3), (3, 2)]
    path = fleury_eulerian_path(4, edges2)
    print("Eulerian path:")
    print(" -> ".join(f"{u}-{v}" for u, v in path))

    # Example 3: Eulerian Path (2 odd degree vertices)
    print("\n=== Example 3: Eulerian Path ===")
    edges3 = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 2)]
    path3 = fleury_eulerian_path(5, edges3)
    print("Eulerian path:")
    print(" -> ".join(f"{u}-{v}" for u, v in path3))
    print(f"Start: {path3[0][0]}, End: {path3[-1][1]}")

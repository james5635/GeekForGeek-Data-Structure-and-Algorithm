"""
Eulerian Path and Circuit

Eulerian Path: A path that visits every edge exactly once.
Eulerian Circuit: An Eulerian path that starts and ends at the same vertex.

Conditions for Undirected Graph:
- Eulerian Circuit: All vertices have even degree AND graph is connected
  (considering only non-zero degree vertices)
- Eulerian Path: Exactly 2 vertices have odd degree AND graph is connected
- Neither: More than 2 vertices have odd degree OR graph is disconnected

Conditions for Directed Graph:
- Eulerian Circuit: in_degree == out_degree for all vertices AND
  all non-zero degree vertices belong to single strongly connected component
- Eulerian Path: At most one vertex has (out_degree - in_degree) = 1,
  at most one vertex has (in_degree - out_degree) = 1, all others have
  equal in/out degree, and underlying undirected graph is connected

Time Complexity: O(V + E)
Space Complexity: O(V)
"""

from typing import List
from collections import defaultdict


def is_eulerian_undirected(num_vertices: int, adj: List[List[int]]) -> int:
    """
    Check if an undirected graph has Eulerian path or circuit.

    Args:
        num_vertices: Number of vertices
        adj: Adjacency list

    Returns:
        2 if Eulerian Circuit exists
        1 if Eulerian Path exists
        0 if neither
    """

    def dfs(node: int, visited: List[bool]) -> None:
        visited[node] = True
        for neighbor in adj[node]:
            if not visited[neighbor]:
                dfs(neighbor, visited)

    # Find first vertex with non-zero degree
    start = -1
    for i in range(num_vertices):
        if len(adj[i]) > 0:
            start = i
            break

    # No edges: trivially Eulerian
    if start == -1:
        return 2

    # Check connectivity of non-zero degree vertices
    visited = [False] * num_vertices
    dfs(start, visited)

    for i in range(num_vertices):
        if len(adj[i]) > 0 and not visited[i]:
            return 0  # Not connected

    # Count odd degree vertices
    odd_count = sum(1 for i in range(num_vertices) if len(adj[i]) % 2 != 0)

    if odd_count == 0:
        return 2  # Eulerian Circuit
    elif odd_count == 2:
        return 1  # Eulerian Path
    else:
        return 0  # Neither


class EulerianGraphUndirected:
    """Graph class with Eulerian path/circuit detection and finding."""

    def __init__(self):
        self.graph = defaultdict(list)
        self.edges_count = defaultdict(int)

    def add_edge(self, u: int, v: int) -> None:
        """Add undirected edge."""
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.edges_count[(min(u, v), max(u, v))] += 1

    def _remove_edge(self, u: int, v: int) -> None:
        """Remove one instance of edge u-v."""
        self.graph[u].remove(v)
        self.graph[v].remove(u)

    def _is_connected(self) -> bool:
        """Check if all non-zero degree vertices are connected."""
        visited = {node: False for node in self.graph}

        start = None
        for node in self.graph:
            if len(self.graph[node]) > 0:
                start = node
                break

        if start is None:
            return True

        stack = [start]
        visited[start] = True
        while stack:
            node = stack.pop()
            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append(neighbor)

        return all(not visited[node] or len(self.graph[node]) == 0 for node in visited)

    def is_eulerian(self) -> str:
        """
        Check Eulerian property.

        Returns:
            'Eulerian Circuit', 'Eulerian Path', or 'Not Eulerian'
        """
        if not self._is_connected():
            return "Not Eulerian"

        odd_degree = sum(1 for node in self.graph if len(self.graph[node]) % 2 != 0)

        if odd_degree == 0:
            return "Eulerian Circuit"
        elif odd_degree == 2:
            return "Eulerian Path"
        return "Not Eulerian"

    def _is_bridge(self, u: int, v: int) -> bool:
        """Check if edge (u, v) is a bridge."""
        self._remove_edge(u, v)
        visited = {node: False for node in self.graph}
        visited[u] = True
        stack = [u]
        while stack:
            node = stack.pop()
            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append(neighbor)

        self.graph[u].append(v)
        self.graph[v].append(u)

        return not visited[v]

    def find_eulerian_path(self) -> List[int]:
        """
        Find an Eulerian path using Fleury's algorithm.

        Returns:
            List of vertices in the Eulerian path
        """
        euler_type = self.is_eulerian()
        if euler_type == "Not Eulerian":
            return []

        # Find start vertex
        start = next(iter(self.graph))
        for node in self.graph:
            if len(self.graph[node]) % 2 != 0:
                start = node
                break

        path = [start]
        current = start

        while self.graph[current]:
            next_vertex = None
            if len(self.graph[current]) == 1:
                next_vertex = self.graph[current][0]
            else:
                for neighbor in self.graph[current]:
                    if not self._is_bridge(current, neighbor):
                        next_vertex = neighbor
                        break
                if next_vertex is None:
                    next_vertex = self.graph[current][0]

            path.append(next_vertex)
            self._remove_edge(current, next_vertex)
            current = next_vertex

        return path


if __name__ == "__main__":
    # Example 1: Eulerian Circuit (all even degrees)
    print("=== Example 1: Eulerian Circuit ===")
    adj1 = [
        [1, 2],  # vertex 0
        [0, 2],  # vertex 1
        [0, 1],  # vertex 2
    ]
    result = is_eulerian_undirected(3, adj1)
    labels = {0: "Neither", 1: "Eulerian Path", 2: "Eulerian Circuit"}
    print(f"Result: {labels[result]}")

    # Example 2: Eulerian Path (exactly 2 odd degree vertices)
    print("\n=== Example 2: Eulerian Path ===")
    adj2 = [
        [1, 2],  # vertex 0, degree 2
        [0, 2, 3],  # vertex 1, degree 3 (odd)
        [0, 1],  # vertex 2, degree 2
        [1, 4],  # vertex 3, degree 2
        [3],  # vertex 4, degree 1 (odd)
    ]
    result2 = is_eulerian_undirected(5, adj2)
    print(f"Result: {labels[result2]}")

    # Example 3: Using the class to find path
    print("\n=== Example 3: Find Eulerian Path ===")
    g = EulerianGraphUndirected()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)

    print(f"Eulerian type: {g.is_eulerian()}")
    path = g.find_eulerian_path()
    print(f"Eulerian Path: {path}")

    # Example 4: Not Eulerian (4 odd degree vertices)
    print("\n=== Example 4: Not Eulerian ===")
    adj4 = [
        [1],  # degree 1 (odd)
        [0, 2],  # degree 2
        [1, 3],  # degree 2
        [2, 4],  # degree 2
        [3],  # degree 1 (odd)
    ]
    # Wait, this has only 2 odd degree vertices. Let me make 4 odd.
    adj4 = [
        [1, 2],  # degree 2
        [0, 2, 3],  # degree 3 (odd)
        [0, 1, 4],  # degree 3 (odd)
        [1],  # degree 1 (odd)
        [2],  # degree 1 (odd)
    ]
    result4 = is_eulerian_undirected(5, adj4)
    print(f"Result: {labels[result4]} (4 odd degree vertices)")

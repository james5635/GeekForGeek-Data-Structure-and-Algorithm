"""
Articulation Points (Cut Vertices) in a Graph

An articulation point (or cut vertex) is a vertex whose removal
(including all its incident edges) increases the number of connected components.

Tarjan's Algorithm:
- Use DFS to track discovery time (disc) and low-link value (low)
- A vertex u is an articulation point if:
  1. u is root of DFS tree and has more than one child, OR
  2. u is not root and has a child v such that low[v] >= disc[u]
     (meaning v's subtree has no back edge to an ancestor of u)

Time Complexity: O(V + E)
Space Complexity: O(V)
"""

from typing import List, Set


def find_articulation_points(num_vertices: int, edges: List[List[int]]) -> List[int]:
    """
    Find all articulation points in an undirected graph.

    Args:
        num_vertices: Number of vertices (0 to V-1)
        edges: List of undirected edges

    Returns:
        Sorted list of articulation points, or [-1] if none exist
    """
    # Build adjacency list
    adj: List[List[int]] = [[] for _ in range(num_vertices)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    disc = [-1] * num_vertices
    low = [-1] * num_vertices
    parent = [-1] * num_vertices
    is_ap = [False] * num_vertices
    timer = [0]

    def dfs(u: int) -> None:
        disc[u] = low[u] = timer[0]
        timer[0] += 1
        children = 0

        for v in adj[u]:
            if disc[v] == -1:  # v not visited
                children += 1
                parent[v] = u
                dfs(v)

                # Update low value
                low[u] = min(low[u], low[v])

                # Check AP condition for non-root
                if parent[u] != -1 and low[v] >= disc[u]:
                    is_ap[u] = True

            elif v != parent[u]:  # Back edge
                low[u] = min(low[u], disc[v])

        # Check AP condition for root
        if parent[u] == -1 and children > 1:
            is_ap[u] = True

    for i in range(num_vertices):
        if disc[i] == -1:
            dfs(i)

    result = [i for i in range(num_vertices) if is_ap[i]]
    return result if result else [-1]


class ArticulationPointFinder:
    """Object-oriented articulation point finder."""

    def __init__(self, num_vertices: int):
        self.num_vertices = num_vertices
        self.adj: List[List[int]] = [[] for _ in range(num_vertices)]

    def add_edge(self, u: int, v: int) -> None:
        """Add undirected edge."""
        self.adj[u].append(v)
        self.adj[v].append(u)

    def find_articulation_points(self) -> Set[int]:
        """
        Find all articulation points.

        Returns:
            Set of articulation point indices
        """
        disc = [-1] * self.num_vertices
        low = [-1] * self.num_vertices
        parent = [-1] * self.num_vertices
        ap_set: Set[int] = set()
        timer = [0]

        def dfs(u: int) -> None:
            disc[u] = low[u] = timer[0]
            timer[0] += 1
            children = 0

            for v in self.adj[u]:
                if disc[v] == -1:
                    children += 1
                    parent[v] = u
                    dfs(v)

                    low[u] = min(low[u], low[v])

                    if parent[u] != -1 and low[v] >= disc[u]:
                        ap_set.add(u)

                elif v != parent[u]:
                    low[u] = min(low[u], disc[v])

            if parent[u] == -1 and children > 1:
                ap_set.add(u)

        for i in range(self.num_vertices):
            if disc[i] == -1:
                dfs(i)

        return ap_set

    def is_articulation_point(self, vertex: int) -> bool:
        """Check if a specific vertex is an articulation point."""
        return vertex in self.find_articulation_points()

    def critical_vertices(self) -> List[int]:
        """Return sorted list of articulation points."""
        return sorted(self.find_articulation_points())


def naive_articulation_points(num_vertices: int, edges: List[List[int]]) -> List[int]:
    """
    Find articulation points using naive O(V * (V + E)) approach.

    For each vertex, remove it and check if the number of connected
    components increases.

    Args:
        num_vertices: Number of vertices
        edges: List of undirected edges

    Returns:
        List of articulation points
    """

    def count_components(excluded: int) -> int:
        """Count connected components excluding a vertex."""
        adj: List[List[int]] = [[] for _ in range(num_vertices)]
        for u, v in edges:
            if u == excluded or v == excluded:
                continue
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * num_vertices
        visited[excluded] = True  # Mark excluded as visited
        components = 0

        for i in range(num_vertices):
            if not visited[i]:
                components += 1
                stack = [i]
                visited[i] = True
                while stack:
                    node = stack.pop()
                    for neighbor in adj[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            stack.append(neighbor)

        return components

    # Count original components
    original = count_components(-1)
    result = []

    for v in range(num_vertices):
        if count_components(v) > original:
            result.append(v)

    return result if result else [-1]


if __name__ == "__main__":
    # Example 1: Basic articulation points
    print("=== Example 1: Basic Graph ===")
    edges1 = [
        [0, 1],
        [1, 2],
        [2, 0],  # Triangle
        [1, 3],  # Bridge
        [3, 4],
        [4, 5],
        [5, 3],  # Another triangle
    ]
    aps = find_articulation_points(6, edges1)
    print(f"Articulation points: {aps}")  # 1 and 3 are articulation points

    # Example 2: Class-based
    print("\n=== Example 2: Class-based ===")
    finder = ArticulationPointFinder(7)
    finder.add_edge(0, 1)
    finder.add_edge(1, 2)
    finder.add_edge(2, 3)
    finder.add_edge(3, 0)
    finder.add_edge(1, 4)
    finder.add_edge(4, 5)
    finder.add_edge(5, 6)

    aps2 = finder.critical_vertices()
    print(f"Articulation points: {aps2}")  # 1 and 4

    # Example 3: Naive approach (verification)
    print("\n=== Example 3: Naive Verification ===")
    aps_naive = naive_articulation_points(
        7, [[0, 1], [1, 2], [2, 3], [3, 0], [1, 4], [4, 5], [5, 6]]
    )
    print(f"Articulation points (naive): {aps_naive}")

    # Example 4: No articulation points (cycle)
    print("\n=== Example 4: No Articulation Points ===")
    edges4 = [[0, 1], [1, 2], [2, 3], [3, 0]]
    aps4 = find_articulation_points(4, edges4)
    print(f"Articulation points: {aps4}")  # [-1]

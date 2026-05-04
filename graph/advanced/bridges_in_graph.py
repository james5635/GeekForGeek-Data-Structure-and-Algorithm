"""
Bridges in a Graph

A bridge (or cut-edge) in an undirected graph is an edge whose removal
increases the number of connected components.

Tarjan's Bridge-Finding Algorithm:
- Use DFS to track discovery time (disc) and low-link value (low) for each vertex
- disc[u]: Time when vertex u was first visited
- low[u]: Earliest discovery time reachable from subtree rooted at u
- Edge (u, v) is a bridge if low[v] > disc[u]

Interpretation:
- low[v] > disc[u] means the subtree at v has no back edge to u or ancestors of u
- Removing (u, v) disconnects v's subtree from the rest

Time Complexity: O(V + E)
Space Complexity: O(V)
"""

from typing import List, Tuple


def find_bridges(num_vertices: int, edges: List[List[int]]) -> List[Tuple[int, int]]:
    """
    Find all bridges in an undirected graph.

    Args:
        num_vertices: Number of vertices (0 to V-1)
        edges: List of undirected edges

    Returns:
        List of bridges as (u, v) tuples with u < v
    """
    # Build adjacency list
    adj: List[List[int]] = [[] for _ in range(num_vertices)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    disc = [-1] * num_vertices
    low = [-1] * num_vertices
    parent = [-1] * num_vertices
    bridges: List[Tuple[int, int]] = []
    timer = [0]

    def dfs(u: int) -> None:
        disc[u] = low[u] = timer[0]
        timer[0] += 1

        for v in adj[u]:
            if disc[v] == -1:  # v not visited
                parent[v] = u
                dfs(v)

                # Update low value
                low[u] = min(low[u], low[v])

                # Check bridge condition
                if low[v] > disc[u]:
                    bridges.append((min(u, v), max(u, v)))

            elif v != parent[u]:  # Back edge
                low[u] = min(low[u], disc[v])

    for i in range(num_vertices):
        if disc[i] == -1:
            dfs(i)

    return bridges


class BridgeFinder:
    """Object-oriented bridge finder with iterative DFS."""

    def __init__(self, num_vertices: int):
        self.num_vertices = num_vertices
        self.adj: List[List[int]] = [[] for _ in range(num_vertices)]

    def add_edge(self, u: int, v: int) -> None:
        """Add undirected edge."""
        self.adj[u].append(v)
        self.adj[v].append(u)

    def find_bridges_iterative(self) -> List[Tuple[int, int]]:
        """
        Find bridges using iterative DFS to avoid recursion limits.

        Returns:
            List of bridges as (u, v) tuples
        """
        disc = [-1] * self.num_vertices
        low = [-1] * self.num_vertices
        parent = [-1] * self.num_vertices
        bridges: List[Tuple[int, int]] = []
        timer = 0

        for start in range(self.num_vertices):
            if disc[start] != -1:
                continue

            stack = [(start, iter(self.adj[start]))]
            disc[start] = low[start] = timer
            timer += 1

            while stack:
                u, children = stack[-1]

                try:
                    v = next(children)
                    if disc[v] == -1:
                        parent[v] = u
                        disc[v] = low[v] = timer
                        timer += 1
                        stack.append((v, iter(self.adj[v])))
                    elif v != parent[u]:
                        low[u] = min(low[u], disc[v])
                except StopIteration:
                    stack.pop()
                    if stack:
                        p = stack[-1][0]
                        low[p] = min(low[p], low[u])
                        if low[u] > disc[p]:
                            bridges.append((min(p, u), max(p, u)))

        return bridges


def is_bridge(num_vertices: int, edges: List[List[int]], u: int, v: int) -> bool:
    """
    Check if a specific edge is a bridge using BFS connectivity check.

    Args:
        num_vertices: Number of vertices
        edges: List of undirected edges
        u, v: Edge to check

    Returns:
        True if removing (u, v) disconnects the graph
    """
    # Build graph without the edge
    adj: List[List[int]] = [[] for _ in range(num_vertices)]
    for a, b in edges:
        if (a == u and b == v) or (a == v and b == u):
            continue
        adj[a].append(b)
        adj[b].append(a)

    # BFS from u
    visited = [False] * num_vertices
    queue = [u]
    visited[u] = True
    count = 0

    while queue:
        node = queue.pop(0)
        count += 1
        for neighbor in adj[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    # Count vertices with non-zero degree in original graph
    total_vertices_with_edges = set()
    for a, b in edges:
        total_vertices_with_edges.add(a)
        total_vertices_with_edges.add(b)

    return count < len(total_vertices_with_edges)


if __name__ == "__main__":
    # Example 1: Simple graph with bridges
    print("=== Example 1: Basic Bridges ===")
    edges1 = [
        [0, 1],
        [1, 2],
        [2, 0],  # Triangle (no bridges)
        [1, 3],  # Bridge
        [3, 4],
        [4, 5],  # Chain (bridges)
        [5, 3],  # Creates a cycle
    ]
    bridges = find_bridges(6, edges1)
    print(f"Bridges: {bridges}")

    # Example 2: Class-based iterative
    print("\n=== Example 2: Iterative DFS ===")
    finder = BridgeFinder(7)
    finder.add_edge(0, 1)
    finder.add_edge(1, 2)
    finder.add_edge(2, 0)
    finder.add_edge(1, 3)
    finder.add_edge(3, 4)
    finder.add_edge(4, 5)
    finder.add_edge(5, 6)

    bridges2 = finder.find_bridges_iterative()
    print(f"Bridges: {bridges2}")

    # Example 3: Check specific edge
    print("\n=== Example 3: Check Specific Edge ===")
    edges3 = [[0, 1], [1, 2], [2, 3], [3, 4]]
    print(f"Is (1,2) a bridge? {is_bridge(5, edges3, 1, 2)}")
    print(f"Is (0,1) a bridge? {is_bridge(5, edges3, 0, 1)}")

    # Example 4: Graph with no bridges
    print("\n=== Example 4: No Bridges (complete graph) ===")
    edges4 = [[0, 1], [0, 2], [1, 2]]
    bridges4 = find_bridges(3, edges4)
    print(f"Bridges: {bridges4}")  # Empty

"""
Longest Path in a Directed Acyclic Graph (DAG)

Given a weighted DAG, find the longest path from a given source vertex
to all other vertices.

Approach:
- Use topological sort to process vertices in linear order
- For each vertex in topo order, relax all outgoing edges (like Bellman-Ford
  but in topological order, so one pass is enough)
- Initialize distances to -infinity, source to 0

Time Complexity: O(V + E)
Space Complexity: O(V)
"""

import sys
from typing import List, Tuple, Optional


def longest_path_dag(
    num_vertices: int, edges: List[Tuple[int, int, int]], source: int
) -> List[Optional[int]]:
    """
    Find longest paths from source to all vertices in a weighted DAG.

    Args:
        num_vertices: Number of vertices (0 to V-1)
        edges: List of (u, v, weight) tuples for directed edges
        source: Source vertex

    Returns:
        List where index i contains longest distance from source to vertex i,
        or None if vertex is unreachable
    """
    # Build adjacency list
    adj: List[List[Tuple[int, int]]] = [[] for _ in range(num_vertices)]
    indegree = [0] * num_vertices

    for u, v, w in edges:
        adj[u].append((v, w))
        indegree[v] += 1

    # Topological sort using Kahn's algorithm
    queue = [i for i in range(num_vertices) if indegree[i] == 0]
    topo_order = []

    while queue:
        u = queue.pop(0)
        topo_order.append(u)
        for v, _ in adj[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)

    # Initialize distances
    dist: List[Optional[int]] = [None] * num_vertices
    dist[source] = 0

    # Process vertices in topological order
    for u in topo_order:
        if dist[u] is not None:
            for v, weight in adj[u]:
                new_dist = dist[u] + weight
                if dist[v] is None or new_dist > dist[v]:
                    dist[v] = new_dist

    return dist


def longest_path_between(
    num_vertices: int, edges: List[Tuple[int, int, int]], src: int, dest: int
) -> Optional[int]:
    """
    Find the longest path from src to dest in a weighted DAG.

    Args:
        num_vertices: Number of vertices
        edges: List of (u, v, weight) tuples
        src: Source vertex
        dest: Destination vertex

    Returns:
        Longest path weight, or None if no path exists
    """
    dist = longest_path_dag(num_vertices, edges, src)
    return dist[dest]


def reconstruct_longest_path(
    num_vertices: int, edges: List[Tuple[int, int, int]], source: int, dest: int
) -> Optional[List[int]]:
    """
    Find and reconstruct the longest path from source to destination.

    Returns:
        List of vertices in the longest path, or None if no path exists
    """
    adj: List[List[Tuple[int, int]]] = [[] for _ in range(num_vertices)]
    indegree = [0] * num_vertices

    for u, v, w in edges:
        adj[u].append((v, w))
        indegree[v] += 1

    queue = [i for i in range(num_vertices) if indegree[i] == 0]
    topo_order = []

    while queue:
        u = queue.pop(0)
        topo_order.append(u)
        for v, _ in adj[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)

    dist: List[Optional[int]] = [None] * num_vertices
    parent: List[Optional[int]] = [None] * num_vertices
    dist[source] = 0

    for u in topo_order:
        if dist[u] is not None:
            for v, weight in adj[u]:
                new_dist = dist[u] + weight
                if dist[v] is None or new_dist > dist[v]:
                    dist[v] = new_dist
                    parent[v] = u

    if dist[dest] is None:
        return None

    # Reconstruct path
    path = []
    current = dest
    while current is not None:
        path.append(current)
        current = parent[current]
    path.reverse()

    return path


if __name__ == "__main__":
    # Example 1: Longest path from vertex 0
    print("=== Example 1: Longest paths from source ===")
    edges = [
        (0, 1, 5),
        (0, 2, 3),
        (1, 3, 6),
        (1, 2, 2),
        (2, 4, 4),
        (2, 5, 2),
        (2, 3, 7),
        (3, 5, 1),
        (3, 4, -1),
        (4, 5, -2),
    ]
    dist = longest_path_dag(6, edges, 0)
    for i, d in enumerate(dist):
        print(f"Longest path from 0 to {i}: {d}")

    # Example 2: Longest path between two specific vertices
    print("\n=== Example 2: Longest path 0 -> 5 ===")
    result = longest_path_between(6, edges, 0, 5)
    print(f"Longest path weight: {result}")

    # Example 3: Reconstruct the path
    print("\n=== Example 3: Reconstruct path ===")
    path = reconstruct_longest_path(6, edges, 0, 5)
    print(f"Longest path: {path}")
    if path:
        print(f"Path length: {len(path) - 1} edges")

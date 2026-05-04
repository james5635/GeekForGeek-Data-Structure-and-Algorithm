"""
0-1 BFS - Shortest Path in a Binary Weighted Graph.

Given a graph where every edge has weight 0 or 1, find the shortest path
from a source vertex to all other vertices.

Algorithm:
  Uses a deque (double-ended queue) instead of a regular queue:
  - Edges with weight 0 are pushed to the FRONT of the deque (processed sooner)
  - Edges with weight 1 are pushed to the BACK of the deque (processed later)

This maintains the invariant that the deque is always sorted by distance,
emulating Dijkstra's algorithm behavior in O(V + E) time instead of O(E log V).

Time Complexity: O(V + E)
Space Complexity: O(V + E)

Why it works:
  By pushing 0-weight edges to the front, we process them before 1-weight
  edges, ensuring vertices are always explored in non-decreasing order of
  distance. This eliminates the need for a priority queue.
"""

from __future__ import annotations
from collections import deque
import math


def zero_one_bfs(n: int, source: int, adj: list[list[tuple[int, int]]]) -> list[int]:
    """Find shortest distances from source to all vertices in a 0-1 weighted graph.

    Args:
        n: Number of vertices (labeled 0 to n-1).
        source: Starting vertex.
        adj: Adjacency list where adj[u] contains (v, weight) tuples.
             Each weight must be 0 or 1.

    Returns:
        List of shortest distances from source to each vertex.
        Unreachable vertices have distance = infinity.
    """
    dist: list[int] = [math.inf] * n
    dist[source] = 0
    dq: deque[int] = deque([source])

    while dq:
        u = dq.popleft()
        for v, weight in adj[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                if weight == 0:
                    dq.appendleft(v)
                else:
                    dq.append(v)

    return dist


def zero_one_bfs_with_path(
    n: int, source: int, destination: int, adj: list[list[tuple[int, int]]]
) -> tuple[int, list[int] | None]:
    """Find shortest path and distance in a 0-1 weighted graph.

    Args:
        n: Number of vertices (labeled 0 to n-1).
        source: Starting vertex.
        destination: Target vertex.
        adj: Adjacency list where adj[u] contains (v, weight) tuples.

    Returns:
        Tuple of (distance, path) where path is a list of vertices
        from source to destination, or None if unreachable.
    """
    dist: list[int] = [math.inf] * n
    parent: list[int | None] = [None] * n
    dist[source] = 0
    dq: deque[int] = deque([source])

    while dq:
        u = dq.popleft()
        if u == destination:
            break
        for v, weight in adj[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                parent[v] = u
                if weight == 0:
                    dq.appendleft(v)
                else:
                    dq.append(v)

    if dist[destination] == math.inf:
        return math.inf, None

    path: list[int] = []
    current: int | None = destination
    while current is not None:
        path.append(current)
        current = parent[current]
    path.reverse()
    return dist[destination], path


if __name__ == "__main__":
    print("=" * 60)
    print("0-1 BFS - Shortest Distances from Source")
    print("=" * 60)
    # Graph with 9 vertices and 13 edges (weights 0 or 1):
    #   Edges: (u, v, weight)
    edges = [
        (0, 1, 0),
        (0, 7, 1),
        (1, 2, 1),
        (1, 7, 1),
        (2, 3, 0),
        (2, 5, 0),
        (2, 8, 1),
        (3, 4, 1),
        (3, 5, 1),
        (4, 5, 1),
        (5, 6, 1),
        (6, 7, 1),
        (7, 8, 1),
    ]
    n = 9
    source = 0
    adj: list[list[tuple[int, int]]] = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))

    dist = zero_one_bfs(n, source, adj)
    print(f"Shortest distances from vertex {source}:")
    for i, d in enumerate(dist):
        label = "infinity" if d == math.inf else str(d)
        print(f"  dist[{i}] = {label}")

    # Expected: [0, 0, 1, 1, 2, 1, 2, 1, 2]

    print("\n" + "=" * 60)
    print("0-1 BFS - Shortest Path from Source to Destination")
    print("=" * 60)
    destination = 6
    distance, path = zero_one_bfs_with_path(n, source, destination, adj)
    if path:
        print(
            f"Shortest path from {source} to {destination}: {' -> '.join(map(str, path))}"
        )
        print(f"Total distance: {distance}")
    else:
        print(f"No path from {source} to {destination}")

    print("\n" + "=" * 60)
    print("0-1 BFS - Disconnected Vertex")
    print("=" * 60)
    # Add an isolated vertex
    n2 = 4
    adj2: list[list[tuple[int, int]]] = [
        [(1, 0), (2, 1)],  # 0
        [(0, 0)],  # 1
        [(0, 1)],  # 2
        [],  # 3 (isolated)
    ]
    dist2 = zero_one_bfs(n2, 0, adj2)
    print(f"Shortest distances from 0: {dist2}")
    # Expected: [0, 0, 1, inf]

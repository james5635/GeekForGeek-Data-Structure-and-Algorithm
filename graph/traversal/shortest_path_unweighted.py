"""
Shortest Path in an Unweighted Graph using BFS.

In an unweighted graph, the shortest path between two vertices is the path
with the minimum number of edges. BFS naturally finds this shortest path
because it explores vertices in order of their distance from the source.

Algorithm:
  1. Run BFS from the source vertex.
  2. Track the parent of each vertex and its distance from the source.
  3. Reconstruct the path from destination back to source using parent pointers.

Time Complexity: O(V + E)
Space Complexity: O(V)
"""

from __future__ import annotations
from collections import deque


def shortest_path_unweighted(
    adj: list[list[int]], source: int, destination: int
) -> list[int] | None:
    """Find the shortest path from source to destination in an unweighted graph.

    Args:
        adj: Adjacency list where adj[i] contains neighbors of vertex i.
        source: Starting vertex.
        destination: Target vertex.

    Returns:
        List of vertices forming the shortest path from source to destination,
        or None if no path exists.
    """
    n = len(adj)
    dist: list[int] = [float("inf")] * n
    parent: list[int | None] = [None] * n

    dist[source] = 0
    queue: deque[int] = deque([source])

    while queue:
        vertex = queue.popleft()
        if vertex == destination:
            break
        for neighbor in adj[vertex]:
            if dist[neighbor] == float("inf"):
                dist[neighbor] = dist[vertex] + 1
                parent[neighbor] = vertex
                queue.append(neighbor)

    if dist[destination] == float("inf"):
        return None

    path: list[int] = []
    current: int | None = destination
    while current is not None:
        path.append(current)
        current = parent[current]
    path.reverse()
    return path


def shortest_path_unweighted_all(
    adj: list[list[int]], source: int
) -> tuple[list[int], list[int | None]]:
    """Find shortest distances and parents from source to ALL vertices.

    Args:
        adj: Adjacency list where adj[i] contains neighbors of vertex i.
        source: Starting vertex.

    Returns:
        Tuple of (distances, parents) where:
          - distances[i] = shortest distance from source to vertex i
          - parents[i] = parent of vertex i in the BFS tree
    """
    n = len(adj)
    dist: list[int] = [float("inf")] * n
    parent: list[int | None] = [None] * n

    dist[source] = 0
    queue: deque[int] = deque([source])

    while queue:
        vertex = queue.popleft()
        for neighbor in adj[vertex]:
            if dist[neighbor] == float("inf"):
                dist[neighbor] = dist[vertex] + 1
                parent[neighbor] = vertex
                queue.append(neighbor)

    return dist, parent


def reconstruct_path(parent: list[int | None], destination: int) -> list[int]:
    """Reconstruct the path from source to destination using parent pointers.

    Args:
        parent: Parent array where parent[i] is the parent of vertex i.
        destination: Target vertex.

    Returns:
        List of vertices from source to destination.
    """
    path: list[int] = []
    current: int | None = destination
    while current is not None:
        path.append(current)
        current = parent[current]
    path.reverse()
    return path


if __name__ == "__main__":
    print("=" * 60)
    print("Shortest Path in Unweighted Graph")
    print("=" * 60)
    # Graph with 8 vertices and 10 edges:
    #   0-1, 1-2, 0-3, 3-4, 4-7, 3-7, 6-7, 4-5, 4-6, 5-6
    adj1: list[list[int]] = [
        [1, 3],  # 0
        [0, 2],  # 1
        [1],  # 2
        [0, 4, 7],  # 3
        [3, 7, 5, 6],  # 4
        [4, 6],  # 5
        [7, 4, 5],  # 6
        [4, 3, 6],  # 7
    ]

    source, dest = 0, 7
    path = shortest_path_unweighted(adj1, source, dest)
    if path:
        print(f"Shortest path from {source} to {dest}: {' -> '.join(map(str, path))}")
        print(f"Distance: {len(path) - 1} edges")
    else:
        print(f"No path from {source} to {dest}")

    print()
    source, dest = 2, 6
    path = shortest_path_unweighted(adj1, source, dest)
    if path:
        print(f"Shortest path from {source} to {dest}: {' -> '.join(map(str, path))}")
        print(f"Distance: {len(path) - 1} edges")
    else:
        print(f"No path from {source} to {dest}")

    print("\n" + "=" * 60)
    print("Shortest Distances from Source to All Vertices")
    print("=" * 60)
    dist, parent = shortest_path_unweighted_all(adj1, 0)
    for i in range(len(adj1)):
        if dist[i] == float("inf"):
            print(f"  Vertex {i}: unreachable")
        else:
            p = reconstruct_path(parent, i)
            print(f"  Vertex {i}: distance={dist[i]}, path={' -> '.join(map(str, p))}")

    print("\n" + "=" * 60)
    print("Disconnected Graph - No Path")
    print("=" * 60)
    adj2: list[list[int]] = [
        [1],  # 0
        [0],  # 1
        [3],  # 2
        [2],  # 3
    ]
    path = shortest_path_unweighted(adj2, 0, 3)
    print(f"Path from 0 to 3: {path}")

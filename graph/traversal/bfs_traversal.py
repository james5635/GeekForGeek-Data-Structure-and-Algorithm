"""
Breadth First Search (BFS) Traversal for a Graph.

BFS explores a graph level by level, visiting all neighbors of a vertex
before moving to the next level. It uses a queue to maintain the order
of exploration.

Time Complexity: O(V + E) where V = vertices, E = edges
Space Complexity: O(V) for visited array and queue

Applications:
  - Shortest path in unweighted graphs
  - Cycle detection
  - Connected components
  - Network routing
"""

from __future__ import annotations
from collections import deque


def bfs(adj: list[list[int]], start: int = 0) -> list[int]:
    """Perform BFS traversal starting from a given vertex.

    Visits all vertices reachable from the start vertex in level-order.

    Args:
        adj: Adjacency list where adj[i] contains neighbors of vertex i.
        start: Starting vertex for BFS. Defaults to 0.

    Returns:
        List of vertices in BFS traversal order.
    """
    n = len(adj)
    visited: list[bool] = [False] * n
    result: list[int] = []
    queue: deque[int] = deque()

    visited[start] = True
    queue.append(start)

    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        for neighbor in adj[vertex]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    return result


def bfs_all(adj: list[list[int]]) -> list[int]:
    """Perform BFS traversal visiting ALL vertices (handles disconnected graphs).

    Iterates through every vertex and starts a new BFS from any unvisited
    vertex, ensuring all connected components are explored.

    Args:
        adj: Adjacency list where adj[i] contains neighbors of vertex i.

    Returns:
        List of all vertices in BFS traversal order.
    """
    n = len(adj)
    visited: list[bool] = [False] * n
    result: list[int] = []

    for i in range(n):
        if visited[i]:
            continue
        queue: deque[int] = deque()
        visited[i] = True
        queue.append(i)
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            for neighbor in adj[vertex]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

    return result


if __name__ == "__main__":
    print("=" * 60)
    print("BFS - Connected Undirected Graph")
    print("=" * 60)
    # Graph:
    #       0
    #      / \
    #     1---2
    #        / \
    #       3   4
    adj1: list[list[int]] = [
        [1, 2],  # 0
        [0, 2],  # 1
        [0, 1, 3, 4],  # 2
        [2],  # 3
        [2],  # 4
    ]
    print(f"BFS from 0: {bfs(adj1, 0)}")

    print("\n" + "=" * 60)
    print("BFS - Disconnected Graph")
    print("=" * 60)
    # Graph has two components: {0, 1, 2, 3} and {4, 5}
    adj2: list[list[int]] = [
        [2, 3],  # 0
        [2],  # 1
        [0, 1],  # 2
        [0],  # 3
        [5],  # 4
        [4],  # 5
    ]
    print(f"BFS from 0 (single):    {bfs(adj2, 0)}")
    print(f"BFS all components:     {bfs_all(adj2)}")

    print("\n" + "=" * 60)
    print("BFS - Directed Graph")
    print("=" * 60)
    adj_directed: list[list[int]] = [
        [1, 2],  # 0 -> 1, 0 -> 2
        [3],  # 1 -> 3
        [3],  # 2 -> 3
        [],  # 3 (sink)
    ]
    print(f"BFS from 0: {bfs(adj_directed, 0)}")

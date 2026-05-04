"""
Depth First Search (DFS) Traversal for a Graph.

DFS explores a graph by going as deep as possible along each branch before
backtracking. It uses a visited set to avoid processing nodes multiple times
(since graphs may contain cycles).

Two implementations are provided:
  1. Recursive DFS - uses the call stack implicitly
  2. Iterative DFS - uses an explicit stack

Time Complexity: O(V + E) where V = vertices, E = edges
Space Complexity: O(V) for visited array + recursion/stack space

Note: There can be multiple valid DFS traversals depending on the order
in which adjacent vertices are explored.
"""

from __future__ import annotations


def dfs_recursive(adj: list[list[int]], start: int = 0) -> list[int]:
    """Perform DFS traversal starting from a given vertex (recursive).

    Traverses all vertices reachable from the start vertex. If the graph
    is disconnected, only the connected component containing start is visited.

    Args:
        adj: Adjacency list where adj[i] contains neighbors of vertex i.
        start: Starting vertex for DFS. Defaults to 0.

    Returns:
        List of vertices in DFS traversal order.
    """

    def _dfs(vertex: int, visited: list[bool], result: list[int]) -> None:
        visited[vertex] = True
        result.append(vertex)
        for neighbor in adj[vertex]:
            if not visited[neighbor]:
                _dfs(neighbor, visited, result)

    n = len(adj)
    visited: list[bool] = [False] * n
    result: list[int] = []
    _dfs(start, visited, result)
    return result


def dfs_recursive_all(adj: list[list[int]]) -> list[int]:
    """Perform DFS traversal visiting ALL vertices (handles disconnected graphs).

    Iterates through every vertex and starts a new DFS from any unvisited
    vertex, ensuring all connected components are explored.

    Args:
        adj: Adjacency list where adj[i] contains neighbors of vertex i.

    Returns:
        List of all vertices in DFS traversal order.
    """

    def _dfs(vertex: int, visited: list[bool], result: list[int]) -> None:
        visited[vertex] = True
        result.append(vertex)
        for neighbor in adj[vertex]:
            if not visited[neighbor]:
                _dfs(neighbor, visited, result)

    n = len(adj)
    visited: list[bool] = [False] * n
    result: list[int] = []
    for i in range(n):
        if not visited[i]:
            _dfs(i, visited, result)
    return result


def dfs_iterative(adj: list[list[int]], start: int = 0) -> list[int]:
    """Perform DFS traversal starting from a given vertex (iterative).

    Uses an explicit stack instead of recursion. The order may differ
    from the recursive version because neighbors are processed in
    reverse order (due to stack LIFO behavior).

    Args:
        adj: Adjacency list where adj[i] contains neighbors of vertex i.
        start: Starting vertex for DFS. Defaults to 0.

    Returns:
        List of vertices in DFS traversal order.
    """
    n = len(adj)
    visited: list[bool] = [False] * n
    result: list[int] = []
    stack: list[int] = [start]

    while stack:
        vertex = stack.pop()
        if visited[vertex]:
            continue
        visited[vertex] = True
        result.append(vertex)
        for neighbor in reversed(adj[vertex]):
            if not visited[neighbor]:
                stack.append(neighbor)

    return result


def dfs_iterative_all(adj: list[list[int]]) -> list[int]:
    """Perform DFS traversal visiting ALL vertices (iterative, handles disconnected).

    Args:
        adj: Adjacency list where adj[i] contains neighbors of vertex i.

    Returns:
        List of all vertices in DFS traversal order.
    """
    n = len(adj)
    visited: list[bool] = [False] * n
    result: list[int] = []

    for i in range(n):
        if visited[i]:
            continue
        stack: list[int] = [i]
        while stack:
            vertex = stack.pop()
            if visited[vertex]:
                continue
            visited[vertex] = True
            result.append(vertex)
            for neighbor in reversed(adj[vertex]):
                if not visited[neighbor]:
                    stack.append(neighbor)

    return result


if __name__ == "__main__":
    print("=" * 60)
    print("DFS - Connected Undirected Graph")
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

    print(f"Recursive DFS from 0:   {dfs_recursive(adj1, 0)}")
    print(f"Iterative DFS from 0:   {dfs_iterative(adj1, 0)}")

    print("\n" + "=" * 60)
    print("DFS - Disconnected Graph")
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

    print(f"DFS from 0 (single):    {dfs_recursive(adj2, 0)}")
    print(f"DFS all components:     {dfs_recursive_all(adj2)}")
    print(f"DFS iterative (all):    {dfs_iterative_all(adj2)}")

    print("\n" + "=" * 60)
    print("DFS - Directed Graph")
    print("=" * 60)
    adj_directed: list[list[int]] = [
        [1, 2],  # 0 -> 1, 0 -> 2
        [3],  # 1 -> 3
        [3],  # 2 -> 3
        [],  # 3 (sink)
    ]
    print(f"DFS from 0:             {dfs_recursive(adj_directed, 0)}")
    print(f"DFS all (from vertex):  {dfs_iterative(adj_directed, 0)}")

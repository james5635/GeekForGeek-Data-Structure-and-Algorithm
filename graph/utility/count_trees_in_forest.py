"""
Count Number of Trees in a Forest.

A forest is a collection of disjoint trees (an undirected graph with no cycles).
This module provides two approaches to count the number of trees:
1. DFS-based approach for adjacency list representation (O(V + E))
2. BFS-based approach for 2D grid representation (O(N * M))

Time Complexity (DFS): O(V + E) where V = vertices, E = edges
Auxiliary Space (DFS): O(V) for visited array

Time Complexity (BFS): O(N * M) where N = rows, M = columns
Auxiliary Space (BFS): O(N * M) for visited array
"""

from collections import deque
from typing import List, Tuple


def count_trees_dfs(adj: List[List[int]], v: int) -> int:
    """
    Count the number of trees in a forest using DFS.

    A forest is represented as an undirected graph using an adjacency list.
    Each connected component is one tree.

    Args:
        adj: Adjacency list where adj[i] contains all vertices connected to vertex i.
        v: Number of vertices in the graph.

    Returns:
        The number of trees (connected components) in the forest.

    Example:
        >>> adj = [[1, 2], [0], [0], [4], [3]]
        >>> count_trees_dfs(adj, 5)
        2
    """

    def dfs_util(u: int, visited: List[bool]) -> None:
        """Perform DFS from vertex u, marking all reachable vertices as visited."""
        visited[u] = True
        for neighbor in adj[u]:
            if not visited[neighbor]:
                dfs_util(neighbor, visited)

    visited = [False] * v
    count = 0

    for u in range(v):
        if not visited[u]:
            dfs_util(u, visited)
            count += 1

    return count


def count_trees_bfs(forest: List[List[int]]) -> int:
    """
    Count the number of trees in a 2D grid forest using BFS.

    Trees are represented as connected regions of 1s in a 2D grid,
    where connectivity is 4-directional (up, down, left, right).

    Args:
        forest: 2D grid where 1 represents a tree node and 0 represents empty space.

    Returns:
        The number of connected tree components in the forest.

    Example:
        >>> forest = [
        ...     [0, 1, 1, 0, 0],
        ...     [0, 0, 0, 0, 0],
        ...     [0, 0, 0, 0, 0],
        ...     [0, 0, 0, 0, 1],
        ...     [0, 0, 0, 0, 0]
        ... ]
        >>> count_trees_bfs(forest)
        2
    """
    if not forest or not forest[0]:
        return 0

    n = len(forest)
    m = len(forest[0])
    visited = [[False] * m for _ in range(n)]

    # 4-directional movements: up, right, down, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def bfs(start: Tuple[int, int]) -> None:
        """Perform BFS from start position, marking all connected tree nodes."""
        queue = deque([start])
        visited[start[0]][start[1]] = True

        while queue:
            x, y = queue.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (
                    0 <= nx < n
                    and 0 <= ny < m
                    and forest[nx][ny] == 1
                    and not visited[nx][ny]
                ):
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    count = 0
    for i in range(n):
        for j in range(m):
            if forest[i][j] == 1 and not visited[i][j]:
                bfs((i, j))
                count += 1

    return count


def add_edge(adj: List[List[int]], u: int, v: int) -> None:
    """
    Add an undirected edge between vertices u and v.

    Args:
        adj: Adjacency list to modify.
        u: First vertex.
        v: Second vertex.
    """
    adj[u].append(v)
    adj[v].append(u)


if __name__ == "__main__":
    # Example 1: DFS approach (adjacency list)
    print("Example 1 - DFS (Adjacency List):")
    print("Edges: {0,1}, {0,2}, {3,4}")
    print("Graph visualization:")
    print("    0       3")
    print("   / \\       \\")
    print("  1   2       4")

    v = 5
    adj: List[List[int]] = [[] for _ in range(v)]
    add_edge(adj, 0, 1)
    add_edge(adj, 0, 2)
    add_edge(adj, 3, 4)

    tree_count = count_trees_dfs(adj, v)
    print(f"\nNumber of trees in forest: {tree_count}\n")

    # Example 2: DFS with single tree
    print("Example 2 - DFS (Single Tree):")
    print("Edges: {0,1}, {1,2}, {2,3}")

    v2 = 4
    adj2: List[List[int]] = [[] for _ in range(v2)]
    add_edge(adj2, 0, 1)
    add_edge(adj2, 1, 2)
    add_edge(adj2, 2, 3)

    tree_count2 = count_trees_dfs(adj2, v2)
    print(f"Number of trees in forest: {tree_count2}\n")

    # Example 3: BFS approach (2D grid)
    print("Example 3 - BFS (2D Grid):")
    forest_grid = [
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0],
    ]
    print("Grid:")
    for row in forest_grid:
        print(" ".join(str(cell) for cell in row))

    grid_tree_count = count_trees_bfs(forest_grid)
    print(f"\nNumber of trees in forest: {grid_tree_count}")

"""
Detect Cycle in a Directed Graph

Problem: Given a directed graph represented as an adjacency list, determine whether
the graph contains a cycle.

Algorithm: DFS with 3-color marking (White/Gray/Black)
- WHITE (0): Node not yet visited
- GRAY (1): Node is currently being processed (in the recursion stack)
- BLACK (2): Node and all its descendants have been fully processed

A cycle exists if during DFS we encounter a GRAY node, meaning we've found
a back edge to a node that's still in the current recursion path.

Time Complexity: O(V + E) where V = vertices, E = edges
Space Complexity: O(V) for the color array and recursion stack
"""

from collections import defaultdict
from enum import Enum


class Color(Enum):
    WHITE = 0  # Not visited
    GRAY = 1  # Currently being processed
    BLACK = 2  # Fully processed


def has_cycle_directed(n: int, edges: list[tuple[int, int]]) -> bool:
    """
    Detect if a directed graph contains a cycle.

    Args:
        n: Number of vertices (labeled 0 to n-1)
        edges: List of directed edges as (source, destination) tuples

    Returns:
        True if the graph contains a cycle, False otherwise
    """
    adj: dict[int, list[int]] = defaultdict(list)
    for src, dst in edges:
        adj[src].append(dst)

    color: list[Color] = [Color.WHITE] * n

    def dfs(node: int) -> bool:
        color[node] = Color.GRAY

        for neighbor in adj[node]:
            if color[neighbor] == Color.GRAY:
                return True
            if color[neighbor] == Color.WHITE and dfs(neighbor):
                return True

        color[node] = Color.BLACK
        return False

    for i in range(n):
        if color[i] == Color.WHITE:
            if dfs(i):
                return True

    return False


def has_cycle_directed_adj(n: int, adj: list[list[int]]) -> bool:
    """
    Detect if a directed graph contains a cycle using adjacency list input.

    Args:
        n: Number of vertices (labeled 0 to n-1)
        adj: Adjacency list where adj[i] contains all neighbors of vertex i

    Returns:
        True if the graph contains a cycle, False otherwise
    """
    color: list[Color] = [Color.WHITE] * n

    def dfs(node: int) -> bool:
        color[node] = Color.GRAY

        for neighbor in adj[node]:
            if color[neighbor] == Color.GRAY:
                return True
            if color[neighbor] == Color.WHITE and dfs(neighbor):
                return True

        color[node] = Color.BLACK
        return False

    for i in range(n):
        if color[i] == Color.WHITE:
            if dfs(i):
                return True

    return False


if __name__ == "__main__":
    print("=" * 60)
    print("Detect Cycle in a Directed Graph")
    print("=" * 60)

    # Example 1: Graph WITH a cycle
    #   0 -> 1 -> 2 -> 0 (cycle!)
    #        |
    #        v
    #        3
    print("\nExample 1: Graph with a cycle")
    n1 = 4
    edges1 = [(0, 1), (1, 2), (2, 0), (1, 3)]
    print(f"  Vertices: {n1}")
    print(f"  Edges: {edges1}")
    print(f"  Has cycle: {has_cycle_directed(n1, edges1)}")

    # Example 2: Graph WITHOUT a cycle (DAG)
    #   0 -> 1 -> 3
    #   |    |
    #   v    v
    #   2 -> 3
    print("\nExample 2: Graph without a cycle (DAG)")
    n2 = 4
    edges2 = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3)]
    print(f"  Vertices: {n2}")
    print(f"  Edges: {edges2}")
    print(f"  Has cycle: {has_cycle_directed(n2, edges2)}")

    # Example 3: Single vertex, no edges
    print("\nExample 3: Single vertex, no edges")
    n3 = 1
    edges3: list[tuple[int, int]] = []
    print(f"  Vertices: {n3}")
    print(f"  Edges: {edges3}")
    print(f"  Has cycle: {has_cycle_directed(n3, edges3)}")

    # Example 4: Self-loop
    #   0 -> 0
    print("\nExample 4: Self-loop")
    n4 = 1
    edges4 = [(0, 0)]
    print(f"  Vertices: {n4}")
    print(f"  Edges: {edges4}")
    print(f"  Has cycle: {has_cycle_directed(n4, edges4)}")

    # Example 5: Disconnected graph, one component has cycle
    #   0 -> 1 (no cycle)
    #   2 -> 3 -> 4 -> 2 (cycle!)
    print("\nExample 5: Disconnected graph with cycle in one component")
    n5 = 5
    edges5 = [(0, 1), (2, 3), (3, 4), (4, 2)]
    print(f"  Vertices: {n5}")
    print(f"  Edges: {edges5}")
    print(f"  Has cycle: {has_cycle_directed(n5, edges5)}")

    # Example 6: Adjacency list format (GeeksforGeeks style)
    print("\nExample 6: Adjacency list format")
    # Graph: 0->1, 1->2, 2->0 (cycle)
    adj6 = [[1], [2], [0], []]
    print(f"  Adjacency list: {adj6}")
    print(f"  Has cycle: {has_cycle_directed_adj(4, adj6)}")

    print("\n" + "=" * 60)

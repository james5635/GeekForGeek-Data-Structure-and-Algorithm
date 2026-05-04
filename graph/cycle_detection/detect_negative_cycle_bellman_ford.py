"""
Detect Negative Cycle using Bellman-Ford Algorithm

Problem: Given a weighted directed graph with potentially negative edge weights,
determine whether the graph contains a negative weight cycle. A negative cycle
is a cycle where the sum of edge weights is negative.

Algorithm: Bellman-Ford Relaxation
1. Initialize distances from a source vertex to all others as infinity, source as 0
2. Relax all edges V-1 times (V = number of vertices)
3. After V-1 iterations, if we can still relax any edge, a negative cycle exists

Why this works: In a graph without negative cycles, the shortest path can have
at most V-1 edges. After V-1 relaxation iterations, all shortest paths are found.
If further relaxation is possible, it means we can keep decreasing distances
indefinitely, which indicates a negative cycle.

Time Complexity: O(V * E) where V = vertices, E = edges
Space Complexity: O(V) for the distance array
"""

import math


def has_negative_cycle_bellman_ford(n: int, edges: list[tuple[int, int, int]]) -> bool:
    """
    Detect if a weighted directed graph contains a negative weight cycle.

    Args:
        n: Number of vertices (labeled 0 to n-1)
        edges: List of weighted edges as (source, destination, weight) tuples

    Returns:
        True if the graph contains a negative weight cycle, False otherwise
    """
    dist: list[float] = [0.0] * n

    for _ in range(n - 1):
        updated = False
        for src, dst, weight in edges:
            if dist[src] != math.inf and dist[src] + weight < dist[dst]:
                dist[dst] = dist[src] + weight
                updated = True
        if not updated:
            break

    for src, dst, weight in edges:
        if dist[src] != math.inf and dist[src] + weight < dist[dst]:
            return True

    return False


def has_negative_cycle_bellman_ford_with_path(
    n: int, edges: list[tuple[int, int, int]]
) -> tuple[bool, list[tuple[int, int, int]] | None]:
    """
    Detect negative cycle and return the cycle edges if found.

    Args:
        n: Number of vertices (labeled 0 to n-1)
        edges: List of weighted edges as (source, destination, weight) tuples

    Returns:
        Tuple of (has_negative_cycle, cycle_edges_or_None)
    """
    dist: list[float] = [0.0] * n
    parent: list[int | None] = [None] * n

    for _ in range(n - 1):
        for src, dst, weight in edges:
            if dist[src] != math.inf and dist[src] + weight < dist[dst]:
                dist[dst] = dist[src] + weight
                parent[dst] = src

    negative_node: int | None = None
    for src, dst, weight in edges:
        if dist[src] != math.inf and dist[src] + weight < dist[dst]:
            negative_node = dst
            break

    if negative_node is None:
        return False, None

    cycle_edges: list[tuple[int, int, int]] = []
    visited: set[int] = set()
    current: int = negative_node

    while current not in visited:
        visited.add(current)
        prev = parent[current]
        if prev is None:
            break
        current = prev

    cycle_start = current
    current = cycle_start
    cycle_nodes: list[int] = []

    while True:
        cycle_nodes.append(current)
        prev = parent[current]
        if prev is None or prev == cycle_start:
            break
        current = prev

    cycle_nodes.append(cycle_start)
    cycle_nodes.reverse()

    for i in range(len(cycle_nodes) - 1):
        u, v = cycle_nodes[i], cycle_nodes[i + 1]
        for src, dst, weight in edges:
            if src == u and dst == v:
                cycle_edges.append((u, v, weight))
                break

    return True, cycle_edges


if __name__ == "__main__":
    print("=" * 60)
    print("Detect Negative Cycle using Bellman-Ford")
    print("=" * 60)

    # Example 1: Graph WITH a negative cycle
    #   0 -> 1 (weight 1)
    #   1 -> 2 (weight -1)
    #   2 -> 0 (weight -1)  => cycle sum = -1 (negative!)
    print("\nExample 1: Graph with negative cycle")
    n1 = 3
    edges1 = [(0, 1, 1), (1, 2, -1), (2, 0, -1)]
    print(f"  Vertices: {n1}")
    print(f"  Edges (src, dst, weight): {edges1}")
    has_neg, cycle = has_negative_cycle_bellman_ford_with_path(n1, edges1)
    print(f"  Has negative cycle: {has_neg}")
    if cycle:
        print(f"  Negative cycle edges: {cycle}")

    # Example 2: Graph WITHOUT a negative cycle
    #   0 -> 1 (weight 1)
    #   1 -> 2 (weight 2)
    #   2 -> 0 (weight 1)  => cycle sum = 4 (positive)
    print("\nExample 2: Graph without negative cycle")
    n2 = 3
    edges2 = [(0, 1, 1), (1, 2, 2), (2, 0, 1)]
    print(f"  Vertices: {n2}")
    print(f"  Edges (src, dst, weight): {edges2}")
    has_neg2, cycle2 = has_negative_cycle_bellman_ford_with_path(n2, edges2)
    print(f"  Has negative cycle: {has_neg2}")

    # Example 3: Disconnected graph with negative cycle in one component
    #   0 -> 1 (weight 5)
    #   2 -> 3 (weight 1)
    #   3 -> 4 (weight -3)
    #   4 -> 2 (weight 1)  => cycle sum = -1 (negative!)
    print("\nExample 3: Disconnected graph with negative cycle")
    n3 = 5
    edges3 = [(0, 1, 5), (2, 3, 1), (3, 4, -3), (4, 2, 1)]
    print(f"  Vertices: {n3}")
    print(f"  Edges (src, dst, weight): {edges3}")
    print(f"  Has negative cycle: {has_negative_cycle_bellman_ford(n3, edges3)}")

    # Example 4: Classic Bellman-Ford example
    #     0
    #    /|
    #   1 |
    #  / \|
    # 2 <-3
    print("\nExample 4: Classic weighted graph")
    n4 = 4
    edges4 = [
        (0, 1, 4),
        (0, 3, 5),
        (1, 2, -3),
        (2, 3, 1),
        (3, 2, 2),
    ]
    print(f"  Vertices: {n4}")
    print(f"  Edges (src, dst, weight): {edges4}")
    print(f"  Has negative cycle: {has_negative_cycle_bellman_ford(n4, edges4)}")

    # Example 5: Self-loop with negative weight
    print("\nExample 5: Self-loop with negative weight")
    n5 = 2
    edges5 = [(0, 1, 1), (1, 1, -1)]
    print(f"  Vertices: {n5}")
    print(f"  Edges (src, dst, weight): {edges5}")
    print(f"  Has negative cycle: {has_negative_cycle_bellman_ford(n5, edges5)}")

    print("\n" + "=" * 60)

"""
Detect Negative Cycle using Floyd-Warshall Algorithm

Problem: Given a weighted directed graph with potentially negative edge weights,
determine whether the graph contains a negative weight cycle.

Algorithm: Floyd-Warshall with diagonal check
The Floyd-Warshall algorithm computes all-pairs shortest paths. After running the
algorithm, if any diagonal entry dist[i][i] < 0, it means there's a negative cycle.

This is because dist[i][i] should always be 0 (distance from a node to itself).
If it becomes negative, it means we found a path from i back to i with negative
total weight, which is a negative cycle.

The algorithm also detects if dist[i][i] becomes negative during execution,
allowing early termination.

Time Complexity: O(V^3) where V = number of vertices
Space Complexity: O(V^2) for the distance matrix
"""

import math

INF = float("inf")


def has_negative_cycle_floyd_warshall(
    n: int, edges: list[tuple[int, int, int]]
) -> bool:
    """
    Detect if a weighted directed graph contains a negative weight cycle
    using the Floyd-Warshall algorithm.

    Args:
        n: Number of vertices (labeled 0 to n-1)
        edges: List of weighted edges as (source, destination, weight) tuples

    Returns:
        True if the graph contains a negative weight cycle, False otherwise
    """
    dist: list[list[float]] = [[INF] * n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0.0

    for src, dst, weight in edges:
        dist[src][dst] = min(dist[src][dst], weight)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != INF and dist[k][j] != INF:
                    new_dist = dist[i][k] + dist[k][j]
                    if new_dist < dist[i][j]:
                        dist[i][j] = new_dist

    for i in range(n):
        if dist[i][i] < 0:
            return True

    return False


def has_negative_cycle_floyd_warshall_with_detection(
    n: int, edges: list[tuple[int, int, int]]
) -> tuple[bool, list[tuple[int, int, int]] | None]:
    """
    Detect negative cycle using Floyd-Warshall and return shortest path matrix.

    Args:
        n: Number of vertices (labeled 0 to n-1)
        edges: List of weighted edges as (source, destination, weight) tuples

    Returns:
        Tuple of (has_negative_cycle, distance_matrix_or_None)
    """
    dist: list[list[float]] = [[INF] * n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0.0

    for src, dst, weight in edges:
        dist[src][dst] = min(dist[src][dst], weight)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != INF and dist[k][j] != INF:
                    new_dist = dist[i][k] + dist[k][j]
                    if new_dist < dist[i][j]:
                        dist[i][j] = new_dist

    has_negative = False
    for i in range(n):
        if dist[i][i] < 0:
            has_negative = True
            break

    if has_negative:
        return True, dist
    return False, dist


def all_pairs_shortest_paths(
    n: int, edges: list[tuple[int, int, int]]
) -> tuple[list[list[float]], bool]:
    """
    Compute all-pairs shortest paths and detect negative cycles.

    Args:
        n: Number of vertices (labeled 0 to n-1)
        edges: List of weighted edges as (source, destination, weight) tuples

    Returns:
        Tuple of (distance_matrix, has_negative_cycle)
    """
    dist: list[list[float]] = [[INF] * n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0.0

    for src, dst, weight in edges:
        dist[src][dst] = min(dist[src][dst], weight)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != INF and dist[k][j] != INF:
                    new_dist = dist[i][k] + dist[k][j]
                    if new_dist < dist[i][j]:
                        dist[i][j] = new_dist

    has_negative = any(dist[i][i] < 0 for i in range(n))

    return dist, has_negative


if __name__ == "__main__":
    print("=" * 60)
    print("Detect Negative Cycle using Floyd-Warshall")
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
    has_neg, dist = has_negative_cycle_floyd_warshall_with_detection(n1, edges1)
    print(f"  Has negative cycle: {has_neg}")
    if dist:
        print("  Distance matrix:")
        for row in dist:
            formatted = [f"{x:6.1f}" if x != INF else "   inf" for x in row]
            print(f"    [{', '.join(formatted)}]")

    # Example 2: Graph WITHOUT a negative cycle
    print("\nExample 2: Graph without negative cycle")
    n2 = 4
    edges2 = [(0, 1, 4), (0, 3, 5), (1, 2, -3), (2, 3, 1), (3, 2, 2)]
    print(f"  Vertices: {n2}")
    print(f"  Edges (src, dst, weight): {edges2}")
    has_neg2, dist2 = has_negative_cycle_floyd_warshall_with_detection(n2, edges2)
    print(f"  Has negative cycle: {has_neg2}")
    if dist2:
        print("  Distance matrix:")
        for row in dist2:
            formatted = [f"{x:6.1f}" if x != INF else "   inf" for x in row]
            print(f"    [{', '.join(formatted)}]")

    # Example 3: Floyd-Warshall classic example (no negative cycle)
    # Input from GeeksforGeeks
    print("\nExample 3: Classic Floyd-Warshall example")
    INF_VAL = int(1e8)
    n3 = 5
    edges3 = [
        (0, 1, 4),
        (0, 3, 5),
        (1, 2, 1),
        (1, 4, 6),
        (2, 0, 2),
        (2, 3, 3),
        (3, 2, 1),
        (3, 4, 2),
        (4, 0, 1),
        (4, 3, 4),
    ]
    print(f"  Vertices: {n3}")
    print(f"  Edges: {edges3}")
    dist3, has_neg3 = all_pairs_shortest_paths(n3, edges3)
    print(f"  Has negative cycle: {has_neg3}")
    print("  Distance matrix:")
    for row in dist3:
        formatted = [f"{x:6.1f}" if x != INF else "   inf" for x in row]
        print(f"    [{', '.join(formatted)}]")

    # Example 4: Graph where negative cycle is only detectable via FW
    # Multiple paths with some negative edges
    print("\nExample 4: Complex graph with negative cycle")
    n4 = 4
    edges4 = [
        (0, 1, 1),
        (1, 2, -1),
        (2, 3, -1),
        (3, 1, -1),
    ]
    print(f"  Vertices: {n4}")
    print(f"  Edges (src, dst, weight): {edges4}")
    print(f"  Has negative cycle: {has_negative_cycle_floyd_warshall(n4, edges4)}")

    print("\n" + "=" * 60)

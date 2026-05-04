"""
Bellman-Ford Algorithm

The Bellman-Ford algorithm finds shortest paths from a single source vertex
to all other vertices in a weighted directed graph. Unlike Dijkstra's algorithm,
it can handle graphs with negative edge weights and can detect negative weight cycles.

Algorithm:
1. Initialize distances to infinity, source distance to 0
2. Relax all edges |V| - 1 times
3. Check for negative weight cycles by attempting one more relaxation

Time Complexity: O(V * E)
Space Complexity: O(V)
"""

from typing import List, Tuple, Optional


def bellman_ford(
    V: int, edges: List[Tuple[int, int, int]], src: int
) -> Optional[List[int]]:
    """
    Find shortest distances from source to all vertices using Bellman-Ford algorithm.

    Args:
        V: Number of vertices (labeled 0 to V-1)
        edges: List of edges as (u, v, weight) tuples representing directed edge u->v
        src: Source vertex index

    Returns:
        List of shortest distances from src to all vertices, or None if a
        negative weight cycle is detected.
        Unreachable vertices have distance = infinity.
    """
    INF = 10**8
    dist = [INF] * V
    dist[src] = 0

    # Relax all edges |V| - 1 times
    for _ in range(V - 1):
        updated = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                updated = True
        # Early termination if no updates
        if not updated:
            break

    # Check for negative weight cycles
    for u, v, w in edges:
        if dist[u] != INF and dist[u] + w < dist[v]:
            return None  # Negative weight cycle detected

    return dist


def bellman_ford_with_path(
    V: int, edges: List[Tuple[int, int, int]], src: int, target: int
) -> Optional[Tuple[int, List[int]]]:
    """
    Find shortest path and distance from source to a specific target.

    Args:
        V: Number of vertices (labeled 0 to V-1)
        edges: List of edges as (u, v, weight) tuples
        src: Source vertex index
        target: Target vertex index

    Returns:
        Tuple of (distance, path) or None if negative cycle or unreachable.
    """
    INF = 10**8
    dist = [INF] * V
    prev = [-1] * V
    dist[src] = 0

    # Relax all edges |V| - 1 times
    for _ in range(V - 1):
        updated = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                updated = True
        if not updated:
            break

    # Check for negative weight cycles
    for u, v, w in edges:
        if dist[u] != INF and dist[u] + w < dist[v]:
            return None

    if dist[target] == INF:
        return None

    # Reconstruct path
    path = []
    node = target
    while node != -1:
        path.append(node)
        node = prev[node]
    path.reverse()

    return dist[target], path


if __name__ == "__main__":
    # Example 1: Graph with negative edges (no negative cycle)
    # Edges: u, v, weight
    V = 5
    edges: List[Tuple[int, int, int]] = [
        (0, 1, -1),
        (0, 2, 4),
        (1, 2, 3),
        (1, 3, 2),
        (1, 4, 2),
        (3, 2, 5),
        (3, 1, 1),
        (4, 3, -3),
    ]

    print("Bellman-Ford Algorithm - Example 1")
    print("=" * 40)
    src = 0
    result = bellman_ford(V, edges, src)

    if result is None:
        print("Graph contains a negative weight cycle!")
    else:
        print(f"Source vertex: {src}")
        for i, d in enumerate(result):
            if d == 10**8:
                print(f"  Vertex {i}: Unreachable")
            else:
                print(f"  Vertex {i}: {d}")

    print()

    # Example 2: Graph with negative weight cycle
    V2 = 3
    edges2: List[Tuple[int, int, int]] = [
        (0, 1, 1),
        (1, 2, -1),
        (2, 0, -1),  # Creates negative cycle: 0->1->2->0 = -1
    ]

    print("Example 2 - Negative Weight Cycle Detection:")
    result2 = bellman_ford(V2, edges2, 0)
    if result2 is None:
        print("  Graph contains a negative weight cycle!")
    else:
        print("  No negative cycle detected.")

    print()

    # Example 3: Path reconstruction
    V3 = 5
    edges3: List[Tuple[int, int, int]] = [
        (0, 1, 6),
        (0, 2, 7),
        (1, 2, 8),
        (1, 3, -4),
        (1, 4, 5),
        (2, 3, 9),
        (2, 4, -3),
        (3, 1, 7),
        (4, 0, 2),
        (4, 3, 7),
    ]

    print("Example 3 - Path Reconstruction (0 to 3):")
    path_result = bellman_ford_with_path(V3, edges3, 0, 3)
    if path_result:
        dist, path = path_result
        print(f"  Distance: {dist}")
        print(f"  Path: {' -> '.join(map(str, path))}")
    else:
        print("  No path found or negative cycle detected.")

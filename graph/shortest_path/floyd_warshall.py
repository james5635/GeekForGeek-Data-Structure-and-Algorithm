"""
Floyd-Warshall Algorithm

The Floyd-Warshall algorithm finds shortest paths between all pairs of vertices
in a weighted graph. It works for both directed and undirected graphs and can
handle negative edge weights, but not negative weight cycles.

The algorithm uses dynamic programming, iteratively improving distance estimates
by considering each vertex as a potential intermediate node.

Algorithm:
1. Initialize distance matrix with direct edge weights
2. For each vertex k as intermediate:
   For each pair (i, j):
     dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

Time Complexity: O(V^3)
Space Complexity: O(V^2)
"""

from typing import List, Optional, Tuple


def floyd_warshall(dist: List[List[int]]) -> List[List[int]]:
    """
    Compute all-pairs shortest paths using Floyd-Warshall algorithm.

    Args:
        dist: N x N matrix where dist[i][j] is the weight of edge i->j.
              Use a large value (e.g., 10^8) for no direct edge.
              dist[i][i] should be 0.

    Returns:
        N x N matrix of shortest distances between all pairs.
        dist[i][j] contains the shortest distance from i to j.
    """
    V = len(dist)
    INF = int(1e8)

    # Create a working copy
    d = [row[:] for row in dist]

    # For each intermediate vertex k
    for k in range(V):
        for i in range(V):
            for j in range(V):
                # Update if path through k is shorter
                if d[i][k] != INF and d[k][j] != INF:
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])

    return d


def floyd_warshall_with_path(
    graph: List[List[int]],
) -> Tuple[List[List[int]], List[List[Optional[int]]]]:
    """
    Compute all-pairs shortest paths with path reconstruction.

    Args:
        graph: N x N adjacency matrix. graph[i][j] is edge weight, 0 means no edge
               (except diagonal). Use float('inf') for no edge.

    Returns:
        Tuple of (distance_matrix, next_vertex_matrix)
        - distance_matrix[i][j]: shortest distance from i to j
        - next_vertex_matrix[i][j]: next vertex on shortest path from i to j
    """
    V = len(graph)
    INF = float("inf")

    # Initialize distance matrix
    dist = [[INF] * V for _ in range(V)]
    next_vertex: List[List[Optional[int]]] = [[None] * V for _ in range(V)]

    for i in range(V):
        dist[i][i] = 0
        next_vertex[i][i] = i

    for i in range(V):
        for j in range(V):
            if graph[i][j] != 0 and i != j:
                dist[i][j] = graph[i][j]
                next_vertex[i][j] = j

    # Floyd-Warshall with path tracking
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] != INF and dist[k][j] != INF:
                    new_dist = dist[i][k] + dist[k][j]
                    if new_dist < dist[i][j]:
                        dist[i][j] = new_dist
                        next_vertex[i][j] = next_vertex[i][k]

    return dist, next_vertex


def reconstruct_path(
    start: int, end: int, next_vertex: List[List[Optional[int]]]
) -> List[int]:
    """
    Reconstruct the shortest path between two vertices.

    Args:
        start: Starting vertex
        end: Ending vertex
        next_vertex: Next vertex matrix from floyd_warshall_with_path

    Returns:
        List of vertices on the shortest path, empty if no path exists.
    """
    if next_vertex[start][end] is None:
        return []

    path = [start]
    current = start
    while current != end:
        current = next_vertex[current][end]
        path.append(current)

    return path


def has_negative_cycle(dist: List[List[int]]) -> bool:
    """
    Check if the result matrix indicates a negative weight cycle.

    Args:
        dist: Distance matrix from floyd_warshall

    Returns:
        True if a negative cycle exists, False otherwise.
    """
    for i in range(len(dist)):
        if dist[i][i] < 0:
            return True
    return False


if __name__ == "__main__":
    # Example 1: Standard graph
    INF = int(1e8)
    dist_matrix = [
        [0, 4, INF, 5, INF],
        [INF, 0, 1, INF, 6],
        [2, INF, 0, 3, INF],
        [INF, INF, 1, 0, 2],
        [1, INF, INF, 4, 0],
    ]

    print("Floyd-Warshall Algorithm - All Pairs Shortest Paths")
    print("=" * 50)
    print("\nInput adjacency matrix:")
    for row in dist_matrix:
        print("  ", [x if x != INF else "INF" for x in row])

    result = floyd_warshall(dist_matrix)

    print("\nShortest distance matrix:")
    for i, row in enumerate(result):
        print(f"  {i}: ", [x if x != INF else "INF" for x in row])

    print()

    # Example 2: Path reconstruction
    graph2 = [
        [0, 3, 0, 7],
        [2, 0, 2, 0],
        [0, 1, 0, 1],
        [0, 0, 2, 0],
    ]

    print("Example 2 - Path Reconstruction:")
    dist2, nxt = floyd_warshall_with_path(graph2)

    V2 = len(graph2)
    for i in range(V2):
        for j in range(V2):
            if i != j and dist2[i][j] != float("inf"):
                path = reconstruct_path(i, j, nxt)
                print(
                    f"  Path {i} -> {j}: {' -> '.join(map(str, path))}, Distance: {dist2[i][j]}"
                )

    print()

    # Example 3: Negative edges (no negative cycle)
    INF3 = int(1e8)
    dist3 = [
        [0, INF3, -2, INF3],
        [4, 0, 3, INF3],
        [INF3, INF3, 0, 2],
        [INF3, -1, INF3, 0],
    ]

    print("Example 3 - Graph with Negative Edges:")
    result3 = floyd_warshall(dist3)
    for i, row in enumerate(result3):
        print(f"  {i}: ", [x if x != INF3 else "INF" for x in row])

    if has_negative_cycle(result3):
        print("\n  Negative cycle detected!")
    else:
        print("\n  No negative cycle.")

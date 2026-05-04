"""
Johnson's Algorithm for All-Pairs Shortest Paths

Johnson's algorithm finds the shortest paths between all pairs of vertices
in a weighted directed graph. It can handle negative edge weights but not
negative weight cycles. It combines Bellman-Ford and Dijkstra's algorithms:

1. Add a new vertex s connected to all vertices with zero-weight edges
2. Run Bellman-Ford from s to get potential values h[v]
3. Reweight edges: w'(u,v) = w(u,v) + h[u] - h[v] (all edges become non-negative)
4. Remove s and run Dijkstra from each vertex
5. Adjust distances back: d(u,v) = d'(u,v) - h[u] + h[v]

This is more efficient than Floyd-Warshall for sparse graphs.

Time Complexity: O(V^2 log V + VE)
Space Complexity: O(V^2)
"""

import heapq
from typing import List, Tuple, Optional


def johnson_algorithm(
    V: int, edges: List[Tuple[int, int, int]]
) -> Optional[List[List[int]]]:
    """
    Find all-pairs shortest paths using Johnson's algorithm.

    Args:
        V: Number of vertices (labeled 0 to V-1)
        edges: List of (u, v, weight) tuples for directed edges

    Returns:
        V x V matrix where result[i][j] is shortest distance from i to j,
        or None if a negative weight cycle exists.
        Unreachable pairs have distance = infinity.
    """
    INF = float("inf")

    # Step 1: Build adjacency list for Bellman-Ford
    # Add a virtual source vertex V connected to all vertices with weight 0
    bf_edges = list(edges)
    for i in range(V):
        bf_edges.append((V, i, 0))

    # Step 2: Run Bellman-Ford from virtual source to get h[] values
    h = _bellman_ford(V + 1, bf_edges, V)

    if h is None:
        return None  # Negative weight cycle detected

    # Remove the virtual source value
    h = h[:V]

    # Step 3: Reweight edges using h values
    reweighted_adj: List[List[Tuple[int, int]]] = [[] for _ in range(V)]
    for u, v, w in edges:
        new_weight = w + h[u] - h[v]
        reweighted_adj[u].append((v, new_weight))

    # Step 4: Run Dijkstra from each vertex
    result: List[List[int]] = [[INF] * V for _ in range(V)]

    for s in range(V):
        dist = _dijkstra(V, reweighted_adj, s)

        for v in range(V):
            if dist[v] != INF:
                # Adjust back to original weights
                result[s][v] = dist[v] + h[v] - h[s]

    return result


def _bellman_ford(
    V: int, edges: List[Tuple[int, int, int]], src: int
) -> Optional[List[int]]:
    """
    Bellman-Ford algorithm to find shortest paths from source.

    Returns:
        List of distances or None if negative cycle detected.
    """
    INF = float("inf")
    dist = [INF] * V
    dist[src] = 0

    # Relax edges V - 1 times
    for _ in range(V - 1):
        updated = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                updated = True
        if not updated:
            break

    # Check for negative cycles
    for u, v, w in edges:
        if dist[u] != INF and dist[u] + w < dist[v]:
            return None

    return dist


def _dijkstra(V: int, adj: List[List[Tuple[int, int]]], src: int) -> List[int]:
    """
    Dijkstra's algorithm for single-source shortest paths.

    Returns:
        List of distances from src to all vertices.
    """
    INF = float("inf")
    dist = [INF] * V
    dist[src] = 0

    pq: List[Tuple[int, int]] = [(0, src)]

    while pq:
        d, u = heapq.heappop(pq)

        if d > dist[u]:
            continue

        for v, weight in adj[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))

    return dist


if __name__ == "__main__":
    # Example 1: Graph with negative edges
    print("Johnson's Algorithm - All Pairs Shortest Paths")
    print("=" * 50)

    V = 4
    edges: List[Tuple[int, int, int]] = [
        (0, 1, -8),
        (0, 2, 2),
        (0, 3, 4),
        (1, 2, 2),
        (1, 3, 6),
        (2, 3, 2),
    ]

    result = johnson_algorithm(V, edges)

    if result is None:
        print("Graph contains a negative weight cycle!")
    else:
        print("Shortest distance matrix:")
        print("     ", end="")
        for j in range(V):
            print(f"  {j}  ", end="")
        print()
        for i, row in enumerate(result):
            print(f"  {i}: ", end="")
            for val in row:
                if val == float("inf"):
                    print(" INF ", end="")
                else:
                    print(f" {val:3d} ", end="")
            print()

    print()

    # Example 2: Another graph
    V2 = 5
    edges2: List[Tuple[int, int, int]] = [
        (0, 1, 3),
        (0, 2, 8),
        (0, 4, -4),
        (1, 3, 1),
        (1, 4, 7),
        (2, 1, 4),
        (3, 0, 2),
        (3, 2, -5),
        (4, 3, 6),
    ]

    print("Example 2 - Graph with Negative Edges:")
    result2 = johnson_algorithm(V2, edges2)

    if result2 is None:
        print("  Negative weight cycle detected!")
    else:
        for i in range(V2):
            for j in range(V2):
                d = result2[i][j]
                if d == float("inf"):
                    print(f"  dist({i}, {j}) = INF")
                else:
                    print(f"  dist({i}, {j}) = {d}")
            print()

    print()

    # Example 3: Graph with negative cycle
    V3 = 3
    edges3: List[Tuple[int, int, int]] = [
        (0, 1, 1),
        (1, 2, -1),
        (2, 0, -1),  # Negative cycle
    ]

    print("Example 3 - Negative Cycle Detection:")
    result3 = johnson_algorithm(V3, edges3)
    if result3 is None:
        print("  Graph contains a negative weight cycle!")
    else:
        print("  No negative cycle found.")

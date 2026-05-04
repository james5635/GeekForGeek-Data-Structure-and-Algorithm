"""
Minimum Weight Cycle in Undirected Graph

Given an undirected, weighted graph, find the cycle with the minimum total
weight (sum of edge weights). A cycle is a path that starts and ends at the
same vertex without repeating edges.

Approach (Dijkstra-based):
For each edge (u, v) with weight w:
1. Temporarily remove edge (u, v)
2. Find shortest path from u to v in the remaining graph
3. The cycle weight = shortest_path(u, v) + w
4. Track the minimum across all edges

This ensures we find the minimum weight cycle by considering every edge as
part of a potential cycle.

Time Complexity: O(E * (V + E) * log V) with Dijkstra
Space Complexity: O(V + E)
"""

import heapq
from typing import List, Tuple


def find_min_cycle(V: int, edges: List[List[int]]) -> int:
    """
    Find the minimum weight cycle in an undirected weighted graph.

    Args:
        V: Number of vertices (labeled 0 to V-1)
        edges: List of [u, v, w] representing undirected edges

    Returns:
        Minimum cycle weight, or -1 if no cycle exists.
    """
    INF = float("inf")

    # Build adjacency list
    adj: List[List[Tuple[int, int]]] = [[] for _ in range(V)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))

    min_cycle = INF

    # For each edge, find shortest path between its endpoints excluding this edge
    for u, v, w in edges:
        dist = _shortest_path_excluding_edge(V, adj, u, v, u, v)
        if dist != INF:
            min_cycle = min(min_cycle, dist + w)

    return min_cycle if min_cycle != INF else -1


def _shortest_path_excluding_edge(
    V: int,
    adj: List[List[Tuple[int, int]]],
    src: int,
    dest: int,
    exclude_u: int,
    exclude_v: int,
) -> float:
    """
    Find shortest path from src to dest, excluding the edge between exclude_u and exclude_v.

    Args:
        V: Number of vertices
        adj: Adjacency list
        src: Source vertex
        dest: Destination vertex
        exclude_u, exclude_v: Vertices of the edge to exclude

    Returns:
        Shortest distance, or infinity if no path exists.
    """
    INF = float("inf")
    dist = [INF] * V
    dist[src] = 0

    pq: List[Tuple[float, int]] = [(0, src)]

    while pq:
        d, u = heapq.heappop(pq)

        if d > dist[u]:
            continue

        if u == dest:
            break

        for v, weight in adj[u]:
            # Skip the excluded edge
            if (u == exclude_u and v == exclude_v) or (
                u == exclude_v and v == exclude_u
            ):
                continue

            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))

    return dist[dest]


def find_min_cycle_with_path(V: int, edges: List[List[int]]) -> Tuple[int, List[int]]:
    """
    Find the minimum weight cycle and return the cycle vertices.

    Args:
        V: Number of vertices
        edges: List of [u, v, w] representing undirected edges

    Returns:
        Tuple of (min_cycle_weight, cycle_vertices)
        Returns (-1, []) if no cycle exists.
    """
    INF = float("inf")

    # Build adjacency list
    adj: List[List[Tuple[int, int]]] = [[] for _ in range(V)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))

    min_cycle = INF
    best_path: List[int] = []

    for u, v, w in edges:
        dist, path = _shortest_path_with_tracking(V, adj, u, v, u, v)
        if dist != INF:
            cycle_weight = dist + w
            if cycle_weight < min_cycle:
                min_cycle = cycle_weight
                best_path = path + [u]  # Close the cycle

    if min_cycle == INF:
        return -1, []

    return min_cycle, best_path


def _shortest_path_with_tracking(
    V: int,
    adj: List[List[Tuple[int, int]]],
    src: int,
    dest: int,
    exclude_u: int,
    exclude_v: int,
) -> Tuple[float, List[int]]:
    """
    Find shortest path with vertex tracking.

    Returns:
        Tuple of (distance, path_as_list)
    """
    INF = float("inf")
    dist = [INF] * V
    prev = [-1] * V
    dist[src] = 0

    pq: List[Tuple[float, int]] = [(0, src)]

    while pq:
        d, u = heapq.heappop(pq)

        if d > dist[u]:
            continue

        if u == dest:
            break

        for v, weight in adj[u]:
            if (u == exclude_u and v == exclude_v) or (
                u == exclude_v and v == exclude_u
            ):
                continue

            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                prev[v] = u
                heapq.heappush(pq, (dist[v], v))

    if dist[dest] == INF:
        return INF, []

    # Reconstruct path
    path = []
    node = dest
    while node != -1:
        path.append(node)
        node = prev[node]
    path.reverse()

    return dist[dest], path


if __name__ == "__main__":
    # Example 1: From GFG
    print("Minimum Weight Cycle in Undirected Graph")
    print("=" * 50)

    V1 = 7
    edges1: List[List[int]] = [
        [0, 1, 2],
        [1, 2, 2],
        [1, 3, 1],
        [1, 4, 1],
        [0, 4, 3],
        [3, 4, 1],
        [2, 3, 4],
    ]

    result1 = find_min_cycle(V1, edges1)
    print(f"Example 1:")
    print(f"  Minimum cycle weight: {result1}")
    # Expected: 6 (cycle 0->1->4->0 = 2+1+3 or 1->3->4->1 = 1+1+1... check)

    print()

    # Example 2: Simple triangle
    V2 = 3
    edges2: List[List[int]] = [
        [0, 1, 1],
        [1, 2, 2],
        [2, 0, 3],
    ]

    result2 = find_min_cycle(V2, edges2)
    print(f"Example 2 - Triangle:")
    print(f"  Minimum cycle weight: {result2}")
    # Cycle: 0->1->2->0 = 1+2+3 = 6

    print()

    # Example 3: With path reconstruction
    V3 = 4
    edges3: List[List[int]] = [
        [0, 1, 1],
        [1, 2, 2],
        [2, 3, 1],
        [3, 0, 3],
        [0, 2, 5],
    ]

    result3, path3 = find_min_cycle_with_path(V3, edges3)
    print(f"Example 3 - With Path:")
    print(f"  Minimum cycle weight: {result3}")
    print(f"  Cycle: {' -> '.join(map(str, path3))}")

    print()

    # Example 4: No cycle
    V4 = 4
    edges4: List[List[int]] = [
        [0, 1, 1],
        [1, 2, 2],
        [2, 3, 3],
    ]

    result4 = find_min_cycle(V4, edges4)
    print(f"Example 4 - No Cycle:")
    print(f"  Result: {result4}")  # Expected: -1

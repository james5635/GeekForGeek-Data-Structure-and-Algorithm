"""
Dijkstra's Shortest Path Algorithm

Dijkstra's algorithm finds the shortest paths from a source vertex to all other
vertices in a weighted graph with non-negative edge weights. It uses a greedy
approach, always selecting the unvisited vertex with the minimum known distance.

Algorithm:
1. Initialize distances to infinity, source distance to 0
2. Use a min-heap (priority queue) to process vertices
3. For each vertex, relax all adjacent edges
4. Continue until all reachable vertices are processed

Time Complexity: O((V + E) * log V) with priority queue
Space Complexity: O(V + E)
"""

import heapq
from typing import List, Tuple


def dijkstra(adj: List[List[Tuple[int, int]]], src: int) -> List[int]:
    """
    Find shortest distances from source to all vertices using Dijkstra's algorithm.

    Args:
        adj: Adjacency list where adj[u] contains list of (v, weight) tuples
        src: Source vertex index

    Returns:
        List of shortest distances from src to all vertices.
        Unreachable vertices have distance = infinity.
    """
    V = len(adj)
    dist = [float("inf")] * V
    dist[src] = 0

    # Min-heap storing (distance, vertex)
    pq: List[Tuple[int, int]] = [(0, src)]

    while pq:
        d, u = heapq.heappop(pq)

        # Skip if we already found a shorter path
        if d > dist[u]:
            continue

        # Explore all neighbors
        for v, weight in adj[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))

    return dist


def dijkstra_with_path(
    adj: List[List[Tuple[int, int]]], src: int, target: int
) -> Tuple[int, List[int]]:
    """
    Find shortest path and distance from source to a specific target.

    Args:
        adj: Adjacency list where adj[u] contains list of (v, weight) tuples
        src: Source vertex index
        target: Target vertex index

    Returns:
        Tuple of (shortest_distance, path_as_list_of_vertices)
    """
    V = len(adj)
    dist = [float("inf")] * V
    dist[src] = 0
    prev = [-1] * V

    pq: List[Tuple[int, int]] = [(0, src)]

    while pq:
        d, u = heapq.heappop(pq)

        if d > dist[u]:
            continue

        if u == target:
            break

        for v, weight in adj[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                prev[v] = u
                heapq.heappush(pq, (dist[v], v))

    # Reconstruct path
    if dist[target] == float("inf"):
        return float("inf"), []

    path = []
    node = target
    while node != -1:
        path.append(node)
        node = prev[node]
    path.reverse()

    return dist[target], path


if __name__ == "__main__":
    # Example 1: Basic graph
    #     4       6
    # 0 ----- 1 ----- 4
    # |       |       |
    # 8       3       10
    # |       |       |
    # 2 ----- 3 ----- (implicit)
    V = 5
    adj: List[List[Tuple[int, int]]] = [
        [(1, 4), (2, 8)],  # 0
        [(0, 4), (4, 6), (2, 3)],  # 1
        [(0, 8), (3, 2), (1, 3)],  # 2
        [(2, 2), (4, 10)],  # 3
        [(1, 6), (3, 10)],  # 4
    ]

    src = 0
    distances = dijkstra(adj, src)

    print("Dijkstra's Algorithm - Shortest Distances")
    print("=" * 40)
    print(f"Source vertex: {src}")
    for i, dist in enumerate(distances):
        if dist == float("inf"):
            print(f"  Vertex {i}: Unreachable")
        else:
            print(f"  Vertex {i}: {dist}")

    print()

    # Example 2: Shortest path with path reconstruction
    print("Shortest Path from 0 to 4:")
    distance, path = dijkstra_with_path(adj, 0, 4)
    print(f"  Distance: {distance}")
    print(f"  Path: {' -> '.join(map(str, path))}")

    print()

    # Example 3: Graph from GFG
    adj2: List[List[Tuple[int, int]]] = [
        [(1, 1), (2, 4)],  # 0
        [(0, 1), (2, 2)],  # 1
        [(0, 4), (1, 2), (3, 1)],  # 2
        [(2, 1)],  # 3
    ]

    print("Example 3 - Another Graph:")
    distances2 = dijkstra(adj2, 0)
    for i, dist in enumerate(distances2):
        print(f"  Vertex 0 -> {i}: {dist}")

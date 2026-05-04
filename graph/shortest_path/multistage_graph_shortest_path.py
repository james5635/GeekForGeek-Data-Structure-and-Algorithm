"""
Multistage Graph Shortest Path

A multistage graph is a directed graph where vertices are partitioned into
k >= 2 disjoint sets (stages). Edges only go from stage i to stage i+1.
The goal is to find the minimum cost path from a source (stage 1) to a
destination (stage k).

This is solved efficiently using dynamic programming with a backward approach:
- cost[i] = minimum cost to reach the destination from vertex i
- cost[i] = min{c(i,j) + cost[j]} for all edges (i,j)

Time Complexity: O(V + E)
Space Complexity: O(V)
"""

from typing import List, Tuple, Dict, Set


def multistage_shortest_path(
    V: int, edges: List[Tuple[int, int, int]], stages: Dict[int, int], k: int
) -> Tuple[int, List[int]]:
    """
    Find the shortest path in a multistage graph using dynamic programming.

    Args:
        V: Number of vertices (labeled 0 to V-1)
        edges: List of (u, v, weight) tuples where edge goes from stage i to i+1
        stages: Dictionary mapping vertex -> stage number (1-indexed)
        k: Number of stages

    Returns:
        Tuple of (minimum_cost, path_as_list)
    """
    INF = float("inf")

    # Build adjacency list
    adj: List[List[Tuple[int, int]]] = [[] for _ in range(V)]
    for u, v, w in edges:
        adj[u].append((v, w))

    # cost[i] = minimum cost from vertex i to destination
    cost = [INF] * V
    # d[i] = next vertex on shortest path from i
    d = [-1] * V

    # Find source (stage 1) and destination (stage k) vertices
    source = None
    destination = None
    for v, stage in stages.items():
        if stage == 1:
            source = v
        elif stage == k:
            destination = v

    if source is None or destination is None:
        raise ValueError("Source (stage 1) or destination (stage k) not found")

    # Initialize destination cost
    cost[destination] = 0

    # Process stages backward (from k-1 to 1)
    for stage in range(k - 1, 0, -1):
        # Get all vertices in this stage
        stage_vertices = [v for v, s in stages.items() if s == stage]

        for i in stage_vertices:
            # Find minimum cost path through neighbors
            for j, w in adj[i]:
                if cost[j] != INF and w + cost[j] < cost[i]:
                    cost[i] = w + cost[j]
                    d[i] = j

    # Reconstruct path
    path = []
    current = source
    while current != -1:
        path.append(current)
        current = d[current]

    return cost[source], path


def multistage_forward(
    V: int, edges: List[Tuple[int, int, int]], stages: Dict[int, int], k: int
) -> Tuple[int, List[int]]:
    """
    Find shortest path using forward approach (from source to destination).

    Args:
        V: Number of vertices
        edges: List of (u, v, weight) tuples
        stages: Dictionary mapping vertex -> stage number
        k: Number of stages

    Returns:
        Tuple of (minimum_cost, path_as_list)
    """
    INF = float("inf")

    # Build reverse adjacency list (for backward edges)
    reverse_adj: List[List[Tuple[int, int]]] = [[] for _ in range(V)]
    for u, v, w in edges:
        reverse_adj[v].append((u, w))

    # Find source and destination
    source = None
    destination = None
    for v, stage in stages.items():
        if stage == 1:
            source = v
        elif stage == k:
            destination = v

    if source is None or destination is None:
        raise ValueError("Source or destination not found")

    # cost[i] = minimum cost from source to vertex i
    cost = [INF] * V
    cost[source] = 0

    # Process stages forward (from 2 to k)
    for stage in range(2, k + 1):
        stage_vertices = [v for v, s in stages.items() if s == stage]

        for j in stage_vertices:
            for i, w in reverse_adj[j]:
                if cost[i] != INF and cost[i] + w < cost[j]:
                    cost[j] = cost[i] + w

    # Reconstruct path by backtracking from destination
    path = [destination]
    current = destination
    while current != source:
        for i, w in reverse_adj[current]:
            if cost[i] + w == cost[current]:
                path.append(i)
                current = i
                break
    path.reverse()

    return cost[destination], path


if __name__ == "__main__":
    # Example 1: Classic multistage graph
    # Stage 1: 0 (source)
    # Stage 2: 1, 2, 3
    # Stage 3: 4, 5
    # Stage 4: 6, 7
    # Stage 5: 8 (destination)
    #
    # Edges with costs:
    # 0->1: 9,  0->2: 7,  0->3: 3
    # 1->4: 4,  1->5: 2
    # 2->4: 2,  2->5: 7
    # 3->4: 11, 3->5: 11
    # 4->6: 6,  4->7: 5
    # 5->6: 4,  5->7: 3
    # 6->8: 4
    # 7->8: 2

    print("Multistage Graph Shortest Path")
    print("=" * 50)

    V1 = 9
    edges1: List[Tuple[int, int, int]] = [
        (0, 1, 9),
        (0, 2, 7),
        (0, 3, 3),
        (1, 4, 4),
        (1, 5, 2),
        (2, 4, 2),
        (2, 5, 7),
        (3, 4, 11),
        (3, 5, 11),
        (4, 6, 6),
        (4, 7, 5),
        (5, 6, 4),
        (5, 7, 3),
        (6, 8, 4),
        (7, 8, 2),
    ]

    stages1: Dict[int, int] = {
        0: 1,
        1: 2,
        2: 2,
        3: 2,
        4: 3,
        5: 3,
        6: 4,
        7: 4,
        8: 5,
    }
    k1 = 5

    # Backward approach
    cost1, path1 = multistage_shortest_path(V1, edges1, stages1, k1)
    print(f"Backward Approach:")
    print(f"  Minimum cost: {cost1}")
    print(f"  Path: {' -> '.join(map(str, path1))}")

    print()

    # Forward approach
    cost2, path2 = multistage_forward(V1, edges1, stages1, k1)
    print(f"Forward Approach:")
    print(f"  Minimum cost: {cost2}")
    print(f"  Path: {' -> '.join(map(str, path2))}")

    print()

    # Example 2: Another multistage graph
    print("Example 2 - Smaller Graph:")
    V2 = 6
    edges2: List[Tuple[int, int, int]] = [
        (0, 1, 1),
        (0, 2, 2),
        (1, 3, 4),
        (1, 4, 3),
        (2, 3, 1),
        (2, 4, 5),
        (3, 5, 2),
        (4, 5, 1),
    ]

    stages2: Dict[int, int] = {
        0: 1,
        1: 2,
        2: 2,
        3: 3,
        4: 3,
        5: 4,
    }
    k2 = 4

    cost3, path3 = multistage_shortest_path(V2, edges2, stages2, k2)
    print(f"  Minimum cost: {cost3}")
    print(f"  Path: {' -> '.join(map(str, path3))}")

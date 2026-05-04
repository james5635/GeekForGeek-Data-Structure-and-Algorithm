"""
Karp's Minimum Mean Weight Cycle Algorithm

Given a directed, strongly connected graph with edge weights, this algorithm
finds the cycle with the minimum mean (average) weight. The mean weight of a
cycle is the sum of its edge weights divided by the number of edges.

Karp's theorem states that the minimum mean weight lambda* can be computed as:
    lambda* = min_v max_0<=k<=n-1 (F_n(v) - F_k(v)) / (n - k)

where F_k(v) is the minimum weight of any path of exactly k edges from a
fixed source s to vertex v.

Algorithm:
1. Choose an arbitrary source vertex
2. Compute F_k(v) for all k in [0, n] and all vertices v using DP
3. For each vertex v, compute max(F_n(v) - F_k(v)) / (n - k) for all k
4. Return the minimum of these values across all vertices

Time Complexity: O(V * E)
Space Complexity: O(V^2)
"""

from typing import List, Tuple


def karp_minimum_mean_cycle(V: int, edges: List[Tuple[int, int, int]]) -> float:
    """
    Find the minimum mean weight of a cycle in a directed graph.

    Args:
        V: Number of vertices (labeled 0 to V-1)
        edges: List of (u, v, weight) tuples for directed edges

    Returns:
        The minimum mean weight of any cycle in the graph.
        Returns float('inf') if no cycle exists.
    """
    INF = float("inf")

    # Build reverse adjacency: for each vertex v, store incoming edges (u, w)
    in_edges: List[List[Tuple[int, int]]] = [[] for _ in range(V)]
    for u, v, w in edges:
        in_edges[v].append((u, w))

    # dp[k][v] = minimum weight path of exactly k edges from vertex 0 to v
    dp: List[List[float]] = [[INF] * V for _ in range(V + 1)]
    dp[0][0] = 0  # Base case: 0 edges from source to itself costs 0

    # Fill DP table
    for k in range(1, V + 1):
        for v in range(V):
            for u, w in in_edges[v]:
                if dp[k - 1][u] != INF:
                    dp[k][v] = min(dp[k][v], dp[k - 1][u] + w)

    # Compute minimum mean weight using Karp's formula
    result = INF

    for v in range(V):
        if dp[V][v] == INF:
            continue

        max_val = -INF
        for k in range(V):
            if dp[k][v] != INF:
                mean = (dp[V][v] - dp[k][v]) / (V - k)
                max_val = max(max_val, mean)

        result = min(result, max_val)

    return result


def karp_minimum_mean_cycle_with_cycle(
    V: int, edges: List[Tuple[int, int, int]]
) -> Tuple[float, List[int]]:
    """
    Find the minimum mean weight cycle and return the cycle vertices.

    Args:
        V: Number of vertices
        edges: List of (u, v, weight) tuples

    Returns:
        Tuple of (min_mean_weight, cycle_vertices)
    """
    INF = float("inf")

    # Build reverse adjacency
    in_edges: List[List[Tuple[int, int]]] = [[] for _ in range(V)]
    for u, v, w in edges:
        in_edges[v].append((u, w))

    # DP with parent tracking
    dp: List[List[float]] = [[INF] * V for _ in range(V + 1)]
    parent: List[List[int]] = [[-1] * V for _ in range(V + 1)]
    dp[0][0] = 0

    for k in range(1, V + 1):
        for v in range(V):
            for u, w in in_edges[v]:
                if dp[k - 1][u] != INF:
                    new_val = dp[k - 1][u] + w
                    if new_val < dp[k][v]:
                        dp[k][v] = new_val
                        parent[k][v] = u

    # Find the vertex that minimizes the mean
    result = INF
    best_v = -1
    best_k = -1

    for v in range(V):
        if dp[V][v] == INF:
            continue

        max_val = -INF
        max_k = -1
        for k in range(V):
            if dp[k][v] != INF:
                mean = (dp[V][v] - dp[k][v]) / (V - k)
                if mean > max_val:
                    max_val = mean
                    max_k = k

        if max_val < result:
            result = max_val
            best_v = v
            best_k = max_k

    if best_v == -1:
        return INF, []

    # Reconstruct the cycle from the path
    # The cycle is the last (V - best_k) vertices of the path of length V to best_v
    path = []
    current = best_v
    current_k = V
    while current_k > 0 and current != -1:
        path.append(current)
        current = parent[current_k][current]
        current_k -= 1
    path.reverse()

    # The cycle is at the end of the path
    cycle_length = V - best_k
    if len(path) >= cycle_length:
        cycle = path[-cycle_length:]
    else:
        cycle = path

    return result, cycle


if __name__ == "__main__":
    # Example 1: Graph from GFG
    print("Karp's Minimum Mean Weight Cycle Algorithm")
    print("=" * 50)

    V1 = 4
    edges1: List[Tuple[int, int, int]] = [
        (0, 1, 1),
        (0, 2, 10),
        (1, 2, 3),
        (2, 3, 2),
        (3, 1, 0),
        (3, 0, 8),
    ]

    mean1 = karp_minimum_mean_cycle(V1, edges1)
    print(f"Example 1:")
    print(f"  Minimum mean weight: {mean1:.4f}")

    # Verify: cycles are:
    # 0->1->2->3->0: (1+3+2+8)/4 = 14/4 = 3.5
    # 1->2->3->1: (3+2+0)/3 = 5/3 = 1.667
    # So minimum is 5/3

    print()

    # Example 2: Simple cycle
    V2 = 3
    edges2: List[Tuple[int, int, int]] = [
        (0, 1, 2),
        (1, 2, 3),
        (2, 0, 4),
    ]

    mean2 = karp_minimum_mean_cycle(V2, edges2)
    print(f"Example 2 - Simple 3-cycle:")
    print(f"  Minimum mean weight: {mean2:.4f}")
    # Cycle: 0->1->2->0: (2+3+4)/3 = 3.0

    print()

    # Example 3: Multiple cycles
    V3 = 5
    edges3: List[Tuple[int, int, int]] = [
        (0, 1, 1),
        (1, 2, 1),
        (2, 0, 1),  # Cycle: mean = 1.0
        (2, 3, 10),
        (3, 4, 10),
        (4, 2, 10),  # Cycle: mean = 10.0
    ]

    mean3, cycle3 = karp_minimum_mean_cycle_with_cycle(V3, edges3)
    print(f"Example 3 - Multiple Cycles:")
    print(f"  Minimum mean weight: {mean3:.4f}")
    print(f"  Cycle vertices: {cycle3}")

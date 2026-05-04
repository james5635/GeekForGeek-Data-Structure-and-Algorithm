"""
Chinese Postman Problem (Route Inspection)

Given a connected undirected graph, find the shortest closed walk that
traverses every edge at least once. This is the route a postman would take
to deliver mail on every street and return to the starting point.

Key insight:
- If all vertices have even degree, an Eulerian circuit exists and the
  answer is simply the sum of all edge weights.
- If some vertices have odd degree, we must duplicate some edges to make
  all degrees even. The minimum weight duplication is found by finding
  a minimum weight perfect matching on the odd-degree vertices.

Algorithm:
1. Find all odd-degree vertices
2. Compute shortest paths between all pairs of odd-degree vertices
3. Find minimum weight perfect matching among odd-degree vertices
4. Add the matched edges (duplicate them) to the graph
5. Find Eulerian circuit in the augmented graph

Time Complexity: O(V^3 + 2^k * k^2) where k = number of odd vertices
Space Complexity: O(V^2)
"""

from typing import List, Tuple, Dict, Optional
from collections import defaultdict
import sys


def floyd_warshall(
    adj: Dict[Tuple[int, int], int], num_vertices: int
) -> List[List[int]]:
    """
    Compute all-pairs shortest paths using Floyd-Warshall.

    Args:
        adj: Edge weights as {(u, v): weight}
        num_vertices: Number of vertices

    Returns:
        Distance matrix
    """
    INF = float("inf")
    dist = [[INF] * num_vertices for _ in range(num_vertices)]

    for i in range(num_vertices):
        dist[i][i] = 0

    for (u, v), w in adj.items():
        dist[u][v] = min(dist[u][v], w)
        dist[v][u] = min(dist[v][u], w)

    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


def min_weight_perfect_matching(dist: List[List[int]], odd_vertices: List[int]) -> int:
    """
    Find minimum weight perfect matching using dynamic programming.

    Args:
        dist: All-pairs shortest path distances
        odd_vertices: List of odd-degree vertex indices

    Returns:
        Minimum total weight of the matching
    """
    k = len(odd_vertices)
    if k == 0:
        return 0
    if k % 2 != 0:
        return -1  # Impossible

    # DP with bitmask
    full_mask = (1 << k) - 1
    memo: Dict[int, int] = {}

    def dp(mask: int) -> int:
        if mask == full_mask:
            return 0
        if mask in memo:
            return memo[mask]

        # Find first unmatched vertex
        i = 0
        while mask & (1 << i):
            i += 1

        # Try pairing i with any unmatched j
        result = float("inf")
        for j in range(i + 1, k):
            if not (mask & (1 << j)):
                new_mask = mask | (1 << i) | (1 << j)
                cost = dist[odd_vertices[i]][odd_vertices[j]]
                result = min(result, cost + dp(new_mask))

        memo[mask] = result
        return result

    return dp(0)


def chinese_postman(num_vertices: int, edges: List[Tuple[int, int, int]]) -> Dict:
    """
    Solve the Chinese Postman Problem.

    Args:
        num_vertices: Number of vertices
        edges: List of (u, v, weight) tuples

    Returns:
        Dictionary with solution details
    """
    # Build edge weight map and degree count
    edge_weights: Dict[Tuple[int, int], int] = {}
    degree = [0] * num_vertices
    total_weight = 0

    for u, v, w in edges:
        degree[u] += 1
        degree[v] += 1
        total_weight += w
        key = (min(u, v), max(u, v))
        if key in edge_weights:
            edge_weights[key] = min(edge_weights[key], w)
        else:
            edge_weights[key] = w

    # Find odd-degree vertices
    odd_vertices = [v for v in range(num_vertices) if degree[v] % 2 == 1]

    if len(odd_vertices) == 0:
        # Eulerian circuit exists
        return {
            "total_distance": total_weight,
            "extra_distance": 0,
            "is_eulerian": True,
            "odd_vertices": [],
            "matching_cost": 0,
        }

    # Compute all-pairs shortest paths
    dist = floyd_warshall(edge_weights, num_vertices)

    # Find minimum weight perfect matching
    matching_cost = min_weight_perfect_matching(dist, odd_vertices)

    return {
        "total_distance": total_weight + matching_cost,
        "extra_distance": matching_cost,
        "is_eulerian": False,
        "odd_vertices": odd_vertices,
        "matching_cost": matching_cost,
    }


def solve_chinese_postman_simple(edges: List[Tuple[int, int, int]]) -> int:
    """
    Simple version: just return minimum total distance.

    Args:
        edges: List of (u, v, weight)

    Returns:
        Minimum total distance to traverse all edges
    """
    if not edges:
        return 0

    vertices = set()
    for u, v, w in edges:
        vertices.add(u)
        vertices.add(v)

    n = max(vertices) + 1
    return chinese_postman(n, edges)["total_distance"]


if __name__ == "__main__":
    # Example 1: Eulerian graph (all even degrees)
    print("=== Example 1: Eulerian Graph ===")
    edges1 = [
        (0, 1, 3),
        (1, 2, 4),
        (2, 3, 5),
        (3, 0, 6),
    ]
    result1 = chinese_postman(4, edges1)
    print(f"Total weight of edges: {sum(w for _, _, w in edges1)}")
    print(f"Postman route length: {result1['total_distance']}")
    print(f"Is Eulerian: {result1['is_eulerian']}")

    # Example 2: Non-Eulerian graph
    print("\n=== Example 2: Non-Eulerian Graph ===")
    # Graph: triangle with a tail (vertices 0,1 form odd degree)
    edges2 = [
        (0, 1, 1),
        (1, 2, 2),
        (2, 0, 3),  # Triangle
        (0, 3, 4),  # Tail
    ]
    result2 = chinese_postman(4, edges2)
    print(f"Total edge weight: {sum(w for _, _, w in edges2)}")
    print(f"Postman route length: {result2['total_distance']}")
    print(f"Odd vertices: {result2['odd_vertices']}")
    print(f"Extra distance needed: {result2['extra_distance']}")

    # Example 3: Simple function
    print("\n=== Example 3: Simple Function ===")
    result3 = solve_chinese_postman_simple(edges2)
    print(f"Minimum route: {result3}")

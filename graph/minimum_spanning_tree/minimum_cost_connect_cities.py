"""
Minimum Cost to Connect All Cities

This problem asks to find the minimum cost to connect all n cities (labeled 1 to n)
given a list of connections where each connection [xi, yi, costi] represents a
bidirectional road between city xi and city yi with repair cost costi.

If it's impossible to connect all cities, return -1.

This is a classic Minimum Spanning Tree problem that can be solved using either
Kruskal's or Prim's algorithm. Here we implement the Kruskal's approach using
Union-Find for efficient cycle detection.

Algorithm:
1. Sort all connections by cost in ascending order.
2. Use Union-Find to track connected components.
3. Iterate through sorted connections and union cities if they are in different
   components, accumulating the cost.
4. Track the number of connected components; if > 1 after processing, return -1.

Time Complexity: O(E log E) for sorting edges
Space Complexity: O(V) for Union-Find structure
"""

from typing import List


class UnionFind:
    """Union-Find data structure for efficient connectivity queries."""

    def __init__(self, n: int) -> None:
        """
        Initialize Union-Find with n elements.

        Args:
            n: Number of elements.
        """
        self.parent: List[int] = list(range(n + 1))  # 1-based indexing
        self.rank: List[int] = [0] * (n + 1)
        self.components = n  # Number of connected components

    def find(self, x: int) -> int:
        """
        Find the root of the set containing x with path compression.

        Args:
            x: Element to find.

        Returns:
            Root of the set containing x.
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        """
        Union the sets containing x and y.

        Args:
            x: First element.
            y: Second element.

        Returns:
            True if union was performed, False if already in the same set.
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        self.components -= 1
        return True


def minimum_cost_connect_cities(n: int, connections: List[List[int]]) -> int:
    """
    Find the minimum cost to connect all cities.

    Args:
        n: Number of cities (labeled 1 to n).
        connections: List of [city1, city2, cost] representing bidirectional connections.

    Returns:
        Minimum cost to connect all cities, or -1 if impossible.
    """
    # Sort connections by cost
    connections.sort(key=lambda x: x[2])

    uf = UnionFind(n)
    total_cost = 0

    for city1, city2, cost in connections:
        if uf.union(city1, city2):
            total_cost += cost
            if uf.components == 1:
                return total_cost

    return -1 if uf.components > 1 else total_cost


def minimum_cost_connect_cities_prim(n: int, connections: List[List[int]]) -> int:
    """
    Find the minimum cost to connect all cities using Prim's algorithm.

    Args:
        n: Number of cities (labeled 1 to n).
        connections: List of [city1, city2, cost] representing bidirectional connections.

    Returns:
        Minimum cost to connect all cities, or -1 if impossible.
    """
    import heapq

    # Build adjacency list (1-based indexing)
    adj: List[List[tuple]] = [[] for _ in range(n + 1)]
    for u, v, w in connections:
        adj[u].append((w, v))
        adj[v].append((w, u))

    # Prim's algorithm
    in_mst: List[bool] = [False] * (n + 1)
    pq = [(0, 1)]  # (cost, city), start from city 1
    mst_cost = 0
    cities_connected = 0

    while pq:
        cost, u = heapq.heappop(pq)

        if in_mst[u]:
            continue

        in_mst[u] = True
        mst_cost += cost
        cities_connected += 1

        for weight, v in adj[u]:
            if not in_mst[v]:
                heapq.heappush(pq, (weight, v))

    return mst_cost if cities_connected == n else -1


if __name__ == "__main__":
    # Example 1: All cities can be connected
    print("=" * 50)
    print("Minimum Cost to Connect All Cities - Example 1")
    print("=" * 50)
    n = 3
    connections = [[1, 2, 5], [1, 3, 6], [2, 3, 1]]
    result = minimum_cost_connect_cities(n, connections)
    print(f"Number of cities: {n}")
    print(f"Connections: {connections}")
    print(f"Minimum cost: {result}")  # Expected: 6

    # Example 2: Cities cannot all be connected
    print("\n" + "=" * 50)
    print("Minimum Cost to Connect All Cities - Example 2")
    print("=" * 50)
    n = 4
    connections = [[1, 2, 3], [3, 4, 4]]
    result = minimum_cost_connect_cities(n, connections)
    print(f"Number of cities: {n}")
    print(f"Connections: {connections}")
    print(f"Minimum cost: {result}")  # Expected: -1

    # Example 3: Larger graph using Prim's approach
    print("\n" + "=" * 50)
    print("Minimum Cost to Connect All Cities - Example 3 (Prim's)")
    print("=" * 50)
    n = 5
    connections = [
        [1, 2, 1],
        [1, 3, 2],
        [1, 4, 3],
        [1, 5, 4],
        [2, 3, 5],
        [2, 5, 7],
        [3, 4, 6],
    ]
    result = minimum_cost_connect_cities_prim(n, connections)
    print(f"Number of cities: {n}")
    print(f"Minimum cost: {result}")  # Expected: 10

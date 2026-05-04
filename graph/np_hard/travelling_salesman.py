"""
Travelling Salesman Problem (TSP) Implementation

Given a 2D matrix cost[n][n] where cost[i][j] denotes the cost of moving
from city i to city j, find the minimum cost to complete a tour from city 0
to all other cities, visiting each city exactly once, and returning to city 0.

This implementation uses Dynamic Programming with bitmask representation for
optimal substructure, achieving O(n^2 * 2^n) time complexity.

Reference: https://www.geeksforgeeks.org/travelling-salesman-problem-using-dynamic-programming/
"""

from typing import List, Optional
import sys


def tsp_dp(cost: List[List[int]]) -> int:
    """
    Solve TSP using Dynamic Programming with bitmask.

    Args:
        cost: A square matrix where cost[i][j] is the cost from city i to j.

    Returns:
        Minimum cost to visit all cities exactly once and return to start.

    Time Complexity: O(n^2 * 2^n)
    Space Complexity: O(n * 2^n)
    """
    n = len(cost)
    if n <= 1:
        return cost[0][0] if n == 1 else 0

    INF = sys.maxsize
    FULL = 1 << n
    full_mask = FULL - 1

    # dp[mask][i] = minimum cost to visit all cities in mask, ending at city i
    dp = [[INF] * n for _ in range(FULL)]
    dp[1][0] = 0  # Start at city 0, only city 0 visited

    # Iterate over all subsets of cities
    for mask in range(1, FULL):
        for i in range(n):
            # Skip if city i is not in mask or state not reachable
            if not (mask & (1 << i)) or dp[mask][i] == INF:
                continue

            # Try to go to every unvisited city j
            for j in range(n):
                if mask & (1 << j):  # Skip if already visited
                    continue

                nxt_mask = mask | (1 << j)
                dp[nxt_mask][j] = min(dp[nxt_mask][j], dp[mask][i] + cost[i][j])

    # Find minimum cost to return to city 0 from any city after visiting all
    ans = INF
    for i in range(n):
        if dp[full_mask][i] != INF:
            ans = min(ans, dp[full_mask][i] + cost[i][0])

    return ans


def tsp_bruteforce(cost: List[List[int]]) -> int:
    """
    Solve TSP using brute force (exploring all permutations).

    Args:
        cost: A square matrix where cost[i][j] is the cost from city i to j.

    Returns:
        Minimum cost to visit all cities exactly once and return to start.

    Time Complexity: O(n!)
    Space Complexity: O(n)
    """
    from itertools import permutations

    n = len(cost)
    if n <= 1:
        return cost[0][0] if n == 1 else 0

    cities = list(range(1, n))  # All cities except starting city 0
    min_cost = float("inf")

    for perm in permutations(cities):
        cost_sum = 0
        current = 0  # Start at city 0

        for city in perm:
            cost_sum += cost[current][city]
            current = city

        # Return to starting city
        cost_sum += cost[current][0]
        min_cost = min(min_cost, cost_sum)

    return min_cost


class TSP:
    """
    A class-based implementation of the Travelling Salesman Problem.

    Attributes:
        cost: The cost matrix between cities.
        n: Number of cities.
    """

    def __init__(self, cost_matrix: List[List[int]]) -> None:
        """
        Initialize TSP with a cost matrix.

        Args:
            cost_matrix: Square matrix of costs between cities.
        """
        self.cost = cost_matrix
        self.n = len(cost_matrix)

    def solve(self) -> int:
        """Solve TSP using DP approach."""
        return tsp_dp(self.cost)

    def get_optimal_path(self) -> tuple[int, List[int]]:
        """
        Get the optimal path and its cost using DP.

        Returns:
            Tuple of (minimum_cost, optimal_path)
        """
        n = self.n
        if n <= 1:
            return (self.cost[0][0] if n == 1 else 0, [0] if n == 1 else [])

        INF = sys.maxsize
        FULL = 1 << n
        full_mask = FULL - 1

        dp = [[INF] * n for _ in range(FULL)]
        parent = [[-1] * n for _ in range(FULL)]
        dp[1][0] = 0

        for mask in range(1, FULL):
            for i in range(n):
                if not (mask & (1 << i)) or dp[mask][i] == INF:
                    continue

                for j in range(n):
                    if mask & (1 << j):
                        continue

                    nxt_mask = mask | (1 << j)
                    if dp[nxt_mask][j] > dp[mask][i] + self.cost[i][j]:
                        dp[nxt_mask][j] = dp[mask][i] + self.cost[i][j]
                        parent[nxt_mask][j] = i

        # Find optimal ending city
        min_cost = INF
        end_city = -1
        for i in range(n):
            if dp[full_mask][i] != INF:
                total = dp[full_mask][i] + self.cost[i][0]
                if total < min_cost:
                    min_cost = total
                    end_city = i

        # Reconstruct path
        path = []
        mask = full_mask
        curr = end_city
        while curr != -1:
            path.append(curr)
            prev = parent[mask][curr]
            mask = mask ^ (1 << curr)
            curr = prev

        path.reverse()
        return (min_cost, [0] + path + [0])


if __name__ == "__main__":
    # Example 1: Simple 2-city tour
    print("Example 1: 2 Cities")
    cost1 = [[0, 111], [112, 0]]
    print(f"Cost matrix: {cost1}")
    print(f"Minimum TSP cost: {tsp_dp(cost1)}")
    print()

    # Example 2: Classic 4-city tour
    print("Example 2: 4 Cities")
    cost2 = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
    print(f"Cost matrix: {cost2}")

    tsp_solver = TSP(cost2)
    min_cost, path = tsp_solver.get_optimal_path()
    print(f"Minimum TSP cost: {min_cost}")
    print(f"Optimal path: {' -> '.join(map(str, path))}")
    print()

    # Verify with brute force
    print(f"Brute force verification: {tsp_bruteforce(cost2)}")

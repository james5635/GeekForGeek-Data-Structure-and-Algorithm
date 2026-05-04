"""
K Centers Problem - Greedy Approximate Algorithm

Given n cities and distances between every pair of cities, select k cities
to place facilities (like warehouses, ATMs, or cloud servers) such that the
maximum distance of any city to its nearest facility is minimized.

This is an NP-Hard problem. The greedy algorithm provides a 2-approximate
solution when distances satisfy the triangle inequality.

Greedy Algorithm (2-Approximate):
1. Choose the first center arbitrarily (city 0)
2. For each remaining center to select:
   - Pick the city that is farthest from all already selected centers
   - The distance is measured as min distance to any selected center

Reference: https://www.geeksforgeeks.org/k-centers-problem-set-1-greedy-approximate-algorithm/
"""

from typing import List, Tuple
import sys


def k_centers_greedy(dist: List[List[int]], k: int) -> Tuple[int, List[int]]:
    """
    Find k centers using greedy approximation algorithm.

    Args:
        dist: Distance matrix where dist[i][j] is distance between city i and j.
        k: Number of centers to select.

    Returns:
        Tuple of (max_distance, list_of_selected_centers).

    Time Complexity: O(n * k)
    Space Complexity: O(n)
    """
    n = len(dist)

    # Distance of each city to its nearest center
    nearest_dist = [sys.maxsize] * n

    # List of selected centers
    centers = []

    # Start with center 0 (can be chosen arbitrarily)
    max_idx = 0

    for _ in range(k):
        # Add the current farthest city as a center
        centers.append(max_idx)

        # Update distances to nearest centers
        for j in range(n):
            nearest_dist[j] = min(nearest_dist[j], dist[max_idx][j])

        # Find the city farthest from all selected centers
        max_idx = 0
        for j in range(n):
            if nearest_dist[j] > nearest_dist[max_idx]:
                max_idx = j

    return (nearest_dist[max_idx], centers)


def k_centers_with_assignment(
    dist: List[List[int]], k: int
) -> Tuple[int, List[int], List[int]]:
    """
    Find k centers and show which city is served by which center.

    Args:
        dist: Distance matrix.
        k: Number of centers to select.

    Returns:
        Tuple of (max_distance, centers, assignments) where assignments[i] is
        the center serving city i.
    """
    n = len(dist)
    nearest_dist = [sys.maxsize] * n
    assigned_center = [-1] * n
    centers = []

    max_idx = 0

    for _ in range(k):
        centers.append(max_idx)

        for j in range(n):
            if dist[max_idx][j] < nearest_dist[j]:
                nearest_dist[j] = dist[max_idx][j]
                assigned_center[j] = max_idx

        max_idx = 0
        for j in range(n):
            if nearest_dist[j] > nearest_dist[max_idx]:
                max_idx = j

    return (nearest_dist[max_idx], centers, assigned_center)


class KCenters:
    """
    A class-based implementation for K Centers problem.

    Attributes:
        n: Number of cities.
        dist: Distance matrix between cities.
    """

    def __init__(self, distance_matrix: List[List[int]]) -> None:
        """
        Initialize K Centers solver.

        Args:
            distance_matrix: Square matrix of distances between cities.
        """
        self.n = len(distance_matrix)
        self.dist = distance_matrix

    def solve(self, k: int) -> Tuple[int, List[int]]:
        """
        Solve K Centers problem using greedy algorithm.

        Args:
            k: Number of centers to select.

        Returns:
            Tuple of (max_distance, centers).
        """
        return k_centers_greedy(self.dist, k)

    def solve_with_details(self, k: int) -> dict:
        """
        Solve with additional details about assignments.

        Returns:
            Dictionary with max_distance, centers, and assignments.
        """
        max_dist, centers, assignments = k_centers_with_assignment(self.dist, k)

        # Group cities by their assigned center
        service_map = {c: [] for c in centers}
        for city, center in enumerate(assignments):
            if city not in centers:
                service_map[center].append(city)

        return {
            "max_distance": max_dist,
            "centers": centers,
            "assignments": assignments,
            "service_map": service_map,
        }


if __name__ == "__main__":
    # Example from GeeksforGeeks
    print("K Centers Problem - Greedy Approximate Algorithm")
    print("=" * 55)

    # Distance matrix for 4 cities
    dist = [[0, 4, 8, 5], [4, 0, 10, 7], [8, 10, 0, 9], [5, 7, 9, 0]]
    k = 2

    print(f"Number of cities: {len(dist)}")
    print(f"Number of centers (k): {k}")
    print(f"Distance matrix:")
    for row in dist:
        print(f"  {row}")
    print()

    # Solve using function
    max_dist, centers = k_centers_greedy(dist, k)
    print(f"Selected centers: {centers}")
    print(f"Maximum distance to nearest center: {max_dist}")
    print()

    # Solve using class with details
    kc = KCenters(dist)
    result = kc.solve_with_details(k)

    print("Detailed Solution:")
    print(f"  Centers: {result['centers']}")
    print(f"  Max distance: {result['max_distance']}")
    print(f"  Assignments: {result['assignments']}")
    print("  Service map:")
    for center, cities in result["service_map"].items():
        print(f"    Center {center} serves: {cities}")
    print()

    # Another example with k=3
    print("Example with k=3:")
    print("-" * 30)
    max_dist3, centers3 = k_centers_greedy(dist, 3)
    print(f"Selected centers: {centers3}")
    print(f"Maximum distance: {max_dist3}")
    print()

    # Larger example
    print("Larger Example (5 cities):")
    print("-" * 30)
    dist2 = [
        [0, 2, 9, 10, 7],
        [2, 0, 6, 4, 5],
        [9, 6, 0, 8, 3],
        [10, 4, 8, 0, 6],
        [7, 5, 3, 6, 0],
    ]
    kc2 = KCenters(dist2)
    result2 = kc2.solve_with_details(2)
    print(f"Centers: {result2['centers']}")
    print(f"Max distance: {result2['max_distance']}")
    print(f"Service map: {result2['service_map']}")

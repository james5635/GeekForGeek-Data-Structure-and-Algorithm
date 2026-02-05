"""
Closest Pair of Points using Divide and Conquer

Problem Description:
Given an array of n points in the 2D plane, find the pair of points
that are closest to each other (minimum Euclidean distance).

Examples:
- Input: points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
  Output: 1.41421 (distance between (2, 3) and (3, 4))

Approach 1: Brute Force - O(n^2)
Approach 2: Divide and Conquer - O(n log n)
Approach 3: Plane Sweep - O(n log n)

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

import math


def euclidean_distance(p1, p2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def euclidean_distance_squared(p1, p2):
    """Calculate squared Euclidean distance."""
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2


def closest_pair_brute_force(points):
    """Find closest pair using brute force. O(n^2)"""
    n = len(points)
    if n < 2:
        return float("inf"), None, None

    min_dist = float("inf")
    closest = None

    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean_distance(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
                closest = (points[i], points[j])

    return min_dist, closest[0], closest[1]


def closest_pair_divide_conquer(points):
    """Find closest pair using divide and conquer. O(n log n)"""
    n = len(points)
    if n < 2:
        return float("inf"), None, None
    if n <= 3:
        return closest_pair_brute_force(points)

    px = sorted(points, key=lambda p: p[0])
    py = sorted(points, key=lambda p: p[1])
    return _closest_recursive(px, py)


def _closest_recursive(px, py):
    """Recursive helper for divide and conquer."""
    n = len(px)
    if n <= 3:
        return closest_pair_brute_force(px)

    mid = n // 2
    mid_point = px[mid]

    pyl = [p for p in py if p[0] <= mid_point[0]]
    pyr = [p for p in py if p[0] > mid_point[0]]

    dl, pl1, pl2 = _closest_recursive(px[:mid], pyl)
    dr, pr1, pr2 = _closest_recursive(px[mid:], pyr)

    d = min(dl, dr)
    best_pair = (pl1, pl2) if dl <= dr else (pr1, pr2)

    strip = [p for p in py if abs(p[0] - mid_point[0]) < d]
    strip_d, sp1, sp2 = _closest_in_strip(strip, d)

    if strip_d < d:
        return strip_d, sp1, sp2
    return d, best_pair[0], best_pair[1]


def _closest_in_strip(strip, d):
    """Find closest pair in strip of width 2d."""
    min_dist = d
    closest = None
    n = len(strip)

    for i in range(n):
        for j in range(i + 1, min(i + 8, n)):
            dist = euclidean_distance(strip[i], strip[j])
            if dist < min_dist:
                min_dist = dist
                closest = (strip[i], strip[j])

    if closest:
        return min_dist, closest[0], closest[1]
    return min_dist, None, None


def closest_pair_plane_sweep(points):
    """Find closest pair using plane sweep. O(n log n)"""
    n = len(points)
    if n < 2:
        return float("inf"), None, None

    px = sorted(points, key=lambda p: p[0])
    active = set()
    min_dist = float("inf")
    closest = None
    left = 0

    for i, p in enumerate(px):
        while px[left][0] < p[0] - min_dist:
            active.discard(px[left])
            left += 1

        for q in list(active):
            if abs(q[1] - p[1]) < min_dist:
                dist = euclidean_distance(p, q)
                if dist < min_dist:
                    min_dist = dist
                    closest = (p, q)

        active.add(p)

    return min_dist, closest[0], closest[1] if closest else (None, None)


def run_tests():
    """Test cases for closest pair of points."""
    test_cases = [
        {
            "points": [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)],
            "expected_dist": 1.4142135623730951,
            "description": "Standard case",
        },
        {
            "points": [(0, 0), (1, 1)],
            "expected_dist": 1.4142135623730951,
            "description": "Two points",
        },
        {
            "points": [(0, 0), (3, 4), (5, 12)],
            "expected_dist": 5.0,
            "description": "Three points",
        },
        {
            "points": [(1, 1), (2, 2), (3, 3), (4, 4)],
            "expected_dist": 1.4142135623730951,
            "description": "Diagonal line",
        },
        {
            "points": [(0, 0)],
            "expected_dist": float("inf"),
            "description": "Single point",
        },
        {
            "points": [],
            "expected_dist": float("inf"),
            "description": "Empty array",
        },
        {
            "points": [(0, 0), (0, 1), (1, 0), (1, 1)],
            "expected_dist": 1.0,
            "description": "Unit square corners",
        },
    ]

    print("Running Closest Pair of Points Tests:")
    print("=" * 60)

    methods = [
        ("Brute Force", closest_pair_brute_force),
        ("Divide & Conquer", closest_pair_divide_conquer),
        ("Plane Sweep", closest_pair_plane_sweep),
    ]

    for method_name, method in methods:
        print(f"\n--- Testing {method_name} ---")
        for i, test in enumerate(test_cases, 1):
            dist, p1, p2 = method(test["points"])
            expected = test["expected_dist"]
            passed = (
                abs(dist - expected) < 1e-9
                if dist != float("inf")
                else dist == expected
            )

            status = "PASS" if passed else "FAIL"
            print(f"\nTest {i}: {status}")
            print(f"Description: {test['description']}")
            print(f"Points: {test['points']}")
            print(f"Expected distance: {expected}")
            print(f"Got distance: {dist}")
            if p1 and p2:
                print(f"Closest pair: {p1}, {p2}")

    print("\n" + "=" * 60)
    print("Tests completed!")
    return True


if __name__ == "__main__":
    run_tests()

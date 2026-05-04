"""Number of integral points between two points."""

import math


def integral_points_two_points(p1: tuple[int, int], p2: tuple[int, int]) -> int:
    """Count integral points on the line segment between two points (exclusive).

    Args:
        p1: First point as (x, y).
        p2: Second point as (x, y).

    Returns:
        Number of integral points strictly between the two points.
    """
    return math.gcd(abs(p2[0] - p1[0]), abs(p2[1] - p1[1])) - 1


if __name__ == "__main__":
    print(f"Integral points: {integral_points_two_points((1, 1), (5, 5))}")
    print(f"Integral points: {integral_points_two_points((0, 0), (6, 9))}")

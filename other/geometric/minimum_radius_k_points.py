"""Find minimum radius such that at least k points lie inside the circle."""

import math


def minimum_radius_k_points(points: list[tuple[float, float]], k: int) -> float:
    """Find minimum radius centered at origin such that at least k points lie inside.

    Args:
        points: List of (x, y) coordinate tuples.
        k: Minimum number of points to enclose.

    Returns:
        Minimum required radius.
    """
    if k > len(points):
        return -1

    distances = [math.sqrt(x * x + y * y) for x, y in points]
    distances.sort()
    return round(distances[k - 1], 4)


if __name__ == "__main__":
    points = [(1, 0), (2, 0), (3, 0), (0, 4), (5, 0)]
    print(f"Min radius for k=3: {minimum_radius_k_points(points, 3)}")

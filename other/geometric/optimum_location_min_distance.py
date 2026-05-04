"""Optimum location of point to minimize total distance."""


def median_value(coords: list[float]) -> float:
    coords.sort()
    n = len(coords)
    if n % 2 == 1:
        return coords[n // 2]
    return (coords[n // 2 - 1] + coords[n // 2]) / 2


def optimum_location_min_distance(
    points: list[tuple[float, float]],
) -> tuple[float, float]:
    """Find the optimum location that minimizes total Manhattan distance to all points.

    Args:
        points: List of (x, y) coordinate tuples.

    Returns:
        Optimal (x, y) location.
    """
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    return (median_value(xs), median_value(ys))


if __name__ == "__main__":
    points = [(1, 2), (3, 4), (5, 6)]
    optimal = optimum_location_min_distance(points)
    print(f"Optimal location: {optimal}")

"""Find simple closed path for a given set of points."""


def simple_closed_path(points: list[tuple[float, float]]) -> list[tuple[float, float]]:
    """Find a simple closed path (non-intersecting polygon) through given points.

    Uses Graham scan-like sorting by polar angle.

    Args:
        points: List of (x, y) coordinate tuples.

    Returns:
        List of points forming a simple closed path.
    """
    import math

    n = len(points)
    if n < 3:
        return points

    def dist_sq(p1: tuple[float, float], p2: tuple[float, float]) -> float:
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

    def cross(
        o: tuple[float, float], a: tuple[float, float], b: tuple[float, float]
    ) -> float:
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    start = min(range(n), key=lambda i: (points[i][1], points[i][0]))
    p0 = points[start]

    def polar_key(p: tuple[float, float]) -> tuple[float, float]:
        angle = math.atan2(p[1] - p0[1], p[0] - p0[0])
        return (angle, dist_sq(p0, p))

    sorted_points = sorted(points, key=polar_key)
    return sorted_points


if __name__ == "__main__":
    points = [(0, 0), (4, 0), (2, 2), (4, 4), (0, 4)]
    path = simple_closed_path(points)
    print(f"Simple closed path: {path}")

"""Convex Hull using Jarvis algorithm (Gift Wrapping)."""


def convex_hull_jarvis(points: list[tuple[float, float]]) -> list[tuple[float, float]]:
    """Compute convex hull using Jarvis March (Gift Wrapping) algorithm.

    Args:
        points: List of (x, y) coordinate tuples.

    Returns:
        List of vertices on the convex hull in counter-clockwise order.
    """
    n = len(points)
    if n < 3:
        return points

    def orientation(
        p: tuple[float, float], q: tuple[float, float], r: tuple[float, float]
    ) -> int:
        val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
        if val == 0:
            return 0
        return 1 if val > 0 else 2

    hull = []

    leftmost = min(range(n), key=lambda i: points[i][0])
    p = leftmost

    while True:
        hull.append(points[p])
        q = (p + 1) % n

        for i in range(n):
            if orientation(points[p], points[i], points[q]) == 2:
                q = i

        p = q
        if p == leftmost:
            break

    return hull


if __name__ == "__main__":
    points = [(0, 0), (4, 0), (2, 2), (4, 4), (0, 4), (2, 1)]
    hull = convex_hull_jarvis(points)
    print(f"Convex hull: {hull}")

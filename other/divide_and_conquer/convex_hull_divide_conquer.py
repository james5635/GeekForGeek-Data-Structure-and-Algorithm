def convex_hull(points: list[tuple[float, float]]) -> list[tuple[float, float]]:
    """
    Find the convex hull of a set of points using divide and conquer.

    Args:
        points: List of (x, y) tuples

    Returns:
        List of points on the convex hull in counter-clockwise order
    """
    if len(points) <= 3:
        return _simple_hull(points)

    points.sort()

    mid = len(points) // 2
    left_hull = convex_hull(points[:mid])
    right_hull = convex_hull(points[mid:])

    return _merge_hulls(left_hull, right_hull)


def _simple_hull(points: list[tuple[float, float]]) -> list[tuple[float, float]]:
    if len(points) <= 1:
        return points[:]

    def _cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    points_sorted = sorted(points)
    lower = []
    for p in points_sorted:
        while len(lower) >= 2 and _cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(points_sorted):
        while len(upper) >= 2 and _cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]


def _merge_hulls(
    left: list[tuple[float, float]], right: list[tuple[float, float]]
) -> list[tuple[float, float]]:
    def _cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    combined = left + right
    return _simple_hull(combined)


if __name__ == "__main__":
    points = [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)]
    hull = convex_hull(points)
    print(hull)

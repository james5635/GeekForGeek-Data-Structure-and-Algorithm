def quickhull(points: list[tuple[float, float]]) -> list[tuple[float, float]]:
    """
    Find the convex hull of a set of points using the QuickHull algorithm.

    Args:
        points: List of (x, y) tuples

    Returns:
        List of points on the convex hull
    """
    if len(points) <= 2:
        return points

    min_x = min(points, key=lambda p: p[0])
    max_x = max(points, key=lambda p: p[0])

    upper = _find_hull(points, min_x, max_x)
    lower = _find_hull(points, max_x, min_x)

    result = upper + lower
    seen = set()
    unique = []
    for p in result:
        if p not in seen:
            seen.add(p)
            unique.append(p)
    return unique


def _find_hull(
    points: list[tuple[float, float]],
    p1: tuple[float, float],
    p2: tuple[float, float],
) -> list[tuple[float, float]]:
    if not points:
        return []

    def _cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    def _distance(o, a, b):
        return abs((a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0]))

    farthest = max(points, key=lambda p: _distance(p1, p2, p))

    set1 = [p for p in points if _cross(p1, farthest, p) > 0]
    set2 = [p for p in points if _cross(farthest, p2, p) > 0]

    return _find_hull(set1, p1, farthest) + [farthest] + _find_hull(set2, farthest, p2)


if __name__ == "__main__":
    points = [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)]
    hull = quickhull(points)
    print(hull)

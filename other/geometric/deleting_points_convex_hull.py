"""Deleting points from convex hull."""

from convex_hull_jarvis import convex_hull_jarvis


def deleting_points_convex_hull(
    points: list[tuple[float, float]], to_delete: list[tuple[float, float]]
) -> list[tuple[float, float]]:
    """Delete points from a set and recompute the convex hull.

    Args:
        points: Original set of (x, y) coordinate tuples.
        to_delete: Points to remove from the set.

    Returns:
        Convex hull of remaining points.
    """
    remaining = [p for p in points if p not in to_delete]
    return convex_hull_jarvis(remaining)


if __name__ == "__main__":
    points = [(0, 0), (4, 0), (2, 2), (4, 4), (0, 4), (2, 1)]
    to_delete = [(0, 0), (0, 4)]
    hull = deleting_points_convex_hull(points, to_delete)
    print(f"Original hull: {convex_hull_jarvis(points)}")
    print(f"New hull: {hull}")

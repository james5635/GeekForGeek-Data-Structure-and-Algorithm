"""Given a set of line segments, find if any two segments intersect."""

from typing import List


class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y


def orientation(p: Point, q: Point, r: Point) -> int:
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    if val == 0:
        return 0
    return 1 if val > 0 else 2


def on_segment(p: Point, q: Point, r: Point) -> bool:
    return (
        q.x <= max(p.x, r.x)
        and q.x >= min(p.x, r.x)
        and q.y <= max(p.y, r.y)
        and q.y >= min(p.y, r.y)
    )


def segments_intersect(p1: Point, q1: Point, p2: Point, q2: Point) -> bool:
    """Check if line segment p1q1 intersects segment p2q2.

    Args:
        p1, q1: Endpoints of first segment.
        p2, q2: Endpoints of second segment.

    Returns:
        True if segments intersect, False otherwise.
    """
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    if o1 != o2 and o3 != o4:
        return True

    if o1 == 0 and on_segment(p1, p2, q1):
        return True
    if o2 == 0 and on_segment(p1, q2, q1):
        return True
    if o3 == 0 and on_segment(p2, p1, q2):
        return True
    if o4 == 0 and on_segment(p2, q1, q2):
        return True

    return False


def check_any_intersection(segments: list[tuple[Point, Point]]) -> bool:
    """Check if any two segments in the set intersect.

    Args:
        segments: List of tuples, each containing two Point objects.

    Returns:
        True if any two segments intersect, False otherwise.
    """
    n = len(segments)
    for i in range(n):
        for j in range(i + 1, n):
            if segments_intersect(
                segments[i][0], segments[i][1], segments[j][0], segments[j][1]
            ):
                return True
    return False


if __name__ == "__main__":
    s1 = (Point(1, 1), Point(4, 4))
    s2 = (Point(1, 4), Point(4, 1))
    print(f"Segments intersect: {segments_intersect(s1[0], s1[1], s2[0], s2[1])}")

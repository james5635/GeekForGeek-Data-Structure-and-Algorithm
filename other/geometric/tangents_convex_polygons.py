"""Tangents to two convex polygons."""

import math


class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y


def cross_product(o: Point, a: Point, b: Point) -> float:
    return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x)


def tangents_convex_polygons(
    poly1: list[Point], poly2: list[Point]
) -> tuple[tuple[Point, Point], tuple[Point, Point]]:
    """Find the upper and lower tangents between two convex polygons.

    Args:
        poly1: First convex polygon as list of Points.
        poly2: Second convex polygon as list of Points.

    Returns:
        Tuple of ((upper_tangent_p1, upper_tangent_p2), (lower_tangent_p1, lower_tangent_p2)).
    """
    n1 = len(poly1)
    n2 = len(poly2)

    rightmost1 = max(range(n1), key=lambda i: poly1[i].x)
    leftmost2 = min(range(n2), key=lambda i: poly2[i].x)

    upper1, upper2 = rightmost1, leftmost2
    done = False

    while not done:
        done = True
        while (
            cross_product(poly2[upper2], poly1[upper1], poly1[(upper1 + 1) % n1]) <= 0
        ):
            upper1 = (upper1 + 1) % n1

        while (
            cross_product(poly1[upper1], poly2[upper2], poly2[(upper2 - 1 + n2) % n2])
            >= 0
        ):
            upper2 = (upper2 - 1 + n2) % n2
            done = False

    lower1, lower2 = rightmost1, leftmost2
    done = False

    while not done:
        done = True
        while (
            cross_product(poly2[lower2], poly1[lower1], poly1[(lower1 - 1 + n1) % n1])
            >= 0
        ):
            lower1 = (lower1 - 1 + n1) % n1

        while (
            cross_product(poly1[lower1], poly2[lower2], poly2[(lower2 + 1) % n2]) <= 0
        ):
            lower2 = (lower2 + 1) % n2
            done = False

    return ((poly1[upper1], poly2[upper2]), (poly1[lower1], poly2[lower2]))


if __name__ == "__main__":
    p1 = [Point(0, 0), Point(2, 1), Point(1, 2)]
    p2 = [Point(4, 0), Point(6, 1), Point(5, 2)]
    upper, lower = tangents_convex_polygons(p1, p2)
    print(f"Upper tangent: ({upper[0].x},{upper[0].y}) to ({upper[1].x},{upper[1].y})")
    print(f"Lower tangent: ({lower[0].x},{lower[0].y}) to ({lower[1].x},{lower[1].y})")

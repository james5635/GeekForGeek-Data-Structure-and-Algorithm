"""Program to find area of triangle."""

import math


def area_triangle(
    x1: float, y1: float, x2: float, y2: float, x3: float, y3: float
) -> float:
    """Calculate the area of a triangle using the coordinate formula.

    Args:
        x1, y1, x2, y2, x3, y3: Coordinates of the three vertices.

    Returns:
        Area of the triangle.
    """
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)


def area_triangle_sides(a: float, b: float, c: float) -> float:
    """Calculate area of triangle using Heron's formula.

    Args:
        a, b, c: Lengths of the three sides.

    Returns:
        Area of the triangle.
    """
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


if __name__ == "__main__":
    print(f"Area using coordinates: {area_triangle(0, 0, 4, 0, 0, 4)}")
    print(f"Area using sides: {area_triangle_sides(3, 4, 5)}")

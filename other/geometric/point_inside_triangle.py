"""Check whether a given point lies inside a triangle or not."""


def point_inside_triangle(
    px: float,
    py: float,
    x1: float,
    y1: float,
    x2: float,
    y2: float,
    x3: float,
    y3: float,
) -> bool:
    """Check if a point lies inside a triangle using barycentric coordinates.

    Args:
        px, py: Point coordinates.
        x1, y1, x2, y2, x3, y3: Triangle vertex coordinates.

    Returns:
        True if point is inside or on edge of triangle, False otherwise.
    """
    d1 = (px - x2) * (y1 - y2) - (x1 - x2) * (py - y2)
    d2 = (px - x3) * (y2 - y3) - (x2 - x3) * (py - y3)
    d3 = (px - x1) * (y3 - y1) - (x3 - x1) * (py - y1)

    has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
    has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)

    return not (has_neg and has_pos)


if __name__ == "__main__":
    print(
        f"(2, 2) in triangle (0,0),(4,0),(0,4): {point_inside_triangle(2, 2, 0, 0, 4, 0, 0, 4)}"
    )
    print(
        f"(5, 5) in triangle (0,0),(4,0),(0,4): {point_inside_triangle(5, 5, 0, 0, 4, 0, 0, 4)}"
    )

"""Minimum area polygon with three points given."""


def area_of_triangle(
    x1: float, y1: float, x2: float, y2: float, x3: float, y3: float
) -> float:
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)


def minimum_area_polygon(
    p1: tuple[float, float], p2: tuple[float, float], p3: tuple[float, float]
) -> float:
    """Calculate the minimum area polygon (triangle) formed by three points.

    Args:
        p1, p2, p3: Three points as (x, y) tuples.

    Returns:
        Area of the triangle.
    """
    return round(area_of_triangle(p1[0], p1[1], p2[0], p2[1], p3[0], p3[1]), 4)


if __name__ == "__main__":
    print(f"Min area: {minimum_area_polygon((0, 0), (4, 0), (0, 4))}")

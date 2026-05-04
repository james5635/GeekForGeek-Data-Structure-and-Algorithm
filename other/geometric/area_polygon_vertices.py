"""Area of a polygon with given n ordered vertices."""


def area_polygon_vertices(vertices: list[tuple[float, float]]) -> float:
    """Calculate area of a polygon using the shoelace formula.

    Args:
        vertices: List of (x, y) coordinates in order.

    Returns:
        Area of the polygon.
    """
    n = len(vertices)
    area = 0.0

    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]

    return abs(area) / 2.0


if __name__ == "__main__":
    square = [(0, 0), (4, 0), (4, 4), (0, 4)]
    print(f"Area: {area_polygon_vertices(square)}")

    triangle = [(0, 0), (4, 0), (0, 4)]
    print(f"Area: {area_polygon_vertices(triangle)}")

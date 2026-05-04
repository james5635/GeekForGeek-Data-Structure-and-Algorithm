"""How to check if a given point lies inside a polygon."""


def point_inside_polygon(
    px: float, py: float, polygon: list[tuple[float, float]]
) -> bool:
    """Check if a point lies inside a polygon using ray casting algorithm.

    Args:
        px, py: Point coordinates.
        polygon: List of (x, y) vertices in order.

    Returns:
        True if point is inside polygon, False otherwise.
    """
    n = len(polygon)
    inside = False

    j = n - 1
    for i in range(n):
        xi, yi = polygon[i]
        xj, yj = polygon[j]

        if ((yi > py) != (yj > py)) and (px < (xj - xi) * (py - yi) / (yj - yi) + xi):
            inside = not inside

        j = i

    return inside


if __name__ == "__main__":
    poly = [(0, 0), (4, 0), (4, 4), (0, 4)]
    print(f"(2, 2) inside: {point_inside_polygon(2, 2, poly)}")
    print(f"(5, 5) inside: {point_inside_polygon(5, 5, poly)}")

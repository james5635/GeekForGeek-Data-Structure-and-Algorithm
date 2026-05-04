"""Program to calculate circumcenter of a triangle."""


def circumcenter_triangle(
    x1: float, y1: float, x2: float, y2: float, x3: float, y3: float
) -> tuple[float, float] | None:
    """Calculate the circumcenter of a triangle.

    Args:
        x1, y1, x2, y2, x3, y3: Coordinates of triangle vertices.

    Returns:
        Tuple of (x, y) circumcenter coordinates or None if collinear.
    """
    d = 2 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    if d == 0:
        return None

    ux = (
        (x1 * x1 + y1 * y1) * (y2 - y3)
        + (x2 * x2 + y2 * y2) * (y3 - y1)
        + (x3 * x3 + y3 * y3) * (y1 - y2)
    ) / d
    uy = (
        (x1 * x1 + y1 * y1) * (x3 - x2)
        + (x2 * x2 + y2 * y2) * (x1 - x3)
        + (x3 * x3 + y3 * y3) * (x2 - x1)
    ) / d
    return (round(ux, 2), round(uy, 2))


if __name__ == "__main__":
    print(f"Circumcenter: {circumcenter_triangle(0, 0, 4, 0, 0, 4)}")

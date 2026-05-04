"""Program to find slope of a line."""


def slope(x1: float, y1: float, x2: float, y2: float) -> float | str:
    """Calculate the slope of a line passing through two points.

    Args:
        x1: X-coordinate of first point.
        y1: Y-coordinate of first point.
        x2: X-coordinate of second point.
        y2: Y-coordinate of second point.

    Returns:
        Slope value or 'Infinity' for vertical lines.
    """
    if x2 - x1 == 0:
        return "Infinity"
    return (y2 - y1) / (x2 - x1)


if __name__ == "__main__":
    print(f"Slope of (1,2) and (5,6): {slope(1, 2, 5, 6)}")
    print(f"Slope of (1,2) and (1,6): {slope(1, 2, 1, 6)}")

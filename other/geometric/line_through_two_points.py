"""Program to find line passing through 2 points."""


def line_through_two_points(x1: float, y1: float, x2: float, y2: float) -> str:
    """Find the equation of a line passing through two points.

    Args:
        x1: X-coordinate of first point.
        y1: Y-coordinate of first point.
        x2: X-coordinate of second point.
        y2: Y-coordinate of second point.

    Returns:
        String representation of the line equation in form ax + by = c.
    """
    a = y1 - y2
    b = x2 - x1
    c = a * x1 + b * y1
    return f"{a}x + {b}y = {c}"


if __name__ == "__main__":
    print(f"Line through (1,2) and (5,6): {line_through_two_points(1, 2, 5, 6)}")

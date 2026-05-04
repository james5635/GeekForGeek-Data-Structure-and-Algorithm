"""Check if a line touches or intersects a circle."""

import math


def line_touches_circle(
    cx: float, cy: float, r: float, a: float, b: float, c: float
) -> str:
    """Check if a line ax + by + c = 0 touches or intersects a circle.

    Args:
        cx, cy: Center of the circle.
        r: Radius of the circle.
        a, b, c: Coefficients of the line equation.

    Returns:
        String describing the relationship.
    """
    dist = abs(a * cx + b * cy + c) / math.sqrt(a * a + b * b)

    if abs(dist - r) < 1e-10:
        return "Line touches the circle"
    elif dist < r:
        return "Line intersects the circle"
    else:
        return "Line is outside the circle"


if __name__ == "__main__":
    print(line_touches_circle(0, 0, 5, 1, 0, -3))
    print(line_touches_circle(0, 0, 5, 1, 0, -5))
    print(line_touches_circle(0, 0, 5, 1, 0, -10))

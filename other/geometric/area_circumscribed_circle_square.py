"""Area of circumscribed circle of a square."""

import math


def area_circumscribed_circle_square(side: float) -> float:
    """Calculate the area of the circumscribed circle of a square.

    Args:
        side: Side length of the square.

    Returns:
        Area of the circumscribed circle.
    """
    radius = side * math.sqrt(2) / 2
    return round(math.pi * radius * radius, 4)


if __name__ == "__main__":
    print(f"Circumscribed circle area: {area_circumscribed_circle_square(4)}")
    print(f"Circumscribed circle area: {area_circumscribed_circle_square(10)}")

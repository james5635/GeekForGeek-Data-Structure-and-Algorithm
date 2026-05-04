"""Check if two given circles touch or intersect."""

import math


def circles_touch_intersect(
    x1: float, y1: float, r1: float, x2: float, y2: float, r2: float
) -> str:
    """Check the relationship between two circles.

    Args:
        x1, y1: Center of first circle.
        r1: Radius of first circle.
        x2, y2: Center of second circle.
        r2: Radius of second circle.

    Returns:
        String describing the relationship.
    """
    dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    if dist > r1 + r2:
        return "Circles are separate"
    elif dist == r1 + r2:
        return "Circles touch externally"
    elif dist < r1 + r2 and dist > abs(r1 - r2):
        return "Circles intersect at two points"
    elif dist == abs(r1 - r2):
        return "Circles touch internally"
    else:
        return "One circle is inside the other"


if __name__ == "__main__":
    print(circles_touch_intersect(0, 0, 5, 10, 0, 5))
    print(circles_touch_intersect(0, 0, 5, 4, 0, 5))
    print(circles_touch_intersect(0, 0, 5, 20, 0, 5))

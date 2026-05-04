"""Program to find area of a circle."""

import math


def area_circle(radius: float) -> float:
    """Calculate the area of a circle.

    Args:
        radius: Radius of the circle.

    Returns:
        Area of the circle.
    """
    return round(math.pi * radius * radius, 4)


if __name__ == "__main__":
    print(f"Area (r=5): {area_circle(5)}")
    print(f"Area (r=10): {area_circle(10)}")

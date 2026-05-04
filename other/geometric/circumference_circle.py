"""Program to find circumference of a circle."""

import math


def circumference_circle(radius: float) -> float:
    """Calculate the circumference of a circle.

    Args:
        radius: Radius of the circle.

    Returns:
        Circumference of the circle.
    """
    return round(2 * math.pi * radius, 4)


if __name__ == "__main__":
    print(f"Circumference (r=5): {circumference_circle(5)}")
    print(f"Circumference (r=10): {circumference_circle(10)}")

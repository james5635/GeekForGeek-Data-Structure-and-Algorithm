"""Program to find third side of triangle using law of cosines."""

import math


def third_side_law_cosines(a: float, b: float, angle_c: float) -> float:
    """Find the third side of a triangle using the law of cosines.

    Args:
        a: Length of first side.
        b: Length of second side.
        angle_c: Angle between sides a and b in degrees.

    Returns:
        Length of the third side.
    """
    angle_rad = math.radians(angle_c)
    c_squared = a * a + b * b - 2 * a * b * math.cos(angle_rad)
    return round(math.sqrt(c_squared), 4)


if __name__ == "__main__":
    print(f"Third side: {third_side_law_cosines(3, 4, 90)}")
    print(f"Third side: {third_side_law_cosines(5, 7, 60)}")

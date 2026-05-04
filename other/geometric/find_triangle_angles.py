"""Find angles of a given triangle."""

import math


def find_triangle_angles(a: float, b: float, c: float) -> tuple[float, float, float]:
    """Find all three angles of a triangle given side lengths.

    Args:
        a, b, c: Lengths of the three sides.

    Returns:
        Tuple of angles in degrees opposite to sides a, b, c.
    """
    angle_a = math.degrees(math.acos((b * b + c * c - a * a) / (2 * b * c)))
    angle_b = math.degrees(math.acos((a * a + c * c - b * b) / (2 * a * c)))
    angle_c = 180 - angle_a - angle_b
    return (round(angle_a, 2), round(angle_b, 2), round(angle_c, 2))


if __name__ == "__main__":
    print(f"Angles of triangle (3,4,5): {find_triangle_angles(3, 4, 5)}")

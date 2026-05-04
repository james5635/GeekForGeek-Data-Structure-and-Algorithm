"""Check if right angles possible given area and hypotenuse."""

import math


def right_triangle_area_hypotenuse(
    area: float, hypotenuse: float
) -> list[tuple[float, float]]:
    """Find the two legs of a right triangle given area and hypotenuse.

    Args:
        area: Area of the right triangle.
        hypotenuse: Length of the hypotenuse.

    Returns:
        List of tuples with the two leg lengths, or empty list if not possible.
    """
    area4 = 4 * area
    disc = hypotenuse * hypotenuse - area4

    if disc < 0:
        return []

    sqrt_disc = math.sqrt(disc)
    a = math.sqrt((hypotenuse * hypotenuse + area4 + 2 * hypotenuse * sqrt_disc) / 4)
    b = math.sqrt((hypotenuse * hypotenuse + area4 - 2 * hypotenuse * sqrt_disc) / 4)

    if abs(disc) < 1e-10:
        return [(round(a, 2), round(a, 2))]

    return [(round(a, 2), round(b, 2))]


if __name__ == "__main__":
    print(f"Area=6, Hyp=5: {right_triangle_area_hypotenuse(6, 5)}")
    print(f"Area=10, Hyp=5: {right_triangle_area_hypotenuse(10, 5)}")

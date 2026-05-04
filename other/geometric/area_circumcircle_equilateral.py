"""Program to calculate area and circumcircle of equilateral triangle."""

import math


def area_circumcircle_equilateral(side: float) -> tuple[float, float, float]:
    """Calculate area, circumcircle radius, and circumcircle area of equilateral triangle.

    Args:
        side: Length of the side of the equilateral triangle.

    Returns:
        Tuple of (triangle_area, circumcircle_radius, circumcircle_area).
    """
    triangle_area = (math.sqrt(3) / 4) * side * side
    circumcircle_radius = side / math.sqrt(3)
    circumcircle_area = math.pi * circumcircle_radius * circumcircle_radius
    return (
        round(triangle_area, 4),
        round(circumcircle_radius, 4),
        round(circumcircle_area, 4),
    )


if __name__ == "__main__":
    side = 6
    area, radius, c_area = area_circumcircle_equilateral(side)
    print(f"Triangle area: {area}")
    print(f"Circumcircle radius: {radius}")
    print(f"Circumcircle area: {c_area}")

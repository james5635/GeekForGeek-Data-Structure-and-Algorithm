"""Equable shapes - shapes where area equals perimeter."""

import math


def equable_triangle(a: float, b: float, c: float) -> bool:
    """Check if a triangle is equable (area equals perimeter).

    Args:
        a, b, c: Side lengths of the triangle.

    Returns:
        True if area equals perimeter, False otherwise.
    """
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    perimeter = a + b + c
    return abs(area - perimeter) < 1e-10


def equable_rectangle(length: float, width: float) -> bool:
    """Check if a rectangle is equable (area equals perimeter).

    Args:
        length: Length of rectangle.
        width: Width of rectangle.

    Returns:
        True if area equals perimeter, False otherwise.
    """
    area = length * width
    perimeter = 2 * (length + width)
    return abs(area - perimeter) < 1e-10


def equable_circle(radius: float) -> bool:
    """Check if a circle is equable (area equals circumference).

    Args:
        radius: Radius of the circle.

    Returns:
        True if area equals circumference, False otherwise.
    """
    area = math.pi * radius * radius
    circumference = 2 * math.pi * radius
    return abs(area - circumference) < 1e-10


if __name__ == "__main__":
    print(f"Triangle (5, 12, 13) equable: {equable_triangle(5, 12, 13)}")
    print(f"Rectangle (4, 4) equable: {equable_rectangle(4, 4)}")
    print(f"Circle (2) equable: {equable_circle(2)}")

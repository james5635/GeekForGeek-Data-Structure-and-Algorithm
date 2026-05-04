"""Program to calculate area and perimeter of trapezium."""

import math


def area_perimeter_trapezium(
    a: float, b: float, c: float, d: float, h: float
) -> tuple[float, float]:
    """Calculate area and perimeter of a trapezium.

    Args:
        a: Length of first parallel side.
        b: Length of second parallel side.
        c: Length of first non-parallel side.
        d: Length of second non-parallel side.
        h: Height of the trapezium.

    Returns:
        Tuple of (area, perimeter).
    """
    area = 0.5 * (a + b) * h
    perimeter = a + b + c + d
    return (area, perimeter)


if __name__ == "__main__":
    area, perimeter = area_perimeter_trapezium(8, 12, 5, 5, 4)
    print(f"Area: {area}, Perimeter: {perimeter}")

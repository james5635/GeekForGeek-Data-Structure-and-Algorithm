"""Find perimeter of cylinder."""

import math


def perimeter_cylinder(radius: float, height: float) -> float:
    """Calculate the total surface perimeter of a cylinder.

    Args:
        radius: Radius of the cylinder base.
        height: Height of the cylinder.

    Returns:
        Total perimeter (sum of all edge lengths).
    """
    return round(2 * (2 * math.pi * radius + 2 * height), 4)


if __name__ == "__main__":
    print(f"Perimeter: {perimeter_cylinder(5, 10)}")
    print(f"Perimeter: {perimeter_cylinder(3, 7)}")

"""Program to calculate volume of ellipsoid."""

import math


def volume_ellipsoid(a: float, b: float, c: float) -> float:
    """Calculate the volume of an ellipsoid.

    Args:
        a, b, c: Semi-axes lengths.

    Returns:
        Volume of the ellipsoid.
    """
    return round((4 / 3) * math.pi * a * b * c, 4)


if __name__ == "__main__":
    print(f"Volume: {volume_ellipsoid(3, 4, 5)}")
    print(f"Volume: {volume_ellipsoid(2, 2, 2)}")

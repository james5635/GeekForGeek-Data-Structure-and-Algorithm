"""Calculate volume and surface area of sphere."""

import math


def volume_surface_area_sphere(radius: float) -> tuple[float, float]:
    """Calculate volume and surface area of a sphere.

    Args:
        radius: Radius of the sphere.

    Returns:
        Tuple of (volume, surface_area).
    """
    volume = (4 / 3) * math.pi * radius**3
    surface_area = 4 * math.pi * radius**2
    return (round(volume, 4), round(surface_area, 4))


if __name__ == "__main__":
    volume, area = volume_surface_area_sphere(5)
    print(f"Volume: {volume}, Surface Area: {area}")

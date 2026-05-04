"""Calculate volume and surface area of cone."""

import math


def volume_surface_area_cone(radius: float, height: float) -> tuple[float, float]:
    """Calculate volume and surface area of a cone.

    Args:
        radius: Radius of the base.
        height: Height of the cone.

    Returns:
        Tuple of (volume, surface_area).
    """
    slant = math.sqrt(radius * radius + height * height)
    volume = (1 / 3) * math.pi * radius * radius * height
    surface_area = math.pi * radius * (radius + slant)
    return (round(volume, 4), round(surface_area, 4))


if __name__ == "__main__":
    volume, area = volume_surface_area_cone(3, 4)
    print(f"Volume: {volume}, Surface Area: {area}")

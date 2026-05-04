"""Program for volume and surface area of frustum of cone."""

import math


def volume_surface_area_frustum(r1: float, r2: float, h: float) -> tuple[float, float]:
    """Calculate volume and surface area of a frustum of a cone.

    Args:
        r1: Radius of the larger base.
        r2: Radius of the smaller base.
        h: Height of the frustum.

    Returns:
        Tuple of (volume, surface_area).
    """
    slant = math.sqrt((r1 - r2) ** 2 + h**2)
    volume = (math.pi * h / 3) * (r1 * r1 + r2 * r2 + r1 * r2)
    surface_area = math.pi * (r1 + r2) * slant + math.pi * (r1 * r1 + r2 * r2)
    return (round(volume, 4), round(surface_area, 4))


if __name__ == "__main__":
    volume, area = volume_surface_area_frustum(5, 3, 8)
    print(f"Volume: {volume}, Surface Area: {area}")

"""Program for volume and surface area of cuboid."""


def volume_surface_area_cuboid(l: float, w: float, h: float) -> tuple[float, float]:
    """Calculate volume and surface area of a cuboid.

    Args:
        l: Length.
        w: Width.
        h: Height.

    Returns:
        Tuple of (volume, surface_area).
    """
    volume = l * w * h
    surface_area = 2 * (l * w + w * h + h * l)
    return (volume, surface_area)


if __name__ == "__main__":
    volume, area = volume_surface_area_cuboid(3, 4, 5)
    print(f"Volume: {volume}, Surface Area: {area}")

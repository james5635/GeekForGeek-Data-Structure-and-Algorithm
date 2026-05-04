"""Program for volume and surface area of cube."""


def volume_surface_area_cube(side: float) -> tuple[float, float]:
    """Calculate volume and surface area of a cube.

    Args:
        side: Side length of the cube.

    Returns:
        Tuple of (volume, surface_area).
    """
    volume = side**3
    surface_area = 6 * side**2
    return (volume, surface_area)


if __name__ == "__main__":
    volume, area = volume_surface_area_cube(5)
    print(f"Volume: {volume}, Surface Area: {area}")

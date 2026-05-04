"""Program for volume of pyramid."""


def volume_pyramid(base_area: float, height: float) -> float:
    """Calculate the volume of a pyramid.

    Args:
        base_area: Area of the base.
        height: Height of the pyramid.

    Returns:
        Volume of the pyramid.
    """
    return round((1 / 3) * base_area * height, 4)


if __name__ == "__main__":
    print(f"Volume: {volume_pyramid(10, 6)}")
    print(f"Volume: {volume_pyramid(25, 10)}")

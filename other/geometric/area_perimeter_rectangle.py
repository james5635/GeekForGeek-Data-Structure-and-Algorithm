"""Program for area and perimeter of rectangle."""


def area_perimeter_rectangle(length: float, width: float) -> tuple[float, float]:
    """Calculate area and perimeter of a rectangle.

    Args:
        length: Length of rectangle.
        width: Width of rectangle.

    Returns:
        Tuple of (area, perimeter).
    """
    area = length * width
    perimeter = 2 * (length + width)
    return (area, perimeter)


if __name__ == "__main__":
    area, perimeter = area_perimeter_rectangle(5, 3)
    print(f"Area: {area}, Perimeter: {perimeter}")

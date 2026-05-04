"""Program to find area of trapezoid."""


def area_trapezoid(a: float, b: float, h: float) -> float:
    """Calculate the area of a trapezoid.

    Args:
        a: Length of first parallel side.
        b: Length of second parallel side.
        h: Height of the trapezoid.

    Returns:
        Area of the trapezoid.
    """
    return 0.5 * (a + b) * h


if __name__ == "__main__":
    print(f"Area: {area_trapezoid(10, 6, 4)}")
    print(f"Area: {area_trapezoid(8, 12, 5)}")

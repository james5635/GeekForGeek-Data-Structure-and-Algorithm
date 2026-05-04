"""Program to find circumference of parallelogram."""


def circumference_parallelogram(a: float, b: float) -> float:
    """Calculate the circumference (perimeter) of a parallelogram.

    Args:
        a: Length of first side.
        b: Length of second side.

    Returns:
        Circumference of the parallelogram.
    """
    return 2 * (a + b)


if __name__ == "__main__":
    print(f"Circumference: {circumference_parallelogram(5, 3)}")
    print(f"Circumference: {circumference_parallelogram(10, 7)}")

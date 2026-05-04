"""Check whether a triangle is valid or not given sides."""


def is_valid_triangle(a: float, b: float, c: float) -> bool:
    """Check if three sides can form a valid triangle.

    Args:
        a: Length of first side.
        b: Length of second side.
        c: Length of third side.

    Returns:
        True if sides form a valid triangle, False otherwise.
    """
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return a + b > c and a + c > b and b + c > a


if __name__ == "__main__":
    print(f"Triangle (3, 4, 5): {is_valid_triangle(3, 4, 5)}")
    print(f"Triangle (1, 2, 8): {is_valid_triangle(1, 2, 8)}")

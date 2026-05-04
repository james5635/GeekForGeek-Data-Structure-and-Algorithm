"""Count integral points inside a triangle."""

import math


def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


def boundary_points(p1: tuple[int, int], p2: tuple[int, int]) -> int:
    return gcd(abs(p1[0] - p2[0]), abs(p1[1] - p2[1]))


def integral_points_triangle(
    x1: int, y1: int, x2: int, y2: int, x3: int, y3: int
) -> int:
    """Count integral points strictly inside a triangle using Pick's theorem.

    Args:
        x1, y1, x2, y2, x3, y3: Triangle vertex coordinates.

    Returns:
        Number of integral points inside the triangle.
    """
    p1, p2, p3 = (x1, y1), (x2, y2), (x3, y3)
    twice_area = abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    b = boundary_points(p1, p2) + boundary_points(p2, p3) + boundary_points(p3, p1)
    return (twice_area - b + 2) // 2


if __name__ == "__main__":
    print(f"Integral points: {integral_points_triangle(0, 0, 4, 0, 0, 4)}")

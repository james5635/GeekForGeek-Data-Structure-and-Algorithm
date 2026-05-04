"""Maximum area of a quadrilateral."""

import math


def maximum_area_quadrilateral(a: float, b: float, c: float, d: float) -> float:
    """Find the maximum possible area of a quadrilateral with given side lengths.

    Args:
        a, b, c, d: Lengths of the four sides.

    Returns:
        Maximum possible area using Brahmagupta's formula.
    """
    s = (a + b + c + d) / 2
    return round(math.sqrt((s - a) * (s - b) * (s - c) * (s - d)), 4)


if __name__ == "__main__":
    print(f"Max area: {maximum_area_quadrilateral(1, 2, 3, 4)}")
    print(f"Max area: {maximum_area_quadrilateral(5, 5, 5, 5)}")

"""Find if possible to rotate page by angle or not."""

import math


def rotate_page(
    p1: tuple[float, float], p2: tuple[float, float], angle: float
) -> tuple[tuple[float, float], tuple[float, float]]:
    """Rotate two points around the origin by a given angle.

    Args:
        p1: First point as (x, y).
        p2: Second point as (x, y).
        angle: Rotation angle in degrees.

    Returns:
        Tuple of rotated points ((x1, y1), (x2, y2)).
    """
    rad = math.radians(angle)
    cos_a = math.cos(rad)
    sin_a = math.sin(rad)

    def rotate(p: tuple[float, float]) -> tuple[float, float]:
        x = p[0] * cos_a - p[1] * sin_a
        y = p[0] * sin_a + p[1] * cos_a
        return (round(x, 4), round(y, 4))

    return (rotate(p1), rotate(p2))


if __name__ == "__main__":
    p1_rotated, p2_rotated = rotate_page((1, 0), (0, 1), 90)
    print(f"Rotated points: {p1_rotated}, {p2_rotated}")

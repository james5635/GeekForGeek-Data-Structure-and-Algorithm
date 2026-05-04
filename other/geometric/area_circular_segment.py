"""Program to find area of a circular segment."""

import math


def area_circular_segment(radius: float, height: float) -> float:
    """Calculate the area of a circular segment.

    Args:
        radius: Radius of the circle.
        height: Height of the segment (sagitta).

    Returns:
        Area of the circular segment.
    """
    if height > 2 * radius or height < 0:
        return -1

    theta = 2 * math.acos((radius - height) / radius)
    sector_area = 0.5 * radius * radius * theta
    triangle_area = 0.5 * radius * radius * math.sin(theta)
    return round(sector_area - triangle_area, 4)


if __name__ == "__main__":
    print(f"Segment area: {area_circular_segment(10, 5)}")
    print(f"Segment area: {area_circular_segment(5, 2)}")

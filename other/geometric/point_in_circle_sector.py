"""Check whether point exists in circle sector or not."""

import math


def point_in_circle_sector(
    px: float,
    py: float,
    cx: float,
    cy: float,
    radius: float,
    start_angle: float,
    end_angle: float,
) -> bool:
    """Check if a point lies inside a circle sector.

    Args:
        px, py: Point coordinates.
        cx, cy: Circle center coordinates.
        radius: Circle radius.
        start_angle: Start angle of sector in degrees.
        end_angle: End angle of sector in degrees.

    Returns:
        True if point is inside the sector, False otherwise.
    """
    dx = px - cx
    dy = py - cy

    if dx * dx + dy * dy > radius * radius:
        return False

    angle = math.degrees(math.atan2(dy, dx))
    if angle < 0:
        angle += 360

    start_angle = start_angle % 360
    end_angle = end_angle % 360

    if start_angle <= end_angle:
        return start_angle <= angle <= end_angle
    else:
        return angle >= start_angle or angle <= end_angle


if __name__ == "__main__":
    print(f"In sector: {point_in_circle_sector(1, 1, 0, 0, 5, 0, 90)}")
    print(f"In sector: {point_in_circle_sector(3, 3, 0, 0, 2, 0, 90)}")

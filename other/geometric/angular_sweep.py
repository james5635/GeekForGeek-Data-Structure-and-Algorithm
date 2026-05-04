"""Angular sweep: maximum points that can be enclosed in a circle of given radius."""

import math


def angular_sweep(points: list[tuple[float, float]], r: float) -> int:
    """Find maximum number of points that can be enclosed in a circle of radius r.

    Args:
        points: List of (x, y) coordinate tuples.
        r: Radius of the circle.

    Returns:
        Maximum number of points enclosable.
    """
    n = len(points)
    if n <= 1:
        return n

    def dist(p1: tuple[float, float], p2: tuple[float, float]) -> float:
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    max_points = 1

    for i in range(n):
        angles = []
        for j in range(n):
            if i == j:
                continue
            d = dist(points[i], points[j])
            if d > 2 * r:
                continue

            base_angle = math.atan2(
                points[j][1] - points[i][1], points[j][0] - points[i][0]
            )
            angle_offset = math.acos(d / (2 * r))

            angles.append((base_angle - angle_offset, 1))
            angles.append((base_angle + angle_offset, -1))

        angles.sort(key=lambda x: (x[0], -x[1]))

        count = 1
        for _, entry in angles:
            count += entry
            max_points = max(max_points, count)

    return max_points


if __name__ == "__main__":
    points = [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1)]
    print(f"Max points in circle r=1.5: {angular_sweep(points, 1.5)}")

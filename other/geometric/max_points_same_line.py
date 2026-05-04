"""Count maximum points on same line."""

import math
from collections import defaultdict


def max_points_same_line(points: list[tuple[int, int]]) -> int:
    """Find the maximum number of points that lie on the same line.

    Args:
        points: List of (x, y) coordinate tuples.

    Returns:
        Maximum number of collinear points.
    """
    n = len(points)
    if n <= 2:
        return n

    max_count = 0

    for i in range(n):
        slopes: defaultdict[str, int] = defaultdict(int)
        duplicate = 1

        for j in range(i + 1, n):
            dx = points[j][0] - points[i][0]
            dy = points[j][1] - points[i][1]

            if dx == 0 and dy == 0:
                duplicate += 1
                continue

            if dx == 0:
                key = "inf"
            elif dy == 0:
                key = "0"
            else:
                g = math.gcd(dx, dy)
                dx //= g
                dy //= g
                if dx < 0:
                    dx, dy = -dx, -dy
                key = f"{dy}/{dx}"

            slopes[key] += 1

        current_max = duplicate
        for count in slopes.values():
            current_max = max(current_max, count + duplicate)

        max_count = max(max_count, current_max)

    return max_count


if __name__ == "__main__":
    points = [(1, 1), (2, 2), (3, 3), (4, 5), (5, 6)]
    print(f"Maximum points on same line: {max_points_same_line(points)}")

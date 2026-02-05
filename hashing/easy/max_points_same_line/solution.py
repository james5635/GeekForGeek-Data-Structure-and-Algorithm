"""
Maximum Points on Same Line

Problem: Given N points on a 2D plane, find the maximum number of points that
lie on the same straight line.

Approach: For each point, calculate the slope of the line formed with every
other point. Use a hash map to count points with the same slope.

Time Complexity: O(n^2) - for each point, check all other points
Space Complexity: O(n) - hash map for slopes
"""

from collections import defaultdict
import math


def max_points_on_line(points):
    """
    Find maximum points on the same line.

    Args:
        points: List of [x, y] coordinates

    Returns:
        Maximum number of points on any line
    """
    n = len(points)
    if n <= 2:
        return n

    max_count = 0

    for i in range(n):
        slopes = defaultdict(int)
        same_point = 1  # Count the current point itself
        vertical = 0

        for j in range(i + 1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]

            # Same point
            if x1 == x2 and y1 == y2:
                same_point += 1
            # Vertical line
            elif x1 == x2:
                vertical += 1
            else:
                # Calculate slope as reduced fraction to avoid floating point
                dx = x2 - x1
                dy = y2 - y1

                # Reduce to simplest form
                g = math.gcd(abs(dx), abs(dy))
                dx //= g
                dy //= g

                # Normalize sign
                if dx < 0:
                    dx = -dx
                    dy = -dy
                elif dx == 0 and dy < 0:
                    dy = -dy

                slope = (dy, dx)
                slopes[slope] += 1

        # Find max for this point
        current_max = vertical
        for count in slopes.values():
            current_max = max(current_max, count)

        max_count = max(max_count, current_max + same_point)

    return max_count


if __name__ == "__main__":
    # Test Case 1: Points on same line
    points1 = [[1, 1], [2, 2], [3, 3]]
    print(f"Points: {points1}")
    print(f"Max points on line: {max_points_on_line(points1)}")
    print()

    # Test Case 2: No three collinear
    points2 = [[1, 1], [2, 2], [3, 5]]
    print(f"Points: {points2}")
    print(f"Max points on line: {max_points_on_line(points2)}")
    print()

    # Test Case 3: Multiple overlapping points
    points3 = [[1, 1], [1, 1], [1, 1]]
    print(f"Points: {points3}")
    print(f"Max points on line: {max_points_on_line(points3)}")
    print()

    # Test Case 4: Vertical line
    points4 = [[1, 1], [1, 2], [1, 3], [2, 2]]
    print(f"Points: {points4}")
    print(f"Max points on line: {max_points_on_line(points4)}")
    print()

    # Test Case 5: Horizontal line
    points5 = [[1, 1], [2, 1], [3, 1], [4, 2]]
    print(f"Points: {points5}")
    print(f"Max points on line: {max_points_on_line(points5)}")
    print()

    # Test Case 6: Single point
    points6 = [[0, 0]]
    print(f"Points: {points6}")
    print(f"Max points on line: {max_points_on_line(points6)}")
    print()

    # Test Case 7: Two points
    points7 = [[1, 1], [2, 2]]
    print(f"Points: {points7}")
    print(f"Max points on line: {max_points_on_line(points7)}")

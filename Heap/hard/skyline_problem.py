# Skyscraper Problem using Heaps
# URL: https://www.geeksforgeeks.org/the-skyline-problem-using-heaps/
# Note: This page returned 404 error and is not available

# The Skyline Problem is typically solved using a sweep line algorithm
# or divide and conquer approach, not directly with heaps.
#
# Problem: Given n buildings with coordinates (left, height, right),
# find the skyline silhouette.
#
# This implementation uses a divide and conquer approach:
#
# Time Complexity: O(n log n)
# Space Complexity: O(n)


def merge_skylines(left, right):
    """
    Merge two skylines efficiently.

    Args:
        left: List of (x, height) tuples for left building
        right: List of (x, height) tuples for right building

    Returns:
        Merged skyline as list of (x, height) tuples
    """
    n1, n2 = len(left), len(right)
    i, j = 0, 0
    result = []
    h1, h2 = 0, 0

    while i < n1 and j < n2:
        if left[i][0] < right[j][0]:
            x = left[i][0]
            h1 = left[i][1]
            i += 1
        elif left[i][0] > right[j][0]:
            x = right[j][0]
            h2 = right[j][1]
            j += 1
        else:
            x = left[i][0]
            h1 = left[i][1]
            h2 = right[j][1]
            i += 1
            j += 1

        height = max(h1, h2)
        if not result or result[-1][1] != height:
            result.append((x, height))

    while i < n1:
        result.append(left[i])
        i += 1

    while j < n2:
        result.append(right[j])
        j += 1

    return result


def get_skyline(buildings, left, right):
    """
    Get skyline using divide and conquer.

    Args:
        buildings: List of (left, height, right) tuples
        left: Start index
        right: End index

    Returns:
        Skyline as list of (x, height) tuples
    """
    if left == right:
        return [(buildings[left][0], buildings[left][1]), (buildings[left][2], 0)]

    mid = (left + right) // 2

    left_skyline = get_skyline(buildings, left, mid)
    right_skyline = get_skyline(buildings, mid + 1, right)

    return merge_skylines(left_skyline, right_skyline)


def print_skyline(buildings):
    """
    Print the skyline of buildings.

    Args:
        buildings: List of (left, height, right) tuples
    """
    if not buildings:
        return []

    skyline = get_skyline(buildings, 0, len(buildings) - 1)

    if skyline and skyline[-1][1] == 0:
        skyline.pop()

    return skyline


if __name__ == "__main__":
    buildings = [
        (1, 11, 5),
        (2, 6, 7),
        (3, 13, 9),
        (12, 7, 16),
        (14, 3, 25),
        (19, 18, 22),
        (23, 13, 29),
        (24, 4, 28),
    ]

    print("Buildings:", buildings)
    print("\nSkyline points:")
    skyline = print_skyline(buildings)
    for point in skyline:
        print(f"  ({point[0]}, {point[1]})")

    print("\n" + "=" * 50)

    buildings2 = [(0, 2, 3), (1, 5, 7)]
    print("\nBuildings:", buildings2)
    print("\nSkyline points:")
    skyline2 = print_skyline(buildings2)
    for point in skyline2:
        print(f"  ({point[0]}, {point[1]})")

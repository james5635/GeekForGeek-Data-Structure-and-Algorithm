"""
K Closest Points to the Origin - GeeksforGeeks
https://www.geeksforgeeks.org/find-k-closest-points-to-the-origin/

Problem: Given a 2D array points[][] where each element is [xi, yi], find the
k points closest to the origin (0, 0) using Euclidean distance.

Note: We use squared distance (x^2 + y^2) to avoid sqrt computation.

Approaches:
1. Sort by distance - O(n*log(n))
2. Quick Select - O(n) average, O(n^2) worst
3. Max Heap of size k - O(n*log(k))

Time Complexity:
- Sorting: O(n*log(n))
- Quick Select: O(n) average
- Max Heap: O(n*log(k))

Space Complexity: O(k) for heap approach
"""

import heapq


def squared_distance(point):
    """Calculate squared Euclidean distance from origin."""
    return point[0] * point[0] + point[1] * point[1]


def partition(points, left, right):
    """Partition for quick select algorithm."""
    pivot = points[right]
    i = left

    for j in range(left, right):
        if squared_distance(points[j]) <= squared_distance(pivot):
            points[i], points[j] = points[j], points[i]
            i += 1

    points[i], points[right] = points[right], points[i]
    return i


def quick_select(points, left, right, k):
    """Find k closest points using quick select."""
    if left <= right:
        pivot_idx = partition(points, left, right)
        left_cnt = pivot_idx - left + 1

        if left_cnt == k:
            return
        elif left_cnt > k:
            quick_select(points, left, pivot_idx - 1, k)
        else:
            quick_select(points, pivot_idx + 1, right, k - left_cnt)


def k_closest_sorting(points, k):
    """
    Approach 1: Sort points by squared distance.
    O(n*log(n)) time, O(1) space
    """
    points_copy = points.copy()
    points_copy.sort(key=squared_distance)
    return points_copy[:k]


def k_closest_quick_select(points, k):
    """
    Approach 2: Quick select algorithm.
    O(n) average time, O(n) space (for recursion)
    """
    points_copy = points.copy()
    quick_select(points_copy, 0, len(points_copy) - 1, k)
    return points_copy[:k]


def k_closest_heap(points, k):
    """
    Approach 3: Max heap of size k.
    O(n*log(k)) time, O(k) space - Most efficient for small k
    """
    max_heap = []

    for i in range(len(points)):
        dist = squared_distance(points[i])

        if len(max_heap) < k:
            heapq.heappush(max_heap, (-dist, points[i]))
        elif dist < -max_heap[0][0]:
            heapq.heappop(max_heap)
            heapq.heappush(max_heap, (-dist, points[i]))

    result = []
    while max_heap:
        result.append(heapq.heappop(max_heap)[1])

    return result


if __name__ == "__main__":
    # Example 1
    points = [[1, 3], [-2, 2], [5, 8], [0, 1]]
    k = 2

    print(f"Points: {points}")
    print(f"k = {k}")

    print("\n1. Sorting approach:")
    for p in k_closest_sorting(points, k):
        print(f"   {p} (dist: {squared_distance(p)})")

    print("\n2. Quick select approach:")
    for p in k_closest_quick_select(points, k):
        print(f"   {p} (dist: {squared_distance(p)})")

    print("\n3. Max heap approach:")
    for p in k_closest_heap(points, k):
        print(f"   {p} (dist: {squared_distance(p)})")

    # Example 2
    print("\n" + "=" * 50)
    points = [[2, 4], [-1, -1], [0, 0]]
    k = 1

    print(f"Points: {points}")
    print(f"k = {k}")
    print(f"K closest: {k_closest_heap(points, k)}")

"""
Maximize Sum of i*arr[i] with Only Rotations Allowed

Problem: Given an array arr[], find the maximum value of sum(i * arr[i])
with only rotations on the array allowed.

Example:
    Input: arr = [8, 3, 1, 2]
    Output: 29
    Explanation:
        Rotation 0: [8, 3, 1, 2] -> 0*8 + 1*3 + 2*1 + 3*2 = 11
        Rotation 1: [3, 1, 2, 8] -> 0*3 + 1*1 + 2*2 + 3*8 = 29  (Maximum)
        Rotation 2: [1, 2, 8, 3] -> 0*1 + 1*2 + 2*8 + 3*3 = 27
        Rotation 3: [2, 8, 3, 1] -> 0*2 + 1*8 + 2*3 + 3*1 = 17

Time Complexity:
    - Naive: O(n²)
    - Optimized: O(n)
    - Space: O(1)

The key insight is that we can compute the sum for rotation i from rotation i-1:
    arr = [a0, a1, a2, ..., a(n-1)]
    R0 = 0*a0 + 1*a1 + 2*a2 + ... + (n-1)*a(n-1)
    R1 = 0*a1 + 1*a2 + ... + (n-2)*a(n-1) + (n-1)*a0

    R1 - R0 = (a1 + a2 + ... + a(n-1) + a0) - n*a0
            = arrSum - n*a0

    General: Rj = R(j-1) + arrSum - n*a(n-j)

Author: Generated for GeekForGeeks DSA Tutorial
"""

from typing import List, Tuple


def max_sum_rotation_naive(arr: List[int]) -> Tuple[int, int]:
    """
    Find maximum sum of i*arr[i] using naive approach.
    Try all rotations and compute sum for each.

    Args:
        arr: Input array

    Returns:
        Tuple of (max_sum, best_rotation)

    Time: O(n²), Space: O(1)
    """
    n = len(arr)
    if n == 0:
        return 0, 0

    max_sum = float("-inf")
    best_rotation = 0

    for rotation in range(n):
        current_sum = 0
        for i in range(n):
            # After rotation, element at index i was at index (i + rotation) % n
            # But in our formula i*arr[i], we want original index contribution
            # Actually, let's think differently:
            # Rotation k means arr[k] moves to index 0, arr[k+1] to index 1, etc.
            idx = (rotation + i) % n
            current_sum += i * arr[idx]

        if current_sum > max_sum:
            max_sum = current_sum
            best_rotation = rotation

    return max_sum, best_rotation


def max_sum_rotation_optimized(arr: List[int]) -> Tuple[int, int]:
    """
    Find maximum sum of i*arr[i] using optimized O(n) approach.

    Key insight: R(j) = R(j-1) + arrSum - n * a(n-j)

    Args:
        arr: Input array

    Returns:
        Tuple of (max_sum, best_rotation)

    Time: O(n), Space: O(1)
    """
    n = len(arr)
    if n == 0:
        return 0, 0
    if n == 1:
        return 0, 0  # 0 * arr[0] = 0

    # Calculate sum of all elements
    arr_sum = sum(arr)

    # Calculate initial sum for R0: 0*a0 + 1*a1 + 2*a2 + ... + (n-1)*a(n-1)
    current_sum = 0
    for i in range(n):
        current_sum += i * arr[i]

    max_sum = current_sum
    best_rotation = 0

    # Compute subsequent rotations using the formula
    # Rj = R(j-1) + arrSum - n * a(n-j)
    for j in range(1, n):
        # After j rotations, element at position 0 is arr[j]
        # The element that moves from end to front is arr[n - j]
        current_sum = current_sum + arr_sum - n * arr[n - j]

        if current_sum > max_sum:
            max_sum = current_sum
            best_rotation = j

    return max_sum, best_rotation


def get_rotated_array(arr: List[int], rotation: int) -> List[int]:
    """Get array after specified number of rotations."""
    n = len(arr)
    rotation = rotation % n
    return arr[rotation:] + arr[:rotation]


def compute_rotation_sum(arr: List[int], rotation: int = 0) -> int:
    """
    Compute sum of i*arr[i] for a specific rotation.

    Args:
        arr: Input array
        rotation: Number of left rotations (default 0)

    Returns:
        Sum of i * arr[i] after rotation
    """
    rotated = get_rotated_array(arr, rotation)
    return sum(i * val for i, val in enumerate(rotated))


def max_sum_rotation_all_methods(arr: List[int]) -> dict:
    """
    Solve using all methods and return comparison.

    Args:
        arr: Input array

    Returns:
        Dictionary with results from each method
    """
    naive_result = max_sum_rotation_naive(arr)
    optimized_result = max_sum_rotation_optimized(arr)

    return {
        "naive": naive_result,
        "optimized": optimized_result,
        "match": naive_result == optimized_result,
    }


def max_sum_rotation_with_path(arr: List[int]) -> Tuple[int, int, List[int]]:
    """
    Find maximum sum along with the actual rotated array.

    Args:
        arr: Input array

    Returns:
        Tuple of (max_sum, best_rotation, rotated_array)
    """
    max_sum, best_rotation = max_sum_rotation_optimized(arr)
    rotated = get_rotated_array(arr, best_rotation)
    return max_sum, best_rotation, rotated


if __name__ == "__main__":
    # Test Case 1: Standard example
    print("=" * 60)
    print("Test Case 1: Standard Example")
    print("=" * 60)

    arr1 = [8, 3, 1, 2]
    print(f"Original array: {arr1}")
    print(f"Array sum: {sum(arr1)}")
    print(f"n = {len(arr1)}")

    print("\nAll rotations and their sums:")
    for r in range(len(arr1)):
        rotated = get_rotated_array(arr1, r)
        total = compute_rotation_sum(arr1, r)
        formula = " + ".join([f"{i}*{val}" for i, val in enumerate(rotated)])
        print(f"  Rotation {r}: {rotated}")
        print(f"    Sum: {formula} = {total}")

    result = max_sum_rotation_with_path(arr1)
    print(f"\nOptimized result:")
    print(f"  Maximum sum: {result[0]}")
    print(f"  Best rotation: {result[1]}")
    print(f"  Rotated array: {result[2]}")

    # Test Case 2: Edge cases
    print("\n" + "=" * 60)
    print("Test Case 2: Edge Cases")
    print("=" * 60)

    # Single element
    arr2 = [5]
    print(f"\nSingle element: {arr2}")
    naive2 = max_sum_rotation_naive(arr2)
    opt2 = max_sum_rotation_optimized(arr2)
    print(f"  Naive: {naive2}, Optimized: {opt2}")

    # Two elements
    arr3 = [1, 2]
    print(f"\nTwo elements: {arr3}")
    for r in range(2):
        rotated = get_rotated_array(arr3, r)
        total = compute_rotation_sum(arr3, r)
        print(f"  Rotation {r}: {rotated} -> sum = {total}")

    # All same elements
    arr4 = [5, 5, 5, 5]
    result4 = max_sum_rotation_with_path(arr4)
    print(f"\nAll same elements: {arr4}")
    print(f"  Maximum sum: {result4[0]}")
    print(f"  Best rotation: {result4[1]}")

    # Test Case 3: Various scenarios
    print("\n" + "=" * 60)
    print("Test Case 3: Various Scenarios")
    print("=" * 60)

    test_cases = [
        [1, 20, 2, 10],
        [10, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [100, 1, 1, 1],
        [1, 1, 1, 100],
    ]

    for i, arr in enumerate(test_cases, 4):
        print(f"\nArray {i}: {arr}")
        comparison = max_sum_rotation_all_methods(arr)
        print(f"  Naive result: {comparison['naive']}")
        print(f"  Optimized result: {comparison['optimized']}")
        print(f"  Match: {'✓' if comparison['match'] else '✗'}")

    # Test Case 4: Performance comparison
    print("\n" + "=" * 60)
    print("Test Case 4: Performance Comparison")
    print("=" * 60)

    import time

    # Large array
    large_arr = list(range(1000, 0, -1))  # Descending from 1000 to 1

    start = time.time()
    result_naive = max_sum_rotation_naive(large_arr)
    time_naive = time.time() - start

    start = time.time()
    result_opt = max_sum_rotation_optimized(large_arr)
    time_opt = time.time() - start

    print(f"Array size: {len(large_arr)}")
    print(f"Maximum sum: {result_opt[0]}")
    print(f"Best rotation: {result_opt[1]}")
    print(f"\nNaive O(n²) time: {time_naive:.6f}s")
    print(f"Optimized O(n) time: {time_opt:.6f}s")
    print(f"Speedup: {time_naive / time_opt:.2f}x")

    # Test Case 5: Mathematical verification
    print("\n" + "=" * 60)
    print("Test Case 5: Mathematical Formula Verification")
    print("=" * 60)

    arr5 = [3, 2, 1, 5, 4]
    print(f"Array: {arr5}")
    print(f"Sum of elements: {sum(arr5)}")

    print("\nVerifying formula: R(j) = R(j-1) + arrSum - n*a(n-j)")
    prev_sum = compute_rotation_sum(arr5, 0)
    print(f"\nR(0) = {prev_sum}")

    for j in range(1, len(arr5)):
        expected = prev_sum + sum(arr5) - len(arr5) * arr5[len(arr5) - j]
        actual = compute_rotation_sum(arr5, j)
        formula = f"R({j - 1}) + {sum(arr5)} - {len(arr5)}*{arr5[len(arr5) - j]}"
        print(f"R({j}) = {formula} = {expected}")
        print(f"       Actual computed: {actual}")
        print(f"       Match: {'✓' if expected == actual else '✗'}")
        prev_sum = actual

    print("\n" + "=" * 60)
    print("All tests completed successfully!")
    print("=" * 60)

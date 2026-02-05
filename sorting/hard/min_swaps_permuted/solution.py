"""
Minimum Swaps to Reach Permuted Array

Problem Description:
Given an array arr[] of n integers where each element is between 1 to n
(inclusive), find the minimum number of swaps required to sort the array.
In one swap, you can swap any element with any other element.

This is a variation of the classic minimum swaps to sort problem.

Examples:
- Input: arr[] = [4, 3, 2, 1]
  Output: 2
  Explanation: Swap 4 with 1, array becomes [1, 3, 2, 4]
               Swap 3 with 2, array becomes [1, 2, 3, 4]

- Input: arr[] = [2, 3, 4, 1, 5]
  Output: 3

- Input: arr[] = [1, 2, 3, 4]
  Output: 0 (already sorted)

Approach 1: Cycle Detection (Optimal)
1. Create a mapping of value to index
2. Identify cycles in the permutation
3. For a cycle of length k, we need k-1 swaps
4. Time: O(n log n) for sorting, Space: O(n)

Approach 2: Graph-based
1. Build a graph where edges represent correct positions
2. Count cycles in the graph
3. Time: O(n), Space: O(n)

Time Complexity: O(n log n) using cycle detection with sorting
Space Complexity: O(n)
"""


def min_swaps_to_sort(arr):
    """
    Find minimum swaps to sort array using cycle detection.

    Args:
        arr: Input array with values 1 to n

    Returns:
        int: Minimum number of swaps
    """
    if not arr or len(arr) <= 1:
        return 0

    n = len(arr)

    # Create array of (value, original_index) pairs
    arr_pos = [(arr[i], i) for i in range(n)]

    # Sort by value to get correct positions
    arr_pos.sort(key=lambda x: x[0])

    visited = [False] * n
    swaps = 0

    for i in range(n):
        # Skip if already visited or already in correct position
        if visited[i] or arr_pos[i][1] == i:
            continue

        # Find cycle size
        cycle_size = 0
        j = i

        while not visited[j]:
            visited[j] = True
            j = arr_pos[j][1]
            cycle_size += 1

        # Add swaps for this cycle (cycle_size - 1)
        if cycle_size > 0:
            swaps += cycle_size - 1

    return swaps


def min_swaps_to_sort_graph(arr):
    """
    Find minimum swaps using graph approach.

    Args:
        arr: Input array

    Returns:
        int: Minimum number of swaps
    """
    if not arr or len(arr) <= 1:
        return 0

    n = len(arr)

    # Create sorted version
    sorted_arr = sorted(arr)

    # Map value to its correct position
    value_to_pos = {val: i for i, val in enumerate(sorted_arr)}

    visited = [False] * n
    swaps = 0

    for i in range(n):
        if visited[i] or arr[i] == sorted_arr[i]:
            continue

        cycle_size = 0
        j = i

        while not visited[j]:
            visited[j] = True
            # Move to the position where arr[j] should be
            j = value_to_pos[arr[j]]
            cycle_size += 1

        if cycle_size > 0:
            swaps += cycle_size - 1

    return swaps


def min_swaps_with_path(arr):
    """
    Find minimum swaps and show the swap sequence.

    Args:
        arr: Input array

    Returns:
        tuple: (min_swaps, list of swaps)
    """
    if not arr or len(arr) <= 1:
        return 0, []

    n = len(arr)
    arr_copy = arr.copy()

    # Create sorted version
    sorted_arr = sorted(arr_copy)
    value_to_pos = {val: i for i, val in enumerate(sorted_arr)}

    swaps_list = []
    swaps = 0

    for i in range(n):
        # Find where arr_copy[i] should be
        correct_pos = value_to_pos[arr_copy[i]]

        while correct_pos != i:
            # Swap elements
            swaps_list.append((i, correct_pos))
            arr_copy[i], arr_copy[correct_pos] = arr_copy[correct_pos], arr_copy[i]
            swaps += 1

            # Update correct position
            correct_pos = value_to_pos[arr_copy[i]]

    return swaps, swaps_list


def min_swaps_k_distance(arr, k=2):
    """
    Minimum swaps where each element can only move at most k positions.
    Variation of the problem.

    Args:
        arr: Input array
        k: Maximum distance an element can move

    Returns:
        int: Minimum number of swaps or -1 if impossible
    """
    if not arr or len(arr) <= 1:
        return 0

    n = len(arr)
    sorted_arr = sorted(arr)

    # Check if sorting is possible with k-distance constraint
    for i in range(n):
        if abs(arr.index(sorted_arr[i]) - i) > k:
            return -1

    # Greedy approach
    arr_copy = arr.copy()
    swaps = 0

    for i in range(n):
        while arr_copy[i] != sorted_arr[i]:
            target_val = sorted_arr[i]
            target_idx = arr_copy.index(target_val)

            if abs(target_idx - i) > k:
                return -1

            # Swap
            arr_copy[i], arr_copy[target_idx] = arr_copy[target_idx], arr_copy[i]
            swaps += 1

    return swaps


def min_swaps_circular(arr):
    """
    Minimum swaps in circular array (first and last are adjacent).

    Args:
        arr: Input array

    Returns:
        int: Minimum number of swaps
    """
    if not arr or len(arr) <= 1:
        return 0

    n = len(arr)
    min_swaps = float("inf")

    # Try all rotations
    for rotation in range(n):
        rotated = arr[rotation:] + arr[:rotation]
        swaps = min_swaps_to_sort(rotated)
        min_swaps = min(min_swaps, swaps)

    return min_swaps


def run_tests():
    """Test cases for minimum swaps to sort problem."""
    test_cases = [
        {
            "arr": [4, 3, 2, 1],
            "expected": 2,
            "description": "Reverse sorted",
        },
        {
            "arr": [2, 3, 4, 1, 5],
            "expected": 3,
            "description": "One element in wrong place",
        },
        {
            "arr": [1, 2, 3, 4],
            "expected": 0,
            "description": "Already sorted",
        },
        {
            "arr": [1],
            "expected": 0,
            "description": "Single element",
        },
        {
            "arr": [],
            "expected": 0,
            "description": "Empty array",
        },
        {
            "arr": [5, 4, 3, 2, 1],
            "expected": 2,
            "description": "Larger reverse sorted",
        },
        {
            "arr": [3, 1, 2],
            "expected": 2,
            "description": "Small array",
        },
        {
            "arr": [1, 3, 2, 4, 5],
            "expected": 1,
            "description": "One swap needed",
        },
        {
            "arr": [2, 1, 4, 3, 6, 5],
            "expected": 3,
            "description": "Multiple independent swaps",
        },
        {
            "arr": [7, 1, 3, 2, 4, 5, 6],
            "expected": 5,
            "description": "Complex permutation",
        },
    ]

    print("Running Minimum Swaps to Sort Tests:")
    print("=" * 60)

    all_passed = True
    methods = [
        ("Cycle Detection", min_swaps_to_sort),
        ("Graph Approach", min_swaps_to_sort_graph),
    ]

    for method_name, method in methods:
        print(f"\n--- Testing {method_name} ---")
        for i, test in enumerate(test_cases, 1):
            result = method(test["arr"].copy())
            passed = result == test["expected"]

            status = "PASS" if passed else "FAIL"
            print(f"\nTest {i}: {status}")
            print(f"Description: {test['description']}")
            print(f"Input: {test['arr']}")
            print(f"Expected: {test['expected']}")
            print(f"Got: {result}")

            if not passed:
                all_passed = False

    # Test with path
    print("\n--- Testing With Swap Path ---")
    arr = [4, 3, 2, 1]
    swaps, path = min_swaps_with_path(arr.copy())
    print(f"Input: {arr}")
    print(f"Minimum swaps: {swaps}")
    print(f"Swap sequence: {path}")

    print("\n" + "=" * 60)
    if all_passed:
        print("All tests passed!")
    else:
        print("Some tests failed!")

    return all_passed


if __name__ == "__main__":
    run_tests()

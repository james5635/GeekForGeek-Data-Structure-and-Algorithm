"""
Unique Triplets with Given Sum

Problem Description:
Given an array arr[] of n integers and a target sum, find all unique
combinations of three elements in the array that sum up to the target.
The triplets should be unique (no duplicates) and each triplet should
be sorted in ascending order.

Examples:
- Input: arr[] = [1, 2, 3, 4, 5], target = 9
  Output: [[1, 3, 5], [2, 3, 4]]

- Input: arr[] = [0, -1, 2, -3, 1], target = 0
  Output: [[-3, 1, 2], [-1, 0, 1]]

- Input: arr[] = [1, 1, 1, 1], target = 3
  Output: [[1, 1, 1]]

Approach 1: Sorting + Two Pointers
1. Sort the array - O(n log n)
2. For each element i, use two pointers (left, right) to find pairs
3. Skip duplicates to ensure unique triplets
4. Time: O(n²), Space: O(1) excluding result

Approach 2: Hash Set (less efficient)
1. For each pair, check if target - sum exists in hash set
2. Use set to avoid duplicates
3. Time: O(n²), Space: O(n)

Approach 3: Binary Search (alternative)
1. Sort the array
2. For each pair, binary search for the third element
3. Time: O(n² log n), Space: O(1)

Time Complexity: O(n²) using two-pointer approach
Space Complexity: O(1) auxiliary space (excluding output)
"""


def find_unique_triplets_two_pointer(arr, target):
    """
    Find all unique triplets with given sum using two-pointer technique.

    Args:
        arr: Input array
        target: Target sum

    Returns:
        list: List of unique triplets, each sorted in ascending order
    """
    if not arr or len(arr) < 3:
        return []

    arr.sort()
    n = len(arr)
    result = []

    for i in range(n - 2):
        # Skip duplicates for first element
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        # Two pointers
        left, right = i + 1, n - 1

        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]

            if current_sum == target:
                result.append([arr[i], arr[left], arr[right]])

                # Skip duplicates for second element
                while left < right and arr[left] == arr[left + 1]:
                    left += 1

                # Skip duplicates for third element
                while left < right and arr[right] == arr[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            elif current_sum < target:
                left += 1
            else:
                right -= 1

    return result


def find_unique_triplets_hash_set(arr, target):
    """
    Find all unique triplets with given sum using hash set.

    Args:
        arr: Input array
        target: Target sum

    Returns:
        list: List of unique triplets
    """
    if not arr or len(arr) < 3:
        return []

    arr.sort()
    n = len(arr)
    result = set()

    for i in range(n - 2):
        # Skip duplicates for first element
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        seen = set()
        for j in range(i + 1, n):
            complement = target - arr[i] - arr[j]

            if complement in seen:
                triplet = tuple(sorted([arr[i], arr[j], complement]))
                result.add(triplet)

            seen.add(arr[j])

    return [list(triplet) for triplet in sorted(result)]


def find_unique_triplets_optimized(arr, target):
    """
    Optimized version with early termination.

    Args:
        arr: Input array
        target: Target sum

    Returns:
        list: List of unique triplets
    """
    if not arr or len(arr) < 3:
        return []

    arr.sort()
    n = len(arr)
    result = []

    for i in range(n - 2):
        # Skip duplicates
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        # Early termination: if smallest possible sum > target, break
        if arr[i] + arr[i + 1] + arr[i + 2] > target:
            break

        # Early termination: if largest possible sum < target, continue
        if arr[i] + arr[n - 2] + arr[n - 1] < target:
            continue

        left, right = i + 1, n - 1

        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]

            if current_sum == target:
                result.append([arr[i], arr[left], arr[right]])

                while left < right and arr[left] == arr[left + 1]:
                    left += 1
                while left < right and arr[right] == arr[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            elif current_sum < target:
                left += 1
            else:
                right -= 1

    return result


def find_unique_triplets_count(arr, target):
    """
    Count the number of unique triplets (without storing them).

    Args:
        arr: Input array
        target: Target sum

    Returns:
        int: Count of unique triplets
    """
    if not arr or len(arr) < 3:
        return 0

    arr.sort()
    n = len(arr)
    count = 0

    for i in range(n - 2):
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        left, right = i + 1, n - 1

        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]

            if current_sum == target:
                count += 1

                while left < right and arr[left] == arr[left + 1]:
                    left += 1
                while left < right and arr[right] == arr[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            elif current_sum < target:
                left += 1
            else:
                right -= 1

    return count


def run_tests():
    """Test cases for unique triplets with given sum."""
    test_cases = [
        {
            "arr": [1, 2, 3, 4, 5],
            "target": 9,
            "expected": [[1, 3, 5], [2, 3, 4]],
            "description": "Standard case",
        },
        {
            "arr": [0, -1, 2, -3, 1],
            "target": 0,
            "expected": [[-3, 1, 2], [-1, 0, 1]],
            "description": "With negative numbers",
        },
        {
            "arr": [1, 1, 1, 1],
            "target": 3,
            "expected": [[1, 1, 1]],
            "description": "All same elements",
        },
        {
            "arr": [1, 2, 3],
            "target": 6,
            "expected": [[1, 2, 3]],
            "description": "Minimum array size",
        },
        {
            "arr": [1, 2, 3],
            "target": 10,
            "expected": [],
            "description": "No valid triplet",
        },
        {
            "arr": [-1, 0, 1, 2, -1, -4],
            "target": 0,
            "expected": [[-1, -1, 2], [-1, 0, 1]],
            "description": "Multiple duplicates",
        },
        {
            "arr": [2, 2, 2, 2, 2],
            "target": 6,
            "expected": [[2, 2, 2]],
            "description": "All duplicates",
        },
        {
            "arr": [],
            "target": 0,
            "expected": [],
            "description": "Empty array",
        },
        {
            "arr": [1, 2],
            "target": 3,
            "expected": [],
            "description": "Less than 3 elements",
        },
        {
            "arr": [-2, 0, 1, 1, 2],
            "target": 0,
            "expected": [[-2, 0, 2], [-2, 1, 1]],
            "description": "Multiple solutions with duplicates",
        },
    ]

    print("Running Unique Triplets with Given Sum Tests:")
    print("=" * 60)

    all_passed = True
    methods = [
        ("Two Pointer", find_unique_triplets_two_pointer),
        ("Hash Set", find_unique_triplets_hash_set),
        ("Optimized", find_unique_triplets_optimized),
    ]

    for method_name, method in methods:
        print(f"\n--- Testing {method_name} ---")
        for i, test in enumerate(test_cases, 1):
            result = method(test["arr"].copy(), test["target"])
            expected = test["expected"]

            # Sort both for comparison
            result_sorted = sorted([sorted(triplet) for triplet in result])
            expected_sorted = sorted([sorted(triplet) for triplet in expected])

            passed = result_sorted == expected_sorted

            status = "PASS" if passed else "FAIL"
            print(f"\nTest {i}: {status}")
            print(f"Description: {test['description']}")
            print(f"Input: {test['arr']}, target={test['target']}")
            print(f"Expected: {expected}")
            print(f"Got: {result}")

            if not passed:
                all_passed = False

    print("\n" + "=" * 60)
    if all_passed:
        print("All tests passed!")
    else:
        print("Some tests failed!")

    return all_passed


if __name__ == "__main__":
    run_tests()

"""
Four Elements that Sum to a Given Value

Problem Description:
Given an array arr[] of n integers and a target sum, find four elements
in the array that sum up to the target value. Return all unique quadruplets.

Examples:
- Input: arr[] = [1, 0, -1, 0, -2, 2], target = 0
  Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

- Input: arr[] = [2, 2, 2, 2, 2], target = 8
  Output: [[2, 2, 2, 2]]

Approach 1: Sorting + Two Pointers (Optimal)
1. Sort the array - O(n log n)
2. Use two nested loops for first two elements
3. Use two pointers for remaining two elements
4. Skip duplicates at each level
5. Time: O(n³), Space: O(1) auxiliary

Approach 2: Hash Map (Alternative)
1. Store all pairs and their sums in hash map
2. For each pair, check if target - sum exists
3. Time: O(n²), Space: O(n²)

Approach 3: Brute Force
1. Check all combinations of 4 elements
2. Time: O(n⁴), Space: O(1)

Time Complexity: O(n³) using sorting + two pointers
Space Complexity: O(1) auxiliary space (excluding output)
"""


def find_four_elements_brute_force(arr, target):
    """
    Find four elements using brute force approach.

    Args:
        arr: Input array
        target: Target sum

    Returns:
        list: List of unique quadruplets
    """
    if not arr or len(arr) < 4:
        return []

    n = len(arr)
    result = set()

    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            for k in range(j + 1, n - 1):
                for l in range(k + 1, n):
                    if arr[i] + arr[j] + arr[k] + arr[l] == target:
                        quad = tuple(sorted([arr[i], arr[j], arr[k], arr[l]]))
                        result.add(quad)

    return [list(quad) for quad in sorted(result)]


def find_four_elements_two_pointer(arr, target):
    """
    Find four elements using sorting + two pointers.
    Optimal approach with O(n³) time.

    Args:
        arr: Input array
        target: Target sum

    Returns:
        list: List of unique quadruplets
    """
    if not arr or len(arr) < 4:
        return []

    arr.sort()
    n = len(arr)
    result = []

    for i in range(n - 3):
        # Skip duplicates for first element
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        # Early termination
        if arr[i] + arr[i + 1] + arr[i + 2] + arr[i + 3] > target:
            break
        if arr[i] + arr[n - 3] + arr[n - 2] + arr[n - 1] < target:
            continue

        for j in range(i + 1, n - 2):
            # Skip duplicates for second element
            if j > i + 1 and arr[j] == arr[j - 1]:
                continue

            # Early termination
            if arr[i] + arr[j] + arr[j + 1] + arr[j + 2] > target:
                break
            if arr[i] + arr[j] + arr[n - 2] + arr[n - 1] < target:
                continue

            left, right = j + 1, n - 1

            while left < right:
                current_sum = arr[i] + arr[j] + arr[left] + arr[right]

                if current_sum == target:
                    result.append([arr[i], arr[j], arr[left], arr[right]])

                    # Skip duplicates
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


def find_four_elements_hash_map(arr, target):
    """
    Find four elements using hash map approach.
    Time: O(n²), Space: O(n²)

    Args:
        arr: Input array
        target: Target sum

    Returns:
        list: List of unique quadruplets
    """
    if not arr or len(arr) < 4:
        return []

    n = len(arr)
    pair_sums = {}
    result = set()

    # Store all pairs and their indices
    for i in range(n - 1):
        for j in range(i + 1, n):
            current_sum = arr[i] + arr[j]
            complement = target - current_sum

            if complement in pair_sums:
                for pair in pair_sums[complement]:
                    a, b = pair
                    # Ensure all four indices are distinct
                    if a != i and a != j and b != i and b != j:
                        quad = tuple(sorted([arr[i], arr[j], arr[a], arr[b]]))
                        result.add(quad)

            if current_sum not in pair_sums:
                pair_sums[current_sum] = []
            pair_sums[current_sum].append((i, j))

    return [list(quad) for quad in sorted(result)]


def find_four_elements_optimized(arr, target):
    """
    Highly optimized version with multiple early terminations.

    Args:
        arr: Input array
        target: Target sum

    Returns:
        list: List of unique quadruplets
    """
    if not arr or len(arr) < 4:
        return []

    arr.sort()
    n = len(arr)
    result = []

    for i in range(n - 3):
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        # Early termination checks
        min_sum = arr[i] + arr[i + 1] + arr[i + 2] + arr[i + 3]
        max_sum = arr[i] + arr[n - 3] + arr[n - 2] + arr[n - 1]

        if min_sum > target:
            break
        if max_sum < target:
            continue

        for j in range(i + 1, n - 2):
            if j > i + 1 and arr[j] == arr[j - 1]:
                continue

            min_sum_j = arr[i] + arr[j] + arr[j + 1] + arr[j + 2]
            max_sum_j = arr[i] + arr[j] + arr[n - 2] + arr[n - 1]

            if min_sum_j > target:
                break
            if max_sum_j < target:
                continue

            left, right = j + 1, n - 1

            while left < right:
                current_sum = arr[i] + arr[j] + arr[left] + arr[right]

                if current_sum == target:
                    result.append([arr[i], arr[j], arr[left], arr[right]])

                    temp_left, temp_right = arr[left], arr[right]
                    while left < right and arr[left] == temp_left:
                        left += 1
                    while left < right and arr[right] == temp_right:
                        right -= 1

                elif current_sum < target:
                    left += 1
                else:
                    right -= 1

    return result


def run_tests():
    """Test cases for four elements sum problem."""
    test_cases = [
        {
            "arr": [1, 0, -1, 0, -2, 2],
            "target": 0,
            "expected": [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]],
            "description": "Standard case with multiple solutions",
        },
        {
            "arr": [2, 2, 2, 2, 2],
            "target": 8,
            "expected": [[2, 2, 2, 2]],
            "description": "All same elements",
        },
        {
            "arr": [1, 2, 3, 4, 5],
            "target": 10,
            "expected": [[1, 2, 3, 4]],
            "description": "Consecutive integers",
        },
        {
            "arr": [1, 2, 3],
            "target": 6,
            "expected": [],
            "description": "Less than 4 elements",
        },
        {
            "arr": [-3, -2, -1, 0, 0, 1, 2, 3],
            "target": 0,
            "expected": [
                [-3, -2, 2, 3],
                [-3, -1, 1, 3],
                [-3, 0, 0, 3],
                [-3, 0, 1, 2],
                [-2, -1, 0, 3],
                [-2, -1, 1, 2],
                [-2, 0, 0, 2],
                [-1, 0, 0, 1],
            ],
            "description": "Negative and positive mix",
        },
        {
            "arr": [0, 0, 0, 0],
            "target": 0,
            "expected": [[0, 0, 0, 0]],
            "description": "All zeros",
        },
        {
            "arr": [1, 1, 1, 2, 2, 2, 3, 3, 3],
            "target": 6,
            "expected": [[1, 1, 2, 2], [1, 1, 1, 3]],
            "description": "Multiple duplicates",
        },
        {
            "arr": [],
            "target": 0,
            "expected": [],
            "description": "Empty array",
        },
    ]

    print("Running Four Elements Sum Tests:")
    print("=" * 60)

    all_passed = True
    methods = [
        ("Two Pointer", find_four_elements_two_pointer),
        ("Optimized", find_four_elements_optimized),
        ("Hash Map", find_four_elements_hash_map),
        ("Brute Force", find_four_elements_brute_force),
    ]

    for method_name, method in methods:
        print(f"\n--- Testing {method_name} ---")
        for i, test in enumerate(test_cases, 1):
            result = method(test["arr"].copy(), test["target"])
            expected = test["expected"]

            # Sort for comparison
            result_sorted = sorted([sorted(quad) for quad in result])
            expected_sorted = sorted([sorted(quad) for quad in expected])

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

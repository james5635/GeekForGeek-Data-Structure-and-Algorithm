"""
4-Sum: Find a Quadruplet with Closest Sum

Problem Description:
Given an array arr[] of n integers and a target value, find four elements
in the array whose sum is closest to the target. Return the closest sum.

Examples:
- Input: arr[] = [1, 0, -1, 0, -2, 2], target = 0
  Output: 0
  Explanation: Closest quadruplet is [-2, -1, 1, 2] with sum 0

- Input: arr[] = [2, 2, 2, 2, 2], target = 8
  Output: 8
  Explanation: Quadruplet [2, 2, 2, 2] has exact sum

- Input: arr[] = [1, 2, 3, 4, 5], target = 100
  Output: 14
  Explanation: Maximum possible sum is 2+3+4+5=14

Approach 1: Sorting + Two Pointers (Optimal)
1. Sort the array - O(n log n)
2. Use two nested loops for first two elements
3. Use two pointers for remaining two elements
4. Track closest sum found
5. Time: O(n³), Space: O(1) auxiliary

Approach 2: Binary Search Variant
1. Sort the array
2. For first two elements, binary search for best pair
3. Time: O(n³ log n), Space: O(1)

Time Complexity: O(n³) using two-pointer approach
Space Complexity: O(1) auxiliary space
"""


def four_sum_closest_brute_force(arr, target):
    """
    Find closest quadruplet sum using brute force.

    Args:
        arr: Input array
        target: Target sum

    Returns:
        int: Closest sum to target
    """
    if not arr or len(arr) < 4:
        return None

    n = len(arr)
    closest_sum = float("inf")
    min_diff = float("inf")

    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            for k in range(j + 1, n - 1):
                for l in range(k + 1, n):
                    current_sum = arr[i] + arr[j] + arr[k] + arr[l]
                    diff = abs(current_sum - target)

                    if diff < min_diff:
                        min_diff = diff
                        closest_sum = current_sum
                    elif diff == min_diff and current_sum < closest_sum:
                        closest_sum = current_sum

    return closest_sum


def four_sum_closest_two_pointer(arr, target):
    """
    Find closest quadruplet sum using sorting + two pointers.
    Optimal O(n³) solution.

    Args:
        arr: Input array
        target: Target sum

    Returns:
        int: Closest sum to target
    """
    if not arr or len(arr) < 4:
        return None

    arr.sort()
    n = len(arr)
    closest_sum = arr[0] + arr[1] + arr[2] + arr[3]

    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            left, right = j + 1, n - 1

            while left < right:
                current_sum = arr[i] + arr[j] + arr[left] + arr[right]

                if current_sum == target:
                    return target

                # Update closest if this sum is closer
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                elif (
                    abs(current_sum - target) == abs(closest_sum - target)
                    and current_sum < closest_sum
                ):
                    closest_sum = current_sum

                if current_sum < target:
                    left += 1
                else:
                    right -= 1

    return closest_sum


def four_sum_closest_optimized(arr, target):
    """
    Optimized version with early termination.

    Args:
        arr: Input array
        target: Target sum

    Returns:
        int: Closest sum to target
    """
    if not arr or len(arr) < 4:
        return None

    arr.sort()
    n = len(arr)
    closest_sum = arr[0] + arr[1] + arr[2] + arr[3]

    for i in range(n - 3):
        # Early termination: if smallest possible sum >= target
        min_sum_i = arr[i] + arr[i + 1] + arr[i + 2] + arr[i + 3]
        if min_sum_i >= target:
            if abs(min_sum_i - target) < abs(closest_sum - target):
                closest_sum = min_sum_i
            break

        # Early termination: if largest possible sum < target
        max_sum_i = arr[i] + arr[n - 3] + arr[n - 2] + arr[n - 1]
        if max_sum_i < target:
            if abs(max_sum_i - target) < abs(closest_sum - target):
                closest_sum = max_sum_i
            continue

        for j in range(i + 1, n - 2):
            min_sum_j = arr[i] + arr[j] + arr[j + 1] + arr[j + 2]
            if min_sum_j >= target:
                if abs(min_sum_j - target) < abs(closest_sum - target):
                    closest_sum = min_sum_j
                break

            max_sum_j = arr[i] + arr[j] + arr[n - 2] + arr[n - 1]
            if max_sum_j < target:
                if abs(max_sum_j - target) < abs(closest_sum - target):
                    closest_sum = max_sum_j
                continue

            left, right = j + 1, n - 1

            while left < right:
                current_sum = arr[i] + arr[j] + arr[left] + arr[right]

                if current_sum == target:
                    return target

                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                if current_sum < target:
                    left += 1
                else:
                    right -= 1

    return closest_sum


def four_sum_closest_with_quadruplet(arr, target):
    """
    Return both the closest sum and the actual quadruplet.

    Args:
        arr: Input array
        target: Target sum

    Returns:
        tuple: (closest_sum, quadruplet)
    """
    if not arr or len(arr) < 4:
        return None, None

    arr.sort()
    n = len(arr)
    closest_sum = arr[0] + arr[1] + arr[2] + arr[3]
    best_quad = [arr[0], arr[1], arr[2], arr[3]]

    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            left, right = j + 1, n - 1

            while left < right:
                current_sum = arr[i] + arr[j] + arr[left] + arr[right]

                if current_sum == target:
                    return target, [arr[i], arr[j], arr[left], arr[right]]

                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                    best_quad = [arr[i], arr[j], arr[left], arr[right]]

                if current_sum < target:
                    left += 1
                else:
                    right -= 1

    return closest_sum, best_quad


def run_tests():
    """Test cases for 4-sum closest problem."""
    test_cases = [
        {
            "arr": [1, 0, -1, 0, -2, 2],
            "target": 0,
            "expected": 0,
            "description": "Exact match exists",
        },
        {
            "arr": [2, 2, 2, 2, 2],
            "target": 8,
            "expected": 8,
            "description": "All same elements",
        },
        {
            "arr": [1, 2, 3, 4, 5],
            "target": 100,
            "expected": 14,
            "description": "Target larger than max sum",
        },
        {
            "arr": [1, 2, 3, 4, 5],
            "target": 1,
            "expected": 10,
            "description": "Target smaller than min sum",
        },
        {
            "arr": [-3, -2, -1, 0, 1, 2, 3],
            "target": 0,
            "expected": 0,
            "description": "Negative and positive with target 0",
        },
        {
            "arr": [0, 0, 0, 0],
            "target": 1,
            "expected": 0,
            "description": "All zeros",
        },
        {
            "arr": [1, 1, 1, 0],
            "target": 100,
            "expected": 3,
            "description": "Small array",
        },
        {
            "arr": [-1, 2, 1, -4],
            "target": 1,
            "expected": -2,
            "description": "Classic 4-sum closest (only one quadruplet)",
        },
        {
            "arr": [],
            "target": 0,
            "expected": None,
            "description": "Empty array",
        },
        {
            "arr": [1, 2, 3],
            "target": 6,
            "expected": None,
            "description": "Less than 4 elements",
        },
    ]

    print("Running 4-Sum Closest Tests:")
    print("=" * 60)

    all_passed = True
    methods = [
        ("Two Pointer", four_sum_closest_two_pointer),
        ("Optimized", four_sum_closest_optimized),
        ("Brute Force", four_sum_closest_brute_force),
    ]

    for method_name, method in methods:
        print(f"\n--- Testing {method_name} ---")
        for i, test in enumerate(test_cases, 1):
            result = method(test["arr"].copy(), test["target"])
            passed = result == test["expected"]

            status = "PASS" if passed else "FAIL"
            print(f"\nTest {i}: {status}")
            print(f"Description: {test['description']}")
            print(f"Input: {test['arr']}, target={test['target']}")
            print(f"Expected: {test['expected']}")
            print(f"Got: {result}")

            if not passed:
                all_passed = False

    # Test quadruplet return
    print("\n--- Testing Quadruplet Return ---")
    arr = [1, 0, -1, 0, -2, 2]
    target = 0
    closest, quad = four_sum_closest_with_quadruplet(arr.copy(), target)
    print(f"Input: {arr}, target={target}")
    print(f"Closest sum: {closest}, Quadruplet: {quad}")
    print(f"Verification: {sum(quad) if quad else 'N/A'}")

    print("\n" + "=" * 60)
    if all_passed:
        print("All tests passed!")
    else:
        print("Some tests failed!")

    return all_passed


if __name__ == "__main__":
    run_tests()

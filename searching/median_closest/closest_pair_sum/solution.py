"""
Closest Pair Sum

Problem Description:
Given two sorted arrays arr1[0...m-1] and arr2[0...n-1], and a target value x,
find a pair (arr1[i], arr2[j]) such that the absolute difference |arr1[i] + arr2[j] - x|
is minimized. Return the pair.

Examples:
- Input: arr1 = [1, 4, 5, 7], arr2 = [10, 20, 30, 40], x = 32
  Output: [1, 30]
  Explanation: 1 + 30 = 31, closest to 32

- Input: arr1 = [1, 4, 5, 7], arr2 = [10, 20, 30, 40], x = 50
  Output: [7, 40]
  Explanation: 7 + 40 = 47, closest to 50

Approach:
Use two pointers - one at start of arr1, one at end of arr2.
Calculate sum and compare with target. If sum is less than target, move arr1 pointer forward.
If sum is greater, move arr2 pointer backward. Track the closest pair.

Time Complexity: O(m + n) where m and n are lengths of arrays
Space Complexity: O(1)
"""


def closest_pair_sum(arr1, arr2, target):
    """
    Find pair from two sorted arrays whose sum is closest to target.

    Args:
        arr1: First sorted array
        arr2: Second sorted array
        target: Target sum

    Returns:
        List containing the pair [elem1, elem2]
    """
    if not arr1 or not arr2:
        return []

    m, n = len(arr1), len(arr2)

    # Initialize pointers
    left = 0  # Pointer for arr1 (start)
    right = n - 1  # Pointer for arr2 (end)

    closest_pair = [arr1[0], arr2[0]]
    min_diff = abs(arr1[0] + arr2[0] - target)

    while left < m and right >= 0:
        current_sum = arr1[left] + arr2[right]
        current_diff = abs(current_sum - target)

        # Update if we found a better pair
        if current_diff < min_diff:
            min_diff = current_diff
            closest_pair = [arr1[left], arr2[right]]

        # Move pointers based on sum comparison
        if current_sum < target:
            # Sum is too small, increase it by moving left forward
            left += 1
        else:
            # Sum is too large or equal, decrease it by moving right backward
            right -= 1

    return closest_pair


def run_tests():
    """Test cases for the closest pair sum problem."""
    test_cases = [
        # Test case 1: Basic case
        {
            "arr1": [1, 4, 5, 7],
            "arr2": [10, 20, 30, 40],
            "target": 32,
            "expected": [1, 30],
            "description": "Basic case: 1+30=31 closest to 32",
        },
        # Test case 2: Another basic case
        {
            "arr1": [1, 4, 5, 7],
            "arr2": [10, 20, 30, 40],
            "target": 50,
            "expected": [7, 40],
            "description": "Target 50: 7+40=47 closest",
        },
        # Test case 3: Exact match
        {
            "arr1": [1, 4, 5, 7],
            "arr2": [10, 20, 30, 40],
            "target": 34,
            "expected": [4, 30],
            "description": "Exact match: 4+30=34",
        },
        # Test case 4: Small arrays
        {
            "arr1": [1, 2],
            "arr2": [3, 4],
            "target": 10,
            "expected": [2, 4],
            "description": "Small arrays: 2+4=6 closest to 10",
        },
        # Test case 5: Negative numbers
        {
            "arr1": [-5, -2, 0, 3],
            "arr2": [-3, 1, 4, 8],
            "target": 0,
            "expected": [-2, 1],
            "description": "With negatives: -2+1=-1 closest to 0",
        },
        # Test case 6: Large difference
        {
            "arr1": [1, 10, 100],
            "arr2": [1, 10, 100],
            "target": 150,
            "expected": [100, 10],
            "description": "Large difference: 100+10=110 or 100+100=200, 110 closer",
        },
        # Test case 7: Single element arrays
        {
            "arr1": [5],
            "arr2": [10],
            "target": 20,
            "expected": [5, 10],
            "description": "Single elements: only one pair possible",
        },
    ]

    print("Running Closest Pair Sum Tests:")
    print("=" * 60)

    all_passed = True
    for i, test in enumerate(test_cases, 1):
        result = closest_pair_sum(
            test["arr1"].copy(), test["arr2"].copy(), test["target"]
        )
        passed = result == test["expected"]

        status = "PASS" if passed else "FAIL"
        print(f"\nTest {i}: {status}")
        print(f"Description: {test['description']}")
        print(f"Array 1: {test['arr1']}")
        print(f"Array 2: {test['arr2']}")
        print(f"Target: {test['target']}")
        print(f"Expected: {test['expected']}")
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

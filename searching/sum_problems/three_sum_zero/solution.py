"""
Three Sum Zero

Problem Description:
Given an array arr[], find all possible indices {i, j, k} of triplet {arr[i], arr[j], arr[k]}
such that their sum is equal to zero and all indices in a triplet should be distinct
(i != j, j != k, k != i). Return indices of a triplet in sorted order (i < j < k).

Examples:
- Input: arr[] = [0, -1, 2, -3, 1]
  Output: [[0, 1, 4], [2, 3, 4]]
  Explanation:
  arr[0] + arr[1] + arr[4] = 0 + (-1) + 1 = 0
  arr[2] + arr[3] + arr[4] = 2 + (-3) + 1 = 0

- Input: arr[] = [1, -2, 1, 0, 5]
  Output: [[0, 1, 2]]
  Explanation: arr[0] + arr[1] + arr[2] = 1 + (-2) + 1 = 0

Approach:
Use a hash map to store indices of each element. For each pair (j, k), compute
the required third element as -(arr[j] + arr[k]) and check if it exists with index i < j.
This avoids duplicates by ensuring i < j < k.

Time Complexity: O(n^2) in worst case
Space Complexity: O(n) for the hash map
"""


def three_sum_zero(arr):
    """
    Find all triplets whose sum is zero.

    Args:
        arr: List of integers

    Returns:
        List of lists containing indices [i, j, k] where i < j < k
    """
    if not arr or len(arr) < 3:
        return []

    n = len(arr)
    result = []

    # Map to store indices for each value
    # Using dictionary to map value -> list of indices
    index_map = {}

    # Check for all pairs j, k
    for j in range(n):
        for k in range(j + 1, n):
            # Value of third index should be
            target = -(arr[j] + arr[k])

            # If such indices exist in map (which contains indices < j)
            if target in index_map:
                for i in index_map[target]:
                    result.append([i, j, k])

        # After j'th index is traversed, we can use it as i
        if arr[j] not in index_map:
            index_map[arr[j]] = []
        index_map[arr[j]].append(j)

    return result


def three_sum_zero_optimized(arr):
    """
    Alternative approach using sorting + two pointers for better average case.
    This returns values instead of indices.

    Args:
        arr: List of integers

    Returns:
        List of lists containing values [a, b, c] where a + b + c = 0
    """
    if not arr or len(arr) < 3:
        return []

    arr = sorted(arr)
    n = len(arr)
    result = []

    for i in range(n - 2):
        # Skip duplicates for i
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        left = i + 1
        right = n - 1

        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]

            if current_sum == 0:
                result.append([arr[i], arr[left], arr[right]])

                # Skip duplicates for left and right
                while left < right and arr[left] == arr[left + 1]:
                    left += 1
                while left < right and arr[right] == arr[right - 1]:
                    right -= 1

                left += 1
                right -= 1
            elif current_sum < 0:
                left += 1
            else:
                right -= 1

    return result


def run_tests():
    """Test cases for the three sum zero problem."""
    test_cases = [
        # Test case 1: Basic case
        {
            "input": [0, -1, 2, -3, 1],
            "expected": [[0, 1, 4], [2, 3, 4]],
            "description": "Basic case with two valid triplets",
        },
        # Test case 2: Single triplet
        {
            "input": [1, -2, 1, 0, 5],
            "expected": [[0, 1, 2]],
            "description": "Single valid triplet",
        },
        # Test case 3: No triplet
        {
            "input": [2, 3, 1, 0, 5],
            "expected": [],
            "description": "No valid triplet exists",
        },
        # Test case 4: Multiple zeros
        {
            "input": [0, 0, 0, 0],
            "expected": [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]],
            "description": "Multiple zeros",
        },
        # Test case 5: All same elements (non-zero)
        {
            "input": [1, 1, 1, 1],
            "expected": [],
            "description": "All same non-zero elements",
        },
        # Test case 6: Negative and positive mix
        {
            "input": [-1, 0, 1, 2, -1, -4],
            "expected": [[0, 1, 2], [0, 3, 4], [1, 2, 5], [1, 4, 5]],
            "description": "Mixed negative and positive",
        },
    ]

    print("Running Three Sum Zero Tests:")
    print("=" * 60)

    all_passed = True
    for i, test in enumerate(test_cases, 1):
        result = three_sum_zero(test["input"].copy())

        # Sort result and expected for comparison
        result_sorted = sorted([sorted(triplet) for triplet in result])
        expected_sorted = sorted([sorted(triplet) for triplet in test["expected"]])

        passed = result_sorted == expected_sorted

        status = "PASS" if passed else "FAIL"
        print(f"\nTest {i}: {status}")
        print(f"Description: {test['description']}")
        print(f"Input: {test['input']}")
        print(f"Expected: {test['expected']}")
        print(f"Got: {result}")

        if not passed:
            all_passed = False

    print("\n" + "=" * 60)
    if all_passed:
        print("All tests passed!")
    else:
        print("Some tests failed!")

    # Also test the optimized version (returns values)
    print("\n\nTesting Optimized Version (returns values):")
    print("-" * 60)
    test_arr = [-1, 0, 1, 2, -1, -4]
    result = three_sum_zero_optimized(test_arr)
    print(f"Input: {test_arr}")
    print(f"Triplets (values): {result}")

    return all_passed


if __name__ == "__main__":
    run_tests()

"""
4 Sum - Find Any Quadruplet Having Given Sum

Given an array of integers and a target sum, find any quadruplet in the array
such that its sum equals the target.

Algorithm:
1. Sort the array
2. Use two nested loops to fix first two elements
3. Use two pointers to find remaining two elements that complete the sum
4. Return any valid quadruplet found

Time Complexity: O(n³) - Two nested loops + two pointers
Space Complexity: O(1) - Only using a few variables (excluding output)
"""


def find_quadruplet_brute_force(arr, target):
    """
    Brute force approach - O(n^4) time.

    Args:
        arr: List of integers
        target: Target sum for quadruplet

    Returns:
        list: A quadruplet with sum equal to target, or empty list
    """
    n = len(arr)

    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            for k in range(j + 1, n - 1):
                for l in range(k + 1, n):
                    if arr[i] + arr[j] + arr[k] + arr[l] == target:
                        return [arr[i], arr[j], arr[k], arr[l]]

    return []


def find_quadruplet(arr, target):
    """
    Optimized approach using sorting and two pointers - O(n^3) time.

    Args:
        arr: List of integers
        target: Target sum for quadruplet

    Returns:
        list: A quadruplet with sum equal to target, or empty list
    """
    n = len(arr)

    if n < 4:
        return []

    # Sort the array
    arr = sorted(arr)

    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            # Use two pointers for remaining two elements
            left = j + 1
            right = n - 1

            while left < right:
                curr_sum = arr[i] + arr[j] + arr[left] + arr[right]

                if curr_sum == target:
                    return [arr[i], arr[j], arr[left], arr[right]]

                elif curr_sum < target:
                    left += 1

                else:  # curr_sum > target
                    right -= 1

    return []


def find_quadruplet_with_hashing(arr, target):
    """
    Alternative approach using hashing - O(n^2) time, O(n^2) space.
    Stores all pair sums and checks if complementary sum exists.

    Args:
        arr: List of integers
        target: Target sum for quadruplet

    Returns:
        list: A quadruplet with sum equal to target, or empty list
    """
    n = len(arr)

    if n < 4:
        return []

    # Dictionary to store pair sums: sum -> list of (i, j) pairs
    pair_sums = {}

    for i in range(n - 1):
        for j in range(i + 1, n):
            pair_sum = arr[i] + arr[j]

            complement = target - pair_sum

            if complement in pair_sums:
                # Found a complementary pair
                for k, l in pair_sums[complement]:
                    # Make sure all indices are distinct
                    if i != k and i != l and j != k and j != l:
                        return [arr[i], arr[j], arr[k], arr[l]]

            # Store current pair
            if pair_sum not in pair_sums:
                pair_sums[pair_sum] = []
            pair_sums[pair_sum].append((i, j))

    return []


def test_find_quadruplet():
    """Test cases for 4-sum quadruplet algorithm."""
    # Test Case 1: Basic case from problem
    arr = [2, 4, 6, 8, 1, 3]
    target = 15
    result = find_quadruplet(arr, target)
    assert len(result) == 4, (
        f"Test 1 failed: Should return 4 elements, got {len(result)}"
    )
    assert sum(result) == target, (
        f"Test 1 failed: Sum should be {target}, got {sum(result)}"
    )
    print("Test 1 passed: Basic case")

    # Test Case 2: No quadruplet exists
    arr = [1, 2, 3, 4, 10]
    target = 20
    result = find_quadruplet(arr, target)
    assert result == [], f"Test 2 failed: Expected empty list, got {result}"
    print("Test 2 passed: No quadruplet exists")

    # Test Case 3: Multiple possible quadruplets
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    target = 20
    result = find_quadruplet(arr, target)
    assert len(result) == 4, f"Test 3 failed: Should return 4 elements"
    assert sum(result) == target, f"Test 3 failed: Sum should be {target}"
    print("Test 3 passed: Multiple possible quadruplets")

    # Test Case 4: Array with duplicates
    arr = [2, 2, 2, 2, 2]
    target = 8
    result = find_quadruplet(arr, target)
    assert len(result) == 4, f"Test 4 failed: Should return 4 elements"
    assert sum(result) == target, f"Test 4 failed: Sum should be {target}"
    print("Test 4 passed: Array with duplicates")

    # Test Case 5: Small array - less than 4 elements
    arr = [1, 2, 3]
    target = 6
    result = find_quadruplet(arr, target)
    assert result == [], f"Test 5 failed: Expected empty list for small array"
    print("Test 5 passed: Small array")

    # Test Case 6: With negative numbers
    arr = [-1, 0, 1, 2, -2, 3]
    target = 0
    result = find_quadruplet(arr, target)
    if result:
        assert sum(result) == target, f"Test 6 failed: Sum should be {target}"
    print("Test 6 passed: With negative numbers")

    # Test Case 7: Large numbers
    arr = [100, 200, 300, 400, 500]
    target = 1000
    result = find_quadruplet(arr, target)
    assert result == [100, 200, 300, 400], (
        f"Test 7 failed: Expected [100, 200, 300, 400], got {result}"
    )
    print("Test 7 passed: Large numbers")

    # Test Case 8: Verify brute force matches optimized
    test_cases = [
        ([2, 4, 6, 8, 1, 3], 15),
        ([1, 2, 3, 4, 10], 20),
        ([1, 2, 3, 4, 5, 6], 15),
        ([2, 2, 2, 2, 2], 8),
    ]

    for i, (arr, target) in enumerate(test_cases, 8):
        result1 = find_quadruplet_brute_force(arr, target)
        result2 = find_quadruplet(arr, target)

        # Both should find a solution or both should not
        if result1:
            assert result2 and sum(result2) == target, (
                f"Test {i} failed: Optimized didn't find solution"
            )
        else:
            assert not result2, (
                f"Test {i} failed: Optimized found solution when brute force didn't"
            )
        print(f"Test {i} passed: Brute force matches optimized")

    # Test Case 9: Hashing approach
    arr = [2, 4, 6, 8, 1, 3]
    target = 15
    result = find_quadruplet_with_hashing(arr, target)
    assert len(result) == 4, f"Test 9 failed: Should return 4 elements"
    assert sum(result) == target, f"Test 9 failed: Sum should be {target}"
    print("Test 9 passed: Hashing approach")

    # Test Case 10: All approaches give consistent results
    import random

    for _ in range(10):
        arr = [random.randint(-10, 10) for _ in range(8)]
        target = random.randint(-20, 20)

        result1 = find_quadruplet(arr, target)
        result2 = find_quadruplet_with_hashing(arr, target)

        # Both should have same success/failure
        if result1:
            assert result2 and sum(result2) == target, (
                "Inconsistent results between approaches"
            )
        else:
            assert not result2, "Inconsistent results between approaches"
    print("Test 10 passed: Random tests - all approaches consistent")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_find_quadruplet()

    # Example usage
    print("\nExample 1:")
    arr = [2, 4, 6, 8, 1, 3]
    target = 15
    result = find_quadruplet(arr, target)
    print(f"Array: {arr}")
    print(f"Target: {target}")
    print(f"Quadruplet: {result}")
    if result:
        print(f"Sum: {sum(result)}")

    print("\nExample 2:")
    arr = [1, 2, 3, 4, 10]
    target = 20
    result = find_quadruplet(arr, target)
    print(f"Array: {arr}")
    print(f"Target: {target}")
    print(f"Quadruplet: {result}")

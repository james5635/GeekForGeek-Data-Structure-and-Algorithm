"""
Find a Triplet that Sum to a Given Value

Problem Description:
    Given an array and a target sum, find if there exists a triplet
    (three elements) in the array that sum up to the target.

Time Complexity: O(n²)
- Sorting: O(n log n)
- Two nested loops: O(n²)

Space Complexity: O(1) auxiliary
- Sorting may use O(log n) to O(n)
- Only using a few pointers

Example:
    Input: arr = [1, 4, 45, 6, 10, 8], target = 22
    Output: True (triplet: [4, 10, 8] or [4, 8, 10])
    Explanation: 4 + 10 + 8 = 22

    Input: arr = [1, 2, 3, 4, 5], target = 100
    Output: False
    Explanation: No triplet sums to 100

Approach:
    1. Sort the array
    2. Fix one element, use two-pointer technique for remaining sum
    3. For each i from 0 to n-3:
       - left = i + 1, right = n - 1
       - While left < right:
         - If arr[i] + arr[left] + arr[right] == target: found!
         - If sum < target: left++ (need larger sum)
         - If sum > target: right-- (need smaller sum)
"""

from typing import List, Tuple, Optional


def find_triplet_sum(arr: List[int], target: int) -> bool:
    """
    Check if any triplet sums to target.

    Args:
        arr: List of integers
        target: Target sum

    Returns:
        True if triplet exists, False otherwise
    """
    if not arr or len(arr) < 3:
        return False

    arr.sort()
    n = len(arr)

    for i in range(n - 2):
        # Skip duplicates to avoid checking same triplet
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        left = i + 1
        right = n - 1

        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]

            if current_sum == target:
                return True
            elif current_sum < target:
                left += 1
            else:
                right -= 1

    return False


def find_triplet_sum_with_values(
    arr: List[int], target: int
) -> Optional[Tuple[int, int, int]]:
    """
    Find the actual triplet that sums to target.

    Args:
        arr: List of integers
        target: Target sum

    Returns:
        Tuple of three integers if found, None otherwise
    """
    if not arr or len(arr) < 3:
        return None

    arr.sort()
    n = len(arr)

    for i in range(n - 2):
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        left = i + 1
        right = n - 1

        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]

            if current_sum == target:
                return (arr[i], arr[left], arr[right])
            elif current_sum < target:
                left += 1
            else:
                right -= 1

    return None


def find_all_triplets_with_sum(
    arr: List[int], target: int
) -> List[Tuple[int, int, int]]:
    """
    Find all unique triplets that sum to target.

    Args:
        arr: List of integers
        target: Target sum

    Returns:
        List of all unique triplets
    """
    if not arr or len(arr) < 3:
        return []

    arr.sort()
    n = len(arr)
    triplets = []

    for i in range(n - 2):
        # Skip duplicates
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        left = i + 1
        right = n - 1

        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]

            if current_sum == target:
                triplets.append((arr[i], arr[left], arr[right]))

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

    return triplets


def find_triplet_sum_brute_force(arr: List[int], target: int) -> bool:
    """
    Brute force approach for verification (O(n³)).

    Args:
        arr: List of integers
        target: Target sum

    Returns:
        True if triplet exists
    """
    n = len(arr)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == target:
                    return True
    return False


# Test cases
def test_find_triplet_sum():
    """Test cases for find_triplet_sum function."""
    # Test case 1: Basic example
    arr1 = [1, 4, 45, 6, 10, 8]
    target1 = 22
    result1 = find_triplet_sum(arr1.copy(), target1)
    assert result1 == True, f"Test 1 failed: {result1}"

    # Test case 2: No triplet exists
    arr2 = [1, 2, 3, 4, 5]
    target2 = 100
    result2 = find_triplet_sum(arr2.copy(), target2)
    assert result2 == False, f"Test 2 failed: {result2}"

    # Test case 3: Triplet with negative numbers (no valid triplet)
    arr3 = [-1, 2, 1, -4]
    target3 = -2
    result3 = find_triplet_sum(arr3.copy(), target3)
    # Possible sums: -1+2+1=2, -1+2-4=-3, -1+1-4=-4, 2+1-4=-1
    # No triplet sums to -2
    assert result3 == False, f"Test 3 failed: {result3}"

    # Test case 4: Exact match
    arr4 = [0, 0, 0]
    target4 = 0
    result4 = find_triplet_sum(arr4.copy(), target4)
    assert result4 == True, f"Test 4 failed: {result4}"

    # Test case 5: Minimum array size
    arr5 = [1, 2, 3]
    target5 = 6
    result5 = find_triplet_sum(arr5.copy(), target5)
    assert result5 == True, f"Test 5 failed: {result5}"

    # Test case 6: Array too small
    arr6 = [1, 2]
    target6 = 3
    result6 = find_triplet_sum(arr6.copy(), target6)
    assert result6 == False, f"Test 6 failed: {result6}"

    # Test case 7: Empty array
    arr7 = []
    target7 = 10
    result7 = find_triplet_sum(arr7.copy(), target7)
    assert result7 == False, f"Test 7 failed: {result7}"

    # Test case 8: Get actual values
    arr8 = [1, 4, 45, 6, 10, 8]
    target8 = 22
    triplet8 = find_triplet_sum_with_values(arr8.copy(), target8)
    assert triplet8 is not None, f"Test 8 failed: triplet not found"
    assert sum(triplet8) == target8, f"Test 8 failed: sum mismatch"

    # Test case 9: Multiple triplets
    arr9 = [-1, 0, 1, 2, -1, -4]
    target9 = 0
    triplets9 = find_all_triplets_with_sum(arr9.copy(), target9)
    assert len(triplets9) > 0, f"Test 9 failed: no triplets found"
    for triplet in triplets9:
        assert sum(triplet) == target9, f"Test 9 failed: triplet sum mismatch"

    # Test case 10: Compare with brute force
    import random

    arr10 = [random.randint(-10, 10) for _ in range(10)]
    target10 = random.randint(-20, 20)
    result10a = find_triplet_sum(arr10.copy(), target10)
    result10b = find_triplet_sum_brute_force(arr10.copy(), target10)
    assert result10a == result10b, f"Test 10 failed: {result10a} != {result10b}"

    print("All test cases passed!")


if __name__ == "__main__":
    # Run test cases
    test_find_triplet_sum()

    # Example usage
    arr = [1, 4, 45, 6, 10, 8]
    target = 22
    print(f"Array: {arr}")
    print(f"Target: {target}")
    print(f"Triplet exists: {find_triplet_sum(arr.copy(), target)}")

    triplet = find_triplet_sum_with_values(arr.copy(), target)
    if triplet:
        print(f"Triplet: {triplet}")

    # Find all triplets
    arr2 = [-1, 0, 1, 2, -1, -4]
    target2 = 0
    print(f"\nArray: {arr2}")
    print(f"Target: {target2}")
    print(f"All triplets: {find_all_triplets_with_sum(arr2.copy(), target2)}")

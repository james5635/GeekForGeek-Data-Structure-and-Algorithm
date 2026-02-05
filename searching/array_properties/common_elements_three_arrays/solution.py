"""
Find Common Elements in Three Sorted Arrays

Problem Description:
Given three sorted arrays, find all common elements among them.

Example:
    Input: arr1 = [1, 5, 10, 20, 40, 80]
            arr2 = [6, 7, 20, 80, 100]
            arr3 = [3, 4, 15, 20, 30, 70, 80, 120]
    Output: [20, 80]

Time Complexity: O(n1 + n2 + n3)
Space Complexity: O(1) excluding output

Approach: Three-pointer technique
    Initialize pointers at start of each array
    If elements at all pointers are equal, add to result
    Otherwise, increment pointer pointing to smallest element
"""


def find_common_elements(arr1, arr2, arr3):
    """
    Find common elements in three sorted arrays.

    Args:
        arr1, arr2, arr3: Three sorted arrays

    Returns:
        List of common elements
    """
    result = []
    i, j, k = 0, 0, 0

    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        if arr1[i] == arr2[j] == arr3[k]:
            # Avoid duplicates in result
            if not result or result[-1] != arr1[i]:
                result.append(arr1[i])
            i += 1
            j += 1
            k += 1
        elif arr1[i] <= arr2[j] and arr1[i] <= arr3[k]:
            i += 1
        elif arr2[j] <= arr1[i] and arr2[j] <= arr3[k]:
            j += 1
        else:
            k += 1

    return result


def find_common_elements_set(arr1, arr2, arr3):
    """
    Find common elements using set intersection.

    Time Complexity: O(n1 + n2 + n3)
    Space Complexity: O(n1 + n2 + n3)

    Args:
        arr1, arr2, arr3: Three arrays

    Returns:
        List of common elements (sorted)
    """
    set1 = set(arr1)
    set2 = set(arr2)
    set3 = set(arr3)

    common = set1.intersection(set2).intersection(set3)
    return sorted(list(common))


def test_find_common_elements():
    """Test cases for find_common_elements."""
    # Test case 1: Basic example
    arr1 = [1, 5, 10, 20, 40, 80]
    arr2 = [6, 7, 20, 80, 100]
    arr3 = [3, 4, 15, 20, 30, 70, 80, 120]
    assert find_common_elements(arr1, arr2, arr3) == [20, 80]
    assert find_common_elements_set(arr1, arr2, arr3) == [20, 80]

    # Test case 2: All arrays same
    arr4 = [1, 2, 3]
    arr5 = [1, 2, 3]
    arr6 = [1, 2, 3]
    assert find_common_elements(arr4, arr5, arr6) == [1, 2, 3]
    assert find_common_elements_set(arr4, arr5, arr6) == [1, 2, 3]

    # Test case 3: No common elements
    arr7 = [1, 2, 3]
    arr8 = [4, 5, 6]
    arr9 = [7, 8, 9]
    assert find_common_elements(arr7, arr8, arr9) == []
    assert find_common_elements_set(arr7, arr8, arr9) == []

    # Test case 4: Single common element
    arr10 = [1, 2, 3]
    arr11 = [3, 4, 5]
    arr12 = [3, 6, 7]
    assert find_common_elements(arr10, arr11, arr12) == [3]
    assert find_common_elements_set(arr10, arr11, arr12) == [3]

    # Test case 5: With duplicates in input
    arr13 = [1, 1, 2, 3, 3]
    arr14 = [1, 3, 3, 4, 5]
    arr15 = [1, 3, 3, 6, 7]
    assert find_common_elements(arr13, arr14, arr15) == [1, 3]
    assert find_common_elements_set(arr13, arr14, arr15) == [1, 3]

    # Test case 6: Empty arrays
    assert find_common_elements([], [], []) == []
    assert find_common_elements_set([], [], []) == []

    print("All test cases passed!")


if __name__ == "__main__":
    test_find_common_elements()

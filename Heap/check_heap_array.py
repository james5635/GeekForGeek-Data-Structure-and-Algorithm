# Python program to check whether a given array represents
# a Binary Max Heap or not


def isMaxHeapRecursive(arr, i, n):
    """
    Recursive function to check if the array represents a Max Heap.

    Args:
        arr: Input array
        i: Current index being checked
        n: Size of the array

    Returns:
        True if the array represents a Max Heap, False otherwise
    """
    # Base case: leaf node
    if i >= (n - 2) // 2 + 1:
        return True

    # Check if current node is greater than its children
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    # If left child exists and is greater than parent
    if left_child < n and arr[left_child] > arr[i]:
        return False

    # If right child exists and is greater than parent
    if right_child < n and arr[right_child] > arr[i]:
        return False

    # Recursively check left and right subtrees
    return isMaxHeapRecursive(arr, left_child, n) and isMaxHeapRecursive(
        arr, right_child, n
    )


def isMaxHeapIterative(arr, n):
    """
    Iterative function to check if the array represents a Max Heap.

    Args:
        arr: Input array
        n: Size of the array

    Returns:
        True if the array represents a Max Heap, False otherwise
    """
    # Start from root and go till the last internal node
    for i in range((n - 2) // 2 + 1):
        left_child = 2 * i + 1
        right_child = 2 * i + 2

        # If left child exists and is greater than parent
        if left_child < n and arr[left_child] > arr[i]:
            return False

        # If right child exists and is greater than parent
        if right_child < n and arr[right_child] > arr[i]:
            return False

    return True


# Driver code to test above functions
if __name__ == "__main__":
    # Test Case 1: Represents a Max Heap
    arr1 = [90, 15, 10, 7, 12, 2]
    n1 = len(arr1)

    print("Array:", arr1)
    print("Is Max Heap (Recursive):", isMaxHeapRecursive(arr1, 0, n1))
    print("Is Max Heap (Iterative):", isMaxHeapIterative(arr1, n1))
    print()

    # Test Case 2: Does not represent a Max Heap
    arr2 = [9, 15, 10, 7, 12, 11]
    n2 = len(arr2)

    print("Array:", arr2)
    print("Is Max Heap (Recursive):", isMaxHeapRecursive(arr2, 0, n2))
    print("Is Max Heap (Iterative):", isMaxHeapIterative(arr2, n2))
    print()

    # Test Case 3: Single element array (always a heap)
    arr3 = [5]
    n3 = len(arr3)

    print("Array:", arr3)
    print("Is Max Heap (Recursive):", isMaxHeapRecursive(arr3, 0, n3))
    print("Is Max Heap (Iterative):", isMaxHeapIterative(arr3, n3))
    print()

    # Test Case 4: Two elements (valid heap if first >= second)
    arr4 = [10, 5]
    n4 = len(arr4)

    print("Array:", arr4)
    print("Is Max Heap (Recursive):", isMaxHeapRecursive(arr4, 0, n4))
    print("Is Max Heap (Iterative):", isMaxHeapIterative(arr4, n4))
    print()

    # Test Case 5: Two elements (invalid heap if first < second)
    arr5 = [5, 10]
    n5 = len(arr5)

    print("Array:", arr5)
    print("Is Max Heap (Recursive):", isMaxHeapRecursive(arr5, 0, n5))
    print("Is Max Heap (Iterative):", isMaxHeapIterative(arr5, n5))
    print()

    # Test Case 6: Larger valid heap
    arr6 = [100, 50, 60, 20, 30, 40, 55]
    n6 = len(arr6)

    print("Array:", arr6)
    print("Is Max Heap (Recursive):", isMaxHeapRecursive(arr6, 0, n6))
    print("Is Max Heap (Iterative):", isMaxHeapIterative(arr6, n6))

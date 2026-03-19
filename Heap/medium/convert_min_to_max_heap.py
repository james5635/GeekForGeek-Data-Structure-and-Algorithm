"""
Convert Min Heap to Max Heap - GeeksforGeeks
https://www.geeksforgeeks.org/convert-min-heap-to-max-heap/

Problem: Given an array representation of a min heap, convert it to a max heap
in-place.

Approach: Bottom-up heapification
- Start from the last non-leaf node (parent of last leaf)
- Heapify each node going up to root
- Since array represents a min heap, we need to fix heap property
  to make it a max heap

Time Complexity: O(n)
Space Complexity: O(1) (in-place)
"""


def max_heapify(arr, i, n):
    """
    Heapify subtree with root at index i.

    Args:
        arr: Array representing heap
        i: Root index of subtree
        n: Size of heap
    """
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i

    if left < n and arr[left] > arr[i]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest, n)


def convert_max_heap(arr):
    """
    Convert min heap array to max heap in-place.

    Args:
        arr: List representing min heap

    Returns:
        None (modifies in-place)
    """
    n = len(arr)

    for i in range((n - 2) // 2, -1, -1):
        max_heapify(arr, i, n)


def print_array(arr, size):
    """Print array elements."""
    for i in range(size):
        print(arr[i], end=" ")
    print()


def is_max_heap(arr):
    """Verify if array represents a valid max heap."""
    n = len(arr)
    for i in range(n):
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[i] < arr[left]:
            return False
        if right < n and arr[i] < arr[right]:
            return False
    return True


def is_complete_binary_tree(arr):
    """Check if array represents a complete binary tree."""
    n = len(arr)
    for i in range(n):
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n:
            if arr[i] < arr[left]:
                return False
        if right < n:
            if arr[i] < arr[right]:
                return False
    return True


if __name__ == "__main__":
    # Example 1
    min_heap = [3, 5, 9, 6, 8, 20, 10, 12, 18, 9]

    print("Min Heap array:")
    print_array(min_heap, len(min_heap))

    convert_max_heap(min_heap)

    print("\nMax Heap array:")
    print_array(min_heap, len(min_heap))

    print(f"\nIs valid max heap: {is_max_heap(min_heap)}")

    # Example 2
    min_heap = [3, 4, 8, 11, 13]

    print("\n" + "=" * 50)
    print("Example 2:")
    print("Min Heap:", min_heap)

    convert_max_heap(min_heap)
    print("Max Heap:", min_heap)
    print(f"Is valid max heap: {is_max_heap(min_heap)}")

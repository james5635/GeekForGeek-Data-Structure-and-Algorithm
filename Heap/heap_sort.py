def heapify(arr, n, i):
    """
    Heapify a subtree rooted with node i which is an index in arr[].
    n is size of heap
    """
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # left = 2*i + 1
    right = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # See if right child of root exists and is greater than root
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)


def heap_sort(arr):
    """
    Main function to do heap sort
    """
    n = len(arr)

    # Build a maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # swap
        heapify(arr, i, 0)


def print_array(arr):
    """Utility function to print array"""
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


def main():
    # Test case from GeeksforGeeks article
    arr = [12, 11, 13, 5, 6, 7]
    n = len(arr)

    print("Original array is:")
    print_array(arr)

    heap_sort(arr)

    print("\nSorted array is:")
    print_array(arr)

    # Additional test cases
    print("\n--- Additional Test Cases ---")

    arr2 = [4, 10, 3, 5, 1]
    print("Original array 2:", end=" ")
    print_array(arr2)
    heap_sort(arr2)
    print("Sorted array 2:", end=" ")
    print_array(arr2)

    arr3 = [1]
    print("Original array 3:", end=" ")
    print_array(arr3)
    heap_sort(arr3)
    print("Sorted array 3:", end=" ")
    print_array(arr3)

    arr4 = []
    print("Original array 4:", end=" ")
    print_array(arr4)
    heap_sort(arr4)
    print("Sorted array 4:", end=" ")
    print_array(arr4)


if __name__ == "__main__":
    main()

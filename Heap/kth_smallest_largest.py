import heapq


def kth_smallest(arr, k):
    """
    Find kth smallest element using max-heap approach
    Time Complexity: O(n log k)
    Space Complexity: O(k)
    """
    # Create a max-heap using negative values (since heapq is min-heap)
    max_heap = []

    # Push first k elements into the max-heap
    for i in range(k):
        heapq.heappush(max_heap, -arr[i])

    # For remaining elements, if current element is smaller than root of max-heap,
    # replace the root with current element
    for i in range(k, len(arr)):
        if -arr[i] > max_heap[0]:  # arr[i] < -max_heap[0]
            heapq.heappop(max_heap)
            heapq.heappush(max_heap, -arr[i])

    # The root of max-heap is the kth smallest element
    return -max_heap[0]


def kth_largest(arr, k):
    """
    Find kth largest element using min-heap approach
    Time Complexity: O(n log k)
    Space Complexity: O(k)
    """
    # Create a min-heap
    min_heap = []

    # Push first k elements into the min-heap
    for i in range(k):
        heapq.heappush(min_heap, arr[i])

    # For remaining elements, if current element is larger than root of min-heap,
    # replace the root with current element
    for i in range(k, len(arr)):
        if arr[i] > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, arr[i])

    # The root of min-heap is the kth largest element
    return min_heap[0]


def main():
    # Test cases from GeeksforGeeks article
    arr = [7, 10, 4, 3, 20, 15]
    k = 3

    print(f"Array: {arr}")
    print(f"k = {k}")

    # Find kth smallest
    kth_small = kth_smallest(arr, k)
    print(f"K-th smallest element is {kth_small}")

    # Find kth largest
    kth_larg = kth_largest(arr, k)
    print(f"K-th largest element is {kth_larg}")

    # Additional test cases
    print("\n--- Additional Test Cases ---")
    arr2 = [12, 3, 5, 7, 19]
    k2 = 2
    print(f"Array: {arr2}, k = {k2}")
    print(f"K-th smallest: {kth_smallest(arr2, k2)}")
    print(f"K-th largest: {kth_largest(arr2, k2)}")

    arr3 = [1]
    k3 = 1
    print(f"Array: {arr3}, k = {k3}")
    print(f"K-th smallest: {kth_smallest(arr3, k3)}")
    print(f"K-th largest: {kth_largest(arr3, k3)}")


if __name__ == "__main__":
    main()

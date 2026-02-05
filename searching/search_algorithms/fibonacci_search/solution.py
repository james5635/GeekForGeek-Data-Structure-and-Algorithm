"""
Fibonacci Search

Problem:
Find the position of an element x in a sorted array using Fibonacci Search.

Fibonacci Search is a comparison-based technique that uses Fibonacci numbers
to divide the array into unequal parts. It uses the fact that Fibonacci
numbers grow exponentially (similar to binary search but with different splits).

Properties:
- Works on sorted arrays
- Uses Fibonacci numbers for dividing array
- Only uses addition and subtraction (no division/multiplication)
- Good for systems where division is expensive

Example:
    Input: arr = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100], key = 85
    Output: 8 (index of 85)

    Input: arr = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100], key = 95
    Output: -1 (not found)

Time Complexity: O(log n) - similar to binary search
Space Complexity: O(1) - iterative approach
"""


def fibonacci_search(arr: list[int], key: int) -> int:
    """
    Search for a key using fibonacci search algorithm.

    Uses Fibonacci numbers to divide the array. Only requires
    addition/subtraction operations.

    Args:
        arr: Sorted array to search in
        key: Element to search for

    Returns:
        Index of the key if found, -1 otherwise
    """
    if not arr:
        return -1

    n = len(arr)

    # Initialize fibonacci numbers
    # fib_m2 = F(m-2), fib_m1 = F(m-1), fib_m = F(m)
    fib_m2 = 0  # (m-2)'th Fibonacci number
    fib_m1 = 1  # (m-1)'th Fibonacci number
    fib_m = fib_m2 + fib_m1  # m'th Fibonacci number

    # Find the smallest fibonacci number >= n
    while fib_m < n:
        fib_m2 = fib_m1
        fib_m1 = fib_m
        fib_m = fib_m2 + fib_m1

    # Marks the eliminated range from front
    offset = -1

    # While there are elements to be inspected
    while fib_m > 1:
        # Check if fib_m2 is a valid location
        i = min(offset + fib_m2, n - 1)

        # If key is greater than the value at index fib_m2,
        # cut the subarray from offset to i
        if arr[i] < key:
            fib_m = fib_m1
            fib_m1 = fib_m2
            fib_m2 = fib_m - fib_m1
            offset = i

        # If key is less than the value at index fib_m2,
        # cut the subarray after i+1
        elif arr[i] > key:
            fib_m = fib_m2
            fib_m1 = fib_m1 - fib_m2
            fib_m2 = fib_m - fib_m1

        # Element found
        else:
            return i

    # Compare last element with key
    if fib_m1 and offset + 1 < n and arr[offset + 1] == key:
        return offset + 1

    return -1


# Alternative implementation with clearer steps
def fibonacci_search_v2(arr: list[int], key: int) -> int:
    """
    Alternative fibonacci search with explicit steps.

    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    if not arr:
        return -1

    n = len(arr)

    # Generate fibonacci numbers until we find one >= n
    fibs = [0, 1]
    while fibs[-1] < n:
        fibs.append(fibs[-1] + fibs[-2])

    # Start from the largest fibonacci number <= n
    idx = len(fibs) - 1
    offset = -1

    while idx > 0:
        # Index to check
        i = min(offset + fibs[idx - 1], n - 1)

        if arr[i] < key:
            # Move right
            offset = i
            idx -= 1
        elif arr[i] > key:
            # Move left (use fib[idx-2])
            idx -= 2
        else:
            return i

    # Check last position
    if idx == 0 and offset + 1 < n and arr[offset + 1] == key:
        return offset + 1

    return -1


if __name__ == "__main__":
    # Test Case 1: Standard case
    arr1 = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]
    key1 = 85
    result = fibonacci_search(arr1, key1)
    print(f"Test 1: arr={arr1}, key={key1}")
    print(f"Result: Index {result}")  # Expected: 8
    assert result == 8, "Test 1 failed"

    # Test Case 2: Key not found
    arr2 = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]
    key2 = 95
    result = fibonacci_search(arr2, key2)
    print(f"\nTest 2: arr={arr2}, key={key2}")
    print(f"Result: Index {result}")  # Expected: -1
    assert result == -1, "Test 2 failed"

    # Test Case 3: First element
    arr3 = [10, 20, 30, 40, 50]
    key3 = 10
    result = fibonacci_search(arr3, key3)
    print(f"\nTest 3: arr={arr3}, key={key3}")
    print(f"Result: Index {result}")  # Expected: 0
    assert result == 0, "Test 3 failed"

    # Test Case 4: Last element
    arr4 = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]
    key4 = 100
    result = fibonacci_search(arr4, key4)
    print(f"\nTest 4: arr={arr4}, key={key4}")
    print(f"Result: Index {result}")  # Expected: 10
    assert result == 10, "Test 4 failed"

    # Test Case 5: Single element
    arr5 = [42]
    key5 = 42
    result = fibonacci_search(arr5, key5)
    print(f"\nTest 5: arr={arr5}, key={key5}")
    print(f"Result: Index {result}")  # Expected: 0
    assert result == 0, "Test 5 failed"

    # Test Case 6: Two elements
    arr6 = [5, 10]
    key6 = 5
    result = fibonacci_search(arr6, key6)
    print(f"\nTest 6: arr={arr6}, key={key6}")
    print(f"Result: Index {result}")  # Expected: 0
    assert result == 0, "Test 6 failed"

    # Test Case 7: Large array
    arr7 = list(range(0, 100, 2))  # [0, 2, 4, ..., 98]
    key7 = 64
    result = fibonacci_search(arr7, key7)
    print(f"\nTest 7: arr size={len(arr7)}, key={key7}")
    print(f"Result: Index {result}")  # Expected: 32
    assert result == 32, "Test 7 failed"

    # Test Case 8: Compare v2
    arr8 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]
    key8 = 14
    result1 = fibonacci_search(arr8, key8)
    result2 = fibonacci_search_v2(arr8, key8)
    print(f"\nTest 8: arr={arr8}, key={key8}")
    print(f"V1 Result: Index {result1}")
    print(f"V2 Result: Index {result2}")
    assert result1 == result2 == 6, "Test 8 failed"

    # Test Case 9: Empty array
    arr9 = []
    key9 = 10
    result = fibonacci_search(arr9, key9)
    print(f"\nTest 9: arr={arr9}, key={key9}")
    print(f"Result: Index {result}")  # Expected: -1
    assert result == -1, "Test 9 failed"

    # Test Case 10: Middle element
    arr10 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
    key10 = 13
    result = fibonacci_search(arr10, key10)
    print(f"\nTest 10: arr={arr10}, key={key10}")
    print(f"Result: Index {result}")  # Expected: 6
    assert result == 6, "Test 10 failed"

    print("\nAll tests passed!")

"""
Missing and Repeating

Find both the missing and repeating number in a range [1, n].

Approaches:
1. Visited Array: O(n) time, O(n) space
2. Array Marking: O(n) time, O(1) space (modifies input)
3. Math Equations: O(n) time, O(1) space
4. XOR: O(n) time, O(1) space
"""


def find_missing_repeating_visited(arr):
    """
    Approach 1: Using visited array.

    Time Complexity: O(n)
    Space Complexity: O(n)

    Algorithm:
    - Create visited array of size n+1
    - Mark elements as visited
    - Number visited twice = repeating
    - Number not visited = missing

    Args:
        arr: List of integers from 1 to n with one missing and one repeating

    Returns:
        Tuple (repeating, missing)
    """
    n = len(arr)
    visited = [False] * (n + 1)
    repeating = -1

    for num in arr:
        if visited[num]:
            repeating = num
        visited[num] = True

    missing = -1
    for i in range(1, n + 1):
        if not visited[i]:
            missing = i
            break

    return repeating, missing


def find_missing_repeating_marking(arr):
    """
    Approach 2: Array marking (modifies input).

    Time Complexity: O(n)
    Space Complexity: O(1)

    Algorithm:
    - Use array indices as markers
    - Traverse array, mark arr[abs(arr[i]) - 1] as negative
    - If already negative, it's the repeating number
    - Positive index + 1 is the missing number

    Args:
        arr: List of integers from 1 to n with one missing and one repeating

    Returns:
        Tuple (repeating, missing)
    """
    n = len(arr)
    repeating = -1

    for i in range(n):
        index = abs(arr[i]) - 1
        if arr[index] < 0:
            repeating = abs(arr[i])
        else:
            arr[index] = -arr[index]

    missing = -1
    for i in range(n):
        if arr[i] > 0:
            missing = i + 1
            break

    return repeating, missing


def find_missing_repeating_math(arr):
    """
    Approach 3: Using mathematical equations.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Let:
    x = repeating number
    y = missing number

    Equations:
    1. Sum of 1..n - Sum of arr = y - x
    2. Sum of squares of 1..n - Sum of squares of arr = y² - x² = (y-x)(y+x)

    From eq 1: y - x = diff_sum
    From eq 2: y + x = diff_sq / diff_sum

    Solving:
    y = (diff_sum + diff_sq/diff_sum) / 2
    x = y - diff_sum

    Args:
        arr: List of integers from 1 to n with one missing and one repeating

    Returns:
        Tuple (repeating, missing)
    """
    n = len(arr)

    # Calculate sums
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    diff_sum = expected_sum - actual_sum  # y - x

    # Calculate sum of squares
    expected_sq_sum = n * (n + 1) * (2 * n + 1) // 6
    actual_sq_sum = sum(x * x for x in arr)
    diff_sq = expected_sq_sum - actual_sq_sum  # y² - x²

    # y + x = (y² - x²) / (y - x)
    sum_val = diff_sq // diff_sum

    # Solve for y and x
    missing = (diff_sum + sum_val) // 2
    repeating = sum_val - missing

    return repeating, missing


def find_missing_repeating_xor(arr):
    """
    Approach 4: Using XOR.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Algorithm:
    1. XOR all elements and 1..n -> gives x ^ y (repeating ^ missing)
    2. Find rightmost set bit in xor_result
    3. Partition numbers based on this bit
    4. XOR within partitions to find x and y
    5. Verify which is repeating by checking in array

    Args:
        arr: List of integers from 1 to n with one missing and one repeating

    Returns:
        Tuple (repeating, missing)
    """
    n = len(arr)

    # XOR all elements and 1..n
    xor_result = 0
    for num in arr:
        xor_result ^= num
    for i in range(1, n + 1):
        xor_result ^= i

    # xor_result = x ^ y (repeating ^ missing)
    # Find rightmost set bit
    rightmost_bit = xor_result & (-xor_result)

    # Partition and XOR
    x = 0
    y = 0

    for num in arr:
        if num & rightmost_bit:
            x ^= num
        else:
            y ^= num

    for i in range(1, n + 1):
        if i & rightmost_bit:
            x ^= i
        else:
            y ^= i

    # Verify which is repeating
    count = sum(1 for num in arr if num == x)
    if count == 2:
        return x, y
    else:
        return y, x


if __name__ == "__main__":
    # Test cases
    test_cases = [
        [3, 1, 2, 5, 3],  # n=5, repeating=3, missing=4
        [1, 2, 2, 4],  # n=4, repeating=2, missing=3
        [2, 2],  # n=2, repeating=2, missing=1
        [1, 1],  # n=2, repeating=1, missing=2
        [4, 3, 6, 2, 1, 1],  # n=6, repeating=1, missing=5
    ]

    print("=" * 70)
    print("Missing and Repeating - Find Both Numbers")
    print("=" * 70)

    for i, arr in enumerate(test_cases, 1):
        arr_copy1 = arr.copy()
        arr_copy2 = arr.copy()
        arr_copy3 = arr.copy()
        arr_copy4 = arr.copy()

        visited_result = find_missing_repeating_visited(arr_copy1)
        marking_result = find_missing_repeating_marking(arr_copy2)
        math_result = find_missing_repeating_math(arr_copy3)
        xor_result = find_missing_repeating_xor(arr_copy4)

        all_match = visited_result == marking_result == math_result == xor_result

        print(f"\nTest {i}: arr = {arr}, n = {len(arr)}")
        print(
            f"  Visited Array O(n) space:  Repeating={visited_result[0]}, Missing={visited_result[1]}"
        )
        print(
            f"  Array Marking O(1) space:  Repeating={marking_result[0]}, Missing={marking_result[1]}"
        )
        print(
            f"  Math Equations O(1):       Repeating={math_result[0]}, Missing={math_result[1]}"
        )
        print(
            f"  XOR O(1) space:            Repeating={xor_result[0]}, Missing={xor_result[1]} {'✓' if all_match else '✗'}"
        )

    print("\n" + "=" * 70)
    print("\nApproach Comparison:")
    print("  1. Visited Array:  Simple, uses O(n) extra space")
    print("  2. Array Marking:  O(1) space, modifies input array")
    print("  3. Math Equations: O(1) space, uses sum & sum of squares")
    print("  4. XOR:            O(1) space, no overflow risk, most elegant")
    print("=" * 70)

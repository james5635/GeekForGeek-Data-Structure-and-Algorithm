"""
Mo's Algorithm - Query Square Root Decomposition (Set 1 Introduction)

Mo's Algorithm is an offline query processing technique that preprocesses all
queries so that the result of one query can be reused in the next query.
It is particularly useful for range query problems on static arrays.

Steps:
1. Divide the array into blocks of size sqrt(n).
2. Sort queries by block number of L, and within the same block by R.
3. Process queries one by one while maintaining a running result.
4. Update the result incrementally instead of recomputing from scratch.

Time Complexity: O((n + m) * sqrt(n)) where n is array size, m is number of queries.
Space Complexity: O(n + m) for storing array and queries.

Source: https://www.geeksforgeeks.org/dsa/mos-algorithm-query-square-root-decomposition-set-1-introduction/
"""

import math


def query_results(arr, queries):
    """
    Process range sum queries using Mo's Algorithm.

    Args:
        arr: List of integers representing the input array.
        queries: List of [L, R] pairs representing query ranges (0-indexed, inclusive).

    Returns:
        List of integers containing the sum for each query range.
    """
    n = len(arr)
    block_size = int(math.sqrt(n))

    # Store original indices to return results in query order
    indexed_queries = []
    for idx, (l, r) in enumerate(queries):
        indexed_queries.append((l, r, idx))

    # Sort queries: by block of L, then by R within the same block
    indexed_queries.sort(key=lambda x: (x[0] // block_size, x[1]))

    # Initialize pointers and current sum
    curr_l = 0
    curr_r = 0
    curr_sum = 0

    results = [0] * len(queries)

    for l, r, original_idx in indexed_queries:
        # Remove extra elements from the left
        while curr_l < l:
            curr_sum -= arr[curr_l]
            curr_l += 1

        # Add elements when moving left boundary backward
        while curr_l > l:
            curr_sum += arr[curr_l - 1]
            curr_l -= 1

        # Add elements of current range
        while curr_r <= r:
            curr_sum += arr[curr_r]
            curr_r += 1

        # Remove elements when right boundary shrinks
        while curr_r > r + 1:
            curr_sum -= arr[curr_r - 1]
            curr_r -= 1

        results[original_idx] = curr_sum

    return results


def query_results_with_output(arr, queries):
    """
    Process and print range sum queries using Mo's Algorithm.

    Args:
        arr: List of integers representing the input array.
        queries: List of [L, R] pairs representing query ranges (0-indexed, inclusive).
    """
    n = len(arr)
    block_size = int(math.sqrt(n))

    # Store original indices
    indexed_queries = []
    for idx, (l, r) in enumerate(queries):
        indexed_queries.append((l, r, idx))

    # Sort queries
    indexed_queries.sort(key=lambda x: (x[0] // block_size, x[1]))

    curr_l = 0
    curr_r = 0
    curr_sum = 0

    results = [0] * len(queries)

    for l, r, original_idx in indexed_queries:
        while curr_l < l:
            curr_sum -= arr[curr_l]
            curr_l += 1

        while curr_l > l:
            curr_sum += arr[curr_l - 1]
            curr_l -= 1

        while curr_r <= r:
            curr_sum += arr[curr_r]
            curr_r += 1

        while curr_r > r + 1:
            curr_sum -= arr[curr_r - 1]
            curr_r -= 1

        results[original_idx] = curr_sum

    for i, (l, r) in enumerate(queries):
        print(f"Sum of [{l}, {r}] is {results[i]}")


if __name__ == "__main__":
    # Example 1 from GeeksforGeeks
    print("=== Example 1: Basic Range Sum Queries ===")
    arr = [1, 1, 2, 1, 3, 4, 5, 2, 8]
    queries = [[0, 4], [1, 3], [2, 4]]

    print(f"Array: {arr}")
    print(f"Queries: {queries}")
    print()
    query_results_with_output(arr, queries)

    # Example 2: Larger array with more queries
    print("\n=== Example 2: Larger Array ===")
    arr2 = [3, 7, 1, 4, 8, 2, 6, 5, 9, 10, 3, 7]
    queries2 = [[0, 5], [2, 8], [4, 11], [1, 3], [6, 9]]

    print(f"Array: {arr2}")
    print(f"Queries: {queries2}")
    print()
    query_results_with_output(arr2, queries2)

    # Example 3: Using the return-value function
    print("\n=== Example 3: Return Values ===")
    arr3 = [1, 1, 2, 1, 3, 4, 5, 2, 8]
    queries3 = [[0, 4], [1, 3], [2, 4]]

    results = query_results(arr3, queries3)
    for i, (l, r) in enumerate(queries3):
        print(f"Sum of [{l}, {r}] is {results[i]}")

    # Verification with brute force
    print("\n=== Verification with Brute Force ===")
    for i, (l, r) in enumerate(queries3):
        brute_force = sum(arr3[l : r + 1])
        print(
            f"Query [{l}, {r}]: Mo's={results[i]}, Brute Force={brute_force}, Match={results[i] == brute_force}"
        )

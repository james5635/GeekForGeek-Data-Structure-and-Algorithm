"""
Count All Possible Walks from Source to Destination with Exactly K Edges

Given a directed graph, count all possible walks from a source vertex
to a destination vertex that use exactly K edges.

Approach 1: Simple Recursion - O(V^K)
Approach 2: Dynamic Programming - O(V^3 * K)
Approach 3: Matrix Exponentiation - O(V^3 * log K)

A walk can visit the same vertex/edge multiple times (unlike a path).
"""

from typing import List


def count_walks_recursive(
    adj_matrix: List[List[int]], src: int, dest: int, k: int
) -> int:
    """
    Count walks using simple recursion.

    Args:
        adj_matrix: Adjacency matrix where adj_matrix[i][j] = 1 if edge exists
        src: Source vertex
        dest: Destination vertex
        k: Exact number of edges

    Returns:
        Number of walks with exactly k edges
    """
    if k == 0:
        return 1 if src == dest else 0
    if k == 1:
        return adj_matrix[src][dest]

    count = 0
    for i in range(len(adj_matrix)):
        if adj_matrix[src][i] == 1:
            count += count_walks_recursive(adj_matrix, i, dest, k - 1)

    return count


def count_walks_dp(adj_matrix: List[List[int]], src: int, dest: int, k: int) -> int:
    """
    Count walks using Dynamic Programming.

    dp[e][i][j] = number of walks from i to j using exactly e edges

    Time Complexity: O(V^3 * K)
    Space Complexity: O(V^2 * K) or O(V^2) with space optimization

    Args:
        adj_matrix: Adjacency matrix
        src: Source vertex
        dest: Destination vertex
        k: Exact number of edges

    Returns:
        Number of walks with exactly k edges
    """
    v = len(adj_matrix)

    # dp[i][j] = walks from i to j with current number of edges
    prev_dp = [[0] * v for _ in range(v)]

    # Base case: 0 edges (walk from i to i)
    for i in range(v):
        prev_dp[i][i] = 1

    # Build up for 1 to k edges
    for _ in range(1, k + 1):
        curr_dp = [[0] * v for _ in range(v)]
        for i in range(v):
            for j in range(v):
                for a in range(v):
                    if adj_matrix[i][a] == 1:
                        curr_dp[i][j] += prev_dp[a][j]
        prev_dp = curr_dp

    return prev_dp[src][dest]


def count_walks_space_optimized(
    adj_matrix: List[List[int]], src: int, dest: int, k: int
) -> int:
    """
    Count walks with O(V^2) space optimization.

    Time Complexity: O(V^3 * K)
    Space Complexity: O(V^2)
    """
    v = len(adj_matrix)

    # dp[j] = walks from src to j with current number of edges
    dp = [0] * v
    dp[src] = 1  # 0 edges: at src

    for _ in range(k):
        new_dp = [0] * v
        for i in range(v):
            if dp[i] > 0:
                for j in range(v):
                    if adj_matrix[i][j] == 1:
                        new_dp[j] += dp[i]
        dp = new_dp

    return dp[dest]


def matrix_multiply(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
    """Multiply two matrices."""
    n = len(a)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if a[i][k] == 0:
                continue
            for j in range(n):
                result[i][j] += a[i][k] * b[k][j]
    return result


def matrix_power(matrix: List[List[int]], k: int) -> List[List[int]]:
    """Compute matrix^k using binary exponentiation."""
    n = len(matrix)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        result[i][i] = 1

    base = [row[:] for row in matrix]

    while k > 0:
        if k % 2 == 1:
            result = matrix_multiply(result, base)
        base = matrix_multiply(base, base)
        k //= 2

    return result


def count_walks_matrix_exponentiation(
    adj_matrix: List[List[int]], src: int, dest: int, k: int
) -> int:
    """
    Count walks using matrix exponentiation.

    The (src, dest) entry of adj_matrix^k gives the number of walks
    from src to dest with exactly k edges.

    Time Complexity: O(V^3 * log K)
    Space Complexity: O(V^2)

    Args:
        adj_matrix: Adjacency matrix
        src: Source vertex
        dest: Destination vertex
        k: Exact number of edges

    Returns:
        Number of walks with exactly k edges
    """
    if k == 0:
        return 1 if src == dest else 0

    result_matrix = matrix_power(adj_matrix, k)
    return result_matrix[src][dest]


if __name__ == "__main__":
    # Example graph:
    #   0 -> 1, 0 -> 2, 0 -> 3
    #   1 -> 3
    #   2 -> 3
    adj = [[0, 1, 1, 1], [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 0]]

    src, dest, k = 0, 3, 2

    # Example 1: Recursive
    print("=== Example 1: Recursive ===")
    result = count_walks_recursive(adj, src, dest, k)
    print(f"Walks from {src} to {dest} with exactly {k} edges: {result}")
    # Paths: 0->1->3, 0->2->3 = 2

    # Example 2: DP
    print("\n=== Example 2: DP ===")
    result = count_walks_dp(adj, src, dest, k)
    print(f"Walks from {src} to {dest} with exactly {k} edges: {result}")

    # Example 3: Matrix Exponentiation
    print("\n=== Example 3: Matrix Exponentiation ===")
    result = count_walks_matrix_exponentiation(adj, src, dest, k)
    print(f"Walks from {src} to {dest} with exactly {k} edges: {result}")

    # Example 4: Larger k value
    print("\n=== Example 4: Larger graph, k=3 ===")
    adj2 = [
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
        [1, 0, 0, 0],  # cycle back
    ]
    k2 = 3
    r1 = count_walks_dp(adj2, 0, 0, k2)
    r2 = count_walks_matrix_exponentiation(adj2, 0, 0, k2)
    print(f"Walks from 0 to 0 with {k2} edges (DP): {r1}")
    print(f"Walks from 0 to 0 with {k2} edges (Matrix): {r2}")

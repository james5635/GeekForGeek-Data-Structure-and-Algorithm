"""
Print All Possible Paths in Matrix

Given a 2D matrix of dimension m x n, print all possible paths from the
top-left corner to the bottom-right corner. From each cell, you can only
move RIGHT or DOWN.

Approach: Backtracking
- Start from top-left cell (0, 0)
- At each cell, try moving right (if possible)
- Try moving down (if possible)
- When reaching bottom-right, print the path
- Backtrack to explore other paths

Examples:
    Input: [[1, 2, 3],
            [4, 5, 6]]
    Output: [1, 4, 5, 6]
            [1, 2, 5, 6]
            [1, 2, 3, 6]
"""


def printPath(path: list) -> None:
    """Print the current path in readable format."""
    print("  [" + ", ".join(str(x) for x in path) + "]")


def findPaths(arr: list, path: list, i: int, j: int, M: int, N: int) -> None:
    """
    Recursive function to find all paths using backtracking.

    Args:
        arr: Input 2D matrix
        path: Current path being built
        i: Current row index
        j: Current column index
        M: Number of rows
        N: Number of columns
    """
    # Base case: If we've reached the bottom-right cell
    if i == M - 1 and j == N - 1:
        path.append(arr[i][j])
        printPath(path)
        path.pop()  # Backtrack
        return

    # Boundary check
    if i < 0 or i >= M or j < 0 or j >= N:
        return

    # Include current cell in path
    path.append(arr[i][j])

    # Move RIGHT in the matrix
    if j + 1 < N:
        findPaths(arr, path, i, j + 1, M, N)

    # Move DOWN in the matrix
    if i + 1 < M:
        findPaths(arr, path, i + 1, j, M, N)

    # Backtrack: Remove current cell from path
    path.pop()


def getAllPaths(arr: list) -> list:
    """
    Find all paths from top-left to bottom-right.

    Args:
        arr: Input 2D matrix

    Returns:
        List of all paths

    Time Complexity: O(2^(M*N))
    Space Complexity: O(M + N) for recursion stack
    """
    if not arr or not arr[0]:
        return []

    M, N = len(arr), len(arr[0])
    all_paths = []
    path = []

    def collectPaths(i, j):
        # Base case
        if i == M - 1 and j == N - 1:
            path.append(arr[i][j])
            all_paths.append(list(path))
            path.pop()
            return

        if i < 0 or i >= M or j < 0 or j >= N:
            return

        path.append(arr[i][j])

        if j + 1 < N:
            collectPaths(i, j + 1)

        if i + 1 < M:
            collectPaths(i + 1, j)

        path.pop()

    collectPaths(0, 0)
    return all_paths


def countPaths(M: int, N: int) -> int:
    """
    Count total number of paths without enumerating them.

    This is equivalent to choosing (M-1) downs from (M+N-2) moves,
    or (N-1) rights from (M+N-2) moves.

    Formula: C(M+N-2, M-1) or C(M+N-2, N-1)
    """
    # Use dynamic programming approach
    dp = [[0] * N for _ in range(M)]

    # There's only one way to reach any cell in first row (move right only)
    for j in range(N):
        dp[0][j] = 1

    # There's only one way to reach any cell in first column (move down only)
    for i in range(M):
        dp[i][0] = 1

    # For other cells, number of paths = paths from above + paths from left
    for i in range(1, M):
        for j in range(1, N):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[M - 1][N - 1]


def main():
    """Test the matrix paths functions."""
    print("=" * 60)
    print("Print All Possible Paths in Matrix")
    print("=" * 60)

    test_cases = [
        [[1, 2, 3], [4, 5, 6]],
        [[1, 2], [3, 4]],
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    ]

    for idx, arr in enumerate(test_cases, 1):
        M, N = len(arr), len(arr[0])
        print(f"\nTest Case {idx}: {M}x{N} Matrix")
        print("-" * 40)

        # Print matrix
        print("Matrix:")
        for row in arr:
            print(f"  {row}")

        # Count paths
        total = countPaths(M, N)
        print(f"\nTotal possible paths: {total}")

        # Print all paths
        print("\nAll paths (top-left to bottom-right):")
        path = []
        findPaths(arr, path, 0, 0, M, N)

    print("\n" + "=" * 60)
    print("Complexity Analysis:")
    print("=" * 60)
    print("Time Complexity: O(2^(M*N))")
    print("  - Each cell can lead to two recursive calls")
    print("Space Complexity: O(M + N)")
    print("  - Maximum depth of recursion stack")
    print("\nPath Counting (DP):")
    print("  Time: O(M * N)")
    print("  Space: O(M * N)")


if __name__ == "__main__":
    main()

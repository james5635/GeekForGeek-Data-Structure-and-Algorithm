"""
Shortest Path in Binary Matrix

Problem:
Given an n x n binary matrix, find the length of the shortest clear path from
top-left cell (0, 0) to bottom-right cell (n-1, n-1).

A clear path:
- All visited cells must be 0
- Adjacent cells are 8-directionally connected (horizontal, vertical, diagonal)
- Path length = number of visited cells

If no path exists, return -1.

Algorithm: BFS with 8 directions
- Start BFS from (0, 0) if it's 0
- Explore all 8 directions from each cell
- First time we reach (n-1, n-1) gives the shortest path

Time Complexity: O(n^2)
Space Complexity: O(n^2)
"""

from collections import deque


def shortest_path_binary_matrix(grid: list[list[int]]) -> int:
    """
    Find the shortest clear path in a binary matrix.

    Args:
        grid: n x n binary matrix (0 = clear, 1 = blocked)

    Returns:
        Length of shortest path, or -1 if no path exists
    """
    if not grid or not grid[0]:
        return -1

    n = len(grid)

    # If start or end is blocked, no path possible
    if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
        return -1

    # Special case: 1x1 grid
    if n == 1:
        return 1

    # 8 directions
    directions = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]

    queue = deque()
    queue.append((0, 0, 1))  # (row, col, path_length)
    grid[0][0] = 1  # Mark as visited

    while queue:
        r, c, length = queue.popleft()

        # Check all 8 directions
        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                # Check if we reached the destination
                if nr == n - 1 and nc == n - 1:
                    return length + 1

                grid[nr][nc] = 1  # Mark as visited
                queue.append((nr, nc, length + 1))

    return -1


def shortest_path_binary_matrix_with_path(
    grid: list[list[int]],
) -> tuple[int, list[tuple[int, int]]]:
    """
    Find shortest path and return the actual path taken.

    Args:
        grid: n x n binary matrix

    Returns:
        Tuple of (length, path) where path is list of (row, col) coordinates
    """
    if not grid or not grid[0]:
        return -1, []

    n = len(grid)

    if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
        return -1, []

    if n == 1:
        return 1, [(0, 0)]

    directions = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]

    # Work on a copy to avoid modifying original
    visited = [[False] * n for _ in range(n)]
    visited[0][0] = True

    queue = deque()
    queue.append((0, 0, 1, [(0, 0)]))

    while queue:
        r, c, length, path = queue.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if (
                0 <= nr < n
                and 0 <= nc < n
                and not visited[nr][nc]
                and grid[nr][nc] == 0
            ):
                new_path = path + [(nr, nc)]

                if nr == n - 1 and nc == n - 1:
                    return length + 1, new_path

                visited[nr][nc] = True
                queue.append((nr, nc, length + 1, new_path))

    return -1, []


if __name__ == "__main__":
    # Example 1
    grid1 = [[0, 1], [1, 0]]
    result1 = shortest_path_binary_matrix([row[:] for row in grid1])
    print(f"Example 1: {result1}")  # Output: 2

    # Example 2
    grid2 = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
    result2 = shortest_path_binary_matrix([row[:] for row in grid2])
    print(f"Example 2: {result2}")  # Output: 4

    # Example 3
    grid3 = [[1, 0, 0], [1, 1, 0], [1, 1, 0]]
    result3 = shortest_path_binary_matrix([row[:] for row in grid3])
    print(f"Example 3: {result3}")  # Output: -1

    # Example 4: Larger grid with path
    grid4 = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
    ]
    result4 = shortest_path_binary_matrix([row[:] for row in grid4])
    print(f"Example 4: {result4}")  # Output: 3 (diagonal path)

    # Example 5: With path reconstruction
    grid5 = [
        [0, 0, 1],
        [1, 0, 0],
        [1, 1, 0],
    ]
    length5, path5 = shortest_path_binary_matrix_with_path([row[:] for row in grid5])
    print(f"Example 5: length = {length5}")
    if path5:
        print(f"  Path: {path5}")

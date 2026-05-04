"""
Rotten Oranges - Minimum Time to Rot All Oranges

Problem:
Given a grid where each cell can be:
  0 = empty cell
  1 = fresh orange
  2 = rotten orange

Every minute, any fresh orange adjacent (4-directionally) to a rotten orange becomes rotten.
Return the minimum time until no fresh orange remains. If impossible, return -1.

Algorithm: Multi-source BFS
- Start BFS from all rotten oranges simultaneously
- Each level of BFS represents one minute
- Track fresh oranges; if any remain after BFS, return -1

Time Complexity: O(rows * cols)
Space Complexity: O(rows * cols)
"""

from collections import deque


def rot_oranges(grid: list[list[int]]) -> int:
    """
    Find the minimum time to rot all oranges.

    Args:
        grid: 2D list where 0=empty, 1=fresh, 2=rotten

    Returns:
        Minimum minutes to rot all oranges, or -1 if impossible
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh_count = 0

    # Initialize queue with all rotten oranges and count fresh oranges
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c))
            elif grid[r][c] == 1:
                fresh_count += 1

    if fresh_count == 0:
        return 0

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    minutes = 0

    while queue and fresh_count > 0:
        minutes += 1
        for _ in range(len(queue)):
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh_count -= 1
                    queue.append((nr, nc))

    return minutes if fresh_count == 0 else -1


if __name__ == "__main__":
    # Example 1
    grid1 = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    print(f"Grid 1: {rot_oranges([row[:] for row in grid1])}")  # Output: 4

    # Example 2
    grid2 = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    print(f"Grid 2: {rot_oranges([row[:] for row in grid2])}")  # Output: -1

    # Example 3
    grid3 = [[0, 2]]
    print(f"Grid 3: {rot_oranges([row[:] for row in grid3])}")  # Output: 0

    # Example 4
    grid4 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    print(
        f"Grid 4: {rot_oranges([row[:] for row in grid4])}"
    )  # Output: -1 (no rotten orange)

    # Example 5
    grid5 = [[2, 2, 2], [1, 1, 1], [1, 1, 1]]
    print(f"Grid 5: {rot_oranges([row[:] for row in grid5])}")  # Output: 2

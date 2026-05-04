"""
Number of Islands in a Graph

Problem:
Given an n x m grid of 'L' (Land) and 'W' (Water), count the number of islands.
An island is a group of adjacent 'L' cells connected horizontally, vertically, or diagonally.

Algorithm: BFS on each unvisited land cell
- Traverse the grid; when an unvisited 'L' is found, start BFS to mark entire island
- Each BFS initiation counts as one island

Time Complexity: O(rows * cols)
Space Complexity: O(rows * cols) for visited array
"""

from collections import deque


def count_islands(grid: list[list[str]]) -> int:
    """
    Count the number of islands in a grid.

    Args:
        grid: 2D list of 'L' (land) and 'W' (water)

    Returns:
        Number of distinct islands
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    island_count = 0

    # 8 directions: horizontal, vertical, diagonal
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

    def bfs(start_r: int, start_c: int) -> None:
        """Perform BFS to mark all cells of an island as visited."""
        queue = deque()
        queue.append((start_r, start_c))
        visited[start_r][start_c] = True

        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == "L" and not visited[nr][nc]:
                        visited[nr][nc] = True
                        queue.append((nr, nc))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "L" and not visited[r][c]:
                bfs(r, c)
                island_count += 1

    return island_count


if __name__ == "__main__":
    # Example 1
    grid1 = [
        ["L", "W", "L", "L", "W"],
        ["W", "W", "L", "W", "W"],
        ["L", "W", "L", "L", "L"],
        ["W", "W", "W", "W", "W"],
    ]
    print(f"Grid 1: {count_islands(grid1)} islands")  # Output: 3

    # Example 2
    grid2 = [
        ["L", "L", "L"],
        ["L", "L", "L"],
        ["L", "L", "L"],
    ]
    print(f"Grid 2: {count_islands(grid2)} islands")  # Output: 1

    # Example 3
    grid3 = [
        ["W", "W", "W"],
        ["W", "W", "W"],
    ]
    print(f"Grid 3: {count_islands(grid3)} islands")  # Output: 0

    # Example 4
    grid4 = [
        ["L", "W", "L"],
        ["W", "L", "W"],
        ["L", "W", "L"],
    ]
    print(f"Grid 4: {count_islands(grid4)} islands")  # Output: 1 (diagonally connected)

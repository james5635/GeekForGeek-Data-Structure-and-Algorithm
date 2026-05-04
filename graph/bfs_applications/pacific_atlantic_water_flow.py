"""
Pacific Atlantic Water Flow

Problem:
Given an m x n matrix of heights where heights[r][c] represents the height of cell (r, c):
- Pacific Ocean touches the left and top edges
- Atlantic Ocean touches the right and bottom edges
- Water can flow to an adjacent cell (up, down, left, right) if the adjacent cell's
  height is less than or equal to the current cell's height

Find all cells from which water can flow to BOTH the Pacific and Atlantic oceans.

Algorithm: Reverse BFS/DFS from ocean edges
- Instead of checking each cell, start from ocean edges and flow "uphill"
- Find all cells reachable from Pacific edges
- Find all cells reachable from Atlantic edges
- Return cells that are reachable from both

Time Complexity: O(m * n)
Space Complexity: O(m * n)
"""

from collections import deque


def pacific_atlantic(heights: list[list[int]]) -> list[list[int]]:
    """
    Find cells that can flow to both Pacific and Atlantic oceans.

    Args:
        heights: m x n matrix of heights

    Returns:
        List of [row, col] coordinates that can reach both oceans
    """
    if not heights or not heights[0]:
        return []

    rows, cols = len(heights), len(heights[0])

    def bfs_from_ocean(ocean_cells: set[tuple[int, int]]) -> set[tuple[int, int]]:
        """BFS from ocean edge cells, flowing uphill."""
        reachable = set(ocean_cells)
        queue = deque(ocean_cells)

        while queue:
            r, c = queue.popleft()

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and (nr, nc) not in reachable
                    and heights[nr][nc] >= heights[r][c]
                ):
                    reachable.add((nr, nc))
                    queue.append((nr, nc))

        return reachable

    # Pacific: top row and left column
    pacific_cells = set()
    for r in range(rows):
        pacific_cells.add((r, 0))
    for c in range(cols):
        pacific_cells.add((0, c))

    # Atlantic: bottom row and right column
    atlantic_cells = set()
    for r in range(rows):
        atlantic_cells.add((r, cols - 1))
    for c in range(cols):
        atlantic_cells.add((rows - 1, c))

    # Find reachable cells from each ocean
    pacific_reachable = bfs_from_ocean(pacific_cells)
    atlantic_reachable = bfs_from_ocean(atlantic_cells)

    # Cells reachable from both oceans
    result = sorted(list(pacific_reachable & atlantic_reachable))
    return [list(cell) for cell in result]


def pacific_atlantic_dfs(heights: list[list[int]]) -> list[list[int]]:
    """
    Find cells that can flow to both oceans using DFS.

    Args:
        heights: m x n matrix of heights

    Returns:
        List of [row, col] coordinates
    """
    if not heights or not heights[0]:
        return []

    rows, cols = len(heights), len(heights[0])

    def dfs(r: int, c: int, visited: set[tuple[int, int]]) -> None:
        visited.add((r, c))

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if (
                0 <= nr < rows
                and 0 <= nc < cols
                and (nr, nc) not in visited
                and heights[nr][nc] >= heights[r][c]
            ):
                dfs(nr, nc, visited)

    pacific_visited = set()
    atlantic_visited = set()

    # Start DFS from Pacific edges
    for r in range(rows):
        dfs(r, 0, pacific_visited)
    for c in range(cols):
        dfs(0, c, pacific_visited)

    # Start DFS from Atlantic edges
    for r in range(rows):
        dfs(r, cols - 1, atlantic_visited)
    for c in range(cols):
        dfs(rows - 1, c, atlantic_visited)

    result = sorted(list(pacific_visited & atlantic_visited))
    return [list(cell) for cell in result]


if __name__ == "__main__":
    # Example 1
    heights1 = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4],
    ]
    result1 = pacific_atlantic(heights1)
    print("Example 1 (BFS):")
    for cell in result1:
        print(f"  {cell}")
    # Expected: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

    # Example 1 with DFS
    result1_dfs = pacific_atlantic_dfs(heights1)
    print("\nExample 1 (DFS):")
    for cell in result1_dfs:
        print(f"  {cell}")

    # Example 2: Simple case
    heights2 = [[1]]
    result2 = pacific_atlantic(heights2)
    print(f"\nExample 2: {result2}")  # Output: [[0, 0]]

    # Example 3: Flat matrix
    heights3 = [
        [1, 1],
        [1, 1],
    ]
    result3 = pacific_atlantic(heights3)
    print(f"\nExample 3 (flat): {result3}")  # Output: [[0,0],[0,1],[1,0],[1,1]]

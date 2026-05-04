"""
Largest Region in Boolean Matrix

Problem:
Given a binary 2D matrix, find the area (number of cells) of the largest region of 1s.
Cells are considered connected if they are adjacent horizontally, vertically, or diagonally.

Algorithm: BFS on each unvisited cell with value 1
- Traverse the matrix; when a 1 is found, start BFS to explore the entire region
- Count the number of cells in each region
- Return the maximum region size

Time Complexity: O(rows * cols)
Space Complexity: O(rows * cols) for visited array, or O(rows + cols) if modifying input
"""

from collections import deque


def largest_region(matrix: list[list[int]]) -> int:
    """
    Find the area of the largest region of 1s in a boolean matrix.

    Args:
        matrix: 2D binary matrix

    Returns:
        Area of the largest connected region of 1s
    """
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    max_area = 0

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

    def bfs(start_r: int, start_c: int) -> int:
        """Perform BFS to count the size of the connected region."""
        area = 0
        queue = deque()
        queue.append((start_r, start_c))
        matrix[start_r][start_c] = 0  # Mark as visited by setting to 0

        while queue:
            r, c = queue.popleft()
            area += 1

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] == 1:
                    matrix[nr][nc] = 0  # Mark as visited
                    queue.append((nr, nc))

        return area

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1:
                area = bfs(r, c)
                max_area = max(max_area, area)

    return max_area


def largest_region_with_visited(matrix: list[list[int]]) -> int:
    """
    Find largest region without modifying the input matrix.

    Args:
        matrix: 2D binary matrix

    Returns:
        Area of the largest connected region of 1s
    """
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    visited = [[False] * cols for _ in range(rows)]
    max_area = 0

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

    def bfs(start_r: int, start_c: int) -> int:
        area = 0
        queue = deque()
        queue.append((start_r, start_c))
        visited[start_r][start_c] = True

        while queue:
            r, c = queue.popleft()
            area += 1

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if matrix[nr][nc] == 1 and not visited[nr][nc]:
                        visited[nr][nc] = True
                        queue.append((nr, nc))

        return area

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1 and not visited[r][c]:
                area = bfs(r, c)
                max_area = max(max_area, area)

    return max_area


if __name__ == "__main__":
    # Example 1
    matrix1 = [
        [0, 0, 1, 1, 0],
        [1, 0, 1, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1],
    ]
    result1 = largest_region([row[:] for row in matrix1])
    print(f"Example 1: {result1}")  # Output: 6

    # Example 2
    matrix2 = [
        [1, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 1],
        [0, 0, 1, 1],
    ]
    result2 = largest_region([row[:] for row in matrix2])
    print(f"Example 2: {result2}")  # Output: 4

    # Example 3
    matrix3 = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
    ]
    result3 = largest_region([row[:] for row in matrix3])
    print(f"Example 3: {result3}")  # Output: 3 (diagonally connected)

    # Example 4
    matrix4 = [
        [0, 0, 0],
        [0, 0, 0],
    ]
    result4 = largest_region([row[:] for row in matrix4])
    print(f"Example 4: {result4}")  # Output: 0

    # Example 5: Using non-modifying version
    matrix5 = [
        [1, 1, 1, 1, 0],
        [1, 0, 0, 1, 0],
        [1, 0, 0, 0, 1],
        [0, 1, 1, 1, 1],
    ]
    result5 = largest_region_with_visited(matrix5)
    print(f"Example 5: {result5}")  # Output: 8

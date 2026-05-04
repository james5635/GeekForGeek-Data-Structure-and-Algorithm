"""
Flood Fill Algorithm

Problem:
Given a 2D image (grid of integers), a starting pixel (sr, sc), and a new color.
Replace the color of the starting pixel and all connected pixels with the same
original color with the new color.

Connectivity: 4-directional (up, down, left, right)

Algorithm: BFS from starting pixel
- Get the original color of starting pixel
- BFS to all adjacent pixels with the same color
- Change their color to the new color

Time Complexity: O(rows * cols)
Space Complexity: O(rows * cols)
"""

from collections import deque


def flood_fill(
    image: list[list[int]], sr: int, sc: int, new_color: int
) -> list[list[int]]:
    """
    Perform flood fill on an image starting from (sr, sc).

    Args:
        image: 2D grid of pixel colors (integers)
        sr: Starting row
        sc: Starting column
        new_color: The new color to fill

    Returns:
        Modified image after flood fill
    """
    if not image or not image[0]:
        return image

    rows, cols = len(image), len(image[0])
    original_color = image[sr][sc]

    # If the new color is the same as original, no changes needed
    if original_color == new_color:
        return image

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    queue = deque()
    queue.append((sr, sc))
    image[sr][sc] = new_color

    while queue:
        r, c = queue.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == original_color:
                image[nr][nc] = new_color
                queue.append((nr, nc))

    return image


if __name__ == "__main__":
    # Example 1
    image1 = [
        [1, 1, 1],
        [1, 1, 0],
        [1, 0, 1],
    ]
    result1 = flood_fill([row[:] for row in image1], 1, 1, 2)
    print("Example 1 (fill from center with color 2):")
    for row in result1:
        print(row)
    # Expected: [[2,2,2],[2,2,0],[2,0,1]]

    # Example 2
    image2 = [
        [0, 0, 0],
        [0, 1, 1],
    ]
    result2 = flood_fill([row[:] for row in image2], 1, 1, 1)
    print("\nExample 2 (same color, no change):")
    for row in result2:
        print(row)
    # Expected: [[0,0,0],[0,1,1]]

    # Example 3
    image3 = [
        [1, 2, 3],
        [4, 1, 5],
        [1, 6, 1],
    ]
    result3 = flood_fill([row[:] for row in image3], 0, 0, 9)
    print("\nExample 3 (fill corner with color 9):")
    for row in result3:
        print(row)
    # Expected: [[9,2,3],[4,9,5],[9,6,1]]

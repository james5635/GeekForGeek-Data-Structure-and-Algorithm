from collections import deque


def shortestPathBinaryMaze(grid, src, dest):
    """
    Find the shortest path in a binary maze from source to destination.
    The maze contains 0s (blocked) and 1s (open).
    Args:
        grid: 2D list representing the maze (0 = blocked, 1 = open)
        src: Tuple (source_row, source_col)
        dest: Tuple (dest_row, dest_col)
    Returns:
        Length of the shortest path, or -1 if no path exists
    """
    if not grid or not grid[0]:
        return -1

    rows = len(grid)
    cols = len(grid[0])

    # Check if source or destination is blocked
    if grid[src[0]][src[1]] == 0 or grid[dest[0]][dest[1]] == 0:
        return -1

    # If source and destination are the same
    if src == dest:
        return 0

    # Directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Queue for BFS: (row, col, distance)
    queue = deque([(src[0], src[1], 0)])

    # Visited matrix
    visited = [[False] * cols for _ in range(rows)]
    visited[src[0]][src[1]] = True

    while queue:
        row, col, dist = queue.popleft()

        # Check all 4 directions
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            # Check if new position is valid
            if (
                0 <= new_row < rows
                and 0 <= new_col < cols
                and not visited[new_row][new_col]
                and grid[new_row][new_col] == 1
            ):
                # If we reached destination
                if (new_row, new_col) == dest:
                    return dist + 1

                visited[new_row][new_col] = True
                queue.append((new_row, new_col, dist + 1))

    # No path found
    return -1


def test_shortestPathBinaryMaze():
    # Test case 1
    grid1 = [
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 0, 0, 0, 0, 1, 0, 0, 1],
    ]
    src1 = (0, 0)
    dest1 = (3, 4)
    print(f"Test 1 - Maze:")
    for row in grid1:
        print(row)
    print(f"Source: {src1}, Destination: {dest1}")
    result1 = shortestPathBinaryMaze(grid1, src1, dest1)
    print(f"Shortest path length: {result1}")
    print(f"Expected: 11")
    print()

    # Test case 2 - No path
    grid2 = [[1, 0, 0], [0, 0, 0], [0, 0, 1]]
    src2 = (0, 0)
    dest2 = (2, 2)
    print(f"Test 2 - Maze:")
    for row in grid2:
        print(row)
    print(f"Source: {src2}, Destination: {dest2}")
    result2 = shortestPathBinaryMaze(grid2, src2, dest2)
    print(f"Shortest path length: {result2}")
    print(f"Expected: -1 (no path)")
    print()

    # Test case 3 - Simple path
    grid3 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    src3 = (0, 0)
    dest3 = (2, 2)
    print(f"Test 3 - Maze:")
    for row in grid3:
        print(row)
    print(f"Source: {src3}, Destination: {dest3}")
    result3 = shortestPathBinaryMaze(grid3, src3, dest3)
    print(f"Shortest path length: {result3}")
    print(f"Expected: 4")
    print()


if __name__ == "__main__":
    test_shortestPathBinaryMaze()

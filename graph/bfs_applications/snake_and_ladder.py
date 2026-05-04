"""
Snake and Ladder Problem - Minimum Dice Throws

Problem:
Given a snake and ladder board (6x6 grid), find the minimum number of dice throws
required to reach the last cell (cell 36) from cell 1.

The board is represented by an array where:
- If board[i] = -1, cell i has no snake or ladder
- If board[i] = x, cell i has a snake/ladder that takes you to cell x
  - If x > i, it's a ladder (go up)
  - If x < i, it's a snake (go down)

Algorithm: BFS
- Treat each cell as a node
- From each cell, there are edges to the next 6 cells (dice roll 1-6)
- If a cell has a snake/ladder, follow it immediately
- BFS finds the shortest path (minimum dice throws)

Time Complexity: O(N) where N is the number of cells
Space Complexity: O(N)
"""

from collections import deque


def min_dice_throws(board: list[int], n: int) -> int:
    """
    Find the minimum number of dice throws to reach cell n*n from cell 1.

    Args:
        board: Array of size n*n where board[i] = -1 or destination cell
               Index 0 represents cell 1, index n*n-1 represents cell n*n
        n: Size of the board (n x n)

    Returns:
        Minimum number of dice throws to reach the destination
    """
    total_cells = n * n
    visited = [False] * total_cells
    queue = deque()

    # Start from cell 1 (index 0)
    queue.append((0, 0))  # (current_cell_index, dice_throws)
    visited[0] = True

    while queue:
        curr_idx, throws = queue.popleft()

        # If we reached the last cell
        if curr_idx == total_cells - 1:
            return throws

        # Try all 6 possible dice outcomes
        for dice in range(1, 7):
            next_idx = curr_idx + dice

            if next_idx >= total_cells:
                break

            if not visited[next_idx]:
                visited[next_idx] = True

                # Check if there's a snake or ladder
                if board[next_idx] != -1:
                    dest_idx = board[next_idx] - 1  # Convert to 0-indexed
                    if not visited[dest_idx]:
                        visited[dest_idx] = True
                        queue.append((dest_idx, throws + 1))
                else:
                    queue.append((next_idx, throws + 1))

    return -1  # Should not reach here for valid boards


def min_dice_throws_with_path(board: list[int], n: int) -> tuple[int, list[int]]:
    """
    Find the minimum dice throws and return the path taken.

    Args:
        board: Array where board[i] = -1 or destination cell (1-indexed)
        n: Board size

    Returns:
        Tuple of (throws, path) where path shows cells visited
    """
    total_cells = n * n
    visited = [False] * total_cells
    parent = [-1] * total_cells
    queue = deque()

    queue.append(0)
    visited[0] = True

    while queue:
        curr_idx = queue.popleft()

        if curr_idx == total_cells - 1:
            # Reconstruct path
            path = []
            idx = curr_idx
            while idx != -1:
                path.append(idx + 1)  # Convert to 1-indexed
                idx = parent[idx]
            path.reverse()

            # Count throws
            throws = 0
            for i in range(1, len(path)):
                if board[path[i - 1] - 1] == -1:
                    throws += 1
            return throws, path

        for dice in range(1, 7):
            next_idx = curr_idx + dice

            if next_idx >= total_cells:
                break

            if not visited[next_idx]:
                visited[next_idx] = True
                parent[next_idx] = curr_idx

                if board[next_idx] != -1:
                    dest_idx = board[next_idx] - 1
                    if not visited[dest_idx]:
                        visited[dest_idx] = True
                        parent[dest_idx] = next_idx
                        queue.append(dest_idx)
                else:
                    queue.append(next_idx)

    return -1, []


if __name__ == "__main__":
    # Example: 6x6 board
    # Cells are 1-indexed, so board[i] corresponds to cell i+1
    # -1 means no snake/ladder
    # A value like 30 at index 1 means cell 2 has a ladder to cell 30
    board = [
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,  # cells 1-6
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,  # cells 7-12
        -1,
        30,
        -1,
        -1,
        -1,
        -1,  # cell 8 has ladder to 30
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,  # cells 19-24
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,  # cells 25-30
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,  # cells 31-36
    ]

    throws = min_dice_throws(board, 6)
    print(f"Minimum dice throws (6x6 board with ladder): {throws}")

    # Example 2: Board with snakes and ladders
    board2 = [
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,  # cells 1-6
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,  # cells 7-12
        -1,
        30,
        -1,
        -1,
        -1,
        -1,  # cell 8: ladder to 30
        -1,
        4,
        -1,
        -1,
        -1,
        -1,  # cell 20: ladder to 4 (not useful)
        -1,
        -1,
        15,
        -1,
        -1,
        -1,  # cell 27: snake to 15
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,  # cells 31-36
    ]

    throws2 = min_dice_throws(board2, 6)
    print(f"Minimum dice throws (with snake): {throws2}")

    # Example 3: Small 3x3 board
    board3 = [-1, -1, 8, -1, -1, -1, -1, 4, -1]  # cell 3->ladder 8, cell 8->snake 4
    throws3, path3 = min_dice_throws_with_path(board3, 3)
    print(f"3x3 board: {throws3} throws, path: {path3}")

"""
The Knight's Tour Problem
https://www.geeksforgeeks.org/dsa/the-knights-tour-problem/

Given an integer n, consider an n × n chessboard. A Knight starts at the top-left corner (0, 0)
and must visit every cell exactly once following the Knight's standard moves in chess.

Approach: Warnsdorff's Algorithm with Backtracking
Time Complexity: O(n^3)
Auxiliary Space: O(n^2)
"""

# Define 8 knight moves globally
dir = [[2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [-1, -2], [1, -2], [2, -1]]


def count_options(board, x, y):
    """
    Count the number of onward moves from position (x, y).
    Used by Warnsdorff's heuristic.

    Args:
        board: The chessboard
        x: Current x position
        y: Current y position

    Returns:
        Number of valid moves from this position
    """
    count = 0
    n = len(board)

    for dx, dy in dir:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == -1:
            count += 1

    return count


def get_sorted_moves(board, x, y):
    """
    Generate valid knight moves from (x, y), sorted by fewest onward moves.
    This implements Warnsdorff's heuristic for better performance.

    Args:
        board: The chessboard
        x: Current x position
        y: Current y position

    Returns:
        List of moves sorted by accessibility (fewest onward moves first)
    """
    move_list = []
    n = len(board)

    for i in range(8):
        nx, ny = x + dir[i][0], y + dir[i][1]
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == -1:
            options = count_options(board, nx, ny)
            move_list.append([options, i])

    move_list.sort()
    return move_list


def knight_tour_util(x, y, step, n, board):
    """
    Recursive function to solve the Knight's Tour.

    Args:
        x: Current x position
        y: Current y position
        step: Current step number
        n: Board size
        board: The chessboard

    Returns:
        True if tour is complete, False otherwise
    """
    if step == n * n:
        return True

    moves = get_sorted_moves(board, x, y)

    for move in moves:
        dir_idx = move[1]
        nx, ny = x + dir[dir_idx][0], y + dir[dir_idx][1]

        board[nx][ny] = step

        if knight_tour_util(nx, ny, step + 1, n, board):
            return True

        # Backtrack
        board[nx][ny] = -1

    return False


def knight_tour(n):
    """
    Find a Knight's Tour on an n x n board.

    Args:
        n: Board size

    Returns:
        n x n board with step numbers, or [[-1]] if no solution exists
    """
    board = [[-1] * n for _ in range(n)]
    board[0][0] = 0  # Start from top-left corner

    if knight_tour_util(0, 0, 1, n, board):
        return board

    return [[-1]]


def print_tour(board):
    """
    Helper function to print the knight's tour.
    """
    if board == [[-1]]:
        print("No solution exists")
        return

    n = len(board)
    # Find the maximum number width for formatting
    max_num = n * n - 1
    width = len(str(max_num))

    for row in board:
        print(" ".join(str(val).rjust(width) for val in row))


def main():
    """
    Main function to demonstrate the algorithm.
    """
    # Test case 1: n = 5
    print("Test Case 1: n = 5")
    print("-" * 30)
    n = 5
    result = knight_tour(n)
    print("Knight's Tour:")
    print_tour(result)
    print()

    # Test case 2: n = 3 (no solution)
    print("Test Case 2: n = 3")
    print("-" * 30)
    n = 3
    result = knight_tour(n)
    print("Knight's Tour:")
    print_tour(result)
    print()

    # Test case 3: n = 6
    print("Test Case 3: n = 6")
    print("-" * 30)
    n = 6
    result = knight_tour(n)
    print("Knight's Tour:")
    print_tour(result)
    print()

    # Test case 4: n = 8
    print("Test Case 4: n = 8")
    print("-" * 30)
    n = 8
    result = knight_tour(n)
    print("Knight's Tour:")
    print_tour(result)


if __name__ == "__main__":
    main()

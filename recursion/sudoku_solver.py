"""
Sudoku Solver
https://www.geeksforgeeks.org/dsa/sudoku-backtracking-7/

Given an incomplete Sudoku in the form of matrix mat[][] of order 9*9, complete the Sudoku.

Approach: Backtracking
Time Complexity: O(9^(n*n))
Auxiliary Space: O(1)
"""


def is_safe(mat, row, col, num):
    """
    Check if it is safe to place num at mat[row][col].

    Args:
        mat: The Sudoku board
        row: Row index
        col: Column index
        num: Number to place (1-9)

    Returns:
        True if safe to place, False otherwise
    """
    # Check if num exists in the row
    for x in range(9):
        if mat[row][x] == num:
            return False

    # Check if num exists in the column
    for x in range(9):
        if mat[x][col] == num:
            return False

    # Check if num exists in the 3x3 sub-matrix
    start_row = row - (row % 3)
    start_col = col - (col % 3)

    for i in range(3):
        for j in range(3):
            if mat[i + start_row][j + start_col] == num:
                return False

    return True


def solve_sudoku_rec(mat, row, col):
    """
    Recursive function to solve the Sudoku.

    Args:
        mat: The Sudoku board
        row: Current row index
        col: Current column index

    Returns:
        True if solution exists, False otherwise
    """
    # Base case: Reached last column of last row
    if row == 8 and col == 9:
        return True

    # If last column of the row, go to next row
    if col == 9:
        row += 1
        col = 0

    # If cell is already occupied, move forward
    if mat[row][col] != 0:
        return solve_sudoku_rec(mat, row, col + 1)

    for num in range(1, 10):
        # If it is safe to place num at current position
        if is_safe(mat, row, col, num):
            mat[row][col] = num

            if solve_sudoku_rec(mat, row, col + 1):
                return True

            # Backtrack
            mat[row][col] = 0

    return False


def solve_sudoku(mat):
    """
    Solve the Sudoku puzzle.

    Args:
        mat: 9x9 Sudoku board with 0 representing empty cells

    Returns:
        True if solution exists (board is modified in place), False otherwise
    """
    return solve_sudoku_rec(mat, 0, 0)


def print_board(mat):
    """
    Helper function to print the Sudoku board.
    """
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            print(mat[i][j], end=" ")
        print()


def main():
    """
    Main function to demonstrate the algorithm.
    """
    # Test case
    print("Sudoku Solver")
    print("=" * 40)

    mat = [
        [3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0],
    ]

    print("Original Sudoku:")
    print_board(mat)
    print()

    if solve_sudoku(mat):
        print("Solved Sudoku:")
        print_board(mat)
    else:
        print("No solution exists!")

    print()
    print("=" * 40)

    # Additional test: Verify solution
    print("Verification:")
    print(
        "- Each row contains 1-9: ", all(set(row) == set(range(1, 10)) for row in mat)
    )
    cols_valid = all(
        set(mat[i][j] for i in range(9)) == set(range(1, 10)) for j in range(9)
    )
    print(f"- Each column contains 1-9: {cols_valid}")


if __name__ == "__main__":
    main()

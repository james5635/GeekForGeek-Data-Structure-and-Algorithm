import random


def is_valid(board, row, col, num):
    """
    Check if it's valid to place num at board[row][col]
    Args:
        board: 9x9 Sudoku board
        row: Row index (0-8)
        col: Column index (0-8)
        num: Number to place (1-9)
    Returns:
        Boolean indicating if placement is valid
    """
    # Check row
    for x in range(9):
        if board[row][x] == num:
            return False

    # Check column
    for x in range(9):
        if board[x][col] == num:
            return False

    # Check 3x3 sub-grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False

    return True


def solve_sudoku(board):
    """
    Solve Sudoku using backtracking
    Args:
        board: 9x9 Sudoku board (0 represents empty cell)
    Returns:
        Boolean indicating if Sudoku was solved
    """
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                # Try numbers 1-9 in random order for variety
                numbers = list(range(1, 10))
                random.shuffle(numbers)
                for num in numbers:
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0  # Backtrack
                return False  # Trigger backtracking
    return True  # Sudoku solved


def generate_sudoku(difficulty=0.5):
    """
    Generate a Sudoku puzzle
    Args:
        difficulty: Float between 0 and 1 indicating difficulty level
                   (0 = easy, 1 = hard)
    Returns:
        9x9 Sudoku puzzle with some cells empty
    """
    # Start with an empty board
    board = [[0 for _ in range(9)] for _ in range(9)]

    # Fill the diagonal 3x3 matrices first (they don't interfere with each other)
    for i in range(0, 9, 3):
        fill_box(board, i, i)

    # Solve the remaining board
    solve_sudoku(board)

    # Remove numbers based on difficulty
    cells = 81
    removals = int(cells * difficulty)

    # Remove random cells
    positions = random.sample(range(81), removals)
    for pos in positions:
        row, col = pos // 9, pos % 9
        board[row][col] = 0

    return board


def fill_box(board, row_start, col_start):
    """
    Fill a 3x3 box with random numbers
    Args:
        board: 9x9 Sudoku board
        row_start: Starting row of the 3x3 box
        col_start: Starting column of the 3x3 box
    """
    nums = list(range(1, 10))
    random.shuffle(nums)
    for i in range(3):
        for j in range(3):
            board[row_start + i][col_start + j] = nums.pop()


def print_sudoku(board):
    """Print Sudoku board in a readable format"""
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")
    print()


def test_sudoku_generator():
    print("Testing Sudoku Generator:")
    print("=" * 30)

    # Generate different difficulty levels
    for diff_name, diff_val in [("Easy", 0.3), ("Medium", 0.5), ("Hard", 0.7)]:
        print(f"\n{diff_name} Sudoku:")
        puzzle = generate_sudoku(diff_val)
        print_sudoku(puzzle)

        # Verify it has the right number of empty cells
        empty_count = sum(1 for i in range(9) for j in range(9) if puzzle[i][j] == 0)
        expected_empty = int(81 * diff_val)
        print(f"Empty cells: {empty_count} (expected ~{expected_empty})")


if __name__ == "__main__":
    test_sudoku_generator()

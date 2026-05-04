def solve_n_queen(n: int) -> list[list[int]] | None:
    """Solve N Queen problem and return board with queens placed (1 = queen)."""
    board = [[0] * n for _ in range(n)]

    def is_safe(row: int, col: int) -> bool:
        for i in range(col):
            if board[row][i] == 1:
                return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        for i, j in zip(range(row, n), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        return True

    def solve(col: int) -> bool:
        if col >= n:
            return True
        for row in range(n):
            if is_safe(row, col):
                board[row][col] = 1
                if solve(col + 1):
                    return True
                board[row][col] = 0
        return False

    if solve(0):
        return board
    return None


if __name__ == "__main__":
    n = 8
    board = solve_n_queen(n)
    if board:
        for row in board:
            print(" ".join("Q" if cell else "." for cell in row))
    else:
        print("No solution found")

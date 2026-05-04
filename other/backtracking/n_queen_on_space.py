def solve_n_queen_space(n: int) -> list[list[int]] | None:
    """Solve N Queen problem in O(n) space using arrays instead of board."""
    queens = [-1] * n

    def is_safe(row: int, col: int) -> bool:
        for r in range(row):
            c = queens[r]
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True

    def solve(row: int) -> bool:
        if row == n:
            return True
        for col in range(n):
            if is_safe(row, col):
                queens[row] = col
                if solve(row + 1):
                    return True
                queens[row] = -1
        return False

    if solve(0):
        board = [[0] * n for _ in range(n)]
        for r in range(n):
            board[r][queens[r]] = 1
        return board
    return None


if __name__ == "__main__":
    n = 8
    board = solve_n_queen_space(n)
    if board:
        for row in board:
            print(" ".join("Q" if cell else "." for cell in row))
    else:
        print("No solution found")

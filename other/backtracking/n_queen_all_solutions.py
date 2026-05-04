def solve_n_queen_all(n: int) -> list[list[list[int]]]:
    """Print all solutions of N-Queen problem."""
    boards: list[list[list[int]]] = []
    queens = [-1] * n

    def is_safe(row: int, col: int) -> bool:
        for r in range(row):
            c = queens[r]
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True

    def solve(row: int) -> None:
        if row == n:
            board = [[0] * n for _ in range(n)]
            for r in range(n):
                board[r][queens[r]] = 1
            boards.append(board)
            return
        for col in range(n):
            if is_safe(row, col):
                queens[row] = col
                solve(row + 1)
                queens[row] = -1

    solve(0)
    return boards


if __name__ == "__main__":
    n = 4
    all_solutions = solve_n_queen_all(n)
    print(f"Found {len(all_solutions)} solutions:")
    for i, board in enumerate(all_solutions):
        print(f"\nSolution {i + 1}:")
        for row in board:
            print(" ".join("Q" if cell else "." for cell in row))

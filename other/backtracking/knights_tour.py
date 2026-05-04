def solve_knights_tour(n: int) -> list[list[int]] | None:
    """Solve the Knight's Tour problem and return the board with move numbers."""
    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

    def is_valid(x: int, y: int, board: list[list[int]]) -> bool:
        return 0 <= x < n and 0 <= y < n and board[x][y] == -1

    def solve_util(board: list[list[int]], x: int, y: int, pos: int) -> bool:
        if pos == n * n:
            return True
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, board):
                board[nx][ny] = pos
                if solve_util(board, nx, ny, pos + 1):
                    return True
                board[nx][ny] = -1
        return False

    board = [[-1] * n for _ in range(n)]
    board[0][0] = 0
    if solve_util(board, 0, 0, 1):
        return board
    return None


if __name__ == "__main__":
    n = 5
    board = solve_knights_tour(n)
    if board:
        for row in board:
            print(" ".join(f"{cell:2d}" for cell in row))
    else:
        print("No solution found")

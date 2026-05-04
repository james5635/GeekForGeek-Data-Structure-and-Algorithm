def knights_tour_warnsdorff(n: int) -> list[list[int]] | None:
    """Solve Knight's Tour using Warnsdorff's algorithm (heuristic approach)."""
    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

    def is_valid(x: int, y: int, board: list[list[int]]) -> bool:
        return 0 <= x < n and 0 <= y < n and board[x][y] == -1

    def get_degree(x: int, y: int, board: list[list[int]]) -> int:
        count = 0
        for dx, dy in moves:
            if is_valid(x + dx, y + dy, board):
                count += 1
        return count

    def solve() -> list[list[int]] | None:
        board = [[-1] * n for _ in range(n)]
        x, y = 0, 0
        board[x][y] = 0
        for _ in range(1, n * n):
            candidates = []
            for dx, dy in moves:
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny, board):
                    degree = get_degree(nx, ny, board)
                    candidates.append((degree, nx, ny))
            if not candidates:
                return None
            candidates.sort()
            _, x, y = candidates[0]
            board[x][y] = _
        return board

    return solve()


if __name__ == "__main__":
    n = 8
    board = knights_tour_warnsdorff(n)
    if board:
        for row in board:
            print(" ".join(f"{cell:2d}" for cell in row))
    else:
        print("No solution found")

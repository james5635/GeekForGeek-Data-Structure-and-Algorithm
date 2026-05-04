def solve_magnet_puzzle(
    top: list[str],
    bottom: list[str],
    left: list[str],
    right: list[str],
    rows: int,
    cols: int,
) -> list[list[str]] | None:
    """Solve the Magnet Puzzle. + and - represent magnetic poles."""
    board = [[" " for _ in range(cols)] for _ in range(rows)]

    def is_valid(r: int, c: int, pole: str) -> bool:
        if pole == "+":
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if board[nr][nc] == "+":
                        return False
        if c < cols - 1 and board[r][c + 1] != " " and board[r][c + 1] == pole:
            return False
        if c > 0 and board[r][c - 1] != " " and board[r][c - 1] == pole:
            return False
        if r < rows - 1 and board[r + 1][c] != " " and board[r + 1][c] == pole:
            return False
        if r > 0 and board[r - 1][c] != " " and board[r - 1][c] == pole:
            return False
        return True

    def check_constraints() -> bool:
        for r in range(rows):
            if left[r] != "X":
                count = sum(1 for c in range(cols) if board[r][c] == left[r])
                if count > int(left[r]):
                    return False
            if right[r] != "X":
                count = sum(1 for c in range(cols) if board[r][c] == right[r])
                if count > int(right[r]):
                    return False
        for c in range(cols):
            if top[c] != "X":
                count = sum(1 for r in range(rows) if board[r][c] == top[c])
                if count > int(top[c]):
                    return False
            if bottom[c] != "X":
                count = sum(1 for r in range(rows) if board[r][c] == bottom[c])
                if count > int(bottom[c]):
                    return False
        return True

    def solve(idx: int) -> bool:
        if idx == rows * cols:
            return check_constraints()
        r, c = divmod(idx, cols)
        for pole in ["+", "-"]:
            if is_valid(r, c, pole):
                board[r][c] = pole
                if check_constraints() and solve(idx + 1):
                    return True
                board[r][c] = " "
        return False

    if solve(0):
        return board
    return None


if __name__ == "__main__":
    top = ["+", "-", "+", "-"]
    bottom = ["-", "+", "-", "+"]
    left = ["1", "2", "2", "1"]
    right = ["2", "1", "1", "2"]
    rows, cols = 4, 4
    board = solve_magnet_puzzle(top, bottom, left, right, rows, cols)
    if board:
        for row in board:
            print(row)
    else:
        print("No solution found")

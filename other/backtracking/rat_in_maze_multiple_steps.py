def solve_rat_in_maze_multiple_steps(maze: list[list[int]]) -> list[list[int]] | None:
    """Solve Rat in a Maze with multiple steps (jump allowed based on cell value)."""
    n = len(maze)
    solution = [[0] * n for _ in range(n)]

    def is_valid(r: int, c: int) -> bool:
        return 0 <= r < n and 0 <= c < n and maze[r][c] > 0 and solution[r][c] == 0

    def solve(r: int, c: int) -> bool:
        if r == n - 1 and c == n - 1:
            solution[r][c] = 1
            return True
        if is_valid(r, c):
            solution[r][c] = 1
            steps = maze[r][c]
            for dr, dc in [(0, steps), (steps, 0), (0, -steps), (-steps, 0)]:
                nr, nc = r + dr, c + dc
                if is_valid(nr, nc):
                    if solve(nr, nc):
                        return True
            solution[r][c] = 0
            return False
        return False

    if solve(0, 0):
        return solution
    return None


if __name__ == "__main__":
    maze = [
        [2, 1, 0, 0],
        [3, 0, 0, 1],
        [0, 1, 0, 1],
        [0, 0, 2, 1],
    ]
    result = solve_rat_in_maze_multiple_steps(maze)
    if result:
        for row in result:
            print(row)
    else:
        print("No path found")

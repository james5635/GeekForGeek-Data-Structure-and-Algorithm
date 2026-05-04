def solve_rat_in_maze(maze: list[list[int]]) -> list[list[int]] | None:
    """Solve Rat in a Maze problem and return the solution path matrix."""
    n = len(maze)
    solution = [[0] * n for _ in range(n)]

    def is_valid(x: int, y: int) -> bool:
        return 0 <= x < n and 0 <= y < n and maze[x][y] == 1 and solution[x][y] == 0

    def solve(x: int, y: int) -> bool:
        if x == n - 1 and y == n - 1 and maze[x][y] == 1:
            solution[x][y] = 1
            return True
        if is_valid(x, y):
            solution[x][y] = 1
            for dx, dy in [(0, 1), (1, 0)]:
                if solve(x + dx, y + dy):
                    return True
            solution[x][y] = 0
            return False
        return False

    if solve(0, 0):
        return solution
    return None


if __name__ == "__main__":
    maze = [
        [1, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 1, 0, 0],
        [1, 1, 1, 1],
    ]
    result = solve_rat_in_maze(maze)
    if result:
        for row in result:
            print(row)
    else:
        print("No path found")

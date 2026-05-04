import random


def generate_random_acyclic_maze(rows: int, cols: int) -> list[list[int]]:
    """Generate a random acyclic maze using randomized DFS.

    Returns a 2D grid where 0 = wall, 1 = path.
    """
    maze = [[0] * cols for _ in range(rows)]

    def carve(r: int, c: int) -> None:
        maze[r][c] = 1
        directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
        random.shuffle(directions)

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0:
                maze[r + dr // 2][c + dc // 2] = 1
                carve(nr, nc)

    start_r, start_c = 1, 1
    maze[start_r][start_c] = 0
    carve(start_r, start_c)
    maze[start_r][start_c] = 1

    return maze


def print_maze(maze: list[list[int]]) -> None:
    """Print maze with visual representation."""
    symbols = {0: "#", 1: " "}
    for row in maze:
        print("".join(symbols[cell] for cell in row))


if __name__ == "__main__":
    random.seed(42)
    rows, cols = 11, 21
    maze = generate_random_acyclic_maze(rows, cols)
    print(f"Maze ({rows}x{cols}):")
    print_maze(maze)

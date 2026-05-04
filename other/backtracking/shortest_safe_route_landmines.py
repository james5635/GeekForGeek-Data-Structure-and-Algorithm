def shortest_safe_route(field: list[list[int]]) -> int:
    """Find shortest safe route in a field with landmines. Cells adjacent to landmines are unsafe."""
    rows, cols = len(field), len(field[0])
    LANDMINE = 0
    unsafe = set()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for r in range(rows):
        for c in range(cols):
            if field[r][c] == LANDMINE:
                unsafe.add((r, c))
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        unsafe.add((nr, nc))

    shortest = float("inf")

    def dfs(r: int, c: int, dist: int, visited: set[tuple[int, int]]) -> None:
        nonlocal shortest
        if c == cols - 1 and (r, c) not in unsafe:
            shortest = min(shortest, dist)
            return
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (
                0 <= nr < rows
                and 0 <= nc < cols
                and (nr, nc) not in unsafe
                and (nr, nc) not in visited
            ):
                visited.add((nr, nc))
                dfs(nr, nc, dist + 1, visited)
                visited.remove((nr, nc))

    for r in range(rows):
        if (r, 0) not in unsafe:
            dfs(r, 0, 1, {(r, 0)})

    return shortest if shortest != float("inf") else -1


if __name__ == "__main__":
    field = [
        [1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1],
    ]
    route = shortest_safe_route(field)
    print(f"Shortest safe route length: {route}")

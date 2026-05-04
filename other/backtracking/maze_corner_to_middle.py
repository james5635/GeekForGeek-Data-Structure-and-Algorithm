def find_paths_corner_to_middle(n: int) -> list[list[tuple[int, int]]]:
    """Find all paths from corner cell (0,0) to middle cell in an n x n maze."""
    mid = n // 2
    paths: list[list[tuple[int, int]]] = []

    def is_valid(r: int, c: int, visited: set[tuple[int, int]]) -> bool:
        return 0 <= r < n and 0 <= c < n and (r, c) not in visited

    def dfs(
        r: int, c: int, path: list[tuple[int, int]], visited: set[tuple[int, int]]
    ) -> None:
        if r == mid and c == mid:
            paths.append(path[:])
            return
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if is_valid(nr, nc, visited):
                visited.add((nr, nc))
                path.append((nr, nc))
                dfs(nr, nc, path, visited)
                path.pop()
                visited.remove((nr, nc))

    visited = {(0, 0)}
    dfs(0, 0, [(0, 0)], visited)
    return paths


if __name__ == "__main__":
    n = 3
    paths = find_paths_corner_to_middle(n)
    print(f"Found {len(paths)} paths from corner to middle:")
    for i, p in enumerate(paths):
        print(f"Path {i + 1}: {p}")

def longest_route_matrix_hurdles(matrix: list[list[int]]) -> int:
    """Find longest possible route in a matrix with hurdles (0 = blocked, 1 = free)."""
    rows, cols = len(matrix), len(matrix[0])
    longest = 0

    def is_valid(r: int, c: int, visited: set[tuple[int, int]]) -> bool:
        return (
            0 <= r < rows
            and 0 <= c < cols
            and matrix[r][c] == 1
            and (r, c) not in visited
        )

    def dfs(r: int, c: int, dist: int, visited: set[tuple[int, int]]) -> None:
        nonlocal longest
        if r == rows - 1 and c == cols - 1:
            longest = max(longest, dist)
            return
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if is_valid(nr, nc, visited):
                visited.add((nr, nc))
                dfs(nr, nc, dist + 1, visited)
                visited.remove((nr, nc))

    if matrix[0][0] == 1:
        dfs(0, 0, 0, {(0, 0)})
    return longest


if __name__ == "__main__":
    matrix = [
        [1, 1, 1, 1],
        [1, 1, 0, 1],
        [1, 1, 1, 1],
        [1, 0, 1, 1],
    ]
    length = longest_route_matrix_hurdles(matrix)
    print(f"Longest route length: {length}")

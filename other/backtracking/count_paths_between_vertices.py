def count_paths(graph: list[list[int]], src: int, dest: int, k: int) -> int:
    """Count possible paths of exactly length k between two vertices."""

    def dfs(current: int, steps: int) -> int:
        if steps == k:
            return 1 if current == dest else 0
        count = 0
        for neighbor, connected in enumerate(graph[current]):
            if connected:
                count += dfs(neighbor, steps + 1)
        return count

    return dfs(src, 0)


if __name__ == "__main__":
    graph = [
        [0, 1, 1, 1],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [1, 1, 1, 0],
    ]
    src, dest, k = 0, 3, 2
    paths = count_paths(graph, src, dest, k)
    print(f"Paths from {src} to {dest} with length {k}: {paths}")

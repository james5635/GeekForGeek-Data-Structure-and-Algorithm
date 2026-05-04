def path_more_than_k_length(
    graph: list[list[tuple[int, int]]], src: int, k: int
) -> bool:
    """Find if there is a path of more than k length from source."""
    n = len(graph)
    visited = [False] * n

    def dfs(v: int, dist: int) -> bool:
        if dist > k:
            return True
        visited[v] = True
        for neighbor, weight in graph[v]:
            if not visited[neighbor]:
                if dfs(neighbor, dist + weight):
                    return True
        visited[v] = False
        return False

    return dfs(src, 0)


if __name__ == "__main__":
    graph = [
        [(1, 10), (2, 5)],
        [(0, 10), (2, 15), (3, 8)],
        [(0, 5), (1, 15), (3, 2)],
        [(1, 8), (2, 2)],
    ]
    src = 0
    k = 15
    print(f"Path > {k} exists: {path_more_than_k_length(graph, src, k)}")
    k = 25
    print(f"Path > {k} exists: {path_more_than_k_length(graph, src, k)}")

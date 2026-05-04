def find_all_paths(graph: list[list[int]], src: int, dest: int) -> list[list[int]]:
    """Find all paths from source to destination in a graph."""
    paths: list[list[int]] = []

    def dfs(v: int, visited: list[bool], path: list[int]) -> None:
        visited[v] = True
        path.append(v)
        if v == dest:
            paths.append(path[:])
        else:
            for neighbor, connected in enumerate(graph[v]):
                if connected and not visited[neighbor]:
                    dfs(neighbor, visited, path)
        path.pop()
        visited[v] = False

    visited = [False] * len(graph)
    dfs(src, visited, [])
    return paths


if __name__ == "__main__":
    graph = [
        [0, 1, 1, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 1],
        [0, 0, 0, 0],
    ]
    src, dest = 0, 3
    paths = find_all_paths(graph, src, dest)
    for p in paths:
        print(p)

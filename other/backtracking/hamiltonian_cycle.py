def has_hamiltonian_cycle(graph: list[list[int]]) -> list[int] | None:
    """Find a Hamiltonian Cycle in the given graph."""
    n = len(graph)
    path = [0]

    def is_valid(v: int) -> bool:
        if graph[path[-1]][v] == 0:
            return False
        if v in path:
            return False
        return True

    def solve() -> bool:
        if len(path) == n:
            return graph[path[-1]][path[0]] == 1
        for v in range(1, n):
            if is_valid(v):
                path.append(v)
                if solve():
                    return True
                path.pop()
        return False

    if solve():
        path.append(0)
        return path
    return None


if __name__ == "__main__":
    graph = [
        [0, 1, 0, 1, 0],
        [1, 0, 1, 1, 1],
        [0, 1, 0, 0, 1],
        [1, 1, 0, 0, 1],
        [0, 1, 1, 1, 0],
    ]
    path = has_hamiltonian_cycle(graph)
    if path:
        print(" -> ".join(map(str, path)))
    else:
        print("No Hamiltonian Cycle found")

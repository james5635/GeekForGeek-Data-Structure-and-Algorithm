def can_color_graph(graph: list[list[int]], m: int) -> list[int] | None:
    """Solve M Coloring Problem and return color assignment for each vertex."""
    n = len(graph)
    colors = [0] * n

    def is_safe(v: int, c: int) -> bool:
        for i in range(n):
            if graph[v][i] == 1 and colors[i] == c:
                return False
        return True

    def solve(v: int) -> bool:
        if v == n:
            return True
        for c in range(1, m + 1):
            if is_safe(v, c):
                colors[v] = c
                if solve(v + 1):
                    return True
                colors[v] = 0
        return False

    if solve(0):
        return colors
    return None


if __name__ == "__main__":
    graph = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0],
    ]
    m = 3
    colors = can_color_graph(graph, m)
    if colors:
        for i, c in enumerate(colors):
            print(f"Vertex {i}: Color {c}")
    else:
        print("No valid coloring exists")

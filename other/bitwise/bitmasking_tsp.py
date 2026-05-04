def bitmasking_tsp(graph: list[list[int]], n: int) -> int:
    """Solve TSP using bitmasking dynamic programming."""
    dp = [[float("inf")] * n for _ in range(1 << n)]
    dp[1][0] = 0
    for mask in range(1 << n):
        for u in range(n):
            if (mask >> u) & 1:
                for v in range(n):
                    if (mask >> v) & 1 == 0:
                        new_mask = mask | (1 << v)
                        dp[new_mask][v] = min(
                            dp[new_mask][v], dp[mask][u] + graph[u][v]
                        )
    return min(dp[(1 << n) - 1][i] for i in range(1, n))


if __name__ == "__main__":
    graph = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
    print(bitmasking_tsp(graph, 4))

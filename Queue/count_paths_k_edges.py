from collections import defaultdict


def countWalksBF(adj, u, dest, k):
    if k == 0:
        return 1 if u == dest else 0
    count = 0
    for v in adj[u]:
        count += countWalksBF(adj, v, dest, k - 1)
    return count


def countWalks(adj, src, dest, k):
    n = len(adj)
    dp = [[0] * n for _ in range(k + 1)]

    for i in range(n):
        dp[0][i] = 1 if i == dest else 0

    for step in range(1, k + 1):
        for u in range(n):
            dp[step][u] = 0
            for v in adj[u]:
                dp[step][u] += dp[step - 1][v]

    return dp[k][src]


if __name__ == "__main__":
    adj = [[0, 1, 1, 1], [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 0]]
    graph = defaultdict(list)
    for i in range(len(adj)):
        for j in range(len(adj[i])):
            if adj[i][j] == 1:
                graph[i].append(j)

    src, dest, k = 0, 3, 2
    expected = 2

    print(f"Brute Force: {countWalksBF(graph, src, dest, k)}")
    print(f"DP Approach: {countWalks(graph, src, dest, k)}")
    print(f"Expected: {expected}")

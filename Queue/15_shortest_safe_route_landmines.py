from collections import deque


def mark_unsafe_cells(mat):
    rows = len(mat)
    cols = len(mat[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == 0:
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols and mat[ni][nj] != 0:
                        mat[ni][nj] = -1

    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == -1:
                mat[i][j] = 0


def shortest_safe_route_dfs(mat):
    rows = len(mat)
    cols = len(mat[0])
    mark_unsafe_cells(mat)

    min_dist = [float("inf")]

    def dfs(i, j, dist, visited):
        if j == cols - 1:
            min_dist[0] = min(min_dist[0], dist)
            return

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if (
                0 <= ni < rows
                and 0 <= nj < cols
                and mat[ni][nj] == 1
                and (ni, nj) not in visited
            ):
                visited.add((ni, nj))
                dfs(ni, nj, dist + 1, visited)
                visited.remove((ni, nj))

    for i in range(rows):
        if mat[i][0] == 1:
            visited = {(i, 0)}
            dfs(i, 0, 1, visited)

    return min_dist[0] if min_dist[0] != float("inf") else -1


def shortest_safe_route_bfs(mat):
    rows = len(mat)
    cols = len(mat[0])
    mark_unsafe_cells(mat)

    queue = deque()
    visited = [[False] * cols for _ in range(rows)]

    for i in range(rows):
        if mat[i][0] == 1:
            queue.append((i, 0, 1))
            visited[i][0] = True

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        i, j, dist = queue.popleft()

        if j == cols - 1:
            return dist

        for di, dj in directions:
            ni, nj = i + di, j + dj
            if (
                0 <= ni < rows
                and 0 <= nj < cols
                and mat[ni][nj] == 1
                and not visited[ni][nj]
            ):
                visited[ni][nj] = True
                queue.append((ni, nj, dist + 1))

    return -1


if __name__ == "__main__":
    mat1 = [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
    ]
    print(shortest_safe_route_dfs([row[:] for row in mat1]))
    print(shortest_safe_route_bfs(mat1))

    mat2 = [
        [1, 1, 0, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
    ]
    print(shortest_safe_route_dfs([row[:] for row in mat2]))
    print(shortest_safe_route_bfs(mat2))

    mat3 = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
    ]
    print(shortest_safe_route_dfs([row[:] for row in mat3]))
    print(shortest_safe_route_bfs(mat3))

from collections import deque


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def is_valid(x, y, rows, cols):
    return 0 <= x < rows and 0 <= y < cols


def bfs(mat, src, dest):
    rows = len(mat)
    cols = len(mat[0])

    if mat[src.x][src.y] == 0 or mat[dest.x][dest.y] == 0:
        return -1

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    visited = [[False] * cols for _ in range(rows)]
    queue = deque()

    queue.append(Point(src.x, src.y))
    visited[src.x][src.y] = True
    dist = 0

    while queue:
        size = len(queue)
        for _ in range(size):
            curr = queue.popleft()

            if curr.x == dest.x and curr.y == dest.y:
                return dist

            for i in range(4):
                nx = curr.x + dx[i]
                ny = curr.y + dy[i]

                if (
                    is_valid(nx, ny, rows, cols)
                    and mat[nx][ny] == 1
                    and not visited[nx][ny]
                ):
                    visited[nx][ny] = True
                    queue.append(Point(nx, ny))

        dist += 1

    return -1


if __name__ == "__main__":
    mat = [
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 0, 0, 0, 0, 1, 0, 0, 1],
    ]

    src = Point(0, 0)
    dest = Point(3, 4)
    print(bfs(mat, src, dest))

from collections import deque


class Cell:
    def __init__(self, x, y, dis):
        self.x = x
        self.y = y
        self.dis = dis


def isInside(x, y, n):
    return 1 <= x <= n and 1 <= y <= n


def minSteps(knightPos, targetPos, n):
    dx = [-2, -1, 1, 2, -2, -1, 1, 2]
    dy = [-1, -2, -2, -1, 1, 2, 2, 1]

    visited = [[False] * (n + 1) for _ in range(n + 1)]
    queue = deque()

    start = Cell(knightPos[0], knightPos[1], 0)
    queue.append(start)
    visited[knightPos[0]][knightPos[1]] = True

    while queue:
        curr = queue.popleft()

        if curr.x == targetPos[0] and curr.y == targetPos[1]:
            return curr.dis

        for i in range(8):
            nx = curr.x + dx[i]
            ny = curr.y + dy[i]

            if isInside(nx, ny, n) and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append(Cell(nx, ny, curr.dis + 1))

    return -1


if __name__ == "__main__":
    knightPos = [1, 1]
    targetPos = [30, 30]
    n = 30
    print(minSteps(knightPos, targetPos, n))

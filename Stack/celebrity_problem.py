def find_celebrity(mat):
    n = len(mat)
    stack = list(range(n))

    while len(stack) > 1:
        a = stack.pop()
        b = stack.pop()
        if mat[a][b] == 1:
            stack.append(b)
        else:
            stack.append(a)

    if not stack:
        return -1

    candidate = stack.pop()
    for i in range(n):
        if i != candidate:
            if mat[candidate][i] == 1 or mat[i][candidate] == 0:
                return -1
    return candidate


if __name__ == "__main__":
    mat1 = [[0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 1, 0]]
    print(find_celebrity(mat1))

    mat2 = [[0, 0], [0, 0]]
    print(find_celebrity(mat2))

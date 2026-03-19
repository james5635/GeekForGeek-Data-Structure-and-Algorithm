from collections import deque


def process_queries(arr, queries):
    dq = deque(arr)
    output = []

    for query in queries:
        qtype = query[0]

        if qtype == 0:
            dq.rotate(-1)

        elif qtype == 1:
            dq.rotate(1)

        elif qtype == 2:
            idx = query[1]
            val = query[2]
            if 0 <= idx < len(dq):
                dq[idx] = val

        elif qtype == 3:
            output.append(list(dq))

    return output


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    queries = [[3], [0], [3], [1], [3], [2, 2, 54], [3]]
    results = process_queries(arr, queries)
    for r in results:
        print(" ".join(map(str, r)))

    print()

    arr2 = [10, 20, 30, 40, 50]
    queries2 = [[0], [0], [3], [2, 0, 99], [3], [1], [3]]
    results2 = process_queries(arr2, queries2)
    for r in results2:
        print(" ".join(map(str, r)))

    print()

    arr3 = [1, 2, 3, 4, 5]
    queries3 = [[2, 1, 10], [3], [0], [3], [1], [3]]
    results3 = process_queries(arr3, queries3)
    for r in results3:
        print(" ".join(map(str, r)))

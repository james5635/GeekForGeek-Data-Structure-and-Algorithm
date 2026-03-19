from collections import deque


def pageFaults(pages, n, capacity):
    s = set()
    fault_count = 0
    queue = deque()

    for i in range(n):
        if pages[i] not in s:
            fault_count += 1
            if len(s) >= capacity:
                val = queue.popleft()
                s.remove(val)
            s.add(pages[i])
            queue.append(pages[i])

    return fault_count


if __name__ == "__main__":
    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    n = len(pages)
    capacity = 4

    result = pageFaults(pages, n, capacity)
    print(f"Page Faults: {result}")
    print(f"Expected: 7")

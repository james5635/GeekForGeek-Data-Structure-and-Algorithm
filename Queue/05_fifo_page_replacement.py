from collections import deque


def pageFaults(pages, n, capacity):
    s = set()
    queue = deque()
    faults = 0

    for page in pages:
        if page not in s:
            faults += 1
            if len(s) == capacity:
                oldest = queue.popleft()
                s.remove(oldest)
            s.add(page)
            queue.append(page)
        else:
            if page in queue:
                queue.remove(page)
                queue.append(page)

    return faults


if __name__ == "__main__":
    pages1 = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    n1 = len(pages1)
    capacity1 = 4
    print(f"Pages: {pages1}")
    print(f"Capacity: {capacity1}")
    print(f"Page Faults: {pageFaults(pages1, n1, capacity1)}")
    print()

    pages2 = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
    n2 = len(pages2)
    capacity2 = 3
    print(f"Pages: {pages2}")
    print(f"Capacity: {capacity2}")
    print(f"Page Faults: {pageFaults(pages2, n2, capacity2)}")
    print()

    pages3 = [1, 2, 3, 4, 5]
    n3 = len(pages3)
    capacity3 = 4
    print(f"Pages: {pages3}")
    print(f"Capacity: {capacity3}")
    print(f"Page Faults: {pageFaults(pages3, n3, capacity3)}")

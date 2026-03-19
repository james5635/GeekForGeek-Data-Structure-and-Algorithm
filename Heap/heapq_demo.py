import heapq


def heapq_demo():
    """
    Demonstrate Python's heapq module with various examples.
    """
    print("=== Python heapq Module Demo ===\n")

    # 1. Creating a heap from a list using heapify
    print("1. Creating a heap using heapify:")
    data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(f"Original data: {data}")
    heapq.heapify(data)
    print(f"After heapify: {data}")
    print(f"Smallest element (heap[0]): {data[0]}\n")

    # 2. Pushing elements to heap using heappush
    print("2. Pushing elements using heappush:")
    heap = []
    elements = [5, 3, 8, 1, 9, 2]
    for elem in elements:
        heapq.heappush(heap, elem)
        print(f"After pushing {elem}: {heap}")
    print(f"Final heap: {heap}\n")

    # 3. Popping elements from heap using heappop
    print("3. Popping elements using heappop (in sorted order):")
    sorted_elements = []
    while heap:
        smallest = heapq.heappop(heap)
        sorted_elements.append(smallest)
        print(f"Popped: {smallest}, Remaining heap: {heap}")
    print(f"Sorted elements: {sorted_elements}\n")

    # 4. Push and pop in one operation (more efficient)
    print("4. Using heappushpop (push then pop smallest):")
    heap = [1, 3, 5, 7, 9]
    heapq.heapify(heap)
    print(f"Initial heap: {heap}")
    result = heapq.heappushpop(heap, 4)
    print(f"After heappushpop(4): returned {result}, heap: {heap}")
    result = heapq.heappushpop(heap, 10)
    print(f"After heappushpop(10): returned {result}, heap: {heap}\n")

    # 5. Pop and push in one operation
    print("5. Using heapreplace (pop then push):")
    heap = [1, 3, 5, 7, 9]
    heapq.heapify(heap)
    print(f"Initial heap: {heap}")
    result = heapq.heapreplace(heap, 4)
    print(f"After heapreplace(4): returned {result}, heap: {heap}")
    result = heapq.heapreplace(heap, 0)
    print(f"After heapreplace(0): returned {result}, heap: {heap}\n")

    # 6. Finding n largest elements
    print("6. Finding n largest elements using nlargest:")
    data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(f"Data: {data}")
    print(f"3 largest: {heapq.nlargest(3, data)}")
    print(f"5 largest: {heapq.nlargest(5, data)}\n")

    # 7. Finding n smallest elements
    print("7. Finding n smallest elements using nsmallest:")
    data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(f"Data: {data}")
    print(f"3 smallest: {heapq.nsmallest(3, data)}")
    print(f"5 smallest: {heapq.nsmallest(5, data)}\n")

    # 8. Heap with tuples (priority queue)
    print("8. Priority queue using heap with tuples:")
    pq = []  # priority queue
    tasks = [
        (3, "Low priority task"),
        (1, "High priority task"),
        (2, "Medium priority task"),
        (1, "Another high priority task"),
        (4, "Very low priority task"),
    ]

    print("Adding tasks to priority queue:")
    for priority, task in tasks:
        heapq.heappush(pq, (priority, task))
        print(f"Added: ({priority}, '{task}')")

    print("\nProcessing tasks in priority order:")
    while pq:
        priority, task = heapq.heappop(pq)
        print(f"Processing: '{task}' (priority {priority})")


def main():
    heapq_demo()


if __name__ == "__main__":
    main()

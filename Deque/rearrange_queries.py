"""
Rearrange and Update Array Elements by Queries

Approach:
- Use deque for efficient rotations
- Query types:
  - 0: Left rotate by 1
  - 1: Right rotate by 1
  - 2 X Y: Update element at index X to value Y
  - 3 X: Print element at index X

Time Complexity: O(q + n) where q is number of queries
Space Complexity: O(n)
"""

from collections import deque


def process_queries(arr, queries):
    """
    Process queries on array:
    0: left rotate, 1: right rotate, 2 X Y: update, 3 X: print
    Returns list of printed values.
    """
    dq = deque(arr)
    results = []

    for query in queries:
        if len(query) == 1:
            q_type = query[0]
            if q_type == 0:
                dq.rotate(-1)
            elif q_type == 1:
                dq.rotate(1)
        else:
            q_type, idx = query[0], query[1]
            if q_type == 2:
                val = query[2]
                temp_list = list(dq)
                temp_list[idx] = val
                dq = deque(temp_list)
            elif q_type == 3:
                results.append(dq[idx])

    return results


def process_queries_manual(arr, queries):
    """
    Process queries without using deque.rotate().
    Manual implementation of rotations.
    """
    left = []
    right = list(arr)
    results = []

    for query in queries:
        if len(query) == 1:
            q_type = query[0]
            if q_type == 0:
                if left and right:
                    right.insert(0, left.pop())
                elif right:
                    left.append(right.pop(0))
            elif q_type == 1:
                if right and left:
                    left.append(right.pop())
                elif right:
                    left.append(right.pop())
                    right.insert(0, left.pop(0))
        else:
            q_type, idx = query[0], query[1]
            if q_type == 2:
                val = query[2]
                combined = left + right
                combined[idx] = val
                mid = len(left)
                left = combined[:mid]
                right = combined[mid:]
            elif q_type == 3:
                combined = left + right
                results.append(combined[idx])

    return results


def main():
    print("=== Rearrange and Update Array Elements by Queries ===\n")

    print("Query Types:")
    print("  0: Left rotate by 1")
    print("  1: Right rotate by 1")
    print("  2 X Y: Update element at index X to value Y")
    print("  3 X: Print element at index X\n")

    arr = [1, 2, 3, 4, 5]
    queries = [[0], [1], [3, 1], [2, 2, 54], [3, 2]]

    print(f"Array: {arr}")
    print(f"Queries: {queries}\n")

    print("Step-by-step execution:")
    print("Initial array: 1 2 3 4 5")

    dq = deque(arr)
    step = 1

    for query in queries:
        if len(query) == 1:
            q_type = query[0]
            if q_type == 0:
                dq.rotate(-1)
                print(f"Query {step}: Left rotate -> {list(dq)}")
            else:
                dq.rotate(1)
                print(f"Query {step}: Right rotate -> {list(dq)}")
        else:
            q_type, idx = query[0], query[1]
            if q_type == 2:
                val = query[2]
                temp_list = list(dq)
                temp_list[idx] = val
                dq = deque(temp_list)
                print(f"Query {step}: Update index {idx} to {val} -> {list(dq)}")
            elif q_type == 3:
                result = dq[idx]
                print(f"Query {step}: Print index {idx} -> Output: {result}")
        step += 1

    results = process_queries(arr, queries)
    print(f"\nPrinted values: {results}")

    print("\n--- Additional Test Cases ---")

    test_cases = [
        {"arr": [1, 2, 3], "queries": [[3, 0], [3, 1], [3, 2]], "expected": [1, 2, 3]},
        {
            "arr": [1, 2, 3, 4],
            "queries": [[0], [0], [3, 0], [3, 3]],
            "expected": [3, 2],
        },
        {
            "arr": [10, 20, 30],
            "queries": [[1], [1], [2, 0, 100], [3, 0]],
            "expected": [100],
        },
    ]

    for i, test in enumerate(test_cases, 1):
        result = process_queries(test["arr"].copy(), test["queries"])
        status = "PASS" if result == test["expected"] else "FAIL"
        print(f"\nTest {i}:")
        print(f"  Array: {test['arr']}")
        print(f"  Queries: {test['queries']}")
        print(f"  Output: {result}")
        print(f"  Expected: {test['expected']}")
        print(f"  Status: {status}")


if __name__ == "__main__":
    main()

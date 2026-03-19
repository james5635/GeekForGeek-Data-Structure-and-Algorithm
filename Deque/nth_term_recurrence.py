"""
Nth term of recurrence relation where each term is product of K terms
Uses deque for efficient rolling product calculation

For K=2: a[i] = a[i-1] * a[i-2]
For K>2: a[i] = product of all K previous terms
"""

from collections import deque


def nth_term_recurrence(arr, n, k=None):
    """
    Find the nth term (1-indexed) of the recurrence relation.
    For K=2: a[i] = a[i-1] * a[i-2]
    For K>2: a[i] = product of all K previous terms
    """
    if k is None:
        k = len(arr)

    if n <= k:
        return arr[n - 1]

    if k == 2:
        dq = deque(arr[:2])
        for _ in range(2, n):
            product = dq[0] * dq[1]
            dq.popleft()
            dq.append(product)
        return dq[-1]
    else:
        dq = deque(arr)
        for _ in range(k, n):
            product = 1
            for val in dq:
                product *= val
            dq.popleft()
            dq.append(product)
        return dq[-1]


def generate_sequence(arr, length, k=None):
    """
    Generate the first 'length' terms of the recurrence relation
    """
    if k is None:
        k = len(arr)

    if length <= k:
        return arr[:length]

    sequence = list(arr)

    if k == 2:
        dq = deque(arr[:2])
        for _ in range(k, length):
            product = dq[0] * dq[1]
            dq.popleft()
            dq.append(product)
            sequence.append(product)
    else:
        dq = deque(arr)
        for _ in range(k, length):
            product = 1
            for val in dq:
                product *= val
            dq.popleft()
            dq.append(product)
            sequence.append(product)

    return sequence


def main():
    print("=" * 60)
    print("Nth Term of Recurrence Relation (Product of K Terms)")
    print("=" * 60)

    print("\n--- Test Case 1 ---")
    arr = [1, 2]
    n = 5
    result = nth_term_recurrence(arr, n)
    sequence = generate_sequence(arr, n + 1)
    print(f"Input: arr = {arr}, n = {n}")
    print(f"Sequence: {sequence}")
    print(f"Output: {result}")
    print(f"Expected: 32 (1,2,2,4,8,32)")
    print(f"Pass: {result == 32}")

    print("\n--- Test Case 2 ---")
    arr = [1, 1, 1]
    n = 6
    result = nth_term_recurrence(arr, n)
    sequence = generate_sequence(arr, n + 1)
    print(f"Input: arr = {arr}, n = {n}")
    print(f"Sequence: {sequence}")
    print(f"Output: {result}")
    print(f"Expected: 1 (1,1,1,1,1,1,1)")
    print(f"Pass: {result == 1}")

    print("\n--- Test Case 3 ---")
    arr = [2, 3]
    n = 4
    result = nth_term_recurrence(arr, n)
    sequence = generate_sequence(arr, n + 1)
    print(f"Input: arr = {arr}, n = {n}")
    print(f"Sequence: {sequence}")
    print(f"Output: {result}")
    print(f"Expected: 18 (2,3,6,18)")
    print(f"Pass: {result == 18}")

    print("\n--- Test Case 4 ---")
    arr = [1, 2, 3, 4]
    n = 5
    result = nth_term_recurrence(arr, n)
    sequence = generate_sequence(arr, n + 1)
    print(f"Input: arr = {arr}, n = {n}")
    print(f"Sequence: {sequence}")
    print(f"Output: {result}")
    print(f"Expected: 24 (1*2*3*4)")
    print(f"Pass: {result == 24}")

    print("\n--- Test Case 5 ---")
    arr = [5]
    n = 3
    result = nth_term_recurrence(arr, n)
    sequence = generate_sequence(arr, n + 1)
    print(f"Input: arr = {arr}, n = {n}")
    print(f"Sequence: {sequence}")
    print(f"Output: {result}")
    print(f"Expected: 125 (5,5,25,125)")
    print(f"Pass: {result == 125}")

    print("\n--- Test Case 6 ---")
    arr = [10]
    n = 1
    result = nth_term_recurrence(arr, n)
    print(f"Input: arr = {arr}, n = {n}")
    print(f"Output: {result}")
    print(f"Expected: 10")
    print(f"Pass: {result == 10}")


if __name__ == "__main__":
    main()

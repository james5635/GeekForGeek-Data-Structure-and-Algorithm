def next_smaller_next_greater(arr):
    n = len(arr)
    next_smaller = [-1] * n
    next_greater = [-1] * n

    stack = []
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            next_smaller[i] = arr[stack[-1]]
        stack.append(i)

    stack = []
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
        if stack:
            next_greater[i] = arr[stack[-1]]
        stack.append(i)

    return next_smaller, next_greater


if __name__ == "__main__":
    arr1 = [5, 1, 9, 2, 5, 1, 7]
    ns, ng = next_smaller_next_greater(arr1)
    print("Array:", arr1)
    print("Next smaller:", ns)
    print("Next greater:", ng)

    arr2 = [4, 8, 2, 1, 9, 5, 6, 3]
    ns, ng = next_smaller_next_greater(arr2)
    print("\nArray:", arr2)
    print("Next smaller:", ns)
    print("Next greater:", ng)

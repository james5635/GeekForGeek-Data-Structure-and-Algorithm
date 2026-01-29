def rotate_arr(arr, d):
    n = len(arr)
    if n == 0:
        return
    d %= n
    # Repeat the rotation d times
    for _ in range(d):
        # Right rotate the array by one position
        last = arr[n - 1]
        for j in range(n - 1, 0, -1):
            arr[j] = arr[j - 1]
        arr[0] = last

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    d = 2
    print(f"Original array: {arr}, d: {d}")
    rotate_arr(arr, d)
    print(f"Rotated array (one by one): {arr}")

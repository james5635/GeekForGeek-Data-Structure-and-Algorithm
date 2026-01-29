def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotate_arr(arr, d):
    n = len(arr)
    if n == 0:
        return
    # Handle the case where d > size of array
    d %= n
    
    # 1. Reverse the entire array
    reverse(arr, 0, n - 1)
    
    # 2. Reverse the first d elements
    reverse(arr, 0, d - 1)
    
    # 3. Reverse the remaining n-d elements
    reverse(arr, d, n - 1)

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    d = 2
    print(f"Original array: {arr}, d: {d}")
    rotate_arr(arr, d)
    print(f"Rotated array (Reversal algorithm): {arr}")

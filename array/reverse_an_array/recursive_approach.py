def reverse_array_recursive(arr, start, end):
    # Base case
    if start >= end:
        return
    
    # Swap elements at start and end
    arr[start], arr[end] = arr[end], arr[start]
    
    # Recursive call for the remaining array
    reverse_array_recursive(arr, start + 1, end - 1)

def reverse_array(arr):
    reverse_array_recursive(arr, 0, len(arr) - 1)

if __name__ == "__main__":
    arr = [1, 4, 3, 2, 6, 5]
    print(f"Original array: {arr}")
    reverse_array(arr)
    print(f"Reversed array: {arr}")

def reverse_array(arr):
    # Using Python's built-in reverse() method
    arr.reverse()

def reverse_array_slicing(arr):
    # Using Python's slicing (creates a new list and copies it back)
    arr[:] = arr[::-1]

if __name__ == "__main__":
    arr1 = [1, 4, 3, 2, 6, 5]
    print(f"Original array 1: {arr1}")
    reverse_array(arr1)
    print(f"Reversed using reverse(): {arr1}")
    
    arr2 = [1, 4, 3, 2, 6, 5]
    print(f"Original array 2: {arr2}")
    reverse_array_slicing(arr2)
    print(f"Reversed using slicing: {arr2}")

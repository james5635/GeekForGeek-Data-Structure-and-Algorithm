import math

def rotate_arr(arr, d):
    n = len(arr)
    if n == 0:
        return
    # Handle the case where d > size of array
    d %= n
    if d == 0:
        return
        
    # Calculate the number of cycles in the rotation
    cycles = math.gcd(n, d)
    
    # Process each cycle
    for i in range(cycles):
        # Start index of current cycle
        curr_idx = i
        curr_ele = arr[curr_idx]
        
        # Rotate elements till we reach the start of cycle
        while True:
            next_idx = (curr_idx + d) % n
            # Swap current element with next index's element
            arr[next_idx], curr_ele = curr_ele, arr[next_idx]
            curr_idx = next_idx
            
            if curr_idx == i:
                break

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    d = 2
    print(f"Original array: {arr}, d: {d}")
    rotate_arr(arr, d)
    print(f"Rotated array (Juggling algorithm): {arr}")

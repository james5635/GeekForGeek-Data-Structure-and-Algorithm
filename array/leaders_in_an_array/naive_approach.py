# Function to find the leaders in an array
def leaders(arr):
    result = []
    n = len(arr)
    for i in range(n):
        # Check elements to the right
        for j in range(i + 1, n):
            # If a larger element is found
            if arr[i] < arr[j]:
                break
        else:
            # If no larger element was found
            result.append(arr[i])
    return result

if __name__ == "__main__":
    arr = [16, 17, 4, 3, 5, 2]
    result = leaders(arr)
    print(" ".join(map(str, result)))

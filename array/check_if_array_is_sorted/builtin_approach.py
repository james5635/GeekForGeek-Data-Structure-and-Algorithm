def is_sorted(arr):
    # sorted() is a built-in method for python
    return arr == sorted(arr)

if __name__ == "__main__":
    arr1 = [10, 20, 30, 40, 50]
    print(f"Array {arr1} is sorted: {is_sorted(arr1)}")
    
    arr2 = [10, 20, 30, 5, 6]
    print(f"Array {arr2} is sorted: {is_sorted(arr2)}")

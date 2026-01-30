def find_kth_smallest(arr, k):
    
    if k < 1 or k > len(arr):
        return "Invalid k"

    arr.sort()
    return arr[k-1]

if __name__ == "__main__":
    nums = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
    k_val = 4
    
    result = find_kth_smallest(nums, k_val)
    
    print(f"Array: {nums}")
    print(f"k: {k_val}")
    print(f"The {k_val}th smallest element is: {result}")

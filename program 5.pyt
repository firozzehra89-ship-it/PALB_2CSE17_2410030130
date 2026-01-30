def find_largest_element(arr):
    if not arr:
        return None
    
    max_val = arr[0]
    
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
            
    return max_val

if __name__ == "__main__":
    arr = [1, 8, 7, 56, 90]
    result = find_largest_element(arr)
    
    print(f"Array: {arr}")
    print(f"Largest Element: {result}")

def get_min_diff(arr, k):
    n = len(arr)
    if n == 1:
        return 0
    
    arr.sort()
    
    res = arr[n-1] - arr[0]
    
    for i in range(n - 1):
        if arr[i+1] < k:
            continue
            
        max_h = max(arr[i] + k, arr[n-1] - k)
        min_h = min(arr[0] + k, arr[i+1] - k)
        
        res = min(res, max_h - min_h)
        
    return res
  
print(get_min_diff([1, 5, 8, 10], 2))  
print(get_min_diff([3, 9, 12, 16, 20], 3))

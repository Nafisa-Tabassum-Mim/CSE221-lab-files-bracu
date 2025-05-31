
def count_number(arr,s):
    first, last = s
    l, r = 0, len(arr) - 1
    left_idx, right_idx = len(arr), -1
    
    while l <= r :
        mid = (l+r)//2
        if arr[mid] >= first:
            left_idx = mid
            r = mid -1
        else:
            l = mid +1
            
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] <= last:
            right_idx = mid 
            l = mid + 1
        else:
            r = mid - 1

    print( right_idx - left_idx + 1)
            
    
    
arr_size, T = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(0, T ):
    s = list(map(int, input().split())) 
    count_number(arr , s)
    
# log n time complexity 
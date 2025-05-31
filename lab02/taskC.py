def LongestSubarray():
    length,data = map(int, input().split())
    arr = list(map(int, input().split()))

    maximum ,sum = 0,0
    i = 0
    for j in range(0,len(arr)):
        sum += arr[j]

        while sum > data and i <= j:
            sum -= arr[i]
            i += 1

        maximum = max(maximum,j-i+1)
    return maximum
    
max_total_index = LongestSubarray()
print(max_total_index)
                                        
            
def twoSum():
    length,data = map(int, input().split())
    arr = list(map(int, input().split()))
    i = 0
    j = len(arr)-1
    while i<j:
        sum = arr[i] + arr[j]
        if sum == data:
            return f'{i+1} {j+1}'
        elif sum < data:
            i += 1
        else:
            j -= 1
    return -1
  

index = twoSum()    
print(index)